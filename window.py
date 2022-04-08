import sys
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import make_audio as a
from StartTest import *
import os

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def btnnt_clicked(self):
        level = self.cmb_level.currentText()
        if level == "3-3": QMessageBox.about(self, "message", "I'm so sorry, but we don't have 3-3 level yet.\n I will make it ASAP.")
        elif level == "5-5":
            dirname = a.MakeAudioFile()
            msg = QMessageBox()
            msg.setWindowTitle("Making New Test Set")
            msg.setText("Success to make new set.\nNew Set : " + dirname)
            msg.exec()
        else: QMessageBox.about(self, "message", "Please select the level.\n  * combo box on the right")
    
    def btnst_clicked(self):
        self.test = self.cmb_list.currentText()
        if not self.test: QMessageBox.about(self, "message", "Please select the one of the test lists.\n  * combo box on the right")
        else:
            ava = starttest(self.test)
            #StartTest(test)

    def initUI(self):
        # Button
        x, y, w, h = 20, 20, 200, 30
        self.btnnt = QPushButton('Make New Test Set', self)
        self.btnnt.setGeometry(x, y, w, h)
        self.btnnt.clicked.connect(self.btnnt_clicked)

        self.btnst = QPushButton('Start Test', self)
        self.btnst.setGeometry(x, y+h+10, w, h)
        self.btnst.clicked.connect(self.btnst_clicked)

        # Combo Box
        self.cmb_level = QComboBox(self)
        self.cmb_level.addItem("")
        self.cmb_level.addItem("3-3")
        self.cmb_level.addItem("5-5")
        self.cmb_level.setGeometry(x+w+10, y, w//2, h)

        self.cmb_list = QComboBox(self)
        self.cmb_list.addItem("")
        folders = [file for file in os.listdir(".\\") if file.startswith('test_')]
        for folder in folders: self.cmb_list.addItem(folder)
        self.cmb_list.setGeometry(x+w+10, y+h+10, w//2, h)

        # Window Setting
        self.setWindowTitle('OPIc Test Program')
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

def InitWindow():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    InitWindow()