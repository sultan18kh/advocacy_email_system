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

# Media Files Configuration
MEDIA_FILES = [
    'media/road_photo1.jpg',
    'media/road_photo2.jpg',
    'media/pothole_video.mp4',
    'media/flooding_video.mp4',
    # Add more media files as needed
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
    'max_attachments': 2,  # Maximum number of attachments per email
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
    'cron_schedule': '0 4 * * *',  # Daily at 4:00 AM UTC (9:00 AM Pakistan time)
    'python_version': '3.11',
    'workflow_name': 'Daily Government Road Complaint Emails',
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
