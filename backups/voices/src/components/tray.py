import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QDialog, QVBoxLayout, QLabel, QDialogButtonBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QSize

def create_icon(is_active=False):
    """Create a custom icon for the system tray
    
    Args:
        is_active (bool): Whether the app is in active mode
    """
    # Create a custom icon using PyQt5
    pixmap = QPixmap(64, 64)
    pixmap.fill(Qt.transparent)
    
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    
    # Draw outer circle - blue when active, gray when passive
    color = QColor(0, 128, 255) if is_active else QColor(120, 120, 120)
    painter.setBrush(color)
    painter.setPen(Qt.NoPen)
    painter.drawEllipse(0, 0, 64, 64)
    
    # Draw inner circle for microphone effect - white when active, light gray when passive
    inner_color = QColor(255, 255, 255) if is_active else QColor(200, 200, 200)
    painter.setBrush(inner_color)
    painter.drawEllipse(20, 20, 24, 24)
    
    painter.end()
    
    return QIcon(pixmap)

class AboutDialog(QDialog):
    """About dialog for the VOICES application"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About VOICES")
        self.setFixedSize(400, 300)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        
        layout = QVBoxLayout()
        
        # Title
        title_label = QLabel("VOICES")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Full name
        full_name = QLabel("Voice Operated Intelligent Command Execution System")
        full_name.setAlignment(Qt.AlignCenter)
        layout.addWidget(full_name)
        
        # Description
        description = QLabel(
            "VOICES is a system tray application that allows you to control\n"
            "your computer using voice commands. It runs silently in your\n"
            "system tray, ready to assist when needed.\n\n"
            "The application has two modes:\n"
            "• PASSIVE: Limited functionality, minimal resource usage\n"
            "• ACTIVE: Full voice command recognition capability\n\n"
            "Toggle between modes by left-clicking the tray icon."
        )
        description.setAlignment(Qt.AlignCenter)
        layout.addWidget(description)
        
        # Version info
        version = QLabel("Version: 0.1.0")
        version.setAlignment(Qt.AlignCenter)
        layout.addWidget(version)
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)
        
        self.setLayout(layout)

class VoicesTrayIcon(QSystemTrayIcon):
    def __init__(self, app):
        super().__init__(parent=None)
        self.app = app
        
        # Initialize state
        self.is_active = False
        
        # Set up the icon
        self.update_icon()
        self.setToolTip("VOICE OPERATED INTELLIGENT COMMAND EXECUTION SYSTEM")
        
        # Create menu - we'll keep this but won't show it on right-click
        menu = QMenu()
        
        # Add title (non-clickable)
        title_action = QAction("VOICES")
        title_action.setEnabled(False)
        menu.addAction(title_action)
        menu.addSeparator()
        
        # Add menu items with actions
        self.toggle_action = QAction("Activate")
        self.toggle_action.triggered.connect(self.toggle_active_state)
        menu.addAction(self.toggle_action)
        
        settings = QAction("Settings")
        settings.triggered.connect(self.open_settings)
        menu.addAction(settings)
        
        # Add About action
        about_action = QAction("About")
        about_action.triggered.connect(self.show_about)
        menu.addAction(about_action)
        
        menu.addSeparator()
        
        exit_action = QAction("Exit")
        exit_action.triggered.connect(self.exit_app)
        menu.addAction(exit_action)
        
        # Set the context menu (will only be shown if we explicitly call it)
        self.setContextMenu(menu)
        
        # Connect the activated signal to handle clicks
        self.activated.connect(self.handle_activation)
        
        # Show the icon
        self.show()
        print("System tray icon is running. Look for it in your system tray!")
        print("Click management is active:")
        print("- Left click: Toggle active/passive mode")
        print("- Middle click: Show About window")
        print("- Right click: Close application")
        print("Current mode: PASSIVE")
    
    def update_icon(self):
        """Update the icon to reflect the current state"""
        self.setIcon(create_icon(self.is_active))
    
    def toggle_active_state(self):
        """Toggle between active and passive states"""
        self.is_active = not self.is_active
        
        # Update icon to reflect new state
        self.update_icon()
        
        # Update menu text
        self.toggle_action.setText("Deactivate" if self.is_active else "Activate")
        
        # Show notification in console only
        mode = "ACTIVE" if self.is_active else "PASSIVE"
        print(f"Mode changed to: {mode}")
    
    def show_about(self):
        """Show the About dialog"""
        about_dialog = AboutDialog()
        about_dialog.exec_()
    
    def handle_activation(self, reason):
        if reason == QSystemTrayIcon.Trigger:  # Left click
            print("Left click detected")
            self.handle_left_click()
        elif reason == QSystemTrayIcon.MiddleClick:  # Middle click
            print("Middle click detected")
            self.handle_middle_click()
        elif reason == QSystemTrayIcon.Context:  # Right click
            print("Right click detected - closing application")
            self.exit_app()
        elif reason == QSystemTrayIcon.DoubleClick:  # Double click
            print("Double click detected")
            self.handle_double_click()
    
    def handle_left_click(self):
        # Handle left click - toggle active/passive state
        self.toggle_active_state()
    
    def handle_middle_click(self):
        # Handle middle click - show About window
        status = "ACTIVE" if self.is_active else "PASSIVE"
        print(f"System Status: Mode is {status}")
        self.show_about()
    
    def handle_double_click(self):
        # Handle double click - which could open a main interface in the future
        print("Double Click - Main Interface")
    
    def open_settings(self):
        print("Settings opened")
    
    def exit_app(self):
        print("Closing application...")
        self.hide()
        self.app.quit()

def run_tray_app():
    """Start the system tray application"""
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # Keep app running when no windows are open
    
    tray_icon = VoicesTrayIcon(app)
    
    return app.exec_()

if __name__ == "__main__":
    sys.exit(run_tray_app()) 