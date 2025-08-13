"""
Configuration file for the Automated Government Email System
Customize these settings according to your needs.
"""

# Primary Recipient Emails (TO field)
RECIPIENT_EMAILS = [
    # Walton Cantonment Board - VERIFIED
    "waltoncb@outlook.com",
    # Chief Minister Punjab and Complaint System - VERIFIED
    "complaints@cm.punjab.gov.pk",  # CM Punjab Complaint Portal
    # Infrastructure Development - VERIFIED
    "info@idap.pk",  # Infrastructure Development Authority Punjab - Verified
    # Planning and Development Board
    "info@pndpunjab.gov.pk",  # Planning & Development Board Punjab
    # Transport and Roads Department
    "info@transport.punjab.gov.pk",  # Transport Department Punjab
    # District Administration - KEEPING EXISTING (Standard format)
    "dc.lahore@punjab.gov.pk",  # Deputy Commissioner Lahore
    "commissioner.lahore@punjab.gov.pk",  # Commissioner Lahore Division
    # Provincial Government - KEEPING EXISTING (Standard format)
    "complaints@punjab.gov.pk",  # Punjab Government Complaints
    "helpline@punjab.gov.pk",  # Punjab Government Helpline
    "citizenportal@punjab.gov.pk",  # Punjab Citizen Portal
]

# CC (Carbon Copy) Emails - for informational purposes
CC_EMAILS = [
    # Media outlets for transparency
    # "editor@dawn.com",  # Dawn News
    # "letters@tribune.com.pk",  # The Express Tribune
    # "feedback@geo.tv",  # Geo News
]

# BCC (Blind Carbon Copy) Emails - for tracking and backup
BCC_EMAILS = [
    # Backup and tracking emails
    "sultan18kh@gmail.com",
    "humakhan1127@gmail.com",
]

# Email Distribution Configuration
EMAIL_DISTRIBUTION_CONFIG = {
    "use_cc": False,  # Enable CC functionality
    "use_bcc": True,  # Enable BCC functionality
    "cc_empty_handling": "skip",  # Options: 'skip', 'send_to_only', 'error'
    "bcc_empty_handling": "skip",  # Options: 'skip', 'send_to_only', 'error'
    "max_cc_emails": 10,  # Maximum CC recipients per email
    "max_bcc_emails": 5,  # Maximum BCC recipients per email
    "validate_cc_bcc": True,  # Validate CC/BCC email formats
    "log_distribution": True,  # Log email distribution details
}

# Email Schedule Configuration
EMAIL_SCHEDULE = {
    "time": "09:00",  # Daily email time (24-hour format)
    "timezone": "Asia/Karachi",  # Pakistan timezone
}

# Anti-Spam Configuration
ANTI_SPAM_CONFIG = {
    "min_delay": 10,  # Minimum delay between operations (seconds)
    "max_delay": 60,  # Maximum delay between operations (seconds)
    "max_file_size_mb": 25,  # Maximum individual file size (MB)
    "max_total_size_mb": 50,  # Maximum total attachment size (MB)
}

