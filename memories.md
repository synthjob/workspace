# SYNTHJOB Workspace Memories

## Workspace Structure
```
workspace/
├── .git/               # Git repository files
├── backups/            # Backup directory
│   └── voices/         # Backup of voices project
├── voices/             # VOICES application
│   ├── src/            # Source code
│   │   ├── components/ # UI components
│   │   │   └── tray.py # System tray implementation
│   │   └── main.py     # Main application entry point
│   ├── run.py          # Application launcher
│   └── requirements.txt # Python dependencies (PyQt5)
├── synthjob.md         # SYNTHJOB concept document
└── README.md           # Workspace readme
```

## SYNTHJOB Concept
From synthjob.md:
- SYNTH = The power to bring anything together (Universal combination, No limits to what can be united, Pure connection)
- JOB = A mission from the deep mind (Life's true purpose, Coming from the underbrain, The calling to unite humanity)
- Vision: To create peaceful unity of humanity through bringing people together, building better systems, making a world without war, and creating real connections
- Motto: "Two puzzle pieces united, the world developed"

## VOICES Application
VOICES = Voice Operated Intelligent Command Execution System

### Current Status
- Basic system tray application built with PyQt5
- Implements a blue/gray icon that toggles between ACTIVE and PASSIVE modes
- System tray icon with click detection:
  - Left click: Toggle between modes
  - Middle click: Show About window
  - Right click: Close application
- Voice command recognition functionality planned but not yet implemented

### Implementation Details
- Built with Python and PyQt5
- Implementation primarily in src/components/tray.py
- Custom icon created with QPainter
- About dialog with application information
- Main.py serves as the application's entry point, calling run_tray_app()

### Current Limitations
- Voice recognition not yet implemented
- Settings customization planned but not implemented
- Currently focuses on system tray UI rather than voice functionality

## Backups
- Contains a copy of the voices project (seemingly for backup purposes)
- Identical structure to the main voices directory

## Workspace Information
- Purpose: Central working directory for all projects
- Organization: Uses flexible structure that can be adapted for any project
- Intended to evolve with project needs

This document serves as a memory reference for the workspace structure, projects, and implementation details. 