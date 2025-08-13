# 📋 Deployment Checklist

## Pre-Deployment Tasks:

- [ ] **Install Dependencies**: `pip install -r requirements.txt`
- [ ] **Verify Dependencies**: `schedule` and `pytz` are installed
- [ ] Create at least one email account (Gmail, Outlook, or Yahoo)
- [ ] Enable 2-Factor Authentication on all accounts
- [ ] Generate app passwords for Gmail and Yahoo
- [ ] Test email accounts manually

## GitHub Setup:

- [ ] Push code to GitHub repository
- [ ] Configure GitHub Secrets (see `SETUP_SECRETS.md`)
- [ ] Enable GitHub Actions in repository settings
- [ ] **Verify workflow name**: "Government Road Complaint Emails (Mon/Wed/Fri)"
- [ ] Test manual workflow execution

## Media Files:

- [ ] Take photos of road conditions
- [ ] Take videos of potholes and flooding
- [ ] Upload files to `media/` directory with ANY descriptive filenames
- [ ] Ensure files are under 25MB each
- [ ] **NEW**: System automatically discovers all valid files

## Testing:

- [ ] **Run local tests**: `python src/test_email.py` (correct path)
- [ ] **Verify dependencies**: Check that `pytz` and `schedule` are installed
- [ ] Test manual workflow trigger in GitHub Actions
- [ ] Verify emails are sent successfully
- [ ] Check spam folders for test emails
- [ ] **Verify file discovery**: Check test output shows media files found

## Configuration Validation:

- [ ] **Email format validation**: All recipient emails are valid
- [ ] **File type validation**: Media files are supported types
- [ ] **Size validation**: Individual files under 25MB, total under 50MB
- [ ] **Path validation**: Media directory is found correctly

## GitHub Actions Verification:

- [ ] **Workflow name**: "Government Road Complaint Emails (Mon/Wed/Fri)" (exact match)
- [ ] **Schedule**: Mon/Wed/Fri at 4:00 AM UTC (9:00 AM PKT)
- [ ] **Dependencies**: requirements.txt includes `schedule` and `pytz`
- [ ] **Secrets configured**: At least one email service
- [ ] **Validation step**: Test runs before email sending

## Monitoring:

- [ ] Check GitHub Actions logs on Mon/Wed/Fri
- [ ] Monitor email delivery success rate
- [ ] Track government responses
- [ ] Document any progress
- [ ] **Timezone verification**: Timestamps show PKT correctly

## Maintenance:

- [ ] Update media files regularly with descriptive names
- [ ] Rotate email accounts if needed
- [ ] Update recipient list as needed
- [ ] Monitor for any blocking issues
- [ ] **Dependency updates**: Keep `pytz` and `schedule` current

## Success Indicators:

- [ ] **Mon/Wed/Fri delivery rate** > 95% (not daily)
- [ ] No email account blocks
- [ ] Government acknowledgment received
- [ ] Media coverage of issue
- [ ] Government action taken
- [ ] **Automatic file discovery** working correctly

## Troubleshooting Checklist:

- [ ] **Dependencies**: `pip list | grep -E "(schedule|pytz)"` shows both installed
- [ ] **Test command**: `python src/test_email.py` runs without errors
- [ ] **GitHub Actions logs**: Check for specific error messages
- [ ] **Workflow name**: Exact match "Government Road Complaint Emails (Mon/Wed/Fri)"
- [ ] **Secrets validation**: All required email secrets configured
- [ ] **Media files**: Check file discovery in test output
- [ ] **Timezone**: PKT timestamps in email content

## Common Issues & Solutions:

### ❌ "No module named 'pytz'"

**Solution**:

```bash
pip install pytz
# or
pip install -r requirements.txt
```

### ❌ Test file not found

**Solution**:

```bash
# Run from project root
python src/test_email.py
# NOT: python test_email.py
```

### ❌ Workflow not found

**Solution**:

- Look for exact name: "Government Road Complaint Emails (Mon/Wed/Fri)"
- Check `.github/workflows/send-daily-emails.yml` exists

### ❌ Media files not discovered

**Solution**:

- Ensure files are in `media/` directory
- Check supported file types (JPG, PNG, MP4, PDF, etc.)
- Run test to see file discovery output

### ❌ Wrong schedule

**Solution**:

- System runs Mon/Wed/Fri only (not daily)
- Time: 9:00 AM Pakistan Time / 4:00 AM UTC
- Cron: `0 4 * * 1,3,5`

## Final Validation:

### ✅ Before Going Live:

1. **Dependencies installed**: `pip install -r requirements.txt`
2. **Tests pass**: `python src/test_email.py` shows all green checkmarks
3. **Manual workflow test**: Successfully sends test email
4. **File discovery working**: Test shows media files found
5. **Correct schedule**: Mon/Wed/Fri at 9:00 AM PKT
6. **Professional content**: Templates are respectful and factual

### ✅ Post-Deployment:

1. **Monitor first week**: Check 3 scheduled sends (Mon/Wed/Fri)
2. **Verify delivery**: Check GitHub Actions logs
3. **Track responses**: Monitor for government acknowledgments
4. **Document results**: Keep records of any progress

---

**Remember**: This system runs Monday, Wednesday, and Friday only for sustainable, professional civic engagement.
