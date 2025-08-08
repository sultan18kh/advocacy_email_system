# 🚀 Automated Government Email Scheduler

This solution sends daily automated emails to government officials about road conditions in Bedian Road & Ali View Garden area, Lahore.

## 📋 Requirements

### requirements.txt
```
schedule==1.2.0
secure-smtplib==0.1.1
```

## 🏗️ Setup Instructions

### Step 1: Create Email Account

**You only need ONE email account to get started!**

Choose one of these options:

1. **Gmail Account** (Recommended)
   - Go to gmail.com and create new account
   - Enable 2-Factor Authentication
   - Generate App Password: Gmail → Settings → Security → App Passwords
   - Note down email and app password

2. **Outlook Account**
   - Go to outlook.com and create new account
   - Enable 2-Factor Authentication if required
   - Note down email and password

3. **Yahoo Account**
   - Go to yahoo.com and create new account
   - Generate App Password if 2FA enabled
   - Note down email and password

**Optional:** Create 2-3 accounts for better rotation and anti-blocking protection.

### Step 2: GitHub Repository Setup

1. **Create New Repository**
   ```bash
   # Create new repo on GitHub
   # Name: government-road-complaints
   # Description: Automated system for road infrastructure complaints
   # Set to Private for security
   ```

2. **Add Files to Repository**
   ```
   government-road-complaints/
   ├── .github/
   │   └── workflows/
   │       └── send-daily-emails.yml
   ├── src/
   │   ├── send_single_email.py
   │   ├── test_email.py
   │   ├── setup.py
   │   └── config.py
   ├── docs/
   │   ├── QUICK_START.md
   │   ├── GITHUB_SECRETS_GUIDE.md
   │   ├── SETUP_SECRETS.md
   │   └── DEPLOYMENT_CHECKLIST.md
   ├── requirements.txt
   ├── README.md
   └── media/
       ├── road_photo1.jpg
       ├── road_photo2.jpg
       ├── pothole_video.mp4
       └── flooding_video.mp4
   ```

3. **Add Your Media Files**
   - Take photos/videos of road conditions
   - Upload to `media/` folder in repository
   - Supported formats: JPG, PNG, MP4, MOV
   - Keep file sizes under 25MB each

### Step 3: Configure GitHub Secrets

Go to your repository → Settings → Secrets and Variables → Actions → New Repository Secret

**Minimum Setup (1 Email Service):**
```
GMAIL_EMAIL = your_gmail@gmail.com
GMAIL_APP_PASSWORD = your_gmail_app_password
```

**OR**
```
OUTLOOK_EMAIL = your_outlook@outlook.com
OUTLOOK_PASSWORD = your_outlook_password
```

**OR**
```
YAHOO_EMAIL = your_yahoo@yahoo.com
YAHOO_PASSWORD = your_yahoo_password
```

**Optional (For Better Rotation):**
Add all 6 secrets if you want to use multiple email services.

### Step 4: Customize Email Recipients

Edit `send_single_email.py` and update the `recipient_emails` list with actual government email addresses:

```python
self.recipient_emails = [
    # Add real email addresses here
    "complaints@waltoncantonment.gov.pk",
    "cm@punjab.gov.pk",
    # ... add more addresses
]
```

### Step 5: Test Setup

1. **Manual Test**
   - Go to Actions tab in your repository
   - Click "Daily Government Road Complaint Emails"
   - Click "Run workflow" → "Run workflow"
   - Check if emails are sent successfully

2. **Check Logs**
   - Monitor the Actions logs for any errors
   - Verify emails are being sent from different accounts
   - Confirm recipients are receiving emails

### Step 6: Schedule Activation

The automated schedule will run daily at 9:00 AM Pakistan Time automatically once the workflow file is in place.

## 🛡️ Anti-Spam & Anti-Blocking Features

### Email Rotation
- Uses 3 different email services (Gmail, Outlook, Yahoo)
- Rotates daily to avoid single-service blocking
- Different templates and content each day

### Content Variation
- 3 different email templates (English formal, Urdu, Legal)
- Templates rotate based on day of year
- Unique timestamps and reference numbers
- Natural language variations

### Sending Patterns
- Random delays between 10-60 seconds
- Professional, legitimate complaint format
- Proper email headers and formatting
- BCC recipients to hide distribution list

### Spam Prevention
- Professional subject lines
- Legitimate government complaint content
- Proper email authentication
- No mass-mailing indicators

## 📨 Email Templates Features

### Template 1: Urgent English
- Emergency tone with constitutional references
- Detailed impact documentation
- Comparison with better-maintained areas
- Professional formatting

### Template 2: Formal Urdu
- Respectful Urdu language
- Cultural context appropriate
- Government protocol compliant
- Local context emphasis

### Template 3: Citizen Rights
- Legal framework references
- Constitutional rights basis
- Escalation timeline mentioned
- Documentation emphasis

## 🗂️ File Structure

