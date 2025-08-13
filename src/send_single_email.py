"""
Automated Government Email Scheduler with HTML Support
Sends automated emails to government officials about road conditions
in Bedian Road & Ali View Garden area, Lahore.
"""

import os
import smtplib
import random
import time
import re
from pathlib import Path
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import schedule
import pytz

# Import configuration
try:
    from config import (
        RECIPIENT_EMAILS,
        ANTI_SPAM_CONFIG,
        EMAIL_TEMPLATES,
        EMAIL_TEMPLATE_CONFIG,
        LOCATION_INFO,
        ISSUE_DETAILS,
        LEGAL_FRAMEWORK,
        CC_EMAILS,
        BCC_EMAILS,
        EMAIL_DISTRIBUTION_CONFIG,
    )
except ImportError:
    # Fallback configuration if config.py is not available
    RECIPIENT_EMAILS = [
        "waltoncb@outlook.com",
        "complaints@cm.punjab.gov.pk",
        "info@idap.pk",
        "dc.lahore@punjab.gov.pk",
        "commissioner.lahore@punjab.gov.pk",
        "complaints@punjab.gov.pk",
        "helpline@punjab.gov.pk",
    ]

    ANTI_SPAM_CONFIG = {
        "min_delay": 10,
        "max_delay": 60,
        "max_attachments": 2,
    }

    EMAIL_TEMPLATES = {
        1: {
            "name": "Basic Complaint Template",
            "language": "English",
            "content_type": "plain",
            "subject_template": "Infrastructure Complaint - {area_name} (Ref: {reference_number})",
            "body_template": "Basic complaint about infrastructure in {area_name}.",
        }
    }

    EMAIL_TEMPLATE_CONFIG = {
        "default_template": 1,
        "template_rotation": True,
        "custom_variables": {"reference_prefix": "ROAD", "response_hours": 48},
        "formatting": {
            "date_format": "%B %d, %Y",
            "time_format": "%I:%M %p PKT",
            "reference_format": "{prefix}-{date}-{random}",
        },
    }

    LOCATION_INFO = {
        "area_name": "Bedian Road & Ali View Garden Area",
        "city": "Lahore",
        "province": "Punjab",
        "country": "Pakistan",
        "coordinates": "31.5204° N, 74.3587° E",
    }

    ISSUE_DETAILS = {
        "primary_issue": "Infrastructure Mismanagement and Neglect",
        "specific_problems": [
            "Poor road conditions",
            "Lack of drainage",
            "No street lighting",
            "Traffic congestion",
        ],
        "affected_population": "Thousands of citizens",
        "duration": "Ongoing for months",
    }

    LEGAL_FRAMEWORK = {
        "constitutional_articles": [
            "Article 9 (Right to Life and Liberty)",
            "Article 25 (Equality of Citizens)",
        ],
        "relevant_laws": [
            "Local Government Act 2013",
            "Punjab Local Government Act 2019",
        ],
        "administrative_bodies": [
            "District Administration Lahore",
            "Punjab Government",
        ],
    }


