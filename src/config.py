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
    "dclahore@punjab.gov.pk",  # Deputy Commissioner Lahore
    "snalahore@punjab.gov.pk",  # Secretary Lahore
    "revenuelahore@gmail.com",  # Revenue Department Lahore
    "adcglhr@gmail.com",  # Additional Deputy Commissioner Lahore
    "doclahore@hotmail.com",  # Director of Commerce Lahore
    "edohealthlhr@yahoo.com",  # Director of Health Lahore
    # Provincial Government - KEEPING EXISTING (Standard format)
    "complaints@punjab.gov.pk",  # Punjab Government Complaints
    "helpline@punjab.gov.pk",  # Punjab Government Helpline
    "citizenportal@punjab.gov.pk",  # Punjab Citizen Portal
    "admnsmu@gmail.com",  # Punjab Special Monitoring Unit
    "info@pmln.org",  # PMLN Party Official
    # Ministry of Information and Broadcasting
    "info@moib.gov.pk",  # MOIB
    # Punjab Traffic Police
    "addlig.trf@punjabpolice.gov.pk",  # Punjab Police
    "dig.traffic@punjabpolice.gov.pk",  # Punjab Police
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
    "sultan512@gmail.com",
    "sukhan@alphabold.com",
    "fatima.umer15@gmail.com",
    "ajbutt48@gmail.com",
    "Mussabsalman12@gmail.com", # AVG Phase 1 Resident
    # "sultan18kh@gmail.com",
    # "humakhan1127@gmail.com",
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

