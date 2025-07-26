import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton)
import subprocess
import threading

class ServerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.server_proc = None

    def init_ui(self):
        self.setWindowTitle('SynthLLaMA - FastAPI Sunucu Kontrolü')
        self.setGeometry(100, 100, 400, 180)
        self.layout = QVBoxLayout()
        self.label = QLabel('Sunucu başlatılmadı.')
        self.btn = QPushButton('Sunucuyu Başlat')
        self.btn.clicked.connect(self.start_server)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)

    def start_server(self):
        self.label.setText('Sunucu başlatılıyor (uvicorn backend:app --reload)...')
        self.btn.setEnabled(False)
        # Sunucuyu ayrı bir thread'de başlat
        threading.Thread(target=self.run_uvicorn, daemon=True).start()

    def run_uvicorn(self):
        self.server_proc = subprocess.Popen([
            sys.executable, '-m', 'uvicorn', 'backend:app', '--reload'
        ])
        self.label.setText('Sunucu çalışıyor: http://localhost:8000')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerWindow()
    window.show()
    sys.exit(app.exec())
