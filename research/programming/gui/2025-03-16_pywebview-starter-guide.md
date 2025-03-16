# Getting Started with PyWebview for Voice App
Date: 2025-03-16

## Introduction

PyWebview is a lightweight Python library that allows you to create desktop applications with web technologies (HTML, CSS, JavaScript) while using Python for your backend logic. This makes it perfect for a voice recognition app where you need both a modern UI and Python's powerful audio processing capabilities.

## Installation

```
pip install pywebview
```

For Windows, you might also need:
```
pip install pywin32
```

## Basic Structure

A PyWebview app typically consists of:
1. A Python backend file
2. HTML/CSS/JS for the frontend
3. Communication between the two

## Sample Voice App Structure

Here's a simple example of how to structure a voice app using PyWebview:

### 1. Project Structure

```
voices-app/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── img/
│   └── index.html
├── voice_processing/
│   ├── __init__.py
│   └── recognizer.py
└── main.py
```

### 2. Python Backend (main.py)

```python
import webview
import os
from voice_processing.recognizer import VoiceRecognizer

class VoiceAPI:
    def __init__(self):
        self.recognizer = VoiceRecognizer()
        self.is_listening = False
    
    def start_listening(self):
        """Start voice recognition"""
        self.is_listening = True
        self.recognizer.start()
        return "Listening started"
    
    def stop_listening(self):
        """Stop voice recognition"""
        self.is_listening = False
        self.recognizer.stop()
        return "Listening stopped"
    
    def get_status(self):
        """Get current status"""
        return {
            "is_listening": self.is_listening,
            "last_text": self.recognizer.last_text
        }

def get_html_path():
    """Get the absolute path to the index.html file"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'app', 'index.html')

if __name__ == '__main__':
    api = VoiceAPI()
    html_path = get_html_path()
    window = webview.create_window(
        'Voice App', 
        html_path, 
        js_api=api,
        width=800, 
        height=600,
        resizable=True
    )
    webview.start(debug=True)
```

### 3. Voice Processing Module (voice_processing/recognizer.py)

```python
import threading
import time

class VoiceRecognizer:
    """
    Simple placeholder for voice recognition.
    Replace with actual implementation using libraries like:
    - SpeechRecognition
    - Picovoice
    - Vosk
    - etc.
    """
    def __init__(self):
        self.last_text = ""
        self._running = False
        self._thread = None
    
    def start(self):
        """Start voice recognition in a separate thread"""
        if self._running:
            return
        
        self._running = True
        self._thread = threading.Thread(target=self._recognition_loop)
        self._thread.daemon = True
        self._thread.start()
    
    def stop(self):
        """Stop voice recognition"""
        self._running = False
        if self._thread:
            self._thread.join(timeout=1.0)
            self._thread = None
    
    def _recognition_loop(self):
        """Simulated recognition loop - replace with actual implementation"""
        while self._running:
            # In a real app, this would process audio and recognize speech
            # For now, just simulate recognition
            time.sleep(2)
            self.last_text = "This is a simulated voice recognition result."
            # In real implementation, you might update UI via JavaScript here
```

### 4. HTML Frontend (app/index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voice Recognition App</title>
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Voice Recognition App</h1>
        
        <div class="status-container">
            <div id="status-indicator" class="status-indicator not-listening"></div>
            <div id="status-text">Not Listening</div>
        </div>
        
        <div class="button-container">
            <button id="start-btn" class="action-button start">Start Listening</button>
            <button id="stop-btn" class="action-button stop" disabled>Stop Listening</button>
        </div>
        
        <div class="result-container">
            <h2>Recognition Results:</h2>
            <div id="result-text" class="result-text">No results yet...</div>
        </div>
    </div>

    <script src="static/js/main.js"></script>
</body>
</html>
```

### 5. JavaScript (app/static/js/main.js)

```javascript
// Wait for PyWebview to be ready
window.addEventListener('pywebviewready', function() {
    // Get elements
    const startBtn = document.getElementById('start-btn');
    const stopBtn = document.getElementById('stop-btn');
    const statusIndicator = document.getElementById('status-indicator');
    const statusText = document.getElementById('status-text');
    const resultText = document.getElementById('result-text');
    
    // Setup polling for status updates
    let statusInterval;
    
    // Add event listeners
    startBtn.addEventListener('click', function() {
        window.pywebview.api.start_listening().then(function(response) {
            console.log(response);
            startBtn.disabled = true;
            stopBtn.disabled = false;
            statusIndicator.className = 'status-indicator listening';
            statusText.textContent = 'Listening...';
            
            // Start polling for status updates
            statusInterval = setInterval(updateStatus, 1000);
        });
    });
    
    stopBtn.addEventListener('click', function() {
        window.pywebview.api.stop_listening().then(function(response) {
            console.log(response);
            startBtn.disabled = false;
            stopBtn.disabled = true;
            statusIndicator.className = 'status-indicator not-listening';
            statusText.textContent = 'Not Listening';
            
            // Stop polling
            clearInterval(statusInterval);
        });
    });
    
    // Function to update status
    function updateStatus() {
        window.pywebview.api.get_status().then(function(status) {
            if (status.last_text) {
                resultText.textContent = status.last_text;
            }
        });
    }
});
```

### 6. CSS (app/static/css/style.css)

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f5f5f5;
    color: #333;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

h1 {
    text-align: center;
    color: #2c3e50;
}

.status-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 20px 0;
}

.status-indicator {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    margin-right: 10px;
}

.not-listening {
    background-color: #e74c3c;
}

.listening {
    background-color: #2ecc71;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% {
        transform: scale(1);
        opacity: 1;
    }
    50% {
        transform: scale(1.1);
        opacity: 0.7;
    }
    100% {
        transform: scale(1);
        opacity: 1;
    }
}

.button-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin: 30px 0;
}

.action-button {
    padding: 12px 24px;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s;
}

.action-button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.start {
    background-color: #2ecc71;
    color: white;
}

.start:hover:not(:disabled) {
    background-color: #27ae60;
}

.stop {
    background-color: #e74c3c;
    color: white;
}

.stop:hover:not(:disabled) {
    background-color: #c0392b;
}

.result-container {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.result-text {
    min-height: 100px;
    padding: 15px;
    background-color: #f9f9f9;
    border-radius: 4px;
    border-left: 4px solid #3498db;
}
```

## Next Steps

1. **Implement real voice recognition**:
   - Replace the placeholder VoiceRecognizer with a real implementation using libraries like Picovoice, SpeechRecognition, or Vosk

2. **Add more UI features**:
   - Visualization of voice levels
   - Settings panel for adjusting sensitivity
   - Voice command history

3. **Package for distribution**:
   - Use PyInstaller to create a standalone executable:
     ```
     pip install pyinstaller
     pyinstaller --windowed --name VoiceApp main.py
     ```

## Resources

- [PyWebview Documentation](https://pywebview.flowrl.com/)
- [Picovoice for Offline Voice Recognition](https://picovoice.ai/)
- [HTML/CSS/JS Tutorials (Mozilla)](https://developer.mozilla.org/en-US/docs/Web)
- [PyInstaller Documentation](https://pyinstaller.org/en/stable/) 