#!/usr/bin/env python3
"""
Load environment variables from .env file and run the email system locally
"""

import os
import sys
from pathlib import Path

def load_env_file():
    """Load environment variables from .env file"""
    env_file = Path('../../.env')
    
    if not env_file.exists():
        print("❌ .env file not found!")
        print("💡 Run './setup_local_secrets.sh' to create it")
        return False
    
    print("📖 Loading environment variables from .env file...")
    
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value
                print(f"✅ Loaded: {key}")
    
    print("🎉 Environment variables loaded successfully!")
    return True

def main():
    """Main function to load env and run the system"""
    print("🔧 Setting up local environment...")
    
    # Load environment variables
    if not load_env_file():
        sys.exit(1)
    
    # Add src directory to Python path
    src_path = Path('src')
    if src_path.exists():
        sys.path.insert(0, str(src_path))
    
    # Import and run the test
    print("\n🧪 Running email system test...")
    try:
        import test_email
        test_email.main()
    except Exception as e:
        print(f"❌ Error running test: {e}")
        print(f"💡 Trying alternative approach...")
        
        # Try running the test script directly
        try:
            os.system(f"cd .. && python3 test_email.py")
        except Exception as e2:
            print(f"❌ Alternative approach also failed: {e2}")
            sys.exit(1)

if __name__ == "__main__":
    main()
