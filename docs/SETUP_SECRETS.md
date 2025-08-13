# 🔐 Complete GitHub Secrets Setup Guide

This guide will walk you through setting up GitHub Secrets step by step.

## 📋 Prerequisites

Before setting up secrets, you need:

1. A GitHub repository with the email system code
2. At least one email account (Gmail, Outlook, or Yahoo)
3. App passwords for Gmail/Yahoo (if using 2FA)

## 🚀 Step-by-Step Setup

### Step 1: Access Your Repository Settings

1. Go to your GitHub repository
2. Click on the **"Settings"** tab at the top
3. In the left sidebar, click **"Secrets and variables"**
4. Click **"Actions"**

![GitHub Settings Navigation](https://docs.github.com/assets/cb-11427/images/help/actions/actions-secrets.png)

### Step 2: Add Your First Email Service

Click the **"New repository secret"** button to add your first email service.

#### Option A: Gmail Setup (Recommended)

**Secret 1:**

- **Name:** `GMAIL_EMAIL`
- **Value:** `your_gmail@gmail.com`

**Secret 2:**

- **Name:** `GMAIL_APP_PASSWORD`
- **Value:** `your_gmail_app_password`

#### Option B: Outlook Setup

**Secret 1:**

- **Name:** `OUTLOOK_EMAIL`
- **Value:** `your_outlook@outlook.com`

**Secret 2:**

- **Name:** `OUTLOOK_PASSWORD`
- **Value:** `your_outlook_password`

#### Option C: Yahoo Setup

**Secret 1:**

- **Name:** `YAHOO_EMAIL`
- **Value:** `your_yahoo@yahoo.com`

**Secret 2:**

- **Name:** `YAHOO_PASSWORD`
- **Value:** `your_yahoo_password`

### Step 3: How to Get App Passwords

#### Gmail App Password:

1. Go to [Gmail](https://gmail.com)
2. Click your profile picture → **"Manage your Google Account"**
3. Click **"Security"** in the left sidebar
4. Under "Signing in to Google," click **"2-Step Verification"**
5. Scroll down and click **"App passwords"**
6. Select **"Mail"** and **"Other (Custom name)"**
7. Enter a name like "Government Email System"
8. Click **"Generate"**
9. Copy the 16-character password (no spaces)

#### Yahoo App Password:

1. Go to [Yahoo Account Security](https://login.yahoo.com/account/security)
2. Click **"2-step verification"**
3. Click **"Manage app passwords"**
4. Click **"Generate app password"**
5. Select **"Mail"** and enter a name
6. Click **"Generate password"**
7. Copy the generated password

#### Outlook Password:

- Use your regular Outlook password
- If you have 2FA enabled, you may need to generate an app password

### Step 4: Add Additional Email Services (Optional)

For better rotation and anti-blocking, add more email services:

#### Add Second Email Service:

Repeat Step 2 with a different email provider.

#### Add Third Email Service:

Repeat Step 2 with the remaining email provider.

### Step 5: Verify Your Secrets

After adding all secrets, you should see them listed like this:

```
GMAIL_EMAIL                    ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
GMAIL_APP_PASSWORD             ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
OUTLOOK_EMAIL                  ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
OUTLOOK_PASSWORD               ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
YAHOO_EMAIL                    ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
YAHOO_PASSWORD                 ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
```

## 🧪 Test Your Setup

### Step 1: Run Manual Test

1. Go to your repository's **"Actions"** tab
2. Click **"Daily Government Road Complaint Emails"**
3. Click **"Run workflow"** button
4. Click **"Run workflow"** again to confirm

### Step 2: Check Results

1. Click on the running workflow
2. Click on the **"send-emails"** job
3. Monitor the logs for success/failure messages

### Expected Success Message:

```
✅ Email sent successfully using Gmail
📧 Template: URGENT: Critical Road Infrastructure Failure...
👥 Recipients: 9
✅ Daily email campaign completed successfully
```

### Common Error Messages:

- `❌ Failed to send email using Gmail: Authentication failed`
  - **Solution:** Check your app password is correct
- `❌ No email services configured`
  - **Solution:** Add at least one email service secret
- `❌ Failed to send email using Gmail: SMTPAuthenticationError`
  - **Solution:** Enable 2FA and use app password

## 🔧 Troubleshooting

### Authentication Errors

**Problem:** `SMTPAuthenticationError` or `Authentication failed`
**Solutions:**

1. For Gmail: Use app password, not regular password
2. For Yahoo: Use app password, not regular password
3. For Outlook: Try regular password first, then app password if needed
4. Check that 2FA is enabled for Gmail/Yahoo

### No Email Services Error

**Problem:** `No email services configured`
**Solutions:**

1. Add at least one email service secret
2. Check secret names are exactly correct (case-sensitive)
3. Ensure both email and password secrets are added

### Workflow Not Running

**Problem:** Workflow doesn't execute
**Solutions:**

1. Check GitHub Actions are enabled in repository settings
2. Verify the workflow file exists in `.github/workflows/`
3. Check the cron schedule in the workflow file

### Emails Not Delivered

**Problem:** Workflow runs but emails not received
**Solutions:**

1. Check spam/junk folders
2. Verify recipient email addresses are correct
3. Check if email service has sending limits
4. Monitor GitHub Actions logs for specific errors

## 📊 Monitoring Your Secrets

### Check Secret Status:

1. Go to Settings → Secrets and variables → Actions
2. Verify all secrets show ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
3. Check that secret names match exactly

### Update Secrets:

1. Click on the secret name
2. Click **"Update"**
3. Enter new value
4. Click **"Update secret"**

### Delete Secrets:

1. Click on the secret name
2. Click **"Delete"**
3. Type the secret name to confirm
4. Click **"Delete secret"**

## 🔒 Security Best Practices

1. **Never commit secrets to your repository**
2. **Use different email accounts for rotation**
3. **Regularly rotate app passwords**
4. **Keep app passwords secure**
5. **Use strong, unique passwords**
6. **Enable 2FA on all email accounts**
7. **Monitor for suspicious activity**

## 📞 Getting Help

If you encounter issues:

1. **Check the logs** in GitHub Actions first
2. **Verify secret names** are exactly correct
3. **Test email credentials** manually
4. **Check this troubleshooting guide**
5. **Create a GitHub issue** in your repository

## ✅ Success Checklist

- [ ] At least one email service configured
- [ ] App passwords generated (for Gmail/Yahoo)
- [ ] Secrets added to GitHub repository
- [ ] Manual workflow test successful
- [ ] Emails received in test
- [ ] Daily automation working
- [ ] Monitoring logs regularly

**Your GitHub Secrets are now configured and ready! 🎉**
