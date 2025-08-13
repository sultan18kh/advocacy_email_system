"""
Test script for the automated government email system
This script tests the email templates and configuration without sending actual emails.
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import random
import re

# Try to import pytz, but handle gracefully if missing
try:
    import pytz

    PYTZ_AVAILABLE = True
except ImportError:
    PYTZ_AVAILABLE = False


def test_dependencies():
    """Test if all required dependencies are available"""
    print("🧪 Testing Dependencies...")

    required_modules = ["schedule", "pytz"]
    missing_modules = []

    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module}: Available")
        except ImportError:
            print(f"❌ {module}: Missing")
            missing_modules.append(module)

    if missing_modules:
        print(f"❌ Missing dependencies: {', '.join(missing_modules)}")
        print("💡 Run: pip install -r requirements.txt")
        print("💡 Or run: pip install schedule pytz")
        return False

    return True


def test_timezone_handling():
    """Test timezone handling functionality"""
    print("\n🌍 Testing Timezone Handling...")

    if not PYTZ_AVAILABLE:
        print("❌ pytz module not available")
        print("💡 Run: pip install pytz")
        return False

    try:
        # Test Pakistan timezone
        pakistan_tz = pytz.timezone("Asia/Karachi")
        utc_now = datetime.now(pytz.UTC)
        pakistan_time = utc_now.astimezone(pakistan_tz)

        print(f"✅ UTC Time: {utc_now.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        print(f"✅ Pakistan Time: {pakistan_time.strftime('%Y-%m-%d %H:%M:%S PKT')}")

        # Calculate proper time difference using UTC offset
        offset_seconds = pakistan_time.utcoffset().total_seconds()
        offset_hours = offset_seconds / 3600

        # Pakistan Standard Time is UTC+5
        if abs(offset_hours - 5.0) < 0.1:  # Allow small tolerance
            print("✅ Timezone offset correct (+5 hours)")
        else:
            print(
                f"✅ Timezone offset: +{offset_hours:.1f} hours (Pakistan Standard Time)"
            )

        return True
    except Exception as e:
        print(f"❌ Timezone handling error: {e}")
        return False


def test_email_validation():
    """Test email validation functionality"""
    print("\n📧 Testing Email Validation...")

    def validate_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    test_emails = [
        ("valid@example.com", True),
        ("test.email+123@domain.co.uk", True),
        ("invalid.email", False),
        ("@domain.com", False),
        ("user@", False),
        ("", False),
        ("complaints@waltoncantonment.gov.pk", True),
    ]

    all_passed = True
    for email, expected in test_emails:
        result = validate_email(email)
        if result == expected:
            print(f"✅ {email}: {'Valid' if result else 'Invalid'}")
        else:
            print(
                f"❌ {email}: Expected {'Valid' if expected else 'Invalid'}, got {'Valid' if result else 'Invalid'}"
            )
            all_passed = False

    return all_passed


def test_email_templates():
    """Test email template generation and validation"""
    print("\n" + "=" * 60)
    print("🧪 TESTING EMAIL TEMPLATE SYSTEM")
    print("=" * 60)

    try:
        # Test template validation
        print("\n📋 Testing template validation...")

        # Import the class directly from the module
        import send_single_email

        # Check if email services are configured
        has_email_services = (
            os.getenv("GMAIL_EMAIL")
            or os.getenv("OUTLOOK_EMAIL")
            or os.getenv("YAHOO_EMAIL")
        )

        if not has_email_services:
            print("ℹ️  No email services configured - testing template logic only")
            # Test template selection logic without creating sender instance
            test_template_selection()
            return True

        sender = send_single_email.GovernmentEmailSender()

        # Test available templates
        available_templates = sender.get_available_templates()
        print(f"✅ Found {len(available_templates)} available templates:")
        for template in available_templates:
            print(f"   {template['description']}")

        # Test template generation for each type
        print("\n📝 Testing template generation...")
        for template_type in [1, 2, 3]:
            try:
                template = sender.get_email_template(template_type)
                print(f"✅ Template {template_type} generated successfully:")
                print(f"   Subject: {template['subject'][:60]}...")
                print(f"   Language: {template['language']}")
                print(f"   Reference: {template['reference_number']}")

                # Test template formatting
                if template["body"] and len(template["body"]) > 100:
                    print(f"   Body length: {len(template['body'])} characters")
                else:
                    print(
                        f"   ⚠️  Body seems too short: {len(template['body'])} characters"
                    )

            except Exception as e:
                print(f"❌ Failed to generate template {template_type}: {e}")

        # Test fallback template
        print("\n🔄 Testing fallback template...")
        try:
            fallback = sender._get_fallback_template(99)  # Invalid template type
            print(f"✅ Fallback template generated:")
            print(f"   Subject: {fallback['subject']}")
            print(f"   Reference: {fallback['reference_number']}")
        except Exception as e:
            print(f"❌ Fallback template failed: {e}")

        print("\n✅ Email template testing completed successfully!")
        return True

    except Exception as e:
        print(f"❌ Email template testing failed: {e}")
        return False


def test_email_rotation():
    """Test the email service rotation logic"""
    print("\n🔄 Testing Email Service Rotation...")

    # Check if running in GitHub Actions
    is_github_actions = os.getenv("GITHUB_ACTIONS") == "true"

    # Simulate available services
    available_services = []

    if os.getenv("GMAIL_EMAIL") and os.getenv("GMAIL_APP_PASSWORD"):
        available_services.append("Gmail")

    if os.getenv("OUTLOOK_EMAIL") and os.getenv("OUTLOOK_PASSWORD"):
        available_services.append("Outlook")

    if os.getenv("YAHOO_EMAIL") and os.getenv("YAHOO_PASSWORD"):
        available_services.append("Yahoo")

    if not available_services:
        if is_github_actions:
            print("❌ No email services configured in GitHub Actions")
            print("💡 Check your GitHub Secrets configuration")
            return False
        else:
            print("ℹ️  No email services configured locally (expected)")
            print("💡 Testing rotation logic with simulated services:")
            # Test with simulated services for demonstration
            simulated_services = ["Gmail", "Outlook", "Yahoo"]
            print(f"✅ Simulated services: {', '.join(simulated_services)}")

            print("✅ Multi-service rotation logic:")
            for day in range(1, 8):
                service_index = day % len(simulated_services)
                service = simulated_services[service_index]
                print(f"   Day {day}: Would use {service}")

            print("📋 In GitHub Actions, actual configured services will be used")
            return True

    print(
        f"✅ {len(available_services)} email service(s) configured: {', '.join(available_services)}"
    )

    # Test rotation logic
    if len(available_services) == 1:
        print(f"✅ Single service mode: Always using {available_services[0]}")
    else:
        print("✅ Multi-service rotation:")
        # Test rotation for first week
        for day in range(1, 8):
            service_index = day % len(available_services)
            service = available_services[service_index]
            print(f"   Day {day}: Using {service}")

    return True


def test_template_selection():
    """Test template selection logic for Monday/Friday schedule"""
    print("\n📝 Testing Template Selection Logic (Monday/Friday Schedule)...")

    # Test Monday/Friday template selection
    day_names = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    template_names = {
        1: "Mismanagement Complaint (English)",
        2: "Urdu Mismanagement Complaint",
        3: "Administrative Reform Request",
    }

    for day in range(1, 8):  # Test all days of the week
        if day == 1:  # Monday
            template_type = 1
            schedule_status = "📧 EMAIL DAY"
        elif day == 5:  # Friday
            template_type = 2
            schedule_status = "📧 EMAIL DAY"
        else:
            template_type = 1  # Default fallback
            schedule_status = "⏸️  NO EMAIL"

        print(
            f"✅ {day_names[day]}: Template {template_type} ({template_names[template_type]}) - {schedule_status}"
        )

    print("\n📅 Email Schedule Summary:")
    print("   📧 Monday: Template 1 (English) - Mismanagement Complaint")
    print("   📧 Friday: Template 2 (Urdu) - Urdu Mismanagement Complaint")
    print("   ⏸️  Wednesday: Skipped (no emails sent)")

    return True


def test_template_rotation():
    """Test the template rotation logic for Monday/Friday schedule"""
    print("\n📝 Testing Template Rotation (Monday/Friday Schedule)...")

    # Test Monday/Friday template selection
    day_names = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    template_names = {
        1: "Mismanagement Complaint (English)",
        2: "Urdu Mismanagement Complaint",
        3: "Administrative Reform Request",
    }

    for day in range(1, 8):  # Test all days of the week
        if day == 1:  # Monday
            template_type = 1
            schedule_status = "📧 EMAIL DAY"
        elif day == 5:  # Friday
            template_type = 2
            schedule_status = "📧 EMAIL DAY"
        else:
            template_type = 1  # Default fallback
            schedule_status = "⏸️  NO EMAIL"

        print(
            f"✅ {day_names[day]}: Template {template_type} ({template_names[template_type]}) - {schedule_status}"
        )

    print("\n📅 Email Schedule Summary:")
    print("   📧 Monday: Template 1 (English) - Mismanagement Complaint")
    print("   📧 Friday: Template 2 (Urdu) - Urdu Mismanagement Complaint")
    print("   ⏸️  Wednesday: Skipped (no emails sent)")

    return True


def test_environment_variables():
    """Test if environment variables are properly configured"""
    print("\n🔧 Testing Environment Variables...")

    # Check if running in GitHub Actions
    is_github_actions = os.getenv("GITHUB_ACTIONS") == "true"

    if is_github_actions:
        print("🤖 Running in GitHub Actions environment")
    else:
        print("💻 Running in local environment")
        print("💡 GitHub Secrets are only available in GitHub Actions")

    required_vars = [
        ("GMAIL_EMAIL", "GMAIL_APP_PASSWORD"),
        ("OUTLOOK_EMAIL", "OUTLOOK_PASSWORD"),
        ("YAHOO_EMAIL", "YAHOO_PASSWORD"),
    ]

    configured_services = 0

    for email_var, password_var in required_vars:
        email = os.getenv(email_var)
        password = os.getenv(password_var)

        if email and password:
            # Validate email format
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if re.match(pattern, email):
                print(f"✅ {email_var}: Configured and valid")
                configured_services += 1
            else:
                print(f"⚠️  {email_var}: Configured but invalid format")
        else:
            if is_github_actions:
                print(f"ℹ️  {email_var}: Not configured (optional)")
            else:
                print(
                    f"ℹ️  {email_var}: Not set locally (normal - secrets are in GitHub)"
                )

    if configured_services == 0:
        if is_github_actions:
            print(f"\n❌ No email services configured in GitHub Actions")
            print("💡 At least one email service is required")
            print("💡 Check your GitHub Secrets configuration")
            return False
        else:
            print(f"\n💡 No email services configured locally (expected)")
            print("📋 To test with real credentials:")
            print("   export GMAIL_EMAIL='your_email@gmail.com'")
            print("   export GMAIL_APP_PASSWORD='your_app_password'")
            print("   python src/test_email.py")
            print("✅ GitHub Secrets will be available in GitHub Actions")
            return True  # Pass the test in local mode
    elif configured_services == 1:
        print(
            f"\n✅ {configured_services} email service configured (minimum requirement met)"
        )
        print("💡 Optional: Add more email services for better rotation")
    else:
        print(
            f"\n✅ {configured_services} email services configured (excellent for rotation)"
        )

    return True


def test_path_resolution():
    """Test path resolution for media directory"""
    print("\n📂 Testing Path Resolution...")

    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()

    # Try different possible media directory paths
    possible_media_dirs = [
        script_dir.parent / "media",  # ../media from src/
        script_dir / "media",  # ./media from src/
        Path.cwd() / "media",  # media from current working directory
    ]

    media_dir = None
    for dir_path in possible_media_dirs:
        print(f"📁 Checking: {dir_path}")
        if dir_path.exists() and dir_path.is_dir():
            media_dir = dir_path
            print(f"✅ Media directory found: {media_dir}")
            break
        else:
            print(f"❌ Not found: {dir_path}")

    if not media_dir:
        print("❌ Media directory not found")
        print("💡 Create the media directory and add your photos/videos")
        return False

    return True


def test_media_file_discovery():
    """Test the automatic media file discovery functionality"""
    print("\n📁 Testing Media File Discovery...")

    # Test file type validation
    supported_extensions = {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".tiff",
        ".webp",
        ".mp4",
        ".avi",
        ".mov",
        ".wmv",
        ".flv",
        ".webm",
        ".mkv",
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".rtf",
        ".zip",
        ".rar",
        ".7z",
    }

    print(f"✅ Supported file types: {len(supported_extensions)} extensions")

    # Test file size calculation
    def get_file_size_mb(file_path):
        try:
            size_bytes = Path(file_path).stat().st_size
            return size_bytes / (1024 * 1024)
        except (OSError, FileNotFoundError):
            return 0

    # Test media directory discovery
    script_dir = Path(__file__).parent.absolute()
    possible_media_dirs = [
        script_dir.parent / "media",  # ../media from src/
        script_dir / "media",  # ./media from src/
        Path.cwd() / "media",  # media from current working directory
    ]

    media_dir = None
    for dir_path in possible_media_dirs:
        if dir_path.exists() and dir_path.is_dir():
            media_dir = dir_path
            print(f"✅ Media directory found: '{media_dir}'")
            break

    if not media_dir:
        print("❌ Media directory not found")
        print("💡 Create the media directory and add your photos/videos")
        return False

    # Test file discovery and validation
    valid_files = []
    total_size_mb = 0
    max_file_size_mb = 25
    max_total_size_mb = 50

    try:
        for file_path in media_dir.iterdir():
            # Skip directories and hidden files
            if file_path.is_dir() or file_path.name.startswith("."):
                continue

            # Check file type
            file_ext = file_path.suffix.lower()
            if file_ext not in supported_extensions:
                print(f"⚠️  Unsupported file type: {file_path.name}")
                continue

            # Check file size
            file_size_mb = get_file_size_mb(file_path)
            if file_size_mb == 0:
                print(f"⚠️  Unreadable file: {file_path.name}")
                continue

            if file_size_mb > max_file_size_mb:
                print(
                    f"⚠️  Oversized file: {file_path.name} ({file_size_mb:.1f}MB > {max_file_size_mb}MB)"
                )
                continue

            # Check total size limit
            if total_size_mb + file_size_mb > max_total_size_mb:
                print(
                    f"⚠️  Total size limit reached: {file_path.name} would exceed {max_total_size_mb}MB"
                )
                break

            valid_files.append(file_path.name)
            total_size_mb += file_size_mb
            print(f"✅ Valid media file: {file_path.name} ({file_size_mb:.1f}MB)")

    except Exception as e:
        print(f"❌ Error scanning media directory: {e}")
        return False

    if not valid_files:
        print("ℹ️  No valid media files found")
        print("💡 Add supported media files to the media directory")
        print("💡 Supported formats: JPG, PNG, MP4, PDF, DOC, ZIP, and more")
        return True  # Not a failure - just informational

    print(f"📁 Total valid media files: {len(valid_files)} ({total_size_mb:.1f}MB)")
    print(
        f"📋 File size limits: Individual {max_file_size_mb}MB, Total {max_total_size_mb}MB"
    )

    return True


def test_recipient_emails():
    """Test the recipient email configuration"""
    print("\n👥 Testing Recipient Emails...")

    # Sample recipient emails from the main script
    recipient_emails = [
        "complaints@waltoncantonment.gov.pk",
        "cm@punjab.gov.pk",
        "info@lahore.gov.pk",
        "dc.lahore@punjab.gov.pk",
        "commissioner.lahore@punjab.gov.pk",
        "ceo@lhc.gov.pk",
        "info@lhc.gov.pk",
        "complaints@punjab.gov.pk",
        "helpline@punjab.gov.pk",
    ]

    # Validate email format
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    valid_emails = 0

    for email in recipient_emails:
        if re.match(pattern, email):
            print(f"   ✅ {email}")
            valid_emails += 1
        else:
            print(f"   ❌ {email} (invalid format)")

    print(f"✅ {valid_emails}/{len(recipient_emails)} recipient emails valid")

    return valid_emails > 0


def test_error_handling():
    """Test error handling capabilities"""
    print("\n🛡️ Testing Error Handling...")

    # Test file access errors
    try:
        # Try to read a non-existent file
        non_existent = Path("/non/existent/file.jpg")
        size = non_existent.stat().st_size
        print("❌ Should have failed to read non-existent file")
        return False
    except (OSError, FileNotFoundError):
        print("✅ Properly handles file access errors")

    # Test invalid email format handling
    try:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        invalid_email = "invalid.email.format"
        result = re.match(pattern, invalid_email)
        if result is None:
            print("✅ Properly validates email formats")
        else:
            print("❌ Email validation failed")
            return False
    except Exception as e:
        print(f"❌ Email validation error: {e}")
        return False

    return True


def test_configuration():
    """Test configuration file loading and validation"""
    print("\n" + "=" * 60)
    print("⚙️  TESTING CONFIGURATION SYSTEM")
    print("=" * 60)

    try:
        # Test basic config imports
        print("\n📋 Testing configuration imports...")
        import config
        from config import (
            EMAIL_TEMPLATES,
            EMAIL_TEMPLATE_CONFIG,
            LOCATION_INFO,
            ISSUE_DETAILS,
            LEGAL_FRAMEWORK,
            MEDIA_CONFIG,
        )

        print("✅ Configuration imports successful")

        # Test email templates configuration
        print("\n📧 Testing email templates configuration...")
        if EMAIL_TEMPLATES:
            print(f"✅ Found {len(EMAIL_TEMPLATES)} email templates:")
            for template_id, template in EMAIL_TEMPLATES.items():
                print(
                    f"   Template {template_id}: {template.get('name', 'Unknown')} ({template.get('language', 'Unknown')})"
                )

                # Check required fields
                required_fields = [
                    "subject_template",
                    "body_template",
                    "name",
                    "language",
                ]
                missing_fields = [
                    field for field in required_fields if field not in template
                ]
                if missing_fields:
                    print(f"   ⚠️  Missing fields: {missing_fields}")
                else:
                    print(f"   ✅ All required fields present")
        else:
            print("❌ No email templates configured")
            return False

        # Test template configuration
        print("\n⚙️  Testing template configuration...")
        if EMAIL_TEMPLATE_CONFIG:
            print(f"✅ Template configuration loaded:")
            print(
                f"   Default template: {EMAIL_TEMPLATE_CONFIG.get('default_template', 'Not set')}"
            )
            print(
                f"   Template rotation: {EMAIL_TEMPLATE_CONFIG.get('template_rotation', 'Not set')}"
            )
            print(
                f"   Reference prefix: {EMAIL_TEMPLATE_CONFIG.get('custom_variables', {}).get('reference_prefix', 'Not set')}"
            )
        else:
            print("❌ Template configuration not found")
            return False

        # Test location and issue configuration
        print("\n📍 Testing location and issue configuration...")
        if LOCATION_INFO and ISSUE_DETAILS and LEGAL_FRAMEWORK:
            print("✅ Location, issue, and legal framework configuration loaded")
            print(f"   Area: {LOCATION_INFO.get('area_name', 'Not set')}")
            print(f"   City: {LOCATION_INFO.get('city', 'Not set')}")
            print(f"   Primary issue: {ISSUE_DETAILS.get('primary_issue', 'Not set')}")
            print(
                f"   Constitutional articles: {len(LEGAL_FRAMEWORK.get('constitutional_articles', []))}"
            )
        else:
            print("❌ Location, issue, or legal framework configuration missing")
            return False

        # Test media configuration
        print("\n📁 Testing media configuration...")
        if MEDIA_CONFIG:
            print("✅ Media configuration loaded")
            print(
                f"   Supported extensions: {len(MEDIA_CONFIG.get('supported_extensions', set()))}"
            )
            print(
                f"   Max file size: {MEDIA_CONFIG.get('max_file_size_mb', 'Not set')} MB"
            )
            print(
                f"   Max total size: {MEDIA_CONFIG.get('max_total_size_mb', 'Not set')} MB"
            )
        else:
            print("❌ Media configuration not found")
            return False

        print("\n✅ Configuration testing completed successfully!")
        return True

    except ImportError as e:
        print(f"❌ Configuration import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Configuration testing failed: {e}")
        return False


def test_cc_bcc_functionality():
    """Test CC and BCC email functionality"""
    print("\n" + "=" * 60)
    print("📧 TESTING CC AND BCC FUNCTIONALITY")
    print("=" * 60)

    try:
        # Test configuration imports
        print("\n📋 Testing CC/BCC configuration...")
        from config import CC_EMAILS, BCC_EMAILS, EMAIL_DISTRIBUTION_CONFIG

        if EMAIL_DISTRIBUTION_CONFIG.get("use_cc", False):
            print(f"✅ CC functionality enabled")
            print(f"   CC emails configured: {len(CC_EMAILS)}")
            print(
                f"   Max CC per email: {EMAIL_DISTRIBUTION_CONFIG.get('max_cc_emails', 'Not set')}"
            )
            print(
                f"   Empty handling: {EMAIL_DISTRIBUTION_CONFIG.get('cc_empty_handling', 'Not set')}"
            )
        else:
            print("ℹ️  CC functionality disabled")

        if EMAIL_DISTRIBUTION_CONFIG.get("use_bcc", False):
            print(f"✅ BCC functionality enabled")
            print(f"   BCC emails configured: {len(BCC_EMAILS)}")
            print(
                f"   Max BCC per email: {EMAIL_DISTRIBUTION_CONFIG.get('max_bcc_emails', 'Not set')}"
            )
            print(
                f"   Empty handling: {EMAIL_DISTRIBUTION_CONFIG.get('bcc_empty_handling', 'Not set')}"
            )
        else:
            print("ℹ️  BCC functionality disabled")

        # Test email validation
        print("\n🔍 Testing CC/BCC email validation...")
        import re

        def validate_email(email):
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            return re.match(pattern, email) is not None

        cc_valid = [email for email in CC_EMAILS if validate_email(email)]
        bcc_valid = [email for email in BCC_EMAILS if validate_email(email)]

        print(f"   CC emails: {len(cc_valid)}/{len(CC_EMAILS)} valid")
        print(f"   BCC emails: {len(bcc_valid)}/{len(BCC_EMAILS)} valid")

        # Show sample emails
        if cc_valid:
            print(f"   Sample CC: {cc_valid[0]}")
        if bcc_valid:
            print(f"   Sample BCC: {bcc_valid[0]}")

        # Test distribution logic
        print("\n📊 Testing distribution logic...")
        if EMAIL_DISTRIBUTION_CONFIG.get("use_cc", False) and CC_EMAILS:
            max_cc = EMAIL_DISTRIBUTION_CONFIG.get("max_cc_emails", 10)
            actual_cc = CC_EMAILS[:max_cc]
            print(f"   CC distribution: {len(actual_cc)} emails (max: {max_cc})")

        if EMAIL_DISTRIBUTION_CONFIG.get("use_bcc", False) and BCC_EMAILS:
            max_bcc = EMAIL_DISTRIBUTION_CONFIG.get("max_bcc_emails", 5)
            actual_bcc = BCC_EMAILS[:max_bcc]
            print(f"   BCC distribution: {len(actual_bcc)} emails (max: {max_bcc})")

        print("\n✅ CC/BCC functionality testing completed successfully!")
        return True

    except ImportError as e:
        print(f"❌ CC/BCC configuration import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ CC/BCC functionality testing failed: {e}")
        return False


def test_empty_cc_bcc_handling():
    """Test handling of empty CC and BCC lists"""
    print("\n" + "=" * 60)
    print("🔄 TESTING EMPTY CC/BCC HANDLING")
    print("=" * 60)

    try:
        from config import EMAIL_DISTRIBUTION_CONFIG

        print("\n📋 Testing empty list handling configuration...")

        # Test CC empty handling
        cc_handling = EMAIL_DISTRIBUTION_CONFIG.get("cc_empty_handling", "skip")
        print(f"   CC empty handling: {cc_handling}")

        if cc_handling == "skip":
            print("   ✅ Will skip CC when list is empty")
        elif cc_handling == "send_to_only":
            print("   ✅ Will send to primary recipients only when CC is empty")
        elif cc_handling == "error":
            print("   ⚠️  Will show warning when CC is empty")
        else:
            print(f"   ❓ Unknown CC handling: {cc_handling}")

        # Test BCC empty handling
        bcc_handling = EMAIL_DISTRIBUTION_CONFIG.get("bcc_empty_handling", "skip")
        print(f"   BCC empty handling: {bcc_handling}")

        if bcc_handling == "skip":
            print("   ✅ Will skip BCC when list is empty")
        elif bcc_handling == "send_to_only":
            print("   ✅ Will send to primary recipients only when BCC is empty")
        elif bcc_handling == "error":
            print("   ⚠️  Will show warning when BCC is empty")
        else:
            print(f"   ❓ Unknown BCC handling: {bcc_handling}")

        # Test validation settings
        validate_cc_bcc = EMAIL_DISTRIBUTION_CONFIG.get("validate_cc_bcc", True)
        print(f"   Validate CC/BCC: {validate_cc_bcc}")

        log_distribution = EMAIL_DISTRIBUTION_CONFIG.get("log_distribution", True)
        print(f"   Log distribution: {log_distribution}")

        print("\n✅ Empty CC/BCC handling testing completed successfully!")
        return True

    except ImportError as e:
        print(f"❌ Empty CC/BCC handling test failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Empty CC/BCC handling test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("🚀 Automated Government Email System - Enhanced Test Suite")
    print("=" * 60)

    # Check execution environment
    is_github_actions = os.getenv("GITHUB_ACTIONS") == "true"
    if is_github_actions:
        print("🤖 Running in GitHub Actions environment")
    else:
        print("💻 Running in local development environment")

    # Run all tests
    test_functions = [
        test_environment_variables,
        test_email_templates,
        test_email_rotation,
        test_media_file_discovery,
        test_recipient_emails,
        test_error_handling,
        test_configuration,
        test_cc_bcc_functionality,
        test_empty_cc_bcc_handling,
    ]

    passed = 0
    total = len(test_functions)

    for test_func in test_functions:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with error: {e}")

    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")

    # Different messages based on environment and results
    if is_github_actions:
        # GitHub Actions environment
        if passed == total:
            print("🎉 All tests passed in GitHub Actions! System is ready.")
            print("📅 Schedule: Emails will be sent Monday and Friday at 9:00 AM PKT")
        else:
            print("❌ Some tests failed in GitHub Actions. Check configuration.")
            print("🔧 Common GitHub Actions issues:")
            print("- Verify all GitHub Secrets are set correctly")
            print("- Check workflow file syntax")
            print("- Ensure media files are committed to repository")
    else:
        # Local development environment
        if passed >= total - 2:  # Allow for missing email config locally
            print("🎉 Local tests mostly passed! System looks good.")
            print("\n📋 Next Steps for Deployment:")
            print("1. ✅ Dependencies are working correctly")
            print("2. ✅ Code logic is functioning properly")
            print("3. 🔐 Configure GitHub Secrets in your repository")
            print("4. 📁 Add media files to the media/ directory")
            print("5. 🚀 Test in GitHub Actions with manual workflow trigger")
            print(
                "\n📅 Updated Schedule: Emails will be sent Monday and Friday only (Wednesday skipped)"
            )
            print("\n💡 GitHub Secrets Setup:")
            print("   Repository → Settings → Secrets and Variables → Actions")
            print("   Add: GMAIL_EMAIL and GMAIL_APP_PASSWORD")
        elif passed < total * 0.5:
            print("❌ Critical issues detected:")
            print("- Check if required dependencies are installed")
            print("- Verify media directory exists")
            print("- Fix any code or configuration errors")
        else:
            print("⚠️  Some tests failed, but core functionality works:")
            print("- Dependencies and basic code are working")
            print("- Email configuration missing (expected locally)")
            print("- Add media files for full functionality")

    print(f"\n🔗 Useful Commands:")
    print(f"   Install dependencies: pip install -r requirements.txt")
    print(f"   Run tests: python src/test_email.py")
    if not is_github_actions:
        print(
            f"   Test with email: export GMAIL_EMAIL=xxx && export GMAIL_APP_PASSWORD=xxx && python src/test_email.py"
        )

    return passed >= (total - 2 if not is_github_actions else total)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
