# 🚀 Quick Start Guide - Automated Government Email System

## ⚡ Get Started in 10 Minutes

### 1. Install Dependencies (2 minutes)

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install schedule pytz
```

### 2. Create Email Account (5 minutes)

**You only need ONE email account to get started!**

Choose one of these options:

- **Gmail** (Recommended): Create account → Enable 2FA → Generate App Password
- **Outlook**: Create account → Enable 2FA if required
- **Yahoo**: Create account → Enable 2FA → Generate App Password

_Optional: Create 2-3 accounts for better rotation and anti-blocking_

### 3. Set Up GitHub Repository (2 minutes)

```bash
# Push this code to a new GitHub repository
git remote add origin https://github.com/yourusername/government-road-complaints.git
git add .
git commit -m "Initial commit: Automated government email system"
git push -u origin main
```

### 4. Configure GitHub Secrets (3 minutes)

Go to your repository → Settings → Secrets and Variables → Actions

**Minimum Setup (1 Email Service):**

- `GMAIL_EMAIL` = your_gmail@gmail.com
- `GMAIL_APP_PASSWORD` = your_gmail_app_password

**OR**

- `OUTLOOK_EMAIL` = your_outlook@outlook.com
- `OUTLOOK_PASSWORD` = your_outlook_password

**OR**

- `YAHOO_EMAIL` = your_yahoo@yahoo.com
- `YAHOO_PASSWORD` = your_yahoo_password

### 5. Add Media Files (2 minutes)

Add ANY photos/videos to `media/` directory with ANY filenames:

- `road_damage_january_2025.jpg` - Photo of potholes
- `flooding_during_rain.mp4` - Video of flooding
- `pothole_damage_to_car.png` - Vehicle damage photos
- `official_complaint_letter.pdf` - Documents

**NEW**: System automatically discovers and validates all files!

### 6. Test the System (1 minute)

**Local Test:**

```bash
python src/test_email.py
```

**GitHub Test:**

- Go to Actions tab in your repository
- Click **"Government Road Complaint Emails (Mon/Wed/Fri)"** (exact name)
- Click "Run workflow" → "Run workflow"
- Check if emails are sent successfully

## 🎯 What Happens Next

✅ **Monday/Wednesday/Friday at 9:00 AM Pakistan Time**: System automatically sends emails
✅ **Email Rotation**: Uses your configured email service(s)
✅ **Template Rotation**: 3 different templates (English, Urdu, Legal)
✅ **Anti-Spam**: Random delays, professional formatting
✅ **Media Attachments**: ALL valid files automatically attached

## 📧 Email Recipients

The system will send emails to:

- Walton Cantonment Board
- Punjab CM Office
- Local Development Authority
- District Administration Lahore
- Punjab Highway Department
- Government complaint cells

## 🛡️ Anti-Blocking Features

- **Email Service Rotation**: Uses your configured service(s) in rotation
- **Content Variation**: Different templates each day
- **Professional Format**: Legitimate government complaint format
- **Random Delays**: 10-60 second delays between operations
- **Reduced Frequency**: Mon/Wed/Fri only (not daily)
- **Media Attachments**: Photos/videos as evidence

## 📊 Monitoring

- **GitHub Actions Logs**: Check Mon/Wed/Fri execution status
- **Email Delivery**: Monitor success rates
- **Government Responses**: Track any acknowledgments
- **Media Coverage**: Document any press coverage

## 🔧 Troubleshooting

### Dependencies Issues?

```bash
# Install missing dependencies
pip install -r requirements.txt
# or individually
pip install schedule pytz
```

### Emails Not Sending?

1. Check GitHub Secrets are configured correctly
2. Verify email password/app password
3. Check spam folders for test emails
4. Look for "Government Road Complaint Emails (Mon/Wed/Fri)" workflow

### Workflow Not Running?

1. Check GitHub Actions are enabled
2. Look for exact workflow name: "Government Road Complaint Emails (Mon/Wed/Fri)"
3. Verify schedule: Mon/Wed/Fri at 4:00 AM UTC (9:00 AM PKT)
4. Test with manual workflow trigger

### Media Files Not Attached?

1. Ensure files are in `media/` directory
2. Check file types are supported (JPG, PNG, MP4, PDF, etc.)
3. Verify files are under 25MB each
4. Run `python src/test_email.py` to see file discovery

### Need to Update Recipients?

Edit `src/config.py` and update the `RECIPIENT_EMAILS` list

## 📈 Success Metrics

**Short Term (1-3 months):**

- Email delivery success rate > 95% (Mon/Wed/Fri)
- Zero email account blocks
- Government acknowledgment received

**Medium Term (3-6 months):**

- Media coverage of issue
- Government inspection visit
- Preliminary repair work started

**Long Term (6-12 months):**

- Complete road reconstruction
- Drainage system installation
- Regular maintenance schedule

## 💰 Cost

**Total Monthly Cost: $0**

- GitHub Actions: Free (2000 minutes/month)
- Email accounts: Free versions sufficient
- File storage: GitHub repository free

## ⚖️ Legal Compliance

This system is designed for legitimate civic engagement:

- Constitutional right to petition government
- Freedom of expression protection
- Professional, respectful communication
- Factual documentation of issues
- Reduced frequency to avoid spam appearance

## 🆕 Latest Features

### ✅ Automatic File Discovery

- Use ANY filenames for your media files
- 22+ supported file types
- Automatic size validation
- Smart attachment management

### ✅ Enhanced Scheduling

- **Monday/Wednesday/Friday only** - more sustainable
- Pakistan timezone support with `pytz`
- Professional sending pattern

### ✅ Improved Testing

- Comprehensive test suite: `python src/test_email.py`
- Better error messages and solutions
- Dependency validation

## 🎉 You're Ready!

Your automated government accountability system is now active and will:

- Send emails **Monday, Wednesday, and Friday** at 9:00 AM Pakistan time
- Use your configured email service(s)
- Use 3 different templates in rotation
- Include ALL valid media files automatically
- Provide detailed logging and error reporting

**The system will start working immediately after you complete the setup steps above!**

---

📖 **For detailed instructions**: See `README.md`
🔐 **For secrets setup**: See `SETUP_SECRETS.md`
📋 **For deployment checklist**: See `DEPLOYMENT_CHECKLIST.md`
🧪 **For testing**: Run `python src/test_email.py`
