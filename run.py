import os
import sys
import subprocess

def install_requirements():
    """Install the required packages."""
    try:
        # Install the packages from requirements.txt
        print("Installing required packages from requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", "--force-reinstall", "-r", "requirements.txt"])
        
        # Install the spaCy model
        print("Downloading spaCy model...")
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])

    except subprocess.CalledProcessError as e:
        print(f"Error occurred during installation: {e}")
        sys.exit(1)

def main():
    # Check if virtual environment is active
    if not hasattr(sys, 'real_prefix') and sys.base_prefix == sys.prefix:
        print("It seems like the virtual environment is not activated.")
        print("Please activate your virtual environment and run this script again.")
        sys.exit(1)
    
    # Install requirements
    install_requirements()
    
    # Start the Flask app
    try:
        print("Starting Flask app...")
        from app import app
        app.run(debug=True)
    except ImportError as e:
        print(f"Failed to import Flask app. Make sure the app is correctly set up: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
