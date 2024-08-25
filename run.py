import os
import sys
import subprocess
import webbrowser
from threading import Timer

def install_spacy_model():
    """Install the spaCy model if it's not already installed."""
    try:
        import spacy
        # Check if the model is already installed
        spacy.load("en_core_web_sm")
        print("SpaCy model 'en_core_web_sm' is already installed.")
    except (ImportError, OSError):
        print("Downloading spaCy model 'en_core_web_sm'...")
        try:
            subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        except subprocess.CalledProcessError as e:
            print(f"Error occurred during spaCy model installation: {e}")
            sys.exit(1)

def open_browser():
    """Open the web browser after starting the server."""
    webbrowser.open_new("http://127.0.0.1:5000/")

def main():
    # Check if virtual environment is active
    if not hasattr(sys, 'real_prefix') and sys.base_prefix == sys.prefix:
        print("It seems like the virtual environment is not activated.")
        print("Please activate your virtual environment and run this script again.")
        sys.exit(1)
    
    # Install the spaCy model only if it's not already installed
    install_spacy_model()

    # Start the Flask app and open the browser only on the first run
    try:
        print("Starting Flask app...")
        from app import app
        if 'WERKZEUG_RUN_MAIN' not in os.environ:  # Check if this is the initial run
            Timer(1, open_browser).start()  # Open the browser after 1 second delay
        app.run(debug=True)
    except ImportError as e:
        print(f"Failed to import Flask app. Make sure the app is correctly set up: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
