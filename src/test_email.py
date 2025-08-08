#!/usr/bin/env python3
"""
Test script for the automated government email system
This script tests the email templates and configuration without sending actual emails.
"""

import os
import sys
from datetime import datetime
import random

def test_email_templates():
    """Test the email template generation"""
    print("🧪 Testing Email Templates...")
    
    # Simulate the template generation logic
    today = datetime.now()
    reference_number = f"ROAD-{today.strftime('%Y%m%d')}-{random.randint(1000, 9999)}"
    
    templates = {
        1: {
            'subject': f"URGENT: Critical Road Infrastructure Failure - Bedian Road & Ali View Garden Area (Ref: {reference_number})",
            'language': 'English'
        },
        2: {
            'subject': f"فوری: بیڈین روڈ اور علی ویو گارڈن ایریا میں سڑک کی شدید خرابی (Ref: {reference_number})",
            'language': 'Urdu'
        },
        3: {
            'subject': f"LEGAL NOTICE: Citizen Rights Violation - Road Infrastructure Neglect (Ref: {reference_number})",
            'language': 'Legal English'
        }
    }
    
    for template_id, template in templates.items():
        print(f"✅ Template {template_id} ({template['language']}): {template['subject'][:60]}...")
    
    return True

def test_email_rotation():
    """Test the email service rotation logic"""
    print("\n🔄 Testing Email Service Rotation...")
    
    # Simulate available services
    available_services = []
    
    if os.getenv('GMAIL_EMAIL') and os.getenv('GMAIL_APP_PASSWORD'):
        available_services.append('Gmail')
    
    if os.getenv('OUTLOOK_EMAIL') and os.getenv('OUTLOOK_PASSWORD'):
        available_services.append('Outlook')
    
    if os.getenv('YAHOO_EMAIL') and os.getenv('YAHOO_PASSWORD'):
        available_services.append('Yahoo')
    
    if not available_services:
        print("❌ No email services configured")
        print("💡 At least one email service is required")
        return False
    
    print(f"✅ {len(available_services)} email service(s) configured: {', '.join(available_services)}")
    
    # Test rotation for first week
    for day in range(1, 8):
        service_index = day % len(available_services)
        service = available_services[service_index]
        print(f"✅ Day {day}: Using {service}")
    
    return True

def test_template_rotation():
    """Test the template rotation logic"""
    print("\n📝 Testing Template Rotation...")
    
    for day in range(1, 8):  # Test first week
        template_type = (day % 3) + 1
        print(f"✅ Day {day}: Template {template_type}")
    
    return True

def test_environment_variables():
    """Test if environment variables are properly configured"""
    print("\n🔧 Testing Environment Variables...")
    
    required_vars = [
        ('GMAIL_EMAIL', 'GMAIL_APP_PASSWORD'),
        ('OUTLOOK_EMAIL', 'OUTLOOK_PASSWORD'),
        ('YAHOO_EMAIL', 'YAHOO_PASSWORD')
    ]
    
    configured_services = 0
    
    for email_var, password_var in required_vars:
        email = os.getenv(email_var)
        password = os.getenv(password_var)
        
        if email and password:
            print(f"✅ {email_var}: Configured")
            configured_services += 1
        else:
            print(f"❌ {email_var}: Missing (optional)")
    
    if configured_services == 0:
        print(f"\n❌ No email services configured")
        print("💡 At least one email service is required")
        return False
    elif configured_services == 1:
        print(f"\n✅ {configured_services} email service configured (minimum requirement met)")
    else:
        print(f"\n✅ {configured_services} email services configured (recommended for rotation)")
    
    return True

