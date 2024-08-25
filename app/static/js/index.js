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
    let currentFileType = "text"; // Default to text

    showRedacted.disabled = true;
    showRedacted.style.opacity = "0.5"; 

    menuToggle.addEventListener('click', () => {
        redactedTextContainer.classList.remove('active');
        menu.classList.add('active');
    });

    showRedacted.addEventListener('click', () => {
        if (!showRedacted.disabled) {  
            menu.classList.remove('active');
            redactedTextContainer.classList.add('active');
        }
    });

    uploadTrigger.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', () => {
        const file = fileInput.files[0];
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                lastRedactedText = data.original_text;
                redactedText.value = lastRedactedText;
                menu.classList.remove('active');
                redactedTextContainer.classList.add('active');

                showRedacted.disabled = false;
                showRedacted.style.opacity = "1"; 

                // Determine the current file type
                if (file.name.endsWith('.docx')) {
                    currentFileType = "word";
                } else if (file.name.endsWith('.xlsx')) {
                    currentFileType = "excel";
                } else {
                    currentFileType = "text";
                }
            }
        })
        .catch(error => {
            console.error('Error during file upload:', error);
            alert('An error occurred during file upload. Please try again.');
        });
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

            showRedacted.disabled = false;
            showRedacted.style.opacity = "1"; 
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
                body: JSON.stringify({ text: lastRedactedText, redaction_level: redactionSlider.value })
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
        fetch('/download', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ redaction_level: redactionSlider.value })
        })
        .then(response => response.blob())
        .then(blob => {
            let downloadName = 'redacted_text.txt';
            if (currentFileType === "word") {
                downloadName = 'redacted_document.docx';
            } else if (currentFileType === "excel") {
                downloadName = 'redacted_document.xlsx';
            }

            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = downloadName;
            link.click();
        })
        .catch(error => {
            console.error('Error during download:', error);
            alert('An error occurred during file download. Please try again.');
        });
    });
});

