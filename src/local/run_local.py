#!/usr/bin/env python3
"""
Load environment variables from .env file and run the email system locally
"""

import os
import sys
from pathlib import Path

def load_env_file():
    """Load environment variables from .env file"""
    # Try multiple possible locations for .env file
    possible_paths = [
        Path('../../.env'),  # From src/local/ directory
        Path('../.env'),     # From src/ directory  
        Path('.env'),        # From root directory
    ]
    
    env_file = None
    for path in possible_paths:
        if path.exists():
            env_file = path
            break
    
    if not env_file:
        print("❌ .env file not found!")
        print("💡 Run './setup_local_secrets.sh' to create it")
        print(f"💡 Searched in: {[str(p) for p in possible_paths]}")
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
    
    # Add src directory to Python path (relative to current script location)
    current_dir = Path(__file__).parent
    src_path = current_dir.parent  # This goes from src/local to src
    if src_path.exists():
        sys.path.insert(0, str(src_path))
        print(f"✅ Added to Python path: {src_path}")
    else:
        print(f"❌ Could not find src directory at: {src_path}")
        sys.exit(1)
    
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
            test_script = current_dir.parent / "test_email.py"
            if test_script.exists():
                print(f"🔄 Running test script directly: {test_script}")
                os.system(f"cd {current_dir.parent} && python3 test_email.py")
            else:
                print(f"❌ Test script not found at: {test_script}")
                sys.exit(1)
        except Exception as e2:
            print(f"❌ Alternative approach also failed: {e2}")
            sys.exit(1)

if __name__ == "__main__":
    main()