```
├── src/                        # Python source code
│   ├── send_single_email.py    # Main email sender
│   ├── test_email.py          # Test suite
│   ├── setup.py               # Setup script
│   └── config.py              # Configuration
├── docs/                       # Documentation
│   ├── QUICK_START.md         # Quick setup guide
│   ├── GITHUB_SECRETS_GUIDE.md # Secrets configuration
│   ├── SETUP_SECRETS.md       # Complete setup guide
│   └── DEPLOYMENT_CHECKLIST.md # Deployment checklist
├── .github/workflows/
│   └── send-daily-emails.yml   # GitHub Actions workflow
├── requirements.txt            # Python dependencies
├── README.md                   # This guide
└── media/                      # Your photos/videos
    ├── road_photo1.jpg
    ├── road_photo2.jpg
    ├── pothole_video.mp4
    └── flooding_video.mp4
```

## 🎯 Targeting Strategy

### Primary Recipients
- Walton Cantonment Board
- Punjab CM Office
- Local Development Authority
- District Administration Lahore
- Punjab Highway Department

### Secondary Recipients  
- Local MNA/MPA offices
- Media outlets for pressure
- Punjab Government complaint cells

### Escalation Path
- Week 1-2: Regular administrative emails
- Week 3-4: Legal framework references
- Month 2+: Media involvement threats
- Month 3+: Court petition warnings

## 📊 Monitoring & Analytics

### GitHub Actions Logs
- Check daily execution status
- Monitor email sending success
- Track template rotation
- View error messages

### Email Tracking
- Monitor government responses
- Track media coverage
- Document any action taken
- Maintain complaint log

## 🔧 Troubleshooting

### Common Issues

1. **Emails Not Sending**
   - Check GitHub Secrets are set correctly
   - Verify email passwords/app passwords
   - Check spam folders for test emails

2. **Blocked Email Accounts**
   - Create new email accounts
   - Update GitHub Secrets
   - Use different email providers

3. **Workflow Not Running**
   - Check cron syntax in workflow file
   - Verify repository is not archived
   - Check GitHub Actions are enabled

4. **Media Files Too Large**
   - Compress videos/images
   - Keep files under 25MB
   - Use efficient formats (JPG, MP4)

### Support Commands

```bash
# Test email configuration locally
python src/test_email.py

# Run setup script
python src/setup.py

# Check GitHub Actions status
# Go to repository → Actions → Latest run

# Validate workflow syntax
# Use GitHub's workflow validator
```

## 📈 Scaling Options

### Increase Frequency
- Modify cron schedule in workflow
- Add multiple daily sends
- Target different officials at different times

### Add More Email Services
- ProtonMail accounts
- Custom SMTP servers
- Business email accounts

### Enhanced Templates
- Add more language variations
- Create issue-specific templates
- Include legal citations

### Media Enhancement
- Regular photo/video updates
- Drone footage of area
- Time-lapse documentation
- Comparative area photos

## ⚖️ Legal Compliance

### Legitimate Use
- Constitutional right to petition government
- Freedom of expression protection
- Citizen complaint mechanisms
- Public service accountability

### Professional Standards
- Respectful communication tone
- Factual information only
- No threatening language
- Proper identification as citizen

### Documentation
- Keep copies of all communications
- Maintain evidence of road conditions
- Document government responses
- Record any improvements made

## 💰 Cost Analysis

### Free Tier Usage
- GitHub Actions: 2000 minutes/month (free)
- Email accounts: Free versions sufficient
- File storage: GitHub repository free
- **Total Monthly Cost: $0**

### Optional Upgrades
- GitHub Pro: $4/month (more Actions minutes)
- Premium email accounts: $5-10/month
- Custom domain: $10-15/year
- **Recommended for scaling: $15-25/month**

## 🎯 Success Metrics

### Short Term (1-3 months)
- Daily email delivery success rate > 95%
- Zero email account blocks
- Template rotation working
- Government acknowledgment received

### Medium Term (3-6 months)
- Media coverage of issue
- Government inspection visit
- Preliminary repair work started
- Community support mobilized

### Long Term (6-12 months)
- Complete road reconstruction
- Drainage system installation
- Street lighting restored
- Regular maintenance schedule

## 📞 Contact & Support

For technical issues with this automation:
1. Check GitHub Actions logs first
2. Verify all secrets are configured
3. Test with manual workflow trigger
4. Create GitHub issue in repository

For road condition updates:
- Update media files in repository
- Modify email templates as needed
- Adjust recipient lists
- Document government responses

---

**Remember**: This is a tool for legitimate civic engagement. Always maintain respectful, professional communication with government officials while persistently advocating for basic infrastructure rights.

## 🚀 Quick Start Checklist

- [ ] Create at least one email account (Gmail, Outlook, or Yahoo)
- [ ] Set up GitHub repository
- [ ] Add all code files
- [ ] Upload media files (photos/videos)
- [ ] Configure GitHub Secrets (minimum 1 email service)
- [ ] Test manual workflow execution
- [ ] Verify daily automation is working
- [ ] Monitor for government responses
- [ ] Document any progress or improvements

**Your automated government accountability system is now ready! 🏆**