class GovernmentEmailSender:
    def __init__(self):
        # Email configuration - these will be set via GitHub Secrets
        self.gmail_email = os.getenv("GMAIL_EMAIL")
        self.gmail_password = os.getenv("GMAIL_APP_PASSWORD")
        self.outlook_email = os.getenv("OUTLOOK_EMAIL")
        self.outlook_password = os.getenv("OUTLOOK_PASSWORD")
        self.yahoo_email = os.getenv("YAHOO_EMAIL")
        self.yahoo_password = os.getenv("YAHOO_PASSWORD")

        # Validate and set recipient emails
        self.recipient_emails = self._validate_recipient_emails(RECIPIENT_EMAILS)

        # Validate and set CC emails
        self.cc_emails = (
            self._validate_cc_emails(CC_EMAILS)
            if EMAIL_DISTRIBUTION_CONFIG.get("use_cc", False)
            else []
        )

        # Validate and set BCC emails
        self.bcc_emails = (
            self._validate_bcc_emails(BCC_EMAILS)
            if EMAIL_DISTRIBUTION_CONFIG.get("use_bcc", False)
            else []
        )

        # Email distribution configuration
        self.email_distribution_config = EMAIL_DISTRIBUTION_CONFIG

        # Configuration from config.py
        self.anti_spam_config = ANTI_SPAM_CONFIG
        self.email_templates = EMAIL_TEMPLATES
        self.template_config = EMAIL_TEMPLATE_CONFIG
        self.location_info = LOCATION_INFO
        self.issue_details = ISSUE_DETAILS
        self.legal_framework = LEGAL_FRAMEWORK

        # Set up timezone
        self.pakistan_tz = pytz.timezone("Asia/Karachi")

        # Build email services list - only include configured services
        self.email_services = self._build_email_services()

        # Check if at least one email service is configured
        if not self.email_services:
            raise ValueError(
                "No email services configured. Please set up at least one email account in GitHub Secrets."
            )

        # Email attachment configuration
        self.max_file_size_mb = 25  # Maximum file size in MB
        self.max_total_size_mb = 50  # Maximum total attachment size in MB
        self.supported_extensions = {
            # Images
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".tiff",
            ".webp",
            # Videos
            ".mp4",
            ".avi",
            ".mov",
            ".wmv",
            ".flv",
            ".webm",
            ".mkv",
            # Documents
            ".pdf",
            ".doc",
            ".docx",
            ".txt",
            ".rtf",
            # Archives
            ".zip",
            ".rar",
            ".7z",
        }

        # Cache for file sizes to avoid repeated calculations
        self._file_size_cache = {}

        # Print available templates
        available_templates = self.get_available_templates()
        if available_templates:
            print(f"📧 Available email templates: {len(available_templates)}")
            for template in available_templates:
                print(f"   {template['description']}")

        # Print email distribution configuration
        print(f"📧 Email Distribution Configuration:")
        print(f"   Primary recipients: {len(self.recipient_emails)}")
        print(
            f"   CC recipients: {len(self.cc_emails)} (enabled: {self.email_distribution_config.get('use_cc', False)})"
        )
        print(
            f"   BCC recipients: {len(self.bcc_emails)} (enabled: {self.email_distribution_config.get('use_bcc', False)})"
        )

        print("✅ GovernmentEmailSender initialized successfully")

    def get_available_templates(self):
        """Get list of available email templates"""
        try:
            templates = []
            for template_id, template in self.email_templates.items():
                content_type = template.get("content_type", "plain")
                templates.append(
                    {
                        "id": template_id,
                        "name": template.get("name", f"Template {template_id}"),
                        "language": template.get("language", "Unknown"),
                        "content_type": content_type,
                        "description": f"Template {template_id}: {template.get('name', 'Unknown')} in {template.get('language', 'Unknown')} ({content_type.upper()})",
                    }
                )
            return templates
        except Exception as e:
            print(f"❌ Error getting available templates: {e}")
            return []

    def _validate_email(self, email):
        """Validate email address format"""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def _validate_recipient_emails(self, emails):
        """Validate all recipient email addresses"""
        valid_emails = []
        for email in emails:
            if self._validate_email(email):
                valid_emails.append(email)
            else:
                print(f"⚠️  Invalid email address skipped: {email}")

        if not valid_emails:
            raise ValueError("No valid recipient email addresses found")

        return valid_emails

    def _validate_cc_emails(self, emails):
        """Validate all CC email addresses"""
        valid_emails = []
        for email in emails:
            if self._validate_email(email):
                valid_emails.append(email)
            else:
                print(f"⚠️  Invalid CC email address skipped: {email}")
        return valid_emails

    def _validate_bcc_emails(self, emails):
        """Validate all BCC email addresses"""
        valid_emails = []
        for email in emails:
            if self._validate_email(email):
                valid_emails.append(email)
            else:
                print(f"⚠️  Invalid BCC email address skipped: {email}")
        return valid_emails

    def _get_email_distribution_list(self):
        """Get the complete email distribution list with proper handling of empty CC/BCC"""
        distribution_config = self.email_distribution_config

        # Start with primary recipients
        all_recipients = self.recipient_emails.copy()
        cc_list = []
        bcc_list = []

        # Handle CC emails
        if distribution_config.get("use_cc", False) and self.cc_emails:
            cc_list = self.cc_emails[: distribution_config.get("max_cc_emails", 10)]
            print(f"📧 CC emails: {len(cc_list)} recipients")
        elif distribution_config.get("use_cc", False) and not self.cc_emails:
            cc_handling = distribution_config.get("cc_empty_handling", "skip")
            if cc_handling == "error":
                print(
                    "⚠️  CC emails enabled but none configured - continuing with primary recipients only"
                )
            elif cc_handling == "send_to_only":
                print("ℹ️  CC emails empty - sending to primary recipients only")

        # Handle BCC emails
        if distribution_config.get("use_bcc", False) and self.bcc_emails:
            bcc_list = self.bcc_emails[: distribution_config.get("max_bcc_emails", 5)]
            print(f"📧 BCC emails: {len(bcc_list)} recipients")
        elif distribution_config.get("use_bcc", False) and not self.bcc_emails:
            bcc_handling = distribution_config.get("bcc_empty_handling", "skip")
            if bcc_handling == "error":
                print(
                    "⚠️  BCC emails enabled but none configured - continuing with primary recipients only"
                )
            elif bcc_handling == "send_to_only":
                print("ℹ️  BCC emails empty - sending to primary recipients only")

        # Log distribution details if enabled
        if distribution_config.get("log_distribution", False):
            print(f"📊 Email Distribution Summary:")
            print(f"   TO: {len(all_recipients)} recipients")
            print(f"   CC: {len(cc_list)} recipients")
            print(f"   BCC: {len(bcc_list)} recipients")
            print(
                f"   Total: {len(all_recipients) + len(cc_list) + len(bcc_list)} recipients"
            )

        return {
            "to": all_recipients,
            "cc": cc_list,
            "bcc": bcc_list,
            "total": len(all_recipients) + len(cc_list) + len(bcc_list),
        }

    def _setup_email_headers(self, msg, service, template):
        """Set up email headers including CC and BCC"""
        distribution = self._get_email_distribution_list()

        # Set basic headers
        msg["From"] = service["email"]
        msg["To"] = ", ".join(distribution["to"])

        # Set CC header if CC emails exist
        if distribution["cc"]:
            msg["Cc"] = ", ".join(distribution["cc"])

        # Set subject
        msg["Subject"] = template["subject"]

        # Note: BCC recipients are not visible in headers for privacy
        return distribution

    def _build_email_services(self):
        """Build list of available email services with validation"""
        services = []

        # Add Gmail if configured
        if self.gmail_email and self.gmail_password:
            if self._validate_email(self.gmail_email):
                services.append(
                    {
                        "name": "Gmail",
                        "email": self.gmail_email,
                        "password": self.gmail_password,
                        "smtp_server": "smtp.gmail.com",
                        "smtp_port": 587,
                    }
                )
            else:
                print(f"⚠️  Invalid Gmail address: {self.gmail_email}")

        # Add Outlook if configured
        if self.outlook_email and self.outlook_password:
            if self._validate_email(self.outlook_email):
                services.append(
                    {
                        "name": "Outlook",
                        "email": self.outlook_email,
                        "password": self.outlook_password,
                        "smtp_server": "smtp-mail.outlook.com",
                        "smtp_port": 587,
                    }
                )
            else:
                print(f"⚠️  Invalid Outlook address: {self.outlook_email}")

        # Add Yahoo if configured
        if self.yahoo_email and self.yahoo_password:
            if self._validate_email(self.yahoo_email):
                services.append(
                    {
                        "name": "Yahoo",
                        "email": self.yahoo_email,
                        "password": self.yahoo_password,
                        "smtp_server": "smtp.mail.yahoo.com",
                        "smtp_port": 587,
                    }
                )
            else:
                print(f"⚠️  Invalid Yahoo address: {self.yahoo_email}")

        return services

    def get_current_time_pakistan(self):
        """Get current time in Pakistan timezone"""
        utc_now = datetime.now(pytz.UTC)
        pakistan_time = utc_now.astimezone(self.pakistan_tz)
        return pakistan_time

    def generate_reference_number(self):
        """Generate a unique reference number"""
        today = self.get_current_time_pakistan()
        prefix = self.template_config["custom_variables"]["reference_prefix"]
        date_str = today.strftime("%Y%m%d")
        random_num = random.randint(1000, 9999)
        return f"{prefix}-{date_str}-{random_num}"

    def format_template_variables(self, template_text, reference_number):
        """Format template with actual values"""
        today = self.get_current_time_pakistan()

        # Prepare variables for template formatting
        variables = {
            "reference_number": reference_number,
            "date_formatted": today.strftime(
                self.template_config["formatting"]["date_format"]
            ),
            "time_formatted": today.strftime(
                self.template_config["formatting"]["time_format"]
            ),
            "area_name": self.location_info["area_name"],
            "city": self.location_info["city"],
            "province": self.location_info["province"],
            "country": self.location_info["country"],
            "primary_issue": self.issue_details["primary_issue"],
            "affected_population": self.issue_details["affected_population"],
            "constitutional_articles": ", ".join(
                self.legal_framework["constitutional_articles"]
            ),
            "relevant_laws": ", ".join(self.legal_framework["relevant_laws"]),
            "administrative_bodies": ", ".join(
                self.legal_framework.get("administrative_bodies", [])
            ),
        }

        # Format specific problems as bullet points
        specific_problems = self.issue_details["specific_problems"]
        variables["specific_problems_formatted"] = "\n".join(
            [f"• {problem}" for problem in specific_problems]
        )

        # Format constitutional articles as bullet points
        constitutional_articles = self.legal_framework["constitutional_articles"]
        variables["constitutional_articles_formatted"] = "\n".join(
            [f"• {article}" for article in constitutional_articles]
        )

        # Format relevant laws as bullet points
        relevant_laws = self.legal_framework["relevant_laws"]
        variables["relevant_laws_formatted"] = "\n".join(
            [f"• {law}" for law in relevant_laws]
        )

        # Format administrative bodies as bullet points
        admin_bodies = self.legal_framework.get("administrative_bodies", [])
        variables["administrative_bodies_formatted"] = "\n".join(
            [f"• {body}" for body in admin_bodies]
        )

        try:
            return template_text.format(**variables)
        except KeyError as e:
            print(f"⚠️  Template variable missing: {e}")
            return template_text

    def get_email_template(self, template_type):
        """Get email template based on type (1, 2, or 3) with HTML support"""
        reference_number = self.generate_reference_number()

        # Get template from configuration
        if template_type not in self.email_templates:
            print(f"⚠️  Template type {template_type} not found, using default")
            template_type = self.template_config["default_template"]

        template_config = self.email_templates[template_type]

        # Format subject and body with variables
        subject = self.format_template_variables(
            template_config["subject_template"], reference_number
        )
        body = self.format_template_variables(
            template_config["body_template"], reference_number
        )

        return {
            "subject": subject,
            "body": body,
            "language": template_config["language"],
            "name": template_config["name"],
            "content_type": template_config.get("content_type", "plain"),
            "reference_number": reference_number,
        }

    def _create_plain_text_fallback(self, html_content):
        """Create plain text version from HTML content"""
        import re
        
        # Remove HTML tags
        text = re.sub(r'<[^<]+?>', '', html_content)
        
        # Replace HTML entities
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&amp;', '&')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&quot;', '"')
        text = text.replace('&#x27;', "'")
        
        # Clean up multiple spaces and newlines
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r' +', ' ', text)
        
        # Clean up extra whitespace around lines
        lines = text.split('\n')
        lines = [line.strip() for line in lines]
        text = '\n'.join(lines)
        
        return text.strip()

    def select_email_service(self):
        """Select email service based on day of year for rotation with proper fallback"""
        if not self.email_services:
            raise ValueError("No email services available")

        if len(self.email_services) == 1:
            return self.email_services[0]

        day_of_year = self.get_current_time_pakistan().timetuple().tm_yday
        service_index = day_of_year % len(self.email_services)
        return self.email_services[service_index]

    def select_template(self):
        """Select template based on day of week for Monday/Friday rotation"""
        if not self.template_config["template_rotation"]:
            return self.template_config["default_template"]

        # Get current day of week (0=Monday, 6=Sunday in isoweekday)
        current_day = self.get_current_time_pakistan().isoweekday()

        # Monday = 1, Friday = 5
        if current_day == 1:  # Monday
            # Use template 1 or 3 (English) for Monday
            return random.choice([1, 3])
        elif current_day == 5:  # Friday
            # Use template 2 (Urdu) for Friday
            return 2
        else:
            # Fallback to default template for any other day
            return self.template_config["default_template"]

    def is_valid_file_type(self, file_path):
        """Check if file type is supported"""
        file_ext = Path(file_path).suffix.lower()
        return file_ext in self.supported_extensions

    def get_file_size_mb(self, file_path):
        """Get file size in MB with caching"""
        if file_path in self._file_size_cache:
            return self._file_size_cache[file_path]

        try:
            size_bytes = Path(file_path).stat().st_size
            size_mb = size_bytes / (1024 * 1024)  # Convert to MB
            self._file_size_cache[file_path] = size_mb
            return size_mb
        except (OSError, FileNotFoundError):
            return 0

    def find_media_directory(self):
        """Find the media directory using proper path resolution"""
        # Get the directory where this script is located
        script_dir = Path(__file__).parent.absolute()

        # Try different possible media directory paths
        possible_media_dirs = [
            script_dir.parent / "media",  # ../media from src/
            script_dir / "media",  # ./media from src/
            Path.cwd() / "media",  # media from current working directory
        ]

        for media_dir in possible_media_dirs:
            if media_dir.exists() and media_dir.is_dir():
                print(f"✅ Media directory found: {media_dir}")
                return media_dir

        print("❌ Media directory not found")
        return None

    def discover_media_files(self):
        """Discover all valid media files in the media directory"""
        media_dir = self.find_media_directory()

        if not media_dir:
            print("Media directory not found. Skipping attachments.")
            return []

        valid_files = []
        total_size_mb = 0

        try:
            for file_path in media_dir.iterdir():
                # Skip directories and hidden files
                if file_path.is_dir() or file_path.name.startswith("."):
                    continue

                # Check file type
                if not self.is_valid_file_type(file_path):
                    print(f"⚠️  Skipping unsupported file type: {file_path.name}")
                    continue

                # Check file size
                file_size_mb = self.get_file_size_mb(file_path)
                if file_size_mb == 0:
                    print(f"⚠️  Skipping unreadable file: {file_path.name}")
                    continue

                if file_size_mb > self.max_file_size_mb:
                    print(
                        f"⚠️  Skipping oversized file: {file_path.name} ({file_size_mb:.1f}MB > {self.max_file_size_mb}MB)"
                    )
                    continue

                # Check total size limit
                if total_size_mb + file_size_mb > self.max_total_size_mb:
                    print(
                        f"⚠️  Total attachment size limit reached ({total_size_mb:.1f}MB + {file_size_mb:.1f}MB > {self.max_total_size_mb}MB)"
                    )
                    break

                valid_files.append(str(file_path))
                total_size_mb += file_size_mb
                print(
                    f"✅ Found valid media file: {file_path.name} ({file_size_mb:.1f}MB)"
                )

        except Exception as e:
            print(f"❌ Error scanning media directory: {e}")
            return []

        print(
            f"📁 Total media files to attach: {len(valid_files)} ({total_size_mb:.1f}MB)"
        )
        return valid_files

    def attach_media_files(self, msg):
        """Attach all valid media files to email"""
        media_files = self.discover_media_files()

        if not media_files:
            print("No valid media files found. Sending email without attachments.")
            return

        attached_count = 0
        for file_path in media_files:
            try:
                file_path_obj = Path(file_path)
                with open(file_path_obj, "rb") as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {file_path_obj.name}",
                    )
                    msg.attach(part)
                attached_count += 1
                print(f"✅ Attached: {file_path_obj.name}")
            except (FileNotFoundError, PermissionError, OSError) as e:
                print(f"❌ Failed to attach {Path(file_path).name}: {e}")
            except Exception as e:
                print(f"❌ Unexpected error attaching {Path(file_path).name}: {e}")

        print(
            f"📎 Successfully attached {attached_count}/{len(media_files)} media files"
        )

    def send_email(self, service, template):
        """Send email using specified service and template with HTML support"""
        try:
            content_type = template.get("content_type", "plain")
            
            # Create multipart message for better compatibility
            if content_type == "html":
                msg = MIMEMultipart('alternative')
                print(f"📧 Creating multipart HTML email")
            else:
                msg = MIMEMultipart()
                print(f"📧 Creating plain text email")

            # Set headers and distribution
            distribution = self._setup_email_headers(msg, service, template)

            # Add email content based on type
            if content_type == "html":
                # Create plain text fallback
                plain_text = self._create_plain_text_fallback(template["body"])
                
                # Add plain text version (fallback)
                part1 = MIMEText(plain_text, 'plain', 'utf-8')
                msg.attach(part1)
                
                # Add HTML version (preferred)
                part2 = MIMEText(template["body"], 'html', 'utf-8')
                msg.attach(part2)
                
                print(f"✅ Added HTML content with plain text fallback")
            else:
                # Plain text only
                msg.attach(MIMEText(template["body"], "plain", "utf-8"))
                print(f"✅ Added plain text content")

            # Attach media files
            self.attach_media_files(msg)

            # Connect to SMTP server with specific error handling
            try:
                server = smtplib.SMTP(service["smtp_server"], service["smtp_port"], timeout=60)
                server.ehlo()  # Identify ourselves
                server.starttls()  # Enable encryption
                server.ehlo()  # Re-identify as encrypted connection
                print(f"✅ Connected to {service['name']} SMTP server")
            except (smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected) as e:
                print(f"❌ Failed to connect to {service['name']} SMTP server: {e}")
                return False
            except Exception as e:
                print(f"❌ Unexpected connection error with {service['name']}: {e}")
                return False

            # Authenticate
            try:
                server.login(service["email"], service["password"])
                print(f"✅ Authenticated with {service['name']}")
            except smtplib.SMTPAuthenticationError as e:
                print(f"❌ Authentication failed for {service['name']}: {e}")
                server.quit()
                return False
            except Exception as e:
                print(f"❌ Unexpected authentication error with {service['name']}: {e}")
                server.quit()
                return False

            # Send email
            try:
                text = msg.as_string()
                all_recipients = distribution["to"] + distribution["cc"] + distribution["bcc"]
                server.sendmail(service["email"], all_recipients, text)
                server.quit()
                print(f"✅ Email sent successfully")
            except smtplib.SMTPRecipientsRefused as e:
                print(f"❌ Recipients refused by {service['name']}: {e}")
                server.quit()
                return False
            except smtplib.SMTPDataError as e:
                print(f"❌ Data error with {service['name']}: {e}")
                server.quit()
                return False
            except Exception as e:
                print(f"❌ Unexpected error sending email with {service['name']}: {e}")
                server.quit()
                return False

            print(f"📧 Service: {service['name']}")
            print(f"📧 Template: {template['name']} ({template['language']}) - {content_type.upper()}")
            print(f"📧 Subject: {template['subject'][:50]}...")
            print(f"👥 Recipients: {distribution['total']}")
            return True

        except Exception as e:
            print(f"❌ Unexpected error in send_email: {e}")
            return False

    def send_daily_emails(self):
        """Main function to send emails with rotation and anti-spam features"""
        current_time = self.get_current_time_pakistan()
        print(
            f"\n🚀 Starting email campaign - {current_time.strftime('%Y-%m-%d %H:%M:%S PKT')}"
        )

        # Select email service and template
        try:
            service = self.select_email_service()
            template_type = self.select_template()
            template = self.get_email_template(template_type)
        except Exception as e:
            print(f"❌ Error in email/template selection: {e}")
            return False

        print(f"📧 Using service: {service['name']}")
        print(
            f"📝 Using template: {template['name']} (Type {template_type}, {template['language']}, {template.get('content_type', 'plain').upper()})"
        )
        print(f"📧 Available services: {len(self.email_services)}")
        print(
            f"📍 Location: {self.location_info['area_name']}, {self.location_info['city']}"
        )

        # Send email
        success = self.send_email(service, template)

        if success:
            print("✅ Email campaign completed successfully")
        else:
            print("❌ Email campaign failed")

        # Random delay to avoid detection
        delay = random.randint(
            self.anti_spam_config["min_delay"], self.anti_spam_config["max_delay"]
        )
        print(f"⏱️ Waiting {delay} seconds before next operation...")
        time.sleep(delay)

        return success

    # Fallback template for testing without configuration
    def _get_fallback_template(self, template_type):
        """Get a fallback template for testing purposes"""
        reference_number = self.generate_reference_number()
        
        fallback_template = {
            "subject": f"Test Email Template {template_type} (Ref: {reference_number})",
            "body": f"""
Test Email Template {template_type}

This is a test email to verify the email system is working correctly.

Reference: {reference_number}
Time: {self.get_current_time_pakistan().strftime('%Y-%m-%d %H:%M:%S PKT')}
Template Type: {template_type}

This email system sends automated complaints to government officials about 
infrastructure issues in Bedian Road & Ali View Garden Area, Lahore.

Best regards,
Automated Email System
            """.strip(),
            "language": "English",
            "name": f"Fallback Template {template_type}",
            "content_type": "plain",
            "reference_number": reference_number,
        }
        
        return fallback_template


def main():
    """Main function to run the email sender"""
    try:
        sender = GovernmentEmailSender()

        # Check if running in GitHub Actions or locally
        if os.getenv("GITHUB_ACTIONS"):
            # GitHub Actions mode - send once
            print("🤖 Running in GitHub Actions mode")
            success = sender.send_daily_emails()
            return success
        else:
            # Local mode - schedule for Monday and Friday only
            print("💻 Running in local mode - scheduling emails for Monday and Friday")
            schedule.every().monday.at("09:00").do(sender.send_daily_emails)
            schedule.every().friday.at("09:00").do(sender.send_daily_emails)

            print(
                "📅 Scheduled: Emails will be sent every Monday and Friday at 9:00 AM PKT"
            )
            print("⏸️  Wednesday emails have been disabled as requested")

            while True:
                schedule.run_pending()
                time.sleep(60)
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error initializing email sender: {e}")
        return False


if __name__ == "__main__":
    success = main()
    if os.getenv("GITHUB_ACTIONS"):
        exit(0 if success else 1)