import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.showMaximized()

        self.navbar = QToolBar()
        self.addToolBar(self.navbar)
        self.navbar.setStyleSheet(
            "background-color: #fff; padding: 10px"
        )

        back_btn = QAction(QIcon('img/left.png'),'Back', self)
        back_btn.triggered.connect(self.browser.back)
        self.navbar.addAction(back_btn)

        forward_btn = QAction(QIcon('img/right.png'), 'Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        self.navbar.addAction(forward_btn)
        self.navbar.setStyleSheet('QToolButton#qt_toolbutton { background-color: #121212; border: none; }')

        reload_btn = QAction(QIcon('img/reload.png'),'Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        self.navbar.addAction(reload_btn)

        self.search_box = QLineEdit(self)
        self.search_box.setText("")
        self.search_box.returnPressed.connect(self.navigate_to_url)
        self.navbar.addWidget(self.search_box)
        self.browser.urlChanged.connect(self.update_url)
        self.search_box.setStyleSheet(
            "padding: 8px; border: 2px solid #ccc; border-radius: 5px;"
        )

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Q:
            self.toggle_navbar_visibility()

        if event.modifiers() == Qt.AltModifier and event.key() == Qt.Key_Left:
            self.browser.page().triggerAction(QWebEnginePage.Back)

        if event.modifiers() == Qt.AltModifier and event.key() == Qt.Key_Right:
            self.browser.page().triggerAction(QWebEnginePage.Forward)

        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_R:
            self.browser.page().triggerAction(QWebEnginePage.Reload)

    def toggle_navbar_visibility(self):
        if self.navbar.isVisible():
            self.navbar.setVisible(False)
        else:
            self.navbar.setVisible(True)


    def navigate_to_url(self):
        url = self.search_box.text()
        if url == "":
            self.search_box.setText("")
            self.browser.setUrl(QUrl(""))
        else:
            self.browser.setUrl(QUrl(f"https://duckduckgo.com/?q={url}"))

    def update_url(self, q):
        self.search_box.setText(q.toString())


app = QApplication(sys.argv)
app.setStyle('Oxygen')
app.setWindowIcon(QIcon('img/icon.png'))
QApplication.setApplicationName('NeoBrowser')
window = MainWindow()
window.setWindowIcon(QIcon('img/icon.png'))
window.show()
sys.exit(app.exec_())