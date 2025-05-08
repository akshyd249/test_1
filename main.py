import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)
browser = QWebEngineView()
browser.setUrl("https://www.google.com")
browser.setWindowTitle("Simple Browser")
browser.resize(1024, 768)
browser.show()
sys.exit(app.exec_())
