import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        # Button & Layout
        """""
        grid = QGridLayout()
        grid.addWidget(QLabel('Setting Level'), 0, 0)
        grid.addWidget(QLabel('3-3'), 1, 0)
        grid.addWidget(QLabel('5-5'), 2, 0)
        grid.addWidget(QPushButton('3-3', self), 1, 1)
        grid.addWidget(QPushButton('5-5', self), 2, 1)
        self.setLayout(grid)
        """""

        # Window Setting
        self.setWindowTitle('OPIc Test Program')
        self.setWindowIcon(QIcon('play_music_audio_18916.png'))
        #self.setGeometry(300, 300, 300, 200)
        self.resize(800,600)
        self.center()
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())