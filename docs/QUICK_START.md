# 🚀 Quick Start Guide - Automated Government Email System

## ⚡ Get Started in 5 Minutes

### 1. Create Email Account (5 minutes)
**You only need ONE email account to get started!**

Choose one of these options:
- **Gmail** (Recommended): Create account → Enable 2FA → Generate App Password
- **Outlook**: Create account → Enable 2FA if required
- **Yahoo**: Create account → Enable 2FA → Generate App Password

*Optional: Create 2-3 accounts for better rotation and anti-blocking*

### 2. Set Up GitHub Repository (2 minutes)
```bash
# Push this code to a new GitHub repository
git remote add origin https://github.com/yourusername/government-road-complaints.git
git add .
git commit -m "Initial commit: Automated government email system"
git push -u origin main
```

### 3. Configure GitHub Secrets (3 minutes)
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

### 4. Add Media Files (2 minutes)
Replace placeholder files in `media/` directory with actual photos/videos:
- `road_photo1.jpg` - Photo of potholes
- `road_photo2.jpg` - Photo of flooding
- `pothole_video.mp4` - Video of road damage
- `flooding_video.mp4` - Video of flooding

### 5. Test the System (1 minute)
- Go to Actions tab in your repository
- Click "Daily Government Road Complaint Emails"
- Click "Run workflow" → "Run workflow"
- Check if emails are sent successfully

## 🎯 What Happens Next

✅ **Daily at 9:00 AM Pakistan Time**: System automatically sends emails
✅ **Email Rotation**: Uses your configured email service(s)
✅ **Template Rotation**: 3 different templates (English, Urdu, Legal)
✅ **Anti-Spam**: Random delays, professional formatting
✅ **Media Attachments**: Photos/videos attached to emails

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
- **Media Attachments**: Photos/videos as evidence

## 📊 Monitoring

- **GitHub Actions Logs**: Check daily execution status
- **Email Delivery**: Monitor success rates
- **Government Responses**: Track any acknowledgments
- **Media Coverage**: Document any press coverage

## 🔧 Troubleshooting

### Emails Not Sending?
1. Check GitHub Secrets are configured
2. Verify email password/app password
3. Check spam folders for test emails

### Workflow Not Running?
1. Check GitHub Actions are enabled
2. Verify cron schedule in workflow file
3. Test with manual workflow trigger

### Need to Update Recipients?
Edit `send_single_email.py` and update the `recipient_emails` list

## 📈 Success Metrics

**Short Term (1-3 months):**
- Daily email delivery success rate > 95%
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

## 🎉 You're Ready!

Your automated government accountability system is now active and will:
- Send daily emails to government officials
- Use your configured email service(s)
- Use 3 different templates
- Include media attachments
- Run automatically every day at 9:00 AM Pakistan time

**The system will start working immediately after you complete the setup steps above!**

---

📖 **For detailed instructions**: See `README.md`
🔐 **For secrets setup**: See `GITHUB_SECRETS_GUIDE.md`
📋 **For deployment checklist**: See `DEPLOYMENT_CHECKLIST.md`