# Email Templates Configuration - COMPLETELY REWRITTEN
EMAIL_TEMPLATES = {
    1: {
        "name": "Mismanagement Complaint Template",
        "language": "English",
        "subject_template": "Urgent: Severe Mismanagement of {area_name} Infrastructure - Citizens Appeal (Ref: {reference_number})",
        "body_template": """Respected Government Officials,

We are writing to express our deep concern about the severe mismanagement and systematic neglect of road infrastructure in {area_name}, {city}. As residents who traverse these roads daily, we feel compelled to bring these critical issues to your attention.

**EVIDENCE OF MISMANAGEMENT:**

**Discriminatory Development Practices:**
• While nearby roads like Airport Road and Ghazi Road have been developed and maintained despite being in much better condition, Bedian Road has been completely neglected
• The road is perfectly maintained within the Cantonment areas and near PAF Club, but becomes horrendous immediately after the Cantonment boundary ends
• This clear disparity demonstrates unfair allocation of development funds and resources

**Lack of Proper Planning and Oversight:**
• Ali View Garden society has been totally neglected despite housing thousands of families
• No proper drainage system has been implemented, causing severe flooding during rains
• Street lighting infrastructure is completely absent, creating safety hazards
• Traffic management systems are non-existent

**Regulatory Failures:**
• Illegal construction of shops and houses directly on main Bedian Road, drastically reducing lane widths and creating dangerous bottlenecks (photographic evidence attached)
• Fruit vendors are permitted to park on the main road without any check and balance, causing severe traffic congestion
• Car wash stations operate without proper drainage systems, further damaging the road surface with no oversight from Walton Cantonment Board

**IMPACT ON THOUSANDS OF DAILY COMMUTERS:**

**Health and Safety Concerns:**
• Pregnant women face severe discomfort and health risks due to constant jolting from potholes
• Elderly citizens with back problems suffer immense pain during travel
• Increased accident rates due to poor road conditions and inadequate lighting
• Emergency vehicles struggle to navigate, potentially costing lives

**Economic Impact:**
• Daily vehicle damage including tires, suspension systems, and engine problems
• Increased fuel consumption due to traffic congestion
• Lost productivity due to extended travel times
• Higher transportation costs affecting local businesses

**Social and Psychological Impact:**
• Daily stress and frustration for thousands of commuters
• Social isolation of Ali View Garden residents due to poor connectivity
• Reduced property values in the affected areas

**CONSTITUTIONAL AND LEGAL CONSIDERATIONS:**

This situation raises concerns under:
• **Article 9 of the Constitution of Pakistan**: Right to Life - which includes safe transportation and basic amenities essential for dignified living
• **Article 25**: Right to Equality - ensuring fair treatment in public service delivery
• **Article 9A**: Right to Clean and Healthy Environment (recently added) - proper road infrastructure contributes to environmental health

**CONSTRUCTIVE RECOMMENDATIONS:**

**Immediate Actions Required:**
1. Comprehensive survey and assessment of Bedian Road and Ali View Garden area
2. Emergency repairs to the most dangerous sections to prevent accidents
3. Installation of temporary lighting for safety
4. Immediate action against illegal constructions encroaching on road space
5. Regulation of street vendors and car wash operations

**Long-term Development Plan:**
1. Complete reconstruction of Bedian Road with proper drainage system
2. Extension of quality infrastructure beyond Cantonment boundaries
3. Development of Ali View Garden society infrastructure
4. Implementation of traffic management systems
5. Regular maintenance schedules

**Fair Resource Allocation:**
• Equal treatment with other areas like Airport Road and Ghazi Road
• Transparent allocation of development funds
• Community involvement in planning and monitoring

**CONTACT INFORMATION:**
Reference Number: {reference_number}
Date: {date_formatted}
Time: {time_formatted}
Location: {area_name}, {city}, {province}

We respectfully request your immediate attention to address these longstanding issues of mismanagement and bring our area up to the same standards enjoyed by other parts of Lahore.

We have attached photographic and video evidence documenting the current conditions and hope for swift action to resolve these matters through proper planning and fair resource allocation.

Thank you for your time and consideration.

Respectfully submitted,
Concerned Residents of {area_name}
{city}, {country}

---
This is a legitimate citizen complaint regarding infrastructure mismanagement.
Reference: {reference_number}""",
    },
    2: {
        "name": "Urdu Mismanagement Complaint Template",
        "language": "Urdu",
        "subject_template": "فوری: {area_name} میں انفراسٹرکچر کی بدانتظامی - شہریوں کی اپیل (Ref: {reference_number})",
        "body_template": """محترم حکومتی عہدیداران،

ہم {area_name} {city} میں سڑکی انفراسٹرکچر کی شدید بدانتظامی اور منظم غفلت کے بارے میں اپنی گہری تشویش کا اظہار کرتے ہوئے یہ خط لکھ رہے ہیں۔

**بدانتظامی کے شواہد:**

**امتیازی ترقیاتی پالیسیاں:**
• جبکہ قریبی سڑکیں جیسے ایئرپورٹ روڈ اور غازی روڈ بہتر حالت میں ہونے کے باوجود ترقی یافتہ اور برقرار رکھی گئی ہیں، بیڈین روڈ کو مکمل طور پر نظرانداز کیا گیا ہے
• یہ سڑک کینٹونمنٹ ایریا اور PAF کلب کے قریب بالکل ٹھیک ہے، لیکن کینٹونمنٹ کی حد ختم ہوتے ہی خوفناک حالت میں ہو جاتی ہے
• یہ واضح تفاوت ترقیاتی فنڈز اور وسائل کی غیر منصفانہ تقسیم کو ظاہر کرتا ہے

**مناسب منصوبہ بندی اور نگرانی کا فقدان:**
• علی ویو گارڈن سوسائٹی کو مکمل طور پر نظرانداز کیا گیا ہے جبکہ یہاں ہزاروں خاندان رہتے ہیں
• مناسب نکاسی آب کا نظام نہیں بنایا گیا، جس سے بارش میں شدید سیلاب آتا ہے
• سٹریٹ لائٹنگ کا نظام مکمل طور پر غائب ہے، جو سیکورٹی کے خطرات پیدا کرتا ہے
• ٹریفک منیجمنٹ سسٹم موجود نہیں ہے

**ریگولیٹری ناکامیاں:**
• مین بیڈین روڈ پر دکانوں اور مکانات کی غیر قانونی تعمیر، جو لین کی چوڑائی کو خطرناک حد تک کم کر دیتی ہے
• فروٹ وینڈرز کو بنا کسی چیک اینڈ بیلنس کے مین روڈ پر کھڑے ہونے کی اجازت، جو شدید ٹریفک جام کا باعث بنتا ہے
• کار واش سٹیشنز مناسب نکاسی کے بغیر کام کرتے ہیں، والٹن کینٹونمنٹ بورڈ کی کوئی نگرانی نہیں

**ہزاروں روزانہ مسافروں پر اثرات:**

**صحت اور سیفٹی کے مسائل:**
• حاملہ خواتین کو گڑھوں کی وجہ سے مسلسل جھٹکوں سے شدید تکلیف اور صحت کے خطرات
• کمر کے مسائل والے بزرگ شہریوں کو سفر کے دوران شدید درد
• خراب سڑک کی حالت اور ناکافی روشنی کی وجہ سے حادثات میں اضافہ
• ایمرجنسی گاڑیوں کو آمد و رفت میں مشکلات

**معاشی اثرات:**
• روزانہ گاڑیوں کو نقصان بشمول ٹائرز، سسپنشن سسٹم اور انجن کے مسائل
• ٹریفک جام کی وجہ سے ایندھن کا زیادہ استعمال
• سفر کے وقت میں اضافے سے پیداواری صلاحیت میں کمی

**آئینی اور قانونی تحفظات:**

یہ صورتحال مندرجہ ذیل کے تحت تشویش کا باعث ہے:
• **پاکستان کے آئین کا آرٹیکل 9**: حق زندگی - جس میں محفوظ نقل و حمل اور بنیادی سہولات شامل ہیں
• **آرٹیکل 25**: مساوات کا حق - عوامی خدمات میں منصفانہ سلوک
• **آرٹیکل 9A**: صاف اور صحت مند ماحول کا حق

**تعمیری تجاویز:**

**فوری اقدامات:**
1. بیڈین روڈ اور علی ویو گارڈن ایریا کا جامع سروے
2. حادثات کو روکنے کے لیے انتہائی خطرناک حصوں کی ہنگامی مرمت
3. سیفٹی کے لیے عارضی روشنی کا انتظام
4. سڑک پر غیر قانونی قبضوں کے خلاف فوری کارروائی

**طویل مدتی ترقیاتی منصوبہ:**
1. مناسب نکاسی آب کے ساتھ بیڈین روڈ کی مکمل تعمیر نو
2. کینٹونمنٹ کی حدود سے آگے معیاری انفراسٹرکچر کی توسیع
3. علی ویو گارڈن سوسائٹی کے انفراسٹرکچر کی ترقی

**رابطہ کی معلومات:**
ریفرنس نمبر: {reference_number}
تاریخ: {date_formatted}
وقت: {time_formatted}
مقام: {area_name}, {city}, {province}

ہم احتراماً آپ سے درخواست کرتے ہیں کہ بدانتظامی کے ان طویل مسائل پر فوری توجہ دیں اور ہمارے علاقے کو لاہور کے دوسرے حصوں جیسا معیار فراہم کریں۔

ہم نے موجودہ حالات کی تصاویر اور ویڈیو شواہد منسلک کیے ہیں اور مناسب منصوبہ بندی اور منصفانہ وسائل کی تقسیم کے ذریعے ان مسائل کے فوری حل کی امید رکھتے ہیں۔

آپ کے وقت اور توجہ کا شکریہ۔

احتراماً،
{area_name} کے تشویش مند رہائشی
{city}, {country}

---
یہ انفراسٹرکچر کی بدانتظامی کے حوالے سے شہریوں کی جائز شکایت ہے۔
ریفرنس: {reference_number}""",
    },
    3: {
        "name": "Administrative Reform Request Template",
        "language": "English",
        "subject_template": "Request for Administrative Review: {area_name} Infrastructure Development (Ref: {reference_number})",
        "body_template": """Honorable Government Officials,

We respectfully submit this formal request for administrative review and corrective action regarding the infrastructure management in {area_name}, {city}. As concerned citizens, we seek your intervention to address systematic issues affecting thousands of residents daily.

**ADMINISTRATIVE REVIEW REQUEST:**

**Current Administrative Challenges:**
Our area faces significant infrastructure challenges that appear to stem from administrative oversights and resource allocation decisions:

• **Inconsistent Development Standards**: While Cantonment-controlled areas maintain excellent infrastructure, civilian areas immediately adjacent show severe deterioration
• **Absent Coordination**: Multiple agencies (Walton Cantonment Board, district administration, development authorities) seem to lack coordination in area management
• **Resource Allocation Imbalances**: Established areas receive regular maintenance while emerging residential areas like Ali View Garden remain underserved

**Specific Administrative Issues Requiring Review:**

**1. Planning and Zoning Failures:**
• Inadequate zoning enforcement allowing commercial encroachment on residential roads
• Missing master planning for integrated infrastructure development
• Lack of traffic impact assessments for new developments

**2. Regulatory Oversight Gaps:**
• Absence of regular road condition monitoring systems
• Inadequate enforcement of building codes and road usage regulations
• Missing coordination between utility services and road maintenance

**3. Service Delivery Inconsistencies:**
• Disparate service levels between different administrative jurisdictions
• Lack of citizen feedback mechanisms for infrastructure reporting
• Absent emergency response protocols for infrastructure failures

**IMPACT ASSESSMENT:**

**Public Health and Safety:**
The current conditions create documented public health and safety concerns:
• Increased emergency response times due to poor road conditions
• Higher accident rates in poorly lit and maintained areas
• Public health risks from stagnant water due to poor drainage

**Economic Implications:**
• Reduced property values affecting thousands of families
• Increased transportation costs for residents and businesses
• Lost economic opportunities due to poor connectivity

**CONSTITUTIONAL FRAMEWORK FOR ACTION:**

Our request aligns with constitutional principles:
• **Article 9**: Ensures right to life which encompasses safe and accessible infrastructure
• **Article 25**: Guarantees equality in public service provision
• **Article 38(d)**: State obligation to provide basic necessities including housing and infrastructure

**PROPOSED ADMINISTRATIVE SOLUTIONS:**

**1. Institutional Coordination:**
• Establish inter-agency coordination committee for area development
• Define clear jurisdictional responsibilities
• Create unified complaint and monitoring system

**2. Planning Integration:**
• Develop comprehensive area master plan
• Integrate utility services planning with road development
• Establish development impact assessment protocols

**3. Service Standardization:**
• Implement uniform infrastructure standards across jurisdictions
• Establish regular maintenance schedules
• Create citizen engagement mechanisms

**4. Resource Optimization:**
• Review and balance resource allocation across areas
• Explore public-private partnership opportunities
• Implement transparent procurement processes

**MONITORING AND ACCOUNTABILITY:**

We respectfully request:
• Establishment of timeline for addressing identified issues
• Regular progress reporting to affected communities
• Creation of citizen oversight mechanisms

**DOCUMENTATION:**

Attached photographic and video evidence demonstrates:
• Current road conditions and safety hazards
• Illegal encroachments affecting traffic flow
• Drainage and lighting infrastructure gaps
• Comparative conditions with nearby developed areas

**CONTACT INFORMATION:**
Reference Number: {reference_number}
Date: {date_formatted}
Time: {time_formatted}
Location: {area_name}, {city}, {province}

We believe that through proper administrative coordination and systematic planning, these challenges can be addressed effectively. We look forward to working collaboratively with relevant authorities to improve infrastructure standards and administrative efficiency.

Thank you for your attention to these important administrative matters.

Respectfully submitted,
Citizens Committee for {area_name} Development
{city}, {country}

---
This is a formal administrative review request for infrastructure development.
Reference: {reference_number}""",
    },
}

