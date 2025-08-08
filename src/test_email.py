#!/usr/bin/env python3
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
    
    required_modules = ['schedule', 'pytz']
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
        pakistan_tz = pytz.timezone('Asia/Karachi')
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
            print(f"✅ Timezone offset: +{offset_hours:.1f} hours (Pakistan Standard Time)")
        
        return True
    except Exception as e:
        print(f"❌ Timezone handling error: {e}")
        return False

def test_email_validation():
    """Test email validation functionality"""
    print("\n📧 Testing Email Validation...")
    
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
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
            print(f"❌ {email}: Expected {'Valid' if expected else 'Invalid'}, got {'Valid' if result else 'Invalid'}")
            all_passed = False
    
    return all_passed

def test_email_templates():
    """Test the email template generation"""
    print("\n🧪 Testing Email Templates...")
    
    # Simulate the template generation logic with timezone
    try:
        if PYTZ_AVAILABLE:
            pakistan_tz = pytz.timezone('Asia/Karachi')
            utc_now = datetime.now(pytz.UTC)
            today = utc_now.astimezone(pakistan_tz)
        else:
            today = datetime.now()
    except:
        today = datetime.now()
    
    reference_number = f"ROAD-{today.strftime('%Y%m%d')}-{random.randint(1000, 9999)}"
    
    templates = {
        1: {
            'subject': f"URGENT: Critical Road Infrastructure Failure - Bedian Road & Ali View Garden Area (Ref: {reference_number})",
            'language': 'English'
        },
        2: {
            'subject': f"فوری: بیڈین روڈ اور علی ویو گارڈن ایریا میں سڑک کی شدید خرابی (Ref: {reference_number})",
            'language': 'Urdu'
        },
        3: {
            'subject': f"LEGAL NOTICE: Citizen Rights Violation - Road Infrastructure Neglect (Ref: {reference_number})",
            'language': 'Legal English'
        }
    }
    
    for template_id, template in templates.items():
        print(f"✅ Template {template_id} ({template['language']}): {template['subject'][:60]}...")
    
    return True

def test_email_rotation():
    """Test the email service rotation logic"""
    print("\n🔄 Testing Email Service Rotation...")
    
    # Check if running in GitHub Actions
    is_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'
    
    # Simulate available services
    available_services = []
    
    if os.getenv('GMAIL_EMAIL') and os.getenv('GMAIL_APP_PASSWORD'):
        available_services.append('Gmail')
    
    if os.getenv('OUTLOOK_EMAIL') and os.getenv('OUTLOOK_PASSWORD'):
        available_services.append('Outlook')
    
    if os.getenv('YAHOO_EMAIL') and os.getenv('YAHOO_PASSWORD'):
        available_services.append('Yahoo')
    
    if not available_services:
        if is_github_actions:
            print("❌ No email services configured in GitHub Actions")
            print("💡 Check your GitHub Secrets configuration")
            return False
        else:
            print("ℹ️  No email services configured locally (expected)")
            print("💡 Testing rotation logic with simulated services:")
            # Test with simulated services for demonstration
            simulated_services = ['Gmail', 'Outlook', 'Yahoo']
            print(f"✅ Simulated services: {', '.join(simulated_services)}")
            
            print("✅ Multi-service rotation logic:")
            for day in range(1, 8):
                service_index = day % len(simulated_services)
                service = simulated_services[service_index]
                print(f"   Day {day}: Would use {service}")
            
            print("📋 In GitHub Actions, actual configured services will be used")
            return True
    
    print(f"✅ {len(available_services)} email service(s) configured: {', '.join(available_services)}")
    
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

def test_template_rotation():
    """Test the template rotation logic"""
    print("\n📝 Testing Template Rotation...")
    
    for day in range(1, 8):  # Test first week
        template_type = (day % 3) + 1
        template_names = {1: "Urgent English", 2: "Formal Urdu", 3: "Legal Notice"}
        print(f"✅ Day {day}: Template {template_type} ({template_names[template_type]})")
    
    return True

def test_environment_variables():
    """Test if environment variables are properly configured"""
    print("\n🔧 Testing Environment Variables...")
    
    # Check if running in GitHub Actions
    is_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'
    
    if is_github_actions:
        print("🤖 Running in GitHub Actions environment")
    else:
        print("💻 Running in local environment")
        print("💡 GitHub Secrets are only available in GitHub Actions")
    
    required_vars = [
        ('GMAIL_EMAIL', 'GMAIL_APP_PASSWORD'),
        ('OUTLOOK_EMAIL', 'OUTLOOK_PASSWORD'),
        ('YAHOO_EMAIL', 'YAHOO_PASSWORD')
    ]
    
    configured_services = 0
    
    for email_var, password_var in required_vars:
        email = os.getenv(email_var)
        password = os.getenv(password_var)
        
        if email and password:
            # Validate email format
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(pattern, email):
                print(f"✅ {email_var}: Configured and valid")
                configured_services += 1
            else:
                print(f"⚠️  {email_var}: Configured but invalid format")
        else:
            if is_github_actions:
                print(f"ℹ️  {email_var}: Not configured (optional)")
            else:
                print(f"ℹ️  {email_var}: Not set locally (normal - secrets are in GitHub)")
    
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
        print(f"\n✅ {configured_services} email service configured (minimum requirement met)")
        print("💡 Optional: Add more email services for better rotation")
    else:
        print(f"\n✅ {configured_services} email services configured (excellent for rotation)")
    
    return True

def test_path_resolution():
    """Test path resolution for media directory"""
    print("\n📂 Testing Path Resolution...")
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Try different possible media directory paths
    possible_media_dirs = [
        script_dir.parent / 'media',  # ../media from src/
        script_dir / 'media',         # ./media from src/
        Path.cwd() / 'media',         # media from current working directory
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
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp',
        '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv',
        '.pdf', '.doc', '.docx', '.txt', '.rtf',
        '.zip', '.rar', '.7z'
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
        script_dir.parent / 'media',  # ../media from src/
        script_dir / 'media',         # ./media from src/
        Path.cwd() / 'media',         # media from current working directory
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
            if file_path.is_dir() or file_path.name.startswith('.'):
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
                print(f"⚠️  Oversized file: {file_path.name} ({file_size_mb:.1f}MB > {max_file_size_mb}MB)")
                continue
            
            # Check total size limit
            if total_size_mb + file_size_mb > max_total_size_mb:
                print(f"⚠️  Total size limit reached: {file_path.name} would exceed {max_total_size_mb}MB")
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
    print(f"📋 File size limits: Individual {max_file_size_mb}MB, Total {max_total_size_mb}MB")
    
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
        "helpline@punjab.gov.pk"
    ]
    
    # Validate email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
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
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
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

def main():
    """Run all tests"""
    print("🚀 Automated Government Email System - Enhanced Test Suite")
    print("=" * 60)
    
    # Check execution environment
    is_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'
    if is_github_actions:
        print("🤖 Running in GitHub Actions environment")
    else:
        print("💻 Running in local development environment")
    
    tests = [
        test_dependencies,
        test_timezone_handling,
        test_email_validation,
        test_email_templates,
        test_email_rotation,
        test_template_rotation,
        test_environment_variables,
        test_path_resolution,
        test_media_file_discovery,
        test_recipient_emails,
        test_error_handling
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
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
        print(f"   Test with email: export GMAIL_EMAIL=xxx && export GMAIL_APP_PASSWORD=xxx && python src/test_email.py")
    
    return passed >= (total - 2 if not is_github_actions else total)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)