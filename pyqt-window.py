import json
from rls.rocket import RocketLeague
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap

 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Rocket League Ranks'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button = QPushButton('GO', self)
        self.button.clicked.connect(self.handleButton)
        pic = QLabel(self)
        pixmap = QPixmap('RL Ranks/17.png')
        pixmap5 = pixmap.scaled(138, 138, QtCore.Qt.KeepAspectRatio)
        pic.setPixmap(pixmap5)
        self.show()

    def handleButton(self):
        key = 'KITT7IJON8TT7XAEABU1PF8DJZ2GDIMH'
        rocket = RocketLeague(api_key=key)
        response = rocket.players.player(id='76561198064487811', platform=1)
        responseJson = response.json()
        print(json.dumps(responseJson, indent=4))
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("plastique")
    ex = App()
    sys.exit(app.exec_())