# Email Templates Configuration - STYLED WITH HTML
EMAIL_TEMPLATES = {
    1: {
        "name": "Mismanagement Complaint Template",
        "language": "English",
        "content_type": "html",  # Specify HTML content type
        "subject_template": "Urgent: Severe Mismanagement of {area_name} Infrastructure - Citizens Appeal (Ref: {reference_number})",
        "body_template": """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Arial', 'Segoe UI', sans-serif;
            line-height: 1.6;
            color: #333333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
        }}
        .header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 8px 8px 0 0;
            margin-bottom: 0;
        }}
        .header h1 {{
            margin: 0;
            font-size: 24px;
            font-weight: bold;
        }}
        .content {{
            background-color: #ffffff;
            padding: 30px;
            border: 1px solid #e0e0e0;
            border-radius: 0 0 8px 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .greeting {{
            font-size: 16px;
            margin-bottom: 25px;
            color: #2c3e50;
        }}
        .section {{
            margin: 25px 0;
            padding: 20px;
            border-left: 4px solid #e74c3c;
            background-color: #fdf2f2;
            border-radius: 0 5px 5px 0;
        }}
        .section h2 {{
            color: #c0392b;
            font-size: 18px;
            margin-top: 0;
            margin-bottom: 15px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .subsection {{
            margin: 20px 0;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
            border-left: 3px solid #3498db;
        }}
        .subsection h3 {{
            color: #2980b9;
            font-size: 16px;
            margin-top: 0;
            margin-bottom: 10px;
            font-weight: bold;
        }}
        .bullet-point {{
            margin: 8px 0;
            padding-left: 10px;
            position: relative;
        }}
        .bullet-point:before {{
            content: "▶";
            color: #e74c3c;
            font-weight: bold;
            position: absolute;
            left: -5px;
        }}
        .impact-section {{
            background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
            border-left: 4px solid #f39c12;
            padding: 20px;
            margin: 25px 0;
            border-radius: 0 5px 5px 0;
        }}
        .impact-section h2 {{
            color: #d35400;
            margin-top: 0;
        }}
        .legal-section {{
            background: linear-gradient(135deg, #ddd6fe 0%, #c4b5fd 100%);
            border-left: 4px solid #8b5cf6;
            padding: 20px;
            margin: 25px 0;
            border-radius: 0 5px 5px 0;
        }}
        .legal-section h2 {{
            color: #6b46c1;
            margin-top: 0;
        }}
        .legal-section p {{
            color: #4c1d95;
        }}
        .legal-section .bullet-point {{
            color: #4c1d95;
        }}
        .recommendations {{
            background: linear-gradient(135deg, #a7f3d0 0%, #6ee7b7 100%);
            border-left: 4px solid #10b981;
            padding: 20px;
            margin: 25px 0;
            border-radius: 0 5px 5px 0;
        }}
        .recommendations h2 {{
            color: #047857;
            margin-top: 0;
        }}
        .contact-info {{
            background-color: #f1f5f9;
            padding: 20px;
            border-radius: 8px;
            border: 2px solid #cbd5e1;
            margin: 25px 0;
        }}
        .contact-info h2 {{
            color: #334155;
            margin-top: 0;
            font-size: 16px;
        }}
        .contact-detail {{
            margin: 5px 0;
            font-weight: bold;
            color: #475569;
        }}
        .closing {{
            margin-top: 30px;
            padding: 20px;
            background-color: #f8fafc;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }}
        .signature {{
            margin-top: 20px;
            font-weight: bold;
            color: #2c3e50;
        }}
        .footer {{
            margin-top: 30px;
            padding: 15px;
            background-color: #2c3e50;
            color: white;
            text-align: center;
            border-radius: 8px;
            font-size: 12px;
        }}
        .highlight {{
            background-color: #fff3cd;
            padding: 2px 6px;
            border-radius: 3px;
            border: 1px solid #ffeaa7;
            font-weight: bold;
        }}
        ol, ul {{
            margin: 10px 0;
            padding-left: 25px;
        }}
        li {{
            margin: 8px 0;
            line-height: 1.5;
        }}
        .numbered-item {{
            background-color: #ffffff;
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
            border-left: 3px solid #3498db;
        }}
        .alert {{
            background-color: #fee2e2;
            border: 1px solid #fecaca;
            color: #991b1b;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🚨 URGENT INFRASTRUCTURE COMPLAINT 🚨</h1>
        <p style="margin: 5px 0 0 0; font-size: 14px; opacity: 0.9;">Citizens Appeal for Immediate Government Action</p>
    </div>
    
    <div class="content">
        <div class="greeting">
            <strong>Respected Government Officials,</strong>
        </div>
        
        <p>We are writing to express our deep concern about the severe mismanagement and systematic neglect of road infrastructure in <span class="highlight">{area_name}, {city}</span>. As residents who traverse these roads daily, we feel compelled to bring these critical issues to your attention.</p>

        <div class="section">
            <h2>🔍 EVIDENCE OF MISMANAGEMENT AND INCOMPETENCE</h2>
            
            <div class="subsection">
                <h3>📊 Discriminatory Development Practices</h3>
                <div class="bullet-point">While nearby roads like <strong>Airport Road, Ghazi Road, and Bhatta Chowk</strong> have been almost completed with proper infrastructure, Bedian Road has been completely neglected despite being in desperate need of attention</div>
                <div class="bullet-point">The <strong>Nawaz Sharif Interchange</strong> was totally revamped with modern infrastructure, yet this small patch of Bedian Road remains completely abandoned</div>
                <div class="bullet-point">The road is perfectly maintained within the <strong>Cantonment areas and near PAF Club</strong>, but becomes horrendous immediately after the Cantonment boundary ends</div>
                <div class="bullet-point">This clear disparity demonstrates <span class="highlight">unfair allocation of development funds and resources</span>, showing systematic neglect of civilian areas</div>
            </div>

            <div class="subsection">
                <h3>🔨 Incompetent Road Maintenance Practices</h3>
                <div class="bullet-point">Potholes are continuously filled with <strong>loose rubble instead of proper road material</strong>, creating a temporary and extremely dangerous solution that fails within days</div>
                <div class="bullet-point">During rain, these rubble-filled patches create <span class="highlight">massive drainage problems</span> and become even more hazardous for vehicles</div>
                <div class="bullet-point">Certain patches of the road have completely deteriorated with <strong>exposed metal underneath</strong>, making these sections completely un-drivable</div>
                <div class="bullet-point">Drivers are forced to swerve around potholes while facing incoming traffic, causing <span class="highlight">widespread stress and significantly increasing the risk of head-on collisions</span></div>
            </div>

            <div class="subsection">
                <h3>📜 Historical Mismanagement and Broken Promises</h3>
                <div class="bullet-point"><strong>Major Mustafa Sabir Shaheed Road</strong> has been "repaired" multiple times, but each attempt has resulted in complete failure due to incompetence and mismanagement</div>
                <div class="bullet-point">These repairs break down after only a few months each time due to the authorities' failure to address the <span class="highlight">underlying sewage and drainage problems</span></div>
                <div class="bullet-point">During the <strong>PMLN Punjab Government</strong> under the leadership of <strong>Mian Shahbaz Sharif as Chief Minister</strong> and <strong>Khawaja Saad Rafique as MNA</strong>, massive development plans were announced for this area</div>
            </div>

            <div class="subsection">
                <h3>📋 Lack of Proper Planning and Oversight</h3>
                <div class="bullet-point"><strong>Ali View Garden society</strong> has been totally neglected despite housing thousands of families and being a significant residential area</div>
                <div class="bullet-point">No proper drainage system has been implemented, causing <span class="highlight">severe flooding during rains</span></div>
                <div class="bullet-point">Street lighting infrastructure is completely absent, creating safety hazards and security concerns</div>
                <div class="bullet-point">Traffic management systems are non-existent, leading to chaotic traffic conditions</div>
            </div>

            <div class="subsection">
                <h3>⚠️ Complete Absence of Check and Balance</h3>
                <div class="bullet-point">There is absolutely <strong>no monitoring or oversight</strong> in this area regarding road conditions or maintenance standards</div>
                <div class="bullet-point">Illegal construction of shops and houses directly on main Bedian Road continues unchecked, drastically reducing lane widths and creating dangerous bottlenecks</div>
                <div class="bullet-point">Fruit vendors are permitted to park on the main road without any regulation, causing severe traffic congestion</div>
                <div class="bullet-point">Car wash stations operate without proper drainage systems, further damaging the road surface with no oversight from Walton Cantonment Board</div>
            </div>
        </div>

        <div class="impact-section">
            <h2>💔 IMPACT ON THOUSANDS OF DAILY COMMUTERS</h2>
            
            <div class="subsection">
                <h3>🏥 Health and Safety Concerns</h3>
                <div class="bullet-point"><strong>Pregnant women</strong> face severe discomfort and health risks due to constant jolting from potholes and the need to navigate around dangerous road patches</div>
                <div class="bullet-point"><strong>Elderly citizens</strong> with back problems suffer immense pain during travel, with some avoiding the route entirely</div>
                <div class="bullet-point">The stress of constantly avoiding potholes while managing incoming traffic causes <span class="highlight">psychological distress for thousands of daily commuters</span></div>
                <div class="bullet-point">Increased accident rates due to poor road conditions, inadequate lighting, and dangerous driving maneuvers required to avoid road hazards</div>
                <div class="bullet-point"><strong>Emergency vehicles</strong> struggle to navigate these conditions, potentially costing lives during critical situations</div>
            </div>

            <div class="subsection">
                <h3>💰 Economic Impact</h3>
                <div class="bullet-point">Daily vehicle damage including tires, suspension systems, and engine problems due to poor road conditions and exposed metal patches</div>
                <div class="bullet-point">Increased fuel consumption due to traffic congestion and the need to drive at reduced speeds</div>
                <div class="bullet-point">Lost productivity due to extended travel times and the mental fatigue from navigating dangerous road conditions</div>
                <div class="bullet-point">Higher transportation costs affecting local businesses and residents</div>
                <div class="bullet-point">Decreased property values in Ali View Garden and surrounding areas due to poor connectivity</div>
            </div>

            <div class="subsection">
                <h3>😔 Social and Psychological Impact</h3>
                <div class="bullet-point">Daily stress and frustration for thousands of commuters who have no alternative routes</div>
                <div class="bullet-point">Social isolation of Ali View Garden residents due to poor connectivity and reluctance of visitors to navigate the dangerous roads</div>
                <div class="bullet-point">Loss of faith in government promises and development plans that never materialize</div>
            </div>
        </div>

        <div class="legal-section">
            <h2>⚖️ CONSTITUTIONAL AND LEGAL CONSIDERATIONS</h2>
            <p>This situation raises serious concerns under:</p>
            
            <div class="subsection">
                <h3>📜 Constitutional Rights Violations</h3>
                <div class="bullet-point"><strong>Article 9 of the Constitution of Pakistan</strong>: Right to Life - which includes safe transportation and basic amenities essential for dignified living</div>
                <div class="bullet-point"><strong>Article 25</strong>: Right to Equality - ensuring fair treatment in public service delivery and equal allocation of development resources</div>
                <div class="bullet-point"><strong>Article 9A</strong>: Right to Clean and Healthy Environment - proper road infrastructure contributes to environmental health and safety</div>
            </div>
        </div>

        <div class="recommendations">
            <h2>💡 CONSTRUCTIVE RECOMMENDATIONS</h2>
            
            <div class="subsection">
                <h3>🚨 Immediate Actions Required</h3>
                <ol>
                    <li class="numbered-item">Comprehensive survey and assessment of Bedian Road and Ali View Garden area by qualified engineers</li>
                    <li class="numbered-item">Emergency repairs using <strong>proper road materials (not rubble)</strong> to the most dangerous sections to prevent accidents</li>
                    <li class="numbered-item">Immediate addressing of exposed metal patches that make sections completely un-drivable</li>
                    <li class="numbered-item">Installation of temporary lighting for safety during evening hours</li>
                    <li class="numbered-item">Immediate action against illegal constructions encroaching on road space</li>
                    <li class="numbered-item">Regulation of street vendors and car wash operations</li>
                </ol>
            </div>

            <div class="subsection">
                <h3>🏗️ Long-term Development Plan</h3>
                <ol>
                    <li class="numbered-item">Complete reconstruction of Bedian Road with proper drainage system to address underlying sewage problems</li>
                    <li class="numbered-item">Extension of quality infrastructure beyond Cantonment boundaries to match standards of nearby completed projects</li>
                    <li class="numbered-item">Development of Ali View Garden society infrastructure as originally planned</li>
                    <li class="numbered-item">Implementation of traffic management systems and proper road signage</li>
                    <li class="numbered-item">Establishment of regular maintenance schedules with proper oversight</li>
                </ol>
            </div>

            <div class="subsection">
                <h3>⚖️ Fair Resource Allocation</h3>
                <div class="bullet-point">Equal treatment with other areas like Airport Road, Ghazi Road, and Bhatta Chowk that have received proper development</div>
                <div class="bullet-point">Transparent allocation of development funds without discrimination between cantonment and civilian areas</div>
                <div class="bullet-point">Revival and implementation of the development plans that were promised during the PMLN government era</div>
                <div class="bullet-point">Community involvement in planning and monitoring to ensure accountability</div>
            </div>
        </div>

        <div class="contact-info">
            <h2>📞 CONTACT INFORMATION</h2>
            <div class="contact-detail">Reference Number: <span class="highlight">{reference_number}</span></div>
            <div class="contact-detail">Date: {date_formatted}</div>
            <div class="contact-detail">Time: {time_formatted}</div>
            <div class="contact-detail">Location: {area_name}, {city}, {province}</div>
        </div>

        <div class="alert">
            ⚠️ We respectfully request your immediate attention to address these longstanding issues of mismanagement and incompetence. The residents of this area deserve the same standard of infrastructure enjoyed by other parts of Lahore, especially considering the promises made and plans announced in previous years.
        </div>

        <div class="closing">
            <p>We have attached photographic and video evidence documenting the current conditions and hope for swift action to resolve these matters through proper planning, competent execution, and fair resource allocation.</p>
            
            <p>Thank you for your time and consideration.</p>
            
            <div class="signature">
                <p>Respectfully submitted,<br>
                <strong>Concerned Residents of {area_name}</strong><br>
                {city}, {country}</p>
            </div>
        </div>
    </div>

    <div class="footer">
        This is a legitimate citizen complaint regarding infrastructure mismanagement and neglect.<br>
        <strong>Reference: {reference_number}</strong>
    </div>
</body>
</html>""",
    },
    2: {
        "name": "Urdu Mismanagement Complaint Template",
        "language": "Urdu",
        "content_type": "html",  # Specify HTML content type
        "subject_template": "فوری: {area_name} میں انفراسٹرکچر کی بدانتظامی - شہریوں کی اپیل (Ref: {reference_number})",
        "body_template": """
<!DOCTYPE html>
<html dir="rtl" lang="ur">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Noto Nastaliq Urdu', 'Arial Unicode MS', 'Tahoma', sans-serif;
            line-height: 1.8;
            color: #333333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            direction: rtl;
            text-align: right;
        }}
        .header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 8px 8px 0 0;
            margin-bottom: 0;
        }}
        .header h1 {{
            margin: 0;
            font-size: 24px;
            font-weight: bold;
        }}
        .content {{
            background-color: #ffffff;
            padding: 30px;
            border: 1px solid #e0e0e0;
            border-radius: 0 0 8px 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .greeting {{
            font-size: 16px;
            margin-bottom: 25px;
            color: #2c3e50;
            font-weight: bold;
        }}
        .section {{
            margin: 25px 0;
            padding: 20px;
            border-right: 4px solid #e74c3c;
            background-color: #fdf2f2;
            border-radius: 5px 0 0 5px;
        }}
        .section h2 {{
            color: #c0392b;
            font-size: 18px;
            margin-top: 0;
            margin-bottom: 15px;
            font-weight: bold;
        }}
        .subsection {{
            margin: 20px 0;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
            border-right: 3px solid #3498db;
        }}
        .subsection h3 {{
            color: #2980b9;
            font-size: 16px;
            margin-top: 0;
            margin-bottom: 10px;
            font-weight: bold;
        }}
        .bullet-point {{
            margin: 12px 0;
            padding-right: 20px;
            position: relative;
            line-height: 1.6;
        }}
        .bullet-point:before {{
            content: "◄";
            color: #e74c3c;
            font-weight: bold;
            position: absolute;
            right: 0;
        }}
        .impact-section {{
            background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
            border-right: 4px solid #f39c12;
            padding: 20px;
            margin: 25px 0;
            border-radius: 5px 0 0 5px;
        }}
        .impact-section h2 {{
            color: #d35400;
            margin-top: 0;
        }}
        .legal-section {{
            background: linear-gradient(135deg, #ddd6fe 0%, #c4b5fd 100%);
            border-right: 4px solid #8b5cf6;
            padding: 20px;
            margin: 25px 0;
            border-radius: 5px 0 0 5px;
        }}
        .legal-section h2 {{
            color: #6b46c1;
            margin-top: 0;
        }}
        .legal-section p {{
            color: #4c1d95;
        }}
        .legal-section .bullet-point {{
            color: #4c1d95;
        }}
        .recommendations {{
            background: linear-gradient(135deg, #a7f3d0 0%, #6ee7b7 100%);
            border-right: 4px solid #10b981;
            padding: 20px;
            margin: 25px 0;
            border-radius: 5px 0 0 5px;
        }}
        .recommendations h2 {{
            color: #047857;
            margin-top: 0;
        }}
        .contact-info {{
            background-color: #f1f5f9;
            padding: 20px;
            border-radius: 8px;
            border: 2px solid #cbd5e1;
            margin: 25px 0;
        }}
        .contact-info h2 {{
            color: #334155;
            margin-top: 0;
            font-size: 16px;
        }}
        .contact-detail {{
            margin: 8px 0;
            font-weight: bold;
            color: #475569;
        }}
        .closing {{
            margin-top: 30px;
            padding: 20px;
            background-color: #f8fafc;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }}
        .signature {{
            margin-top: 20px;
            font-weight: bold;
            color: #2c3e50;
        }}
        .footer {{
            margin-top: 30px;
            padding: 15px;
            background-color: #2c3e50;
            color: white;
            text-align: center;
            border-radius: 8px;
            font-size: 12px;
        }}
        .highlight {{
            background-color: #fff3cd;
            padding: 2px 6px;
            border-radius: 3px;
            border: 1px solid #ffeaa7;
            font-weight: bold;
        }}
        ol, ul {{
            margin: 10px 0;
            padding-right: 25px;
        }}
        li {{
            margin: 10px 0;
            line-height: 1.6;
        }}
        .numbered-item {{
            background-color: #ffffff;
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
            border-right: 3px solid #3498db;
        }}
        .alert {{
            background-color: #fee2e2;
            border: 1px solid #fecaca;
            color: #991b1b;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🚨 فوری انفراسٹرکچر شکایت 🚨</h1>
        <p style="margin: 5px 0 0 0; font-size: 14px; opacity: 0.9;">حکومتی فوری اقدام کے لیے شہریوں کی اپیل</p>
    </div>
    
    <div class="content">
        <div class="greeting">
            محترم حکومتی عہدیداران،
        </div>
        
        <p>ہم <span class="highlight">{area_name} {city}</span> میں سڑکی انفراسٹرکچر کی شدید بدانتظامی اور منظم غفلت کے بارے میں اپنی گہری تشویش کا اظہار کرتے ہوئے یہ خط لکھ رہے ہیں۔</p>

        <div class="section">
            <h2>🔍 بدانتظامی اور نااہلی کے شواہد</h2>
            
            <div class="subsection">
                <h3>📊 امتیازی ترقیاتی پالیسیاں</h3>
                <div class="bullet-point">جبکہ قریبی سڑکیں جیسے <strong>ایئرپورٹ روڈ، غازی روڈ اور بھٹہ چوک</strong> تقریباً مکمل ہو چکے ہیں، بیڈین روڈ کو مکمل طور پر نظرانداز کیا گیا ہے</div>
                <div class="bullet-point"><strong>نواز شریف انٹرچینج</strong> کو جدید انفراسٹرکچر کے ساتھ مکمل طور پر تبدیل کر دیا گیا، لیکن بیڈین روڈ کا یہ چھوٹا سا حصہ مکمل طور پر لاوارش ہے</div>
                <div class="bullet-point">یہ سڑک <strong>کینٹونمنٹ ایریا اور PAF کلب</strong> کے قریب بالکل ٹھیک ہے، لیکن کینٹونمنٹ کی حد ختم ہوتے ہی خوفناک حالت میں ہو جاتی ہے</div>
                <div class="bullet-point">یہ واضح تفاوت <span class="highlight">ترقیاتی فنڈز اور وسائل کی غیر منصفانہ تقسیم</span> کو ظاہر کرتا ہے</div>
            </div>

            <div class="subsection">
                <h3>🔨 نااہل سڑک مرمت کے طریقے</h3>
                <div class="bullet-point">گڑھوں کو مسلسل <strong>پتھر اور ملبے سے بھرا جاتا ہے</strong> بجائے مناسب سڑک کے مواد کے، جو ایک عارضی اور انتہائی خطرناک حل ہے</div>
                <div class="bullet-point">بارش کے وقت یہ ملبے سے بھرے گڑھے <span class="highlight">بڑے نکاسی آب کے مسائل</span> پیدا کرتے ہیں اور گاڑیوں کے لیے اور بھی خطرناک ہو جاتے ہیں</div>
                <div class="bullet-point">سڑک کے کچھ حصے مکمل طور پر ختم ہو گئے ہیں اور <strong>نیچے دھات نظر آ رہا ہے</strong>، جس سے یہ حصے مکمل طور پر ناقابل استعمال ہیں</div>
                <div class="bullet-point">ڈرائیورز کو آنے والی ٹریفک کے ساتھ گڑھوں سے بچنے کے لیے مجبور کیا جاتا ہے، جو <span class="highlight">وسیع پیمانے پر تناؤ اور حادثات کا خطرہ</span> پیدا کرتا ہے</div>
            </div>

            <div class="subsection">
                <h3>📜 تاریخی بدانتظامی اور ٹوٹے ہوئے وعدے</h3>
                <div class="bullet-point"><strong>میجر مصطفیٰ صابر شہید روڈ</strong> کی کئی بار "مرمت" ہوئی ہے، لیکن ہر بار نااہلی اور بدانتظامی کی وجہ سے مکمل ناکامی ہوئی</div>
                <div class="bullet-point">یہ مرمت صرف چند مہینوں بعد ٹوٹ جاتی ہے کیونکہ حکام <span class="highlight">بنیادی سیوریج اور نکاسی کے مسائل</span> حل کرنے میں ناکام ہیں</div>
                <div class="bullet-point"><strong>پی ایم ایل این پنجاب حکومت</strong> کے دوران <strong>میاں شہباز شریف</strong> کی قیادت میں بطور وزیر اعلیٰ اور <strong>خواجہ سعد رفیق</strong> کی بطور ایم این اے، اس علاقے کے لیے بڑے ترقیاتی منصوبوں کا اعلان کیا گیا تھا</div>
            </div>

            <div class="subsection">
                <h3>📋 مناسب منصوبہ بندی اور نگرانی کا فقدان</h3>
                <div class="bullet-point"><strong>علی ویو گارڈن سوسائٹی</strong> کو مکمل طور پر نظرانداز کیا گیا ہے جبکہ یہاں ہزاروں خاندان رہتے ہیں</div>
                <div class="bullet-point">مناسب نکاسی آب کا نظام نہیں بنایا گیا، جس سے <span class="highlight">بارش میں شدید سیلاب</span> آتا ہے</div>
                <div class="bullet-point">سٹریٹ لائٹنگ کا نظام مکمل طور پر غائب ہے، جو سیکورٹی کے خطرات پیدا کرتا ہے</div>
                <div class="bullet-point">ٹریفک منیجمنٹ سسٹم موجود نہیں ہے</div>
            </div>

            <div class="subsection">
                <h3>⚠️ چیک اینڈ بیلنس کی مکمل عدم موجودگی</h3>
                <div class="bullet-point">اس علاقے میں سڑک کی حالت یا مرمت کے معیار کے بارے میں <strong>کوئی نگرانی یا نظارت نہیں</strong> ہے</div>
                <div class="bullet-point">مین بیڈین روڈ پر دکانوں اور مکانات کی غیر قانونی تعمیر بلا روک ٹوک جاری ہے</div>
                <div class="bullet-point">فروٹ وینڈرز کو بنا کسی ضابطے کے مین روڈ پر کھڑے ہونے کی اجازت ہے</div>
                <div class="bullet-point">کار واش سٹیشنز مناسب نکاسی کے بغیر کام کرتے ہیں، والٹن کینٹونمنٹ بورڈ کی کوئی نگرانی نہیں</div>
            </div>
        </div>

        <div class="impact-section">
            <h2>💔 ہزاروں روزانہ مسافروں پر اثرات</h2>
            
            <div class="subsection">
                <h3>🏥 صحت اور سیفٹی کے مسائل</h3>
                <div class="bullet-point"><strong>حاملہ خواتین</strong> کو گڑھوں اور خطرناک سڑک کی وجہ سے مسلسل جھٹکوں سے شدید تکلیف اور صحت کے خطرات</div>
                <div class="bullet-point"><strong>بزرگ شہریوں</strong> کو کمر کے مسائل کی وجہ سے سفر کے دوران شدید درد، کچھ اس راستے سے مکمل طور پر بچتے ہیں</div>
                <div class="bullet-point">آنے والی ٹریفک کے ساتھ گڑھوں سے بچنے کا تناؤ <span class="highlight">ہزاروں مسافروں کے لیے نفسیاتی پریشانی</span> کا باعث ہے</div>
                <div class="bullet-point">خراب سڑک کی حالت اور ناکافی روشنی کی وجہ سے حادثات میں اضافہ</div>
                <div class="bullet-point"><strong>ایمرجنسی گاڑیوں</strong> کو ان حالات میں آمد و رفت میں مشکلات</div>
            </div>

            <div class="subsection">
                <h3>💰 معاشی اثرات</h3>
                <div class="bullet-point">خراب سڑک کی حالت اور کھلے دھات کی وجہ سے روزانہ گاڑیوں کو نقصان</div>
                <div class="bullet-point">ٹریفک جام اور کم رفتار سے چلنے کی وجہ سے ایندھن کا زیادہ استعمال</div>
                <div class="bullet-point">خطرناک سڑک کی حالت کی وجہ سے سفر کے وقت میں اضافہ اور ذہنی تھکان</div>
                <div class="bullet-point">مقامی کاروبار اور رہائشیوں کو متاثر کرنے والے زیادہ ٹرانسپورٹ اخراجات</div>
                <div class="bullet-point">علی ویو گارڈن اور آس پاس کے علاقوں میں خراب رابطے کی وجہ سے جائیداد کی قیمتوں میں کمی</div>
            </div>

            <div class="subsection">
                <h3>😔 سماجی اور نفسیاتی اثرات</h3>
                <div class="bullet-point">ہزاروں مسافروں کے لیے روزانہ تناؤ اور مایوسی جن کے پاس متبادل راستے نہیں ہیں</div>
                <div class="bullet-point">علی ویو گارڈن کے رہائشیوں کی سماجی علیحدگی خراب رابطے اور خطرناک سڑکوں پر سفر کی ہچکچاہٹ کی وجہ سے</div>
                <div class="bullet-point">حکومتی وعدوں اور ترقیاتی منصوبوں سے اعتماد کا خاتمہ جو کبھی عملی شکل نہیں لیتے</div>
            </div>
        </div>

        <div class="legal-section">
            <h2>⚖️ آئینی اور قانونی تحفظات</h2>
            <p>یہ صورتحال مندرجہ ذیل کے تحت سنگین تشویش کا باعث ہے:</p>
            
            <div class="subsection">
                <h3>📜 آئینی حقوق کی خلاف ورزیاں</h3>
                <div class="bullet-point"><strong>پاکستان کے آئین کا آرٹیکل 9</strong>: حق زندگی - جس میں محفوظ نقل و حمل اور بنیادی سہولات شامل ہیں</div>
                <div class="bullet-point"><strong>آرٹیکل 25</strong>: مساوات کا حق - عوامی خدمات میں منصفانہ سلوک اور ترقیاتی وسائل کی مساوی تقسیم</div>
                <div class="bullet-point"><strong>آرٹیکل 9A</strong>: صاف اور صحت مند ماحول کا حق</div>
            </div>
        </div>

        <div class="recommendations">
            <h2>💡 تعمیری تجاویز</h2>
            
            <div class="subsection">
                <h3>🚨 فوری اقدامات</h3>
                <ol>
                    <li class="numbered-item">بیڈین روڈ اور علی ویو گارڈن ایریا کا ماہر انجینئرز کی طرف سے جامع سروے</li>
                    <li class="numbered-item">حادثات کو روکنے کے لیے <strong>مناسب سڑک کے مواد (ملبہ نہیں)</strong> کے ساتھ انتہائی خطرناک حصوں کی ہنگامی مرمت</li>
                    <li class="numbered-item">کھلے دھات کے پیچز کا فوری حل جو سڑک کو مکمل طور پر ناقابل استعمال بناتے ہیں</li>
                    <li class="numbered-item">شام کے وقت سیفٹی کے لیے عارضی روشنی کا انتظام</li>
                    <li class="numbered-item">سڑک پر غیر قانونی قبضوں کے خلاف فوری کارروائی</li>
                    <li class="numbered-item">سٹریٹ وینڈرز اور کار واش سٹیشنز کا ضابطہ</li>
                </ol>
            </div>

            <div class="subsection">
                <h3>🏗️ طویل مدتی ترقیاتی منصوبہ</h3>
                <ol>
                    <li class="numbered-item">بنیادی سیوریج کے مسائل کے حل کے ساتھ بیڈین روڈ کی مکمل تعمیر نو</li>
                    <li class="numbered-item">قریبی مکمل ہونے والے منصوبوں کے معیار کے مطابق کینٹونمنٹ کی حدود سے آگے معیاری انفراسٹرکچر کی توسیع</li>
                    <li class="numbered-item">اصل منصوبے کے مطابق علی ویو گارڈن سوسائٹی کے انفراسٹرکچر کی ترقی</li>
                    <li class="numbered-item">ٹریفک منیجمنٹ سسٹم اور مناسب روڈ سائنیج کا نفاذ</li>
                    <li class="numbered-item">مناسب نگرانی کے ساتھ باقاعدگی سے مرمت کے شیڈول کا قیام</li>
                </ol>
            </div>

            <div class="subsection">
                <h3>⚖️ منصفانہ وسائل کی تقسیم</h3>
                <div class="bullet-point">ایئرپورٹ روڈ، غازی روڈ، اور بھٹہ چوک جیسے علاقوں کے ساتھ مساوی سلوک جنہیں مناسب ترقی ملی ہے</div>
                <div class="bullet-point">کینٹونمنٹ اور سول علاقوں کے درمیان امتیاز کے بغیر ترقیاتی فنڈز کی شفاف تقسیم</div>
                <div class="bullet-point">پی ایم ایل این حکومت کے دور میں کیے گئے وعدوں اور منصوبوں کا احیاء اور نفاذ</div>
                <div class="bullet-point">جوابدہی کو یقینی بنانے کے لیے منصوبہ بندی اور نگرانی میں کمیونٹی کی شمولیت</div>
            </div>
        </div>

        <div class="contact-info">
            <h2>📞 رابطہ کی معلومات</h2>
            <div class="contact-detail">ریفرنس نمبر: <span class="highlight">{reference_number}</span></div>
            <div class="contact-detail">تاریخ: {date_formatted}</div>
            <div class="contact-detail">وقت: {time_formatted}</div>
            <div class="contact-detail">مقام: {area_name}, {city}, {province}</div>
        </div>

        <div class="alert">
            ⚠️ ہم احتراماً آپ سے درخواست کرتے ہیں کہ بدانتظامی اور نااہلی کے ان طویل مسائل پر فوری توجہ دیں۔ اس علاقے کے رہائشی لاہور کے دوسرے حصوں جیسے انفراسٹرکچر کے مستحق ہیں، خاص طور پر ان وعدوں اور منصوبوں کو دیکھتے ہوئے جو پچھلے سالوں میں کیے گئے تھے۔
        </div>

        <div class="closing">
            <p>ہم نے موجودہ حالات کی تصاویر اور ویڈیو شواہد منسلک کیے ہیں اور مناسب منصوبہ بندی، قابل عمل، اور منصفانہ وسائل کی تقسیم کے ذریعے ان مسائل کے فوری حل کی امید رکھتے ہیں۔</p>
            
            <p>آپ کے وقت اور توجہ کا شکریہ۔</p>
            
            <div class="signature">
                <p>احتراماً،<br>
                <strong>{area_name} کے تشویش مند رہائشی</strong><br>
                {city}, {country}</p>
            </div>
        </div>
    </div>

    <div class="footer">
        یہ انفراسٹرکچر کی بدانتظامی اور غفلت کے حوالے سے شہریوں کی جائز شکایت ہے۔<br>
        <strong>ریفرنس: {reference_number}</strong>
    </div>
</body>
</html>""",
    },
    3: {
        "name": "Administrative Reform Request Template",
        "language": "English",
        "content_type": "html",  # Specify HTML content type
        "subject_template": "Request for Administrative Review: {area_name} Infrastructure Development (Ref: {reference_number})",
        "body_template": """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Arial', 'Segoe UI', sans-serif;
            line-height: 1.6;
            color: #333333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 8px 8px 0 0;
            margin-bottom: 0;
        }}
        .header h1 {{
            margin: 0;
            font-size: 24px;
            font-weight: bold;
        }}
        .content {{
            background-color: #ffffff;
            padding: 30px;
            border: 1px solid #e0e0e0;
            border-radius: 0 0 8px 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .greeting {{
            font-size: 16px;
            margin-bottom: 25px;
            color: #2c3e50;
        }}
        .section {{
            margin: 25px 0;
            padding: 20px;
            border-left: 4px solid #9b59b6;
            background-color: #f8f4fd;
            border-radius: 0 5px 5px 0;
        }}
        .section h2 {{
            color: #8e44ad;
            font-size: 18px;
            margin-top: 0;
            margin-bottom: 15px;
            font-weight: bold;
        }}
        .subsection {{
            margin: 20px 0;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
            border-left: 3px solid #3498db;
        }}
        .subsection h3 {{
            color: #2980b9;
            font-size: 16px;
            margin-top: 0;
            margin-bottom: 10px;
            font-weight: bold;
        }}
        .bullet-point {{
            margin: 8px 0;
            padding-left: 15px;
            position: relative;
        }}
        .bullet-point:before {{
            content: "•";
            color: #9b59b6;
            font-weight: bold;
            position: absolute;
            left: 0;
        }}
        .contact-info {{
            background-color: #f1f5f9;
            padding: 20px;
            border-radius: 8px;
            border: 2px solid #cbd5e1;
            margin: 25px 0;
        }}
        .contact-info h2 {{
            color: #334155;
            margin-top: 0;
            font-size: 16px;
        }}
        .contact-detail {{
            margin: 5px 0;
            font-weight: bold;
            color: #475569;
        }}
        .closing {{
            margin-top: 30px;
            padding: 20px;
            background-color: #f8fafc;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }}
        .signature {{
            margin-top: 20px;
            font-weight: bold;
            color: #2c3e50;
        }}
        .footer {{
            margin-top: 30px;
            padding: 15px;
            background-color: #2c3e50;
            color: white;
            text-align: center;
            border-radius: 8px;
            font-size: 12px;
        }}
        .highlight {{
            background-color: #e8f4fd;
            padding: 2px 6px;
            border-radius: 3px;
            border: 1px solid #bee5eb;
            font-weight: bold;
        }}
        ol, ul {{
            margin: 10px 0;
            padding-left: 25px;
        }}
        li {{
            margin: 8px 0;
            line-height: 1.5;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📋 ADMINISTRATIVE REVIEW REQUEST</h1>
        <p style="margin: 5px 0 0 0; font-size: 14px; opacity: 0.9;">Infrastructure Development & Management</p>
    </div>
    
    <div class="content">
        <div class="greeting">
            <strong>Honorable Government Officials,</strong>
        </div>
        
        <p>We respectfully submit this formal request for administrative review and corrective action regarding the infrastructure management in <span class="highlight">{area_name}, {city}</span>. As concerned citizens, we seek your intervention to address systematic issues affecting thousands of residents daily.</p>

        <div class="section">
            <h2>📊 ADMINISTRATIVE REVIEW REQUEST</h2>
            
            <div class="subsection">
                <h3>Current Administrative Challenges</h3>
                <p>Our area faces significant infrastructure challenges that appear to stem from administrative oversights and resource allocation decisions:</p>
                <div class="bullet-point"><strong>Inconsistent Development Standards</strong>: While Cantonment-controlled areas maintain excellent infrastructure, civilian areas immediately adjacent show severe deterioration</div>
                <div class="bullet-point"><strong>Absent Coordination</strong>: Multiple agencies (Walton Cantonment Board, district administration, development authorities) seem to lack coordination in area management</div>
                <div class="bullet-point"><strong>Resource Allocation Imbalances</strong>: Established areas receive regular maintenance while emerging residential areas like Ali View Garden remain underserved</div>
            </div>

            <div class="subsection">
                <h3>1. Planning and Zoning Failures</h3>
                <div class="bullet-point">Inadequate zoning enforcement allowing commercial encroachment on residential roads</div>
                <div class="bullet-point">Missing master planning for integrated infrastructure development</div>
                <div class="bullet-point">Lack of traffic impact assessments for new developments</div>
            </div>

            <div class="subsection">
                <h3>2. Regulatory Oversight Gaps</h3>
                <div class="bullet-point">Absence of regular road condition monitoring systems</div>
                <div class="bullet-point">Inadequate enforcement of building codes and road usage regulations</div>
                <div class="bullet-point">Missing coordination between utility services and road maintenance</div>
            </div>

            <div class="subsection">
                <h3>3. Service Delivery Inconsistencies</h3>
                <div class="bullet-point">Disparate service levels between different administrative jurisdictions</div>
                <div class="bullet-point">Lack of citizen feedback mechanisms for infrastructure reporting</div>
                <div class="bullet-point">Absent emergency response protocols for infrastructure failures</div>
            </div>
        </div>

        <div class="section">
            <h2>📈 IMPACT ASSESSMENT</h2>
            
            <div class="subsection">
                <h3>Public Health and Safety</h3>
                <p>The current conditions create documented public health and safety concerns:</p>
                <div class="bullet-point">Increased emergency response times due to poor road conditions</div>
                <div class="bullet-point">Higher accident rates in poorly lit and maintained areas</div>
                <div class="bullet-point">Public health risks from stagnant water due to poor drainage</div>
            </div>

            <div class="subsection">
                <h3>Economic Implications</h3>
                <div class="bullet-point">Reduced property values affecting thousands of families</div>
                <div class="bullet-point">Increased transportation costs for residents and businesses</div>
                <div class="bullet-point">Lost economic opportunities due to poor connectivity</div>
            </div>
        </div>

        <div class="section">
            <h2>⚖️ CONSTITUTIONAL FRAMEWORK FOR ACTION</h2>
            <p>Our request aligns with constitutional principles:</p>
            <div class="bullet-point"><strong>Article 9</strong>: Ensures right to life which encompasses safe and accessible infrastructure</div>
            <div class="bullet-point"><strong>Article 25</strong>: Guarantees equality in public service provision</div>
            <div class="bullet-point"><strong>Article 38(d)</strong>: State obligation to provide basic necessities including housing and infrastructure</div>
        </div>

        <div class="section">
            <h2>💡 PROPOSED ADMINISTRATIVE SOLUTIONS</h2>
            
            <div class="subsection">
                <h3>1. Institutional Coordination</h3>
                <div class="bullet-point">Establish inter-agency coordination committee for area development</div>
                <div class="bullet-point">Define clear jurisdictional responsibilities</div>
                <div class="bullet-point">Create unified complaint and monitoring system</div>
            </div>

            <div class="subsection">
                <h3>2. Planning Integration</h3>
                <div class="bullet-point">Develop comprehensive area master plan</div>
                <div class="bullet-point">Integrate utility services planning with road development</div>
                <div class="bullet-point">Establish development impact assessment protocols</div>
            </div>

            <div class="subsection">
                <h3>3. Service Standardization</h3>
                <div class="bullet-point">Implement uniform infrastructure standards across jurisdictions</div>
                <div class="bullet-point">Establish regular maintenance schedules</div>
                <div class="bullet-point">Create citizen engagement mechanisms</div>
            </div>

            <div class="subsection">
                <h3>4. Resource Optimization</h3>
                <div class="bullet-point">Review and balance resource allocation across areas</div>
                <div class="bullet-point">Explore public-private partnership opportunities</div>
                <div class="bullet-point">Implement transparent procurement processes</div>
            </div>
        </div>

        <div class="section">
            <h2>📋 MONITORING AND ACCOUNTABILITY</h2>
            <p>We respectfully request:</p>
            <div class="bullet-point">Establishment of timeline for addressing identified issues</div>
            <div class="bullet-point">Regular progress reporting to affected communities</div>
            <div class="bullet-point">Creation of citizen oversight mechanisms</div>
            
            <p><strong>Documentation:</strong> Attached photographic and video evidence demonstrates current road conditions, safety hazards, illegal encroachments, drainage gaps, and comparative conditions with nearby developed areas.</p>
        </div>

        <div class="contact-info">
            <h2>📞 CONTACT INFORMATION</h2>
            <div class="contact-detail">Reference Number: <span class="highlight">{reference_number}</span></div>
            <div class="contact-detail">Date: {date_formatted}</div>
            <div class="contact-detail">Time: {time_formatted}</div>
            <div class="contact-detail">Location: {area_name}, {city}, {province}</div>
        </div>

        <div class="closing">
            <p>We believe that through proper administrative coordination and systematic planning, these challenges can be addressed effectively. We look forward to working collaboratively with relevant authorities to improve infrastructure standards and administrative efficiency.</p>
            
            <p>Thank you for your attention to these important administrative matters.</p>
            
            <div class="signature">
                <p>Respectfully submitted,<br>
                <strong>Citizens Committee for {area_name} Development</strong><br>
                {city}, {country}</p>
            </div>
        </div>
    </div>

    <div class="footer">
        This is a formal administrative review request for infrastructure development.<br>
        <strong>Reference: {reference_number}</strong>
    </div>
</body>
</html>""",
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
        "Potholes continuously filled with rubble instead of proper road material, creating dangerous temporary solutions",
        "Exposed metal patches where road has completely deteriorated, making sections un-drivable",
        "Drivers forced to avoid potholes while managing incoming traffic, causing stress and accident risks",
        "Complete absence of check and balance in road maintenance and oversight",
        "Discriminatory development - Airport Road, Ghazi Road, and Bhatta Chowk completed while Bedian Road neglected",
        "Nawaz Sharif Interchange fully revamped while nearby Bedian Road remains abandoned",
        "Major Mustafa Sabir Shaheed Road repeatedly repaired but fails due to incompetence in addressing sewage issues",
        "Broken promises from PMLN government era under Shahbaz Sharif and Khawaja Saad Rafique regarding area development",
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
    "duration": "Ongoing systemic neglect for years despite promises of development",
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
    "cron_schedule": "0 4 * * 1,3,5",  # Mon, Wed, Fri at 4:00 AM UTC (9:00 AM Pakistan time)
    "python_version": "3.11",
    "workflow_name": "Government Road Complaint Emails (Mon/Wed/Fri)",
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
