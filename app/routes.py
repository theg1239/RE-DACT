from flask import request, jsonify, render_template
from datetime import datetime
import logging
import colorama
from colorama import Fore, Style
from app import app  # Import the app object from the __init__.py file
from app.init_presidio import recognize_and_anonymize_entities  # Ensure this is imported

# Initialize colorama
colorama.init(autoreset=True)

# Configure logging
logging.basicConfig(filename='log.txt', level=logging.INFO)

def log_event(message, color):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    colored_message = f"{color}[{timestamp}] [<RE-DACT>] {message}{Style.RESET_ALL}"
    logging.info(colored_message)
    print(colored_message)

@app.route('/')
def index():
    log_event("Web interface accessed", Fore.CYAN)
    return render_template('index.html')

@app.route('/redact', methods=['POST'])
def redact_text_route():
    if request.method == 'POST':
        input_text = request.json.get('text', '')
        redaction_level = request.json.get('redaction_level', 100)  # Default to full redaction
        log_event("Text input received", Fore.YELLOW)
        start_time = datetime.now()
        try:
            redacted_output = recognize_and_anonymize_entities(input_text, redaction_level)  # Pass redaction level
            end_time = datetime.now()
            elapsed_time = (end_time - start_time).total_seconds()
            log_event(f"Redaction complete. ({elapsed_time:.2f}s)", Fore.GREEN)
            return jsonify({"redacted_text": redacted_output})
        except Exception as e:
            log_event(f"Redaction failed: {str(e)}", Fore.RED)
            return jsonify({"error": "Redaction failed"}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        log_event("File upload attempted without file", Fore.RED)
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        log_event("File upload attempted with no selected file", Fore.RED)
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.txt'):
        log_event(f"File '{file.filename}' uploaded", Fore.BLUE)
        content = file.read().decode('utf-8')
        original_text = content  # Store the original text
        redacted_output = recognize_and_anonymize_entities(content, redaction_level=100)  # Fully redacted by default
        return jsonify({"original_text": original_text, "redacted_text": redacted_output})

    log_event("Invalid file format attempted", Fore.RED)
    return jsonify({"error": "Invalid file format. Please upload a .txt file."}), 400
