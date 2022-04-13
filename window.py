import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QDesktopWidget, QPushButton, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from make_audio import MakeAudioFile
from StartTest import starttest
import os

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        if self.ErrorCheck(): self.initUI()
        else: sys.exit()
    
    def ErrorCheck(self):
        if os.path.isdir("res") == False:            
            QMessageBox.about(self, "Error", "[Error] 'res' Folder Not Found...\nPlease make this folder")
            return 0
        if len(os.listdir("res")) < 7:
            QMessageBox.about(self, "Error", "[Error] There are no enough files in 'res' folder.\nPlease check the files\n\t* png : audio ava help start\n\t* txt : combo roleplaying socialissue")
            return 0
        return 1
    
    def btnnt_clicked(self):
        level = self.cmb_level.currentText()
        if level == "3-3": QMessageBox.about(self, "message", "I'm so sorry, but we don't have 3-3 level yet.\n I will make it ASAP.")
        elif level == "5-5":
            dirname = MakeAudioFile()
            self.hide()
            msg = QMessageBox()
            msg.setWindowTitle("Making New Test Set")
            msg.setWindowIcon(QIcon('res\\audio.png'))
            msg.setText("Success to make new set.\nNew Set : " + dirname)
            msg.exec()
            self.show()
            self.cmb_list.addItem(dirname)
            self.cmb_list.setCurrentText(dirname)
        else: QMessageBox.about(self, "message", "Please select the level.\n  * combo box on the right")
    
    def btnst_clicked(self):
        self.test = self.cmb_list.currentText()
        if not self.test: QMessageBox.about(self, "message", "Please select the one of the test lists.\n  * combo box on the right")
        else:
            self.hide()
            ava = starttest(self.test)
            ava.setWindowFlags(ava.windowFlags()&~Qt.WindowContextHelpButtonHint)
            ava.exec_()
            self.show()

    def initUI(self):
        # Button
        x, y, w, h = 20, 20, 200, 30
        self.btnnt = QPushButton('Make New Test Set', self)
        self.btnnt.setGeometry(x, y, w, h)
        self.btnnt.clicked.connect(self.btnnt_clicked)
        self.btnnt.setStyleSheet("background: lightgray")

        self.btnst = QPushButton('Start Test', self)
        self.btnst.setGeometry(x, y+h+10, w, h)
        self.btnst.clicked.connect(self.btnst_clicked)
        self.btnst.setStyleSheet("background: lightgray")

        # Combo Box
        self.cmb_level = QComboBox(self)
        self.cmb_level.addItem("3-3")
        self.cmb_level.addItem("5-5")
        self.cmb_level.setGeometry(x+w+10, y, w//2, h)
        self.cmb_level.setCurrentIndex(self.cmb_level.count()-1)
        self.cmb_level.setStyleSheet("background: white; border: 1px solid")

        self.cmb_list = QComboBox(self)
        folders = [file for file in os.listdir(".\\") if file.startswith('test_')]
        for folder in folders: self.cmb_list.addItem(folder)
        self.cmb_list.setGeometry(x+w+10, y+h+10, w//2, h)
        self.cmb_list.setCurrentIndex(self.cmb_list.count()-1)
        self.cmb_list.setStyleSheet("background: white; border: 1px solid")

        # Window Setting
        self.setWindowTitle('OPIc Test Program')
        self.setWindowIcon(QIcon('res\\audio.png'))
        self.setStyleSheet("background: white")
        self.resize(350,120)
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