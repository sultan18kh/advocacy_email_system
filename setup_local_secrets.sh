# Setup Local GitHub Secrets for Email System
# This script helps you set environment variables to run the email system locally

echo "🔧 Setting up local environment variables for email system..."
echo ""

# Check if .env file exists, if not create it
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    touch .env
fi

echo "📧 Please provide your email service credentials:"
echo ""

# Gmail Setup
echo "🔵 Gmail Setup (Recommended):"
read -p "Enter your Gmail address (or press Enter to skip): " GMAIL_EMAIL
if [ ! -z "$GMAIL_EMAIL" ]; then
    read -s -p "Enter your Gmail App Password: " GMAIL_APP_PASSWORD
    echo ""
    echo "GMAIL_EMAIL=$GMAIL_EMAIL" >> .env
    echo "GMAIL_APP_PASSWORD=$GMAIL_APP_PASSWORD" >> .env
    echo "✅ Gmail credentials added"
else
    echo "⏭️  Skipping Gmail setup"
fi

echo ""

# Outlook Setup
echo "🟣 Outlook Setup:"
read -p "Enter your Outlook address (or press Enter to skip): " OUTLOOK_EMAIL
if [ ! -z "$OUTLOOK_EMAIL" ]; then
    read -s -p "Enter your Outlook password: " OUTLOOK_PASSWORD
    echo ""
    echo "OUTLOOK_EMAIL=$OUTLOOK_EMAIL" >> .env
    echo "OUTLOOK_PASSWORD=$OUTLOOK_PASSWORD" >> .env
    echo "✅ Outlook credentials added"
else
    echo "⏭️  Skipping Outlook setup"
fi

echo ""

# Yahoo Setup
echo "🟡 Yahoo Setup:"
read -p "Enter your Yahoo address (or press Enter to skip): " YAHOO_EMAIL
if [ ! -z "$YAHOO_EMAIL" ]; then
    read -s -p "Enter your Yahoo App Password: " YAHOO_PASSWORD
    echo ""
    echo "YAHOO_EMAIL=$YAHOO_EMAIL" >> .env
    echo "YAHOO_PASSWORD=$YAHOO_PASSWORD" >> .env
    echo "✅ Yahoo credentials added"
else
    echo "⏭️  Skipping Yahoo setup"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Source the .env file: source .env"
echo "2. Test the setup: python3 src/test_email.py"
echo "3. Run the email system: python3 src/send_single_email.py"
echo ""
echo "🔒 Security note: The .env file contains sensitive information."
echo "   Make sure it's in your .gitignore file and never commit it to version control."
echo ""
echo "📖 For more information, see docs/SETUP_SECRETS.md"