# Email Template Configuration
EMAIL_TEMPLATE_CONFIG = {
    "default_template": 1,
    "template_rotation": True,
    "custom_variables": {
        "reference_prefix": "ROAD",
        "escalation_days": 7,
        "response_hours": 48,  # Changed from 24 to 48 hours for more reasonable expectation
    },
    "formatting": {
        "date_format": "%B %d, %Y",
        "time_format": "%I:%M %p PKT",
        "reference_format": "{prefix}-{date}-{random}",
    },
}

# Location Information
LOCATION_INFO = {
    "area_name": "Bedian Road & Ali View Garden Area",
    "city": "Lahore",
    "province": "Punjab",
    "country": "Pakistan",
    "coordinates": "31.5204° N, 74.3587° E",  # Approximate coordinates
}

# Issue Details - UPDATED WITH SPECIFIC CONCERNS
ISSUE_DETAILS = {
    "primary_issue": "Infrastructure Mismanagement and Neglect",
    "specific_problems": [
        "Discriminatory development - Airport Road and Ghazi Road prioritized over Bedian Road",
        "Road quality deteriorates immediately after Cantonment boundary ends",
        "Complete neglect of Ali View Garden society infrastructure",
        "Illegal construction of shops reducing road width and creating bottlenecks",
        "Unregulated fruit vendors causing traffic congestion",
        "Car wash stations operating without proper drainage oversight",
        "Absence of street lighting creating security hazards",
        "Poor drainage system causing flooding during rains",
        "Lack of traffic management and organization",
    ],
    "affected_population": "Thousands of daily commuters and residents",
    "duration": "Ongoing systemic neglect for years",
}

