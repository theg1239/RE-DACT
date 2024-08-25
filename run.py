import os
import subprocess
import sys

def create_virtual_environment():
    # Check if the virtual environment already exists
    if not os.path.exists("venv"):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
    else:
        print("Virtual environment already exists.")

def install_requirements():
    print("Installing required packages...")
    subprocess.check_call([os.path.join("venv", "Scripts", "pip"), "install", "-r", "requirements.txt"])

def run_server():
    print("Starting the server...")
    subprocess.call(["cmd.exe", "/c", "start_webui.bat"])

if __name__ == "__main__":
    create_virtual_environment()
    install_requirements()
    run_server()