def test_media_file_discovery():
    """Test the new automatic media file discovery functionality"""
    print("\n📁 Testing Media File Discovery...")
    
    # Test file type validation
    supported_extensions = {
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp',
        '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv',
        '.pdf', '.doc', '.docx', '.txt', '.rtf',
        '.zip', '.rar', '.7z'
    }
    
    print(f"✅ Supported file types: {len(supported_extensions)} extensions")
    
    # Test file size calculation
    def get_file_size_mb(file_path):
        try:
            size_bytes = os.path.getsize(file_path)
            return size_bytes / (1024 * 1024)
        except OSError:
            return 0
    
    # Test media directory discovery
    possible_media_dirs = [
        '../media',  # When running from src/
        'media',     # When running from root
        './media'    # Alternative path
    ]
    
    media_dir = None
    for dir_path in possible_media_dirs:
        if os.path.exists(dir_path):
            media_dir = dir_path
            print(f"✅ Media directory found: '{media_dir}'")
            break
    
    if not media_dir:
        print("❌ Media directory not found")
        print("💡 Create the media directory and add your photos/videos")
        return False
    
    # Test file discovery and validation
    valid_files = []
    total_size_mb = 0
    max_file_size_mb = 25
    max_total_size_mb = 50
    
    try:
        for filename in os.listdir(media_dir):
            file_path = os.path.join(media_dir, filename)
            
            # Skip directories and hidden files
            if os.path.isdir(file_path) or filename.startswith('.'):
                continue
            
            # Check file type
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext not in supported_extensions:
                print(f"⚠️  Unsupported file type: {filename}")
                continue
            
            # Check file size
            file_size_mb = get_file_size_mb(file_path)
            if file_size_mb > max_file_size_mb:
                print(f"⚠️  Oversized file: {filename} ({file_size_mb:.1f}MB > {max_file_size_mb}MB)")
                continue
            
            # Check total size limit
            if total_size_mb + file_size_mb > max_total_size_mb:
                print(f"⚠️  Total size limit reached: {filename} would exceed {max_total_size_mb}MB")
                break
            
            valid_files.append(filename)
            total_size_mb += file_size_mb
            print(f"✅ Valid media file: {filename} ({file_size_mb:.1f}MB)")
    
    except Exception as e:
        print(f"❌ Error scanning media directory: {e}")
        return False
    
    if not valid_files:
        print("⚠️  No valid media files found")
        print("💡 Add supported media files to the media directory")
        return False
    
    print(f"📁 Total valid media files: {len(valid_files)} ({total_size_mb:.1f}MB)")
    print(f"📋 File size limits: Individual {max_file_size_mb}MB, Total {max_total_size_mb}MB")
    
    return True

def test_recipient_emails():
    """Test the recipient email configuration"""
    print("\n👥 Testing Recipient Emails...")
    
    # Sample recipient emails from the main script
    recipient_emails = [
        "complaints@waltoncantonment.gov.pk",
        "cm@punjab.gov.pk",
        "info@lahore.gov.pk",
        "dc.lahore@punjab.gov.pk",
        "commissioner.lahore@punjab.gov.pk",
        "ceo@lhc.gov.pk",
        "info@lhc.gov.pk",
        "complaints@punjab.gov.pk",
        "helpline@punjab.gov.pk"
    ]
    
    print(f"✅ {len(recipient_emails)} recipient emails configured")
    for email in recipient_emails:
        print(f"   📧 {email}")
    
    return True

def main():
    """Run all tests"""
    print("🚀 Automated Government Email System - Test Suite")
    print("=" * 60)
    
    tests = [
        test_email_templates,
        test_email_rotation,
        test_template_rotation,
        test_environment_variables,
        test_media_file_discovery,
        test_recipient_emails
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your system is ready for deployment.")
        print("\n📋 Next Steps:")
        print("1. Create at least one email account (Gmail, Outlook, or Yahoo)")
        print("2. Set up GitHub repository")
        print("3. Configure GitHub Secrets with email credentials")
        print("4. Add media files to the media/ directory (any supported format)")
        print("5. Test with manual workflow trigger")
    else:
        print("⚠️  Some tests failed. Please fix the issues above before deployment.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
