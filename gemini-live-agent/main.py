#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini Live Agent - PySide6 Desktop Application
Basic desktop application with a simple interface
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QLabel, QPushButton, QTextEdit, 
    QLineEdit, QMenuBar, QStatusBar, QSplitter
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        # Set window properties
        self.setWindowTitle("Gemini Live Agent")
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QVBoxLayout(central_widget)
        
        # Create title label
        title_label = QLabel("Gemini Live Agent")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        main_layout.addWidget(title_label)
        
        # Create input section
        input_layout = QHBoxLayout()
        input_label = QLabel("Input:")
        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Enter your message here...")
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.on_send_clicked)
        
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_line)
        input_layout.addWidget(self.send_button)
        main_layout.addLayout(input_layout)
        
        # Create splitter for output areas
        splitter = QSplitter(Qt.Horizontal)
        
        # Create output text area
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText("Agent responses will appear here...")
        
        # Create log text area
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setPlaceholderText("Log messages will appear here...")
        
        splitter.addWidget(self.output_text)
        splitter.addWidget(self.log_text)
        splitter.setSizes([400, 400])
        
        main_layout.addWidget(splitter)
        
        # Create control buttons
        button_layout = QHBoxLayout()
        self.clear_button = QPushButton("Clear Output")
        self.clear_button.clicked.connect(self.clear_output)
        
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        
        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()
        button_layout.addWidget(self.exit_button)
        
        main_layout.addLayout(button_layout)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        # Connect Enter key to send button
        self.input_line.returnPressed.connect(self.on_send_clicked)
        
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('File')
        
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu('Edit')
        
        clear_action = QAction('Clear Output', self)
        clear_action.setShortcut('Ctrl+L')
        clear_action.triggered.connect(self.clear_output)
        edit_menu.addAction(clear_action)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        
        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def on_send_clicked(self):
        """Handle send button click"""
        user_input = self.input_line.text().strip()
        if user_input:
            # Display user input
            self.output_text.append(f"<b>User:</b> {user_input}")
            
            # Log the input
            self.log_text.append(f"[INPUT] {user_input}")
            
            # Clear input field
            self.input_line.clear()
            
            # Simulate agent response (placeholder)
            response = f"Echo: {user_input}"
            self.output_text.append(f"<b>Agent:</b> {response}")
            self.log_text.append(f"[OUTPUT] {response}")
            
            # Update status
            self.status_bar.showMessage(f"Processed: {user_input[:30]}..." if len(user_input) > 30 else f"Processed: {user_input}")
            
    def clear_output(self):
        """Clear output and log text areas"""
        self.output_text.clear()
        self.log_text.clear()
        self.status_bar.showMessage("Output cleared")
        
    def show_about(self):
        """Show about dialog"""
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.about(self, "About Gemini Live Agent", 
                         "Gemini Live Agent\n\nA simple PySide6 desktop application\nfor AI agent interaction.")


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Gemini Live Agent")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("Synthjob")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
