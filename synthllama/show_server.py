import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
import subprocess
import threading
import time

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SynthLLaMA Sohbet')
        self.setGeometry(100, 100, 900, 600)
        vbox = QVBoxLayout(self)
        self.browser = QWebEngineView()
        vbox.addWidget(self.browser)
        # Kısa bir bekleme ile sunucuya istek yap
        threading.Thread(target=self.delayed_load, daemon=True).start()
    
    def delayed_load(self):
        time.sleep(2.5)  # Sunucunun başlaması için kısa bir gecikme
        self.browser.setUrl('http://localhost:8000')

if __name__ == "__main__":
    # İlk olarak sunucuyu başlat
    subprocess.Popen([sys.executable, '-m', 'uvicorn', 'backend:app', '--reload'])
    # Ana pencereyi başlat
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
