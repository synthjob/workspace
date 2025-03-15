# VOICES - Voice Operated Intelligent Command Execution System

A system that allows you to control your computer using voice commands.

## Project Structure

```
voices/
├── src/                # Source code directory
│   ├── components/     # UI components
│   │   └── tray.py     # System tray implementation
│   └── main.py         # Main application logic
├── run.py              # Application entry point
└── requirements.txt    # Python dependencies
```

## Getting Started

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python run.py
   ```

3. Look for the icon in your system tray!

## Features

- Minimalist design with no popup windows
- System tray icon with visual state indication:
  - Gray icon: PASSIVE mode
  - Blue icon: ACTIVE mode
- Click detection:
  - Left click: Toggle between ACTIVE and PASSIVE modes
  - Middle click: Show About window with app information
  - Right click: Close application
- Mode-based operation:
  - PASSIVE mode: Limited functionality, minimal resource usage
  - ACTIVE mode: Full voice command recognition (coming soon)
- Intelligent command execution (coming soon)
- Customizable settings (coming soon)

## Dependencies

- Python 3.6+
- PyQt5 (for system tray functionality and UI) 