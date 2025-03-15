import sys
from src.components.tray import run_tray_app

def main():
    """Main entry point for the VOICES application"""
    print("Starting VOICES - Voice Operated Intelligent Command Execution System")
    return run_tray_app()

if __name__ == "__main__":
    sys.exit(main()) 