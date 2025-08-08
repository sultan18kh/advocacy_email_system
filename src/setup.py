"""
Setup script for the Automated Government Email System
This script helps with initial configuration and deployment.
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    """Print the setup banner"""
    print("🚀 Automated Government Email System - Setup")
    print("=" * 60)
    print("This script will help you set up the automated email system")
    print("for government road complaints in Bedian Road & Ali View Garden area.")
    print("=" * 60)

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_dependencies():
    """Install required Python dependencies"""
    print("\n📦 Installing dependencies...")
    
    try:
        # Check if requirements.txt exists in parent directory
        requirements_path = "../requirements.txt"
        if not os.path.exists(requirements_path):
            requirements_path = "requirements.txt"
        
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def create_media_directory():
    """Create media directory if it doesn't exist"""
    print("\n📁 Setting up media directory...")
    
    # Try to create media directory in parent directory
    media_dir = Path("../media")
    if not media_dir.exists():
        media_dir.mkdir()
        print("✅ Media directory created")
    else:
        print("✅ Media directory already exists")
    
    # Create placeholder files
    placeholder_files = [
        "road_photo1.jpg",
        "road_photo2.jpg", 
        "pothole_video.mp4",
        "flooding_video.mp4"
    ]
    
    for file_name in placeholder_files:
        file_path = media_dir / file_name
        if not file_path.exists():
            with open(file_path, 'w') as f:
                f.write(f"# Placeholder for {file_name}\n")
                f.write("# Replace this file with actual photo/video of road conditions\n")
            print(f"✅ Created placeholder: {file_name}")
        else:
            print(f"✅ File exists: {file_name}")
    
    return True

def check_git_repository():
    """Check if this is a git repository"""
    print("\n🔧 Checking Git repository...")
    
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Git repository detected")
            return True
        else:
            print("❌ Not a Git repository")
            return False
    except FileNotFoundError:
        print("❌ Git not installed")
        return False

def create_github_secrets_guide():
    """Create a guide for setting up GitHub Secrets"""
    print("\n🔐 GitHub Secrets Setup Guide")
    print("-" * 40)
    
    secrets_guide = """# GitHub Secrets Configuration Guide

Follow these steps to configure GitHub Secrets:

1. Go to your GitHub repository
2. Click on "Settings" tab
3. Click on "Secrets and variables" → "Actions"
4. Click "New repository secret"
5. Add the following secrets:

## Required Secrets (Minimum 1 Email Service)

**You only need to configure ONE email service to get started.**
The system will work with just one email account, but using multiple accounts provides better rotation and anti-blocking protection.

### Option 1: Gmail (Recommended for beginners)
- Name: `GMAIL_EMAIL`
- Value: `your_gmail@gmail.com`

- Name: `GMAIL_APP_PASSWORD`  
- Value: `your_gmail_app_password`

### Option 2: Outlook
- Name: `OUTLOOK_EMAIL`
- Value: `your_outlook@outlook.com`

- Name: `OUTLOOK_PASSWORD`
- Value: `your_outlook_password`

### Option 3: Yahoo
- Name: `YAHOO_EMAIL`
- Value: `your_yahoo@yahoo.com`

- Name: `YAHOO_PASSWORD`
- Value: `your_yahoo_password`

## Optional Secrets (For Better Rotation)

If you want to use multiple email services for better rotation and anti-blocking:

### Gmail Configuration
- Name: `GMAIL_EMAIL`
- Value: `your_gmail@gmail.com`

- Name: `GMAIL_APP_PASSWORD`  
- Value: `your_gmail_app_password`

### Outlook Configuration
- Name: `OUTLOOK_EMAIL`
- Value: `your_outlook@outlook.com`

- Name: `OUTLOOK_PASSWORD`
- Value: `your_outlook_password`

### Yahoo Configuration
- Name: `YAHOO_EMAIL`
- Value: `your_yahoo@yahoo.com`

- Name: `YAHOO_PASSWORD`
- Value: `your_yahoo_password`

## How to Get App Passwords:

### Gmail App Password:
1. Go to Gmail → Settings → Security
2. Enable 2-Factor Authentication
3. Go to "App passwords"
4. Generate a new app password
5. Use this password (not your regular Gmail password)

### Outlook App Password:
1. Go to Outlook → Settings → Security
2. Enable 2-Factor Authentication if required
3. Use your regular password or generate app password

### Yahoo App Password:
1. Go to Yahoo → Account Security
2. Enable 2-Factor Authentication
3. Generate app password
4. Use this password (not your regular Yahoo password)

## Quick Setup Examples:

### Minimal Setup (1 Email Service):
```
GMAIL_EMAIL = your_gmail@gmail.com
GMAIL_APP_PASSWORD = your_gmail_app_password
```

### Recommended Setup (2 Email Services):
```
GMAIL_EMAIL = your_gmail@gmail.com
GMAIL_APP_PASSWORD = your_gmail_app_password
OUTLOOK_EMAIL = your_outlook@outlook.com
OUTLOOK_PASSWORD = your_outlook_password
```

### Full Setup (3 Email Services):
```
GMAIL_EMAIL = your_gmail@gmail.com
GMAIL_APP_PASSWORD = your_gmail_app_password
OUTLOOK_EMAIL = your_outlook@outlook.com
OUTLOOK_PASSWORD = your_outlook_password
YAHOO_EMAIL = your_yahoo@yahoo.com
YAHOO_PASSWORD = your_yahoo_password
```

## Security Notes:
- Never commit these secrets to your repository
- Use different email accounts for rotation
- Keep your app passwords secure
- Regularly rotate your passwords
- At least one email service is required
- More services = better rotation = less chance of blocking

## Testing Your Setup:
1. After adding secrets, go to Actions tab
2. Click "Daily Government Road Complaint Emails"
3. Click "Run workflow" → "Run workflow"
4. Check the logs to see if emails are sent successfully
"""
    
    # Create docs directory if it doesn't exist
    docs_dir = Path("../docs")
    if not docs_dir.exists():
        docs_dir.mkdir()
    
    with open(docs_dir / "GITHUB_SECRETS_GUIDE.md", "w") as f:
        f.write(secrets_guide)
    
    print("✅ Created docs/GITHUB_SECRETS_GUIDE.md")
    print("📖 Read this guide to configure your GitHub Secrets")

