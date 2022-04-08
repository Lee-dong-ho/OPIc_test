import os
import playsound as p
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from time import sleep

class starttest(QWidget):
  def __init__(self, msg):
    super().__init__()
    self.dirname = msg
    self.initUI()

  def btnnext_clicked(self):
    StartTest(self.dirname)

  def initUI(self):
    btnnext = QPushButton("NEXT", self)
    btnnext.setGeometry(50,50,150,30)
    btnnext.clicked.connect(self.btnnext_clicked)

    self.setWindowTitle(self.dirname)
    self.setWindowIcon(QIcon(''))
    self.resize(500,500)
    self.center()
    self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

def StartTest(dirname):
  for audio in range(1,16):
    file = os.getcwd() + "\\" + dirname + "\\" + str(audio) + ".mp3"
    print(file)
    p.playsound(file)
    sleep(1)