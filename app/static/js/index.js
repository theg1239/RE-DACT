document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menuToggle');
    const showRedacted = document.getElementById('showRedacted');
    const redactButton = document.getElementById('redactButton');
    const menu = document.getElementById('menu');
    const redactedTextContainer = document.getElementById('redactedTextContainer');
    const redactedText = document.getElementById('redactedText');
    const inputText = document.getElementById('inputText');
    const uploadTrigger = document.getElementById('uploadTrigger');
    const fileInput = document.getElementById('fileInput');
    const redactionSlider = document.getElementById('redactionSlider');
    const downloadButton = document.getElementById('downloadButton');

    let lastRedactedText = "";

    // Initially disable the "Show Redacted" button
    showRedacted.disabled = true;
    showRedacted.style.opacity = "0.5"; // Make it look disabled

    menuToggle.addEventListener('click', () => {
        redactedTextContainer.classList.remove('active');
        menu.classList.add('active');
    });

    showRedacted.addEventListener('click', () => {
        if (!showRedacted.disabled) {  // Only allow click if not disabled
            menu.classList.remove('active');
            redactedTextContainer.classList.add('active');
        }
    });

    uploadTrigger.addEventListener('click', () => {
        fileInput.click();
    });

    redactButton.addEventListener('click', () => {
        const text = inputText.value;
        if (!text.trim()) return;

        fetch('/redact', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text, redaction_level: redactionSlider.value })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            lastRedactedText = data.redacted_text;
            redactedText.value = lastRedactedText;
            menu.classList.remove('active');
            redactedTextContainer.classList.add('active');

            // Enable the "Show Redacted" button once redaction is done
            showRedacted.disabled = false;
            showRedacted.style.opacity = "1"; // Make it look enabled
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred during redaction. Please try again.');
        });
    });

    redactionSlider.addEventListener('input', () => {
        if (lastRedactedText) {
            fetch('/redact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: inputText.value, redaction_level: redactionSlider.value })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Server error: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                redactedText.value = data.redacted_text;
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred during redaction. Please try again.');
            });
        }
    });

    downloadButton.addEventListener('click', () => {
        const blob = new Blob([redactedText.value], { type: 'text/plain' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'redacted_text.txt';
        link.click();
    });
});