# Legal Framework - VERIFIED CONSTITUTIONAL ARTICLES
LEGAL_FRAMEWORK = {
    "constitutional_articles": [
        "Article 9 (Right to Life and Liberty)",
        "Article 25 (Equality of Citizens)",
        "Article 9A (Right to Clean and Healthy Environment)",  # Recently added
    ],
    "relevant_laws": [
        "Local Government Act 2013",
        "Punjab Local Government Act 2019",
        "Punjab Development of Cities Act 1976",
        "Cantonment Act 2004",
    ],
    "administrative_bodies": [
        "Infrastructure Development Authority Punjab (IDAP)",
        "Planning and Development Board Punjab",
        "Walton Cantonment Board",
        "District Administration Lahore",
    ],
}

# Email Service Configuration
EMAIL_SERVICES = [
    {
        "name": "Gmail",
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "env_email": "GMAIL_EMAIL",
        "env_password": "GMAIL_APP_PASSWORD",
    },
    {
        "name": "Outlook",
        "smtp_server": "smtp-mail.outlook.com",
        "smtp_port": 587,
        "env_email": "OUTLOOK_EMAIL",
        "env_password": "OUTLOOK_PASSWORD",
    },
    {
        "name": "Yahoo",
        "smtp_server": "smtp.mail.yahoo.com",
        "smtp_port": 587,
        "env_email": "YAHOO_EMAIL",
        "env_password": "YAHOO_PASSWORD",
    },
]

# GitHub Actions Configuration
GITHUB_ACTIONS_CONFIG = {
    "cron_schedule": "0 4 * * 1,5",  # Mon, Fri at 4:00 AM UTC (9:00 AM Pakistan time)
    "python_version": "3.11",
    "workflow_name": "Government Road Complaint Emails (Mon/Fri)",
}

# Monitoring Configuration
MONITORING_CONFIG = {
    "log_success_rate": True,
    "track_template_rotation": True,
    "monitor_email_delivery": True,
    "alert_on_failure": True,
}

# Development/Testing Configuration
DEV_CONFIG = {
    "test_mode": False,  # Set to True for testing without sending emails
    "dry_run": False,  # Set to True to simulate email sending
    "verbose_logging": True,  # Set to True for detailed logs
    "max_test_emails": 1,  # Maximum emails to send in test mode
}

# Media File Configuration
MEDIA_CONFIG = {
    "supported_extensions": {
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
    },
    "max_file_size_mb": 25,  # Maximum individual file size
    "max_total_size_mb": 50,  # Maximum total attachment size
    "auto_discovery": True,  # Automatically discover files in media directory
}
