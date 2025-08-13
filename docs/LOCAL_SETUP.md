# Local Setup Guide

This guide helps you set up the email system to run locally on your machine.

## Quick Setup

### Option 1: Interactive Setup (Recommended)
```bash
# Run the interactive setup script
./setup_local_secrets.sh
```

### Option 2: Manual Setup
Create a `.env` file in the project root with your email credentials:

```bash
# Create .env file
touch .env
```

Add your email credentials to the `.env` file:
```bash
# Gmail (Recommended)
GMAIL_EMAIL=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password

# Outlook (Optional)
OUTLOOK_EMAIL=your_email@outlook.com
OUTLOOK_PASSWORD=your_password

# Yahoo (Optional)
YAHOO_EMAIL=your_email@yahoo.com
YAHOO_PASSWORD=your_app_password

# System Configuration
GITHUB_ACTIONS=false
TEST_MODE=true
VERBOSE_LOGGING=true
```

## Email Service Setup

### Gmail Setup (Recommended)
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings: https://myaccount.google.com/
   - Security → 2-Step Verification → App passwords
   - Generate a new app password for "Mail"
3. Use this app password (not your regular Gmail password)

### Outlook Setup
1. Use your regular Outlook password
2. If you have 2FA enabled, you may need to generate an app password

### Yahoo Setup
1. Enable 2-Factor Authentication on your Yahoo account
2. Generate an App Password:
   - Account Security → Generate app password
3. Use this app password (not your regular Yahoo password)

## Running the System

### Quick Start Scripts

**Test the System:**
```bash
# Test email configuration and templates
python3 run_local.py
```

**Send Actual Emails:**
```bash
# Send government complaint emails
python3 run_email_system.py
```

### Manual Environment Loading
```bash
# Source the .env file directly
source .env
```

### Manual Testing
```bash
# Test email configuration
python3 src/test_email.py

# Send emails manually
python3 src/send_single_email.py
```

## Troubleshooting

### Common Issues

1. **"No email services configured"**
   - Make sure you've added at least one email service to `.env`
   - Check that the credentials are correct
   - Use the provided scripts: `python3 run_local.py`

2. **"Authentication failed for Gmail"**
   - You need to use an **App Password**, not your regular Gmail password
   - Run: `./update_gmail_password.sh` to update it
   - Or manually generate an app password from Google Account settings

3. **"Permission denied"**
   - Make sure the setup script is executable: `chmod +x setup_local_secrets.sh`

4. **"Module not found"**
   - Use the provided scripts: `python3 run_local.py` or `python3 run_email_system.py`
   - These scripts handle the Python path automatically

### Gmail App Password Issues

If you get this error:
```
❌ Authentication failed for Gmail: (534, b'5.7.9 Application-specific password required...')
```

**Solution:**
1. Go to: https://myaccount.google.com/
2. Security → 2-Step Verification → App passwords
3. Generate new app password for "Mail"
4. Run: `./update_gmail_password.sh`
5. Enter the new 16-character app password

### Getting Help

- Check the logs in the scripts for detailed error messages
- Ensure all required Python packages are installed: `pip install -r requirements.txt`
- Verify your email service settings and app passwords
- Use the provided scripts which handle environment loading automatically

## File Structure

### Scripts Created for Local Development:
- `run_local.py` - Test the email system locally (loads .env automatically)
- `run_email_system.py` - Send actual emails locally (loads .env automatically)
- `update_gmail_password.sh` - Update Gmail app password
- `setup_local_secrets.sh` - Initial interactive setup

### Configuration Files:
- `.env` - Your email credentials (never commit this file)
- `.env.backup*` - Automatic backups of your configuration

## Security Notes

- ✅ The `.env` file is already in `.gitignore`
- ✅ Never commit your `.env` file to version control
- ✅ Use different email accounts for better rotation
- ✅ Keep your app passwords secure
- ✅ Regularly rotate your passwords
- ✅ Automatic backups are created when updating passwords

## Next Steps

After successful setup:
1. Test with: `python3 run_local.py`
2. Send emails with: `python3 run_email_system.py`
3. Check your email to verify delivery
4. Monitor the system for any issues

## Success Indicators

- ✅ All tests pass in `run_local.py`
- ✅ Emails are sent successfully in `run_email_system.py`
- ✅ No authentication errors
- ✅ Media files are attached correctly
- ✅ HTML templates are generated properly
