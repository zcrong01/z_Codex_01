#_Part_00100_imports  [주석단위]
import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel

from .bridge import AppBridge

#_Part_00200_paths_and_config  [주석단위]
ROOT_DIR = Path(__file__).resolve().parent.parent
APP_DIR = ROOT_DIR / "app"
INDEX_HTML = APP_DIR / "index.html"

#_Part_00300_mainwindow  [주석단위]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("블록으로 만드는 아두이노 코딩")
        self.resize(1300, 820)

        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

        self.channel = QWebChannel(self.view.page())
        self.bridge = AppBridge(str(ROOT_DIR))
        self.channel.registerObject("AppBridge", self.bridge)
        self.view.page().setWebChannel(self.channel)

        self.view.load(QUrl.fromLocalFile(str(INDEX_HTML)))

#_Part_00400_entrypoint  [주석단위]
def main() -> int:
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
