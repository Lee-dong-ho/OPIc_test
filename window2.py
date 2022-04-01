from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class window2(QWidget):
    def __init__(self, parent):
        super(window2, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # Window Setting
        self.setWindowTitle('Making New Test Set...')
        self.setWindowIcon(QIcon('play_music_audio_18916.png'))
        #self.setGeometry(300, 300, 300, 200)
        self.resize(350,150)
        self.center()
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())