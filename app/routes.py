# app/routes.py

from flask import current_app as app
from flask import render_template, request, jsonify
from .redaction_model import advanced_redact_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redact', methods=['POST'])
def redact():
    data = request.get_json()
    original_text = data.get('text', '')
    redacted_text = advanced_redact_text(original_text)
    return jsonify({'redacted_text': redacted_text})
