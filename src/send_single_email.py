"""
Automated Government Email Scheduler
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
        TEMPLATE_CONFIG,
        LOCATION_INFO,
        ISSUE_DETAILS,
        LEGAL_FRAMEWORK
    )
except ImportError:
    # Fallback configuration if config.py is not available
    RECIPIENT_EMAILS = [
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
    
    ANTI_SPAM_CONFIG = {
        'min_delay': 10,
        'max_delay': 60,
        'max_attachments': 2,
    }
    
    TEMPLATE_CONFIG = {
        'include_legal_references': True,
        'include_constitutional_rights': True,
        'include_escalation_timeline': True,
        'include_media_attachments': True,
    }
    
    LOCATION_INFO = {
        'area_name': 'Bedian Road & Ali View Garden Area',
        'city': 'Lahore',
        'province': 'Punjab',
        'country': 'Pakistan',
        'coordinates': '31.5204° N, 74.3587° E',
    }
    
    ISSUE_DETAILS = {
        'primary_issue': 'Road Infrastructure Failure',
        'specific_problems': [
            'Massive potholes causing vehicle damage',
            'Complete absence of proper drainage',
            'No street lighting creating security hazards',
            'Traffic congestion affecting emergency response',
            'Economic losses due to vehicle repairs'
        ],
        'affected_population': 'Thousands of citizens',
        'duration': 'Ongoing for months',
    }
    
    LEGAL_FRAMEWORK = {
        'constitutional_articles': [
            'Article 9 (Right to Life)',
            'Article 25 (Right to Equality)',
        ],
        'relevant_laws': [
            'Local Government Act 2013',
            'Punjab Local Government Act 2019',
            'Public Service Delivery Act 2019',
        ],
        'escalation_path': [
            'Provincial Ombudsman',
            'National Accountability Bureau',
            'Media outlets',
            'Court of Law',
        ],
    }

class GovernmentEmailSender:
    def __init__(self):
        # Email configuration - these will be set via GitHub Secrets
        self.gmail_email = os.getenv('GMAIL_EMAIL')
        self.gmail_password = os.getenv('GMAIL_APP_PASSWORD')
        self.outlook_email = os.getenv('OUTLOOK_EMAIL')
        self.outlook_password = os.getenv('OUTLOOK_PASSWORD')
        self.yahoo_email = os.getenv('YAHOO_EMAIL')
        self.yahoo_password = os.getenv('YAHOO_PASSWORD')
        
        # Validate and set recipient emails
        self.recipient_emails = self._validate_recipient_emails(RECIPIENT_EMAILS)
        
        # Configuration from config.py
        self.anti_spam_config = ANTI_SPAM_CONFIG
        self.template_config = TEMPLATE_CONFIG
        self.location_info = LOCATION_INFO
        self.issue_details = ISSUE_DETAILS
        self.legal_framework = LEGAL_FRAMEWORK
        
        # Set up timezone
        self.pakistan_tz = pytz.timezone('Asia/Karachi')
        
        # Build email services list - only include configured services
        self.email_services = self._build_email_services()
        
        # Check if at least one email service is configured
        if not self.email_services:
            raise ValueError("No email services configured. Please set up at least one email account in GitHub Secrets.")
        
        # Email attachment configuration
        self.max_file_size_mb = 25  # Maximum file size in MB
        self.max_total_size_mb = 50  # Maximum total attachment size in MB
        self.supported_extensions = {
            # Images
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp',
            # Videos
            '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv',
            # Documents
            '.pdf', '.doc', '.docx', '.txt', '.rtf',
            # Archives
            '.zip', '.rar', '.7z'
        }
        
        # Cache for file sizes to avoid repeated calculations
        self._file_size_cache = {}

    def _validate_email(self, email):
        """Validate email address format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
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

    def _build_email_services(self):
        """Build list of available email services with validation"""
        services = []
        
        # Add Gmail if configured
        if self.gmail_email and self.gmail_password:
            if self._validate_email(self.gmail_email):
                services.append({
                    'name': 'Gmail',
                    'email': self.gmail_email,
                    'password': self.gmail_password,
                    'smtp_server': 'smtp.gmail.com',
                    'smtp_port': 587
                })
            else:
                print(f"⚠️  Invalid Gmail address: {self.gmail_email}")
        
        # Add Outlook if configured
        if self.outlook_email and self.outlook_password:
            if self._validate_email(self.outlook_email):
                services.append({
                    'name': 'Outlook',
                    'email': self.outlook_email,
                    'password': self.outlook_password,
                    'smtp_server': 'smtp-mail.outlook.com',
                    'smtp_port': 587
                })
            else:
                print(f"⚠️  Invalid Outlook address: {self.outlook_email}")
        
        # Add Yahoo if configured
        if self.yahoo_email and self.yahoo_password:
            if self._validate_email(self.yahoo_email):
                services.append({
                    'name': 'Yahoo',
                    'email': self.yahoo_email,
                    'password': self.yahoo_password,
                    'smtp_server': 'smtp.mail.yahoo.com',
                    'smtp_port': 587
                })
            else:
                print(f"⚠️  Invalid Yahoo address: {self.yahoo_email}")
        
        return services

    def get_current_time_pakistan(self):
        """Get current time in Pakistan timezone"""
        utc_now = datetime.now(pytz.UTC)
        pakistan_time = utc_now.astimezone(self.pakistan_tz)
        return pakistan_time

    def get_email_template(self, template_type):
        """Get email template based on type (1, 2, or 3)"""
        today = self.get_current_time_pakistan()
        reference_number = f"ROAD-{today.strftime('%Y%m%d')}-{random.randint(1000, 9999)}"
        
        # Use configuration data in templates
        area_name = self.location_info['area_name']
        city = self.location_info['city']
        province = self.location_info['province']
        country = self.location_info['country']
        primary_issue = self.issue_details['primary_issue']
        specific_problems = self.issue_details['specific_problems']
        affected_population = self.issue_details['affected_population']
        constitutional_articles = self.legal_framework['constitutional_articles']
        relevant_laws = self.legal_framework['relevant_laws']
        escalation_path = self.legal_framework['escalation_path']
        
        templates = {
            1: {
                'subject': f"URGENT: Critical {primary_issue} - {area_name} (Ref: {reference_number})",
                'body': f"""Dear Government Officials,

I am writing to bring to your immediate attention a critical infrastructure failure that is severely impacting the daily lives of {affected_population} in the {area_name} of {city}.

**EMERGENCY SITUATION:**
The road conditions in our area have deteriorated to such an extent that they now pose serious safety risks to motorists, pedestrians, and emergency vehicles. This situation constitutes a violation of citizens' fundamental rights under {', '.join(constitutional_articles)} of the Constitution of {country}.

**CURRENT CONDITIONS:**
{chr(10).join([f"- {problem}" for problem in specific_problems])}

**COMPARATIVE ANALYSIS:**
While our area suffers from complete neglect, nearby areas like DHA, Gulberg, and Model Town enjoy excellent road infrastructure. This discrimination violates the principle of equal treatment under the law.

**IMMEDIATE ACTION REQUIRED:**
1. Emergency road inspection by qualified engineers
2. Temporary repairs to prevent further accidents
3. Comprehensive road reconstruction plan
4. Installation of proper drainage system
5. Street lighting restoration

**LEGAL FRAMEWORK:**
This complaint is filed under:
{chr(10).join([f"- {article}" for article in constitutional_articles])}
{chr(10).join([f"- {law}" for law in relevant_laws])}

**ESCALATION TIMELINE:**
If no action is taken within 7 days, this matter will be escalated to:
{chr(10).join([f"- {path}" for path in escalation_path])}

**CONTACT INFORMATION:**
Reference Number: {reference_number}
Date: {today.strftime('%B %d, %Y')}
Time: {today.strftime('%I:%M %p PKT')}
Location: {area_name}, {city}, {province}

We expect immediate acknowledgment and action plan within 24 hours.

Sincerely,
Concerned Citizens of {area_name}
{city}, {country}

---
This is an automated complaint system for legitimate civic engagement.
Reference: {reference_number}"""
            },
            
            2: {
                'subject': f"فوری: {area_name} میں {primary_issue} (Ref: {reference_number})",
                'body': f"""محترم حکومتی عہدیداران،

میں آپ کی توجہ فوری طور پر {area_name} {city} میں موجودہ {primary_issue} کی طرف مبذول کروانا چاہتا ہوں جو {affected_population} کی روزمرہ زندگی کو شدید متاثر کر رہی ہے۔

**ہنگامی صورتحال:**
ہمارے علاقے میں سڑک کی حالت اتنی خراب ہو گئی ہے کہ یہ موٹرسائیکل سواروں، پیدل چلنے والوں اور ہنگامی گاڑیوں کے لیے سنگین خطرات کا باعث بن رہی ہے۔ یہ صورتحال {country} کے آئین کے {', '.join(constitutional_articles)} کی خلاف ورزی ہے۔

**موجودہ حالات:**
{chr(10).join([f"- {problem}" for problem in specific_problems])}

**فوری کارروائی مطلوب:**
1. ماہر انجینئرز کی طرف سے ہنگامی معائنہ
2. مزید حادثات کو روکنے کے لیے عارضی مرمت
3. مکمل سڑک کی تعمیر نو کا منصوبہ
4. مناسب نکاسی آب کا نظام
5. سڑک کی روشنی کی بحالی

**رابطہ کی معلومات:**
ریفرنس نمبر: {reference_number}
تاریخ: {today.strftime('%B %d, %Y')}
وقت: {today.strftime('%I:%M %p PKT')}
مقام: {area_name}, {city}, {province}

ہم 24 گھنٹوں کے اندر فوری تسلیم اور کارروائی کا منصوبہ توقع رکھتے ہیں۔

آپ کا مخلص،
{area_name} کے تشویش مند شہری
{city}, {country}

---
یہ جائز شہری مشغولیت کے لیے ایک خودکار شکایت کا نظام ہے۔
ریفرنس: {reference_number}"""
            },
            
            3: {
                'subject': f"LEGAL NOTICE: Citizen Rights Violation - {primary_issue} (Ref: {reference_number})",
                'body': f"""Dear Government Officials,

This communication serves as a formal legal notice regarding the systematic violation of citizen rights through the continued neglect of road infrastructure in the {area_name} of {city}.

**LEGAL BASIS:**
This complaint is filed under the following legal frameworks:
{chr(10).join([f"- Constitution of {country}, {article}" for article in constitutional_articles])}
{chr(10).join([f"- {law}" for law in relevant_laws])}

**VIOLATIONS DOCUMENTED:**
1. **Right to Life Violation**: Dangerous road conditions causing accidents
2. **Right to Equality Violation**: Discriminatory infrastructure development
3. **Public Service Failure**: Inadequate road maintenance and repair
4. **Economic Rights Violation**: Financial losses due to vehicle damage
5. **Safety Rights Violation**: Lack of street lighting and drainage

**DOCUMENTED EVIDENCE:**
- Photographic evidence of road conditions
- Video documentation of flooding and potholes
- Comparative analysis with other areas
- Economic impact assessment
- Safety hazard documentation

**LEGAL REMEDIES SOUGHT:**
1. Immediate road inspection and temporary repairs
2. Comprehensive infrastructure development plan
3. Equal treatment with other areas of {city}
4. Compensation for vehicle damage caused by road conditions
5. Implementation of safety measures

**ESCALATION PROCEDURE:**
If no satisfactory response is received within 7 days:
{chr(10).join([f"- {path}" for path in escalation_path])}

**LEGAL REPRESENTATION:**
This matter may be escalated to legal representation if immediate action is not taken.

**CONTACT INFORMATION:**
Reference Number: {reference_number}
Date: {today.strftime('%B %d, %Y')}
Time: {today.strftime('%I:%M %p PKT')}
Location: {area_name}, {city}, {province}
Legal Notice ID: LN-{today.strftime('%Y%m%d')}-{random.randint(100, 999)}

**ACKNOWLEDGMENT REQUIRED:**
Please acknowledge receipt of this legal notice within 24 hours and provide a detailed response plan within 7 days.

Sincerely,
Citizens of {area_name}
{city}, {country}

---
This is a legitimate legal notice for civic rights protection.
Reference: {reference_number}
Legal Notice ID: LN-{today.strftime('%Y%m%d')}-{random.randint(100, 999)}"""
            }
        }
        
        return templates.get(template_type, templates[1])

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
        """Select template based on day of year for rotation"""
        day_of_year = self.get_current_time_pakistan().timetuple().tm_yday
        template_type = (day_of_year % 3) + 1
        return template_type

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
            script_dir.parent / 'media',  # ../media from src/
            script_dir / 'media',         # ./media from src/
            Path.cwd() / 'media',         # media from current working directory
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
                if file_path.is_dir() or file_path.name.startswith('.'):
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
                    print(f"⚠️  Skipping oversized file: {file_path.name} ({file_size_mb:.1f}MB > {self.max_file_size_mb}MB)")
                    continue
                
                # Check total size limit
                if total_size_mb + file_size_mb > self.max_total_size_mb:
                    print(f"⚠️  Total attachment size limit reached ({total_size_mb:.1f}MB + {file_size_mb:.1f}MB > {self.max_total_size_mb}MB)")
                    break
                
                valid_files.append(str(file_path))
                total_size_mb += file_size_mb
                print(f"✅ Found valid media file: {file_path.name} ({file_size_mb:.1f}MB)")
        
        except Exception as e:
            print(f"❌ Error scanning media directory: {e}")
            return []
        
        print(f"📁 Total media files to attach: {len(valid_files)} ({total_size_mb:.1f}MB)")
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
                with open(file_path_obj, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {file_path_obj.name}'
                    )
                    msg.attach(part)
                attached_count += 1
                print(f"✅ Attached: {file_path_obj.name}")
            except (FileNotFoundError, PermissionError, OSError) as e:
                print(f"❌ Failed to attach {Path(file_path).name}: {e}")
            except Exception as e:
                print(f"❌ Unexpected error attaching {Path(file_path).name}: {e}")
        
        print(f"📎 Successfully attached {attached_count}/{len(media_files)} media files")

    def send_email(self, service, template):
        """Send email using specified service and template with improved error handling"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = service['email']
            msg['To'] = ', '.join(self.recipient_emails)
            msg['Subject'] = template['subject']
            
            # Add body
            msg.attach(MIMEText(template['body'], 'plain'))
            
            # Attach media files
            self.attach_media_files(msg)
            
            # Connect to SMTP server with specific error handling
            try:
                server = smtplib.SMTP(service['smtp_server'], service['smtp_port'])
                server.starttls()
            except (smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected) as e:
                print(f"❌ Failed to connect to {service['name']} SMTP server: {e}")
                return False
            except Exception as e:
                print(f"❌ Unexpected connection error with {service['name']}: {e}")
                return False
            
            # Authenticate
            try:
                server.login(service['email'], service['password'])
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
                server.sendmail(service['email'], self.recipient_emails, text)
                server.quit()
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
            
            print(f"✅ Email sent successfully using {service['name']}")
            print(f"📧 Template: {template['subject'][:50]}...")
            print(f"👥 Recipients: {len(self.recipient_emails)}")
            return True
            
        except Exception as e:
            print(f"❌ Unexpected error in send_email: {e}")
            return False

    def send_daily_emails(self):
        """Main function to send emails with rotation and anti-spam features"""
        current_time = self.get_current_time_pakistan()
        print(f"\n🚀 Starting email campaign - {current_time.strftime('%Y-%m-%d %H:%M:%S PKT')}")
        
        # Select email service and template
        try:
            service = self.select_email_service()
            template_type = self.select_template()
            template = self.get_email_template(template_type)
        except Exception as e:
            print(f"❌ Error in email/template selection: {e}")
            return False
        
        print(f"📧 Using service: {service['name']}")
        print(f"📝 Using template: {template_type}")
        print(f"📧 Available services: {len(self.email_services)}")
        print(f"📍 Location: {self.location_info['area_name']}, {self.location_info['city']}")
        
        # Send email
        success = self.send_email(service, template)
        
        if success:
            print("✅ Email campaign completed successfully")
        else:
            print("❌ Email campaign failed")
        
        # Random delay to avoid detection
        delay = random.randint(
            self.anti_spam_config['min_delay'], 
            self.anti_spam_config['max_delay']
        )
        print(f"⏱️ Waiting {delay} seconds before next operation...")
        time.sleep(delay)
        
        return success

def main():
    """Main function to run the email sender"""
    try:
        sender = GovernmentEmailSender()
        
        # Check if running in GitHub Actions or locally
        if os.getenv('GITHUB_ACTIONS'):
            # GitHub Actions mode - send once
            print("🤖 Running in GitHub Actions mode")
            success = sender.send_daily_emails()
            return success
        else:
            # Local mode - schedule daily
            print("💻 Running in local mode - scheduling emails")
            schedule.every().day.at("09:00").do(sender.send_daily_emails)
            
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
    if os.getenv('GITHUB_ACTIONS'):
        exit(0 if success else 1)