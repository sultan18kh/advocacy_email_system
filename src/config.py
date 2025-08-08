"""
Configuration file for the Automated Government Email System
Customize these settings according to your needs.
"""

# Email Recipients - UPDATE THESE WITH REAL GOVERNMENT EMAILS
RECIPIENT_EMAILS = [
    # Primary Government Offices
    "complaints@waltoncantonment.gov.pk",
    "cm@punjab.gov.pk",
    "info@lahore.gov.pk",
    "dc.lahore@punjab.gov.pk",
    "commissioner.lahore@punjab.gov.pk",
    
    # Development Authorities
    "ceo@lhc.gov.pk",
    "info@lhc.gov.pk",
    "director@lhc.gov.pk",
    
    # Government Complaint Cells
    "complaints@punjab.gov.pk",
    "helpline@punjab.gov.pk",
    "citizenportal@punjab.gov.pk",
    
    # Local Government
    "mayor@lahore.gov.pk",
    "commissioner.lahore@punjab.gov.pk",
    
    # Highway Department
    "ce@punjabhighways.gov.pk",
    "info@punjabhighways.gov.pk",
    
    # Additional Recipients (add more as needed)
    # "your_additional_email@domain.com",
]

# Email Schedule Configuration
EMAIL_SCHEDULE = {
    'time': '09:00',  # Daily email time (24-hour format)
    'timezone': 'Asia/Karachi',  # Pakistan timezone
}

# Anti-Spam Configuration
ANTI_SPAM_CONFIG = {
    'min_delay': 10,  # Minimum delay between operations (seconds)
    'max_delay': 60,  # Maximum delay between operations (seconds)
    'max_file_size_mb': 25,  # Maximum individual file size (MB)
    'max_total_size_mb': 50,  # Maximum total attachment size (MB)
}

# Email Templates Configuration
TEMPLATE_CONFIG = {
    'include_legal_references': True,
    'include_constitutional_rights': True,
    'include_escalation_timeline': True,
    'include_media_attachments': True,
}

# Location Information
LOCATION_INFO = {
    'area_name': 'Bedian Road & Ali View Garden Area',
    'city': 'Lahore',
    'province': 'Punjab',
    'country': 'Pakistan',
    'coordinates': '31.5204° N, 74.3587° E',  # Approximate coordinates
}

# Issue Details
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

# Legal Framework
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

# Email Service Configuration
EMAIL_SERVICES = [
    {
        'name': 'Gmail',
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'env_email': 'GMAIL_EMAIL',
        'env_password': 'GMAIL_APP_PASSWORD',
    },
    {
        'name': 'Outlook',
        'smtp_server': 'smtp-mail.outlook.com',
        'smtp_port': 587,
        'env_email': 'OUTLOOK_EMAIL',
        'env_password': 'OUTLOOK_PASSWORD',
    },
    {
        'name': 'Yahoo',
        'smtp_server': 'smtp.mail.yahoo.com',
        'smtp_port': 587,
        'env_email': 'YAHOO_EMAIL',
        'env_password': 'YAHOO_PASSWORD',
    },
]

# GitHub Actions Configuration
GITHUB_ACTIONS_CONFIG = {
    'cron_schedule': '0 4 * * 1,3,5',  # Mon, Wed, Fri at 4:00 AM UTC (9:00 AM Pakistan time)
    'python_version': '3.11',
    'workflow_name': 'Government Road Complaint Emails (Mon/Wed/Fri)',
}

# Monitoring Configuration
MONITORING_CONFIG = {
    'log_success_rate': True,
    'track_template_rotation': True,
    'monitor_email_delivery': True,
    'alert_on_failure': True,
}

# Development/Testing Configuration
DEV_CONFIG = {
    'test_mode': False,  # Set to True for testing without sending emails
    'dry_run': False,    # Set to True to simulate email sending
    'verbose_logging': True,  # Set to True for detailed logs
    'max_test_emails': 1,  # Maximum emails to send in test mode
}

# Media File Configuration
MEDIA_CONFIG = {
    'supported_extensions': {
        # Images
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp',
        # Videos
        '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv',
        # Documents
        '.pdf', '.doc', '.docx', '.txt', '.rtf',
        # Archives
        '.zip', '.rar', '.7z'
    },
    'max_file_size_mb': 25,  # Maximum individual file size
    'max_total_size_mb': 50,  # Maximum total attachment size
    'auto_discovery': True,   # Automatically discover files in media directory
}