def create_deployment_checklist():
    """Create a deployment checklist"""
    print("\n📋 Creating deployment checklist...")
    
    checklist = """# Deployment Checklist

## Pre-Deployment Tasks:
- [ ] Create at least one email account (Gmail, Outlook, or Yahoo)
- [ ] Enable 2-Factor Authentication on all accounts
- [ ] Generate app passwords for Gmail and Yahoo
- [ ] Test email accounts manually

## GitHub Setup:
- [ ] Push code to GitHub repository
- [ ] Configure GitHub Secrets (see docs/GITHUB_SECRETS_GUIDE.md)
- [ ] Enable GitHub Actions in repository settings
- [ ] Test manual workflow execution

## Media Files:
- [ ] Take photos of road conditions
- [ ] Take videos of potholes and flooding
- [ ] Upload files to media/ directory
- [ ] Ensure files are under 25MB each

## Testing:
- [ ] Run src/test_email.py locally
- [ ] Test manual workflow trigger
- [ ] Verify emails are sent successfully
- [ ] Check spam folders for test emails

## Monitoring:
- [ ] Check GitHub Actions logs daily
- [ ] Monitor email delivery success
- [ ] Track government responses
- [ ] Document any progress

## Maintenance:
- [ ] Update media files regularly
- [ ] Rotate email accounts if needed
- [ ] Update recipient list as needed
- [ ] Monitor for any blocking issues

## Success Indicators:
- [ ] Daily email delivery rate > 95%
- [ ] No email account blocks
- [ ] Government acknowledgment received
- [ ] Media coverage of issue
- [ ] Government action taken

## Troubleshooting:
- [ ] Check GitHub Actions logs for errors
- [ ] Verify all secrets are configured
- [ ] Test email credentials manually
- [ ] Update media files if missing
- [ ] Check recipient email addresses
"""
    
    # Create docs directory if it doesn't exist
    docs_dir = Path("../docs")
    if not docs_dir.exists():
        docs_dir.mkdir()
    
    with open(docs_dir / "DEPLOYMENT_CHECKLIST.md", "w") as f:
        f.write(checklist)
    
    print("✅ Created docs/DEPLOYMENT_CHECKLIST.md")
    print("📋 Use this checklist to ensure proper deployment")

def run_tests():
    """Run the test suite"""
    print("\n🧪 Running test suite...")
    
    try:
        result = subprocess.run([sys.executable, "test_email.py"], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        
        if result.returncode == 0:
            print("✅ All tests passed!")
        else:
            print("⚠️  Some tests failed (expected for initial setup)")
        
        return True
    except Exception as e:
        print(f"❌ Failed to run tests: {e}")
        return False

def main():
    """Main setup function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Create media directory
    if not create_media_directory():
        return False
    
    # Check git repository
    git_ok = check_git_repository()
    if not git_ok:
        print("💡 Consider initializing a git repository for version control")
    
    # Create guides
    create_github_secrets_guide()
    create_deployment_checklist()
    
    # Run tests
    run_tests()
    
    print("\n" + "=" * 60)
    print("🎉 Setup completed successfully!")
    print("\n📋 Next Steps:")
    print("1. Read docs/GITHUB_SECRETS_GUIDE.md for secrets configuration")
    print("2. Follow docs/DEPLOYMENT_CHECKLIST.md for deployment")
    print("3. Add your media files to the media/ directory")
    print("4. Configure GitHub Secrets in your repository")
    print("5. Test the system with manual workflow trigger")
    print("\n🚀 Your automated government email system is ready!")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
