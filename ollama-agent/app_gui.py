import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ollama Agent (Masaüstü)")
        self.resize(700, 600)
        webview = QWebEngineView()
        webview.load("http://localhost:5000")  # Flask sunucu adresi
        self.setCentralWidget(webview)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
