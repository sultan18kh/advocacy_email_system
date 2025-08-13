# 🚀 Automated Government Email Scheduler

This solution sends automated emails to government officials about road conditions in Bedian Road & Ali View Garden area, Lahore.

## 📋 Requirements

### requirements.txt

```
schedule==1.2.0
pytz==2023.3
```

**Note**: Previous versions incorrectly listed `secure-smtplib` which doesn't exist. The system uses Python's built-in `smtplib`.

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
   - Supported formats: JPG, PNG, MP4, MOV, PDF, DOC, ZIP, and more
   - Keep file sizes under 25MB each
   - **NEW**: System automatically discovers all valid files

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

### Step 4: Test Setup

1. **Install Dependencies Locally (Optional)**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run Local Tests**

   ```bash
   python src/test_email.py
   ```

3. **Manual GitHub Test**
   - Go to Actions tab in your repository
   - Click "Government Road Complaint Emails (Mon/Wed/Fri)"
   - Click "Run workflow" → "Run workflow"
   - Check if emails are sent successfully

### Step 5: Schedule Activation

The automated schedule will run **Monday, Wednesday, and Friday at 9:00 AM Pakistan Time** automatically once the workflow file is in place.

## 🛡️ Anti-Spam & Anti-Blocking Features

### Email Rotation

- Uses up to 3 different email services (Gmail, Outlook, Yahoo)
- Rotates between services to avoid single-service blocking
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
- **Reduced frequency**: Mon/Wed/Fri only (not daily)

### Spam Prevention

- Professional subject lines
- Legitimate government complaint content
- Proper email authentication
- Timezone-aware timestamps

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
│   ├── send_single_email.py    # Main email sender (UPDATED)
│   ├── test_email.py          # Test suite (ENHANCED)
│   ├── setup.py               # Setup script
│   └── config.py              # Configuration (UPDATED)
├── docs/                       # Documentation
│   ├── QUICK_START.md         # Quick setup guide
│   ├── GITHUB_SECRETS_GUIDE.md # Secrets configuration
│   ├── SETUP_SECRETS.md       # Complete setup guide
│   └── DEPLOYMENT_CHECKLIST.md # Deployment checklist
├── .github/workflows/
│   └── send-daily-emails.yml   # GitHub Actions workflow (Mon/Wed/Fri)
├── requirements.txt            # Python dependencies (FIXED)
├── README.md                   # This guide
└── media/                      # Your photos/videos (AUTO-DISCOVERED)
    ├── [any_photo_name].jpg
    ├── [any_video_name].mp4
    └── [any_document_name].pdf
```

## 🆕 New Features (Latest Version)

### ✅ Automatic Media File Discovery

- **No more fixed filenames** - use any descriptive names
- **22 supported file types** - images, videos, documents, archives
- **Smart size management** - automatic validation and limits
- **Detailed logging** - shows what's included/skipped

### ✅ Enhanced Timezone Support

- **Pakistan Standard Time** (PKT) support with `pytz`
- **Accurate scheduling** - proper UTC to PKT conversion
- **Timezone-aware timestamps** in all emails

### ✅ Improved Error Handling

- **Specific SMTP errors** - authentication, connection, sending
- **File validation** - type, size, accessibility checks
- **Better debugging** - detailed error messages and solutions

### ✅ Reduced Frequency

- **Mon/Wed/Fri only** - more sustainable approach
- **Professional pattern** - avoids daily spam appearance
- **Better compliance** - less likely to trigger filters

## 🎯 Targeting Strategy

### Primary Recipients

- Walton Cantonment Board
- Punjab CM Office
- Local Development Authority
- District Administration Lahore
- Punjab Highway Department

### Schedule

- **Monday**: Administrative focus
- **Wednesday**: Follow-up and escalation
- **Friday**: Weekly summary and pressure

## 📊 Monitoring & Analytics

### GitHub Actions Logs

- Check execution status Mon/Wed/Fri
- Monitor email sending success
- Track template rotation
- View detailed error messages

### Email Tracking

- Monitor government responses
- Track media coverage
- Document any action taken
- Maintain complaint log

## 🔧 Troubleshooting

### Common Issues

1. **"No module named 'pytz'" Error**

   ```bash
   pip install pytz
   # or
   pip install -r requirements.txt
   ```

2. **Emails Not Sending**

   - Check GitHub Secrets are set correctly
   - Verify email passwords/app passwords
   - Check spam folders for test emails

3. **Workflow Not Running**

   - Look for "Government Road Complaint Emails (Mon/Wed/Fri)" (exact name)
   - Check cron syntax: `0 4 * * 1,3,5` (Mon/Wed/Fri at 4 AM UTC)
   - Verify repository is not archived

4. **Media Files Not Found**
   - Ensure files are in `media/` directory
   - Check file types are supported (see list above)
   - Verify files are under 25MB each

### Support Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Test configuration
python src/test_email.py

# Check GitHub Actions status
# Go to repository → Actions → Latest run
```

## 📈 Scaling Options

### Increase Frequency

- Modify cron schedule: `0 4 * * *` for daily
- Add multiple sends per day
- Target different officials at different times

### Add More Email Services

- ProtonMail accounts
- Custom SMTP servers
- Business email accounts

### Enhanced Media

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
- Clear identification as automated system

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

## 🎯 Success Metrics

### Short Term (1-3 months)

- Email delivery success rate > 95%
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

## 🚀 Quick Start Checklist

- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Create at least one email account (Gmail, Outlook, or Yahoo)
- [ ] Set up GitHub repository
- [ ] Add all code files
- [ ] Upload media files (any supported format, any filename)
- [ ] Configure GitHub Secrets (minimum 1 email service)
- [ ] Test: `python src/test_email.py`
- [ ] Test manual workflow execution
- [ ] Verify Mon/Wed/Fri automation is working
- [ ] Monitor for government responses

**Your automated government accountability system is now ready! 🏆**

---

**Latest Update**: Enhanced with automatic file discovery, timezone support, improved error handling, and reduced to Mon/Wed/Fri schedule for better sustainability.
