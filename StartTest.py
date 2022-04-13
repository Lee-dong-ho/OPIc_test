import os
from playsound import playsound
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication, QDesktopWidget, QLabel, QTextBrowser, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QSize, QTimer, Qt
from time import sleep

class starttest(QDialog):
  Notsolved = "background-color: lightgray; border: 1.5px outset gray"
  Solved = "background-color: lightblue; border: 1.5px outset gray"
  qcur = 1
  tcnt = 150
  x = 30
  y = 30
  def __init__(self, msg):
    super().__init__()
    self.dirname = msg
    self.path = os.getcwd() + "\\" + msg + "\\"
    f = open(f"{msg}\\Questions.txt","r")
    self.texts = f.readlines()
    f.close()
    self.initUI()
    self.show()

  def StartNextQuestion(self):
    if self.qcur > 15: self.close()
    self.timer.stop()
    self.tcnt = 150
    self.lb_timer.setText(self.init_time)
    self.btnnext.setEnabled(False)
    self.btnstart.setEnabled(True)
    self.q[self.qcur].setStyleSheet(self.Solved)
    self.qtext.clear()
    self.qcur += 1
  
  def timeout(self):
    self.tcnt -= 1
    remain_time = f"{self.tcnt//60}:{self.tcnt%60:02d}"
    self.lb_timer.setText(remain_time)
    if self.tcnt < 1:
      self.StartNextQuestion()

  def btnnext_clicked(self):    
    self.StartNextQuestion()

  def btnstart_clicked(self):
    file = f"{self.dirname}/{str(self.qcur)}.mp3"
    print(file)
    playsound(file)
    sleep(3)
    playsound(file)
    self.timer.start(1000)
    self.btnnext.setEnabled(True)
    self.btnstart.setEnabled(False)

  def btnshowq_clicked(self):
    if self.qtext.toPlainText():
      self.qtext.clear()
      self.btnshowq.setText("Show Question")
    else:
      self.qtext.setText(self.texts[self.qcur-1])
      self.btnshowq.setText("Hide Question")
  
  def btnhelp_clicked(self):
    msg = QMessageBox()
    msg.setWindowTitle("help")
    msg.setText("좌측상단 : Ava 이미지와 재생버튼\n" \
                "좌측하단 : 남은 시간 표시\n" \
                "우측상단 : 현재 문제 번호 표시\n" \
                "우측하단 : Show Question 버튼 - 현재 문제를 text로 보여줌\n" \
                "               Next 버튼 - 다음 문제로 이동\n\n" \
                "1. 재생 버튼 클릭\n" \
                "2. 문제 2번 듣기(3초간격)\n" \
                "3. 대답 후 Next 버튼 클릭\n" \
                "4. 대답 중 시간이 경과했을 경우 자동으로 다음 문제로 넘어감.\n" \
                "  * 문제를 듣기 전 Next 버튼 클릭할 수 없음.")
    msg.exec()

  def initUI(self):
    self.createImageField()
    self.createTimeField()
    self.createStatusField()
    self.createButtonField()
    self.createHelpField()

    # UI
    self.setStyleSheet("background: white")

    # Configuration
    self.setWindowTitle(self.dirname)
    self.setWindowIcon(QIcon('res\\audio.png'))
    self.resize(700,500)
    self.center()
  
  def createImageField(self):
    AvaImg = QPixmap()
    AvaImg.load("res\\ava.png")
    lb_picture = QLabel(self)
    lb_picture.setPixmap(AvaImg)
    lb_picture.move(self.x, self.y)

    self.btnstart = QPushButton(self)
    self.btnstart.clicked.connect(self.btnstart_clicked)
    pixmap = QPixmap()
    pixmap.load("res\\start.png")
    icon = QIcon()
    icon.addPixmap(pixmap)
    self.btnstart.setIcon(icon)
    self.btnstart.setIconSize(QSize(30,30))
    self.btnstart.setGeometry(self.x, self.y + 235, 30,30)
  
  def createTimeField(self):
    self.timer = QTimer()
    self.timer.timeout.connect(self.timeout)
    self.init_time = f"{self.tcnt//60}:{self.tcnt%60:02d}"
    self.lb_timer = QLabel(self.init_time, self)
    self.lb_timer.setFont(QFont("Helvetica",40))
    self.lb_timer.move(self.x + 60, self.y + 320)

  def createStatusField(self):
    self.q = [QLabel(str(i), self) for i in range(1,16)]
    for i in range(15):
      self.q[i].setStyleSheet(self.Notsolved)
      self.q[i].setAlignment(Qt.AlignCenter)
      if i < 10: self.q[i].setGeometry(self.x + 250 + i*40, self.y, 30, 30)
      else: self.q[i].setGeometry(self.x + 250 + (i-10)*40, self.y + 40, 30, 30)
    self.q[0].setStyleSheet(self.Solved)

    self.qtext = QTextBrowser(self)
    self.qtext.setFont(QFont("Helvetica", 12))
    self.qtext.setStyleSheet("background-color: transparent; border-style: none")
    self.qtext.setGeometry(self.x + 250, self.y + 100, 380, 100)
  
  def createButtonField(self):
    self.btnshowq = QPushButton("Show Question", self)
    self.btnshowq.setGeometry(self.x + 320, self.y + 400, 150, 30)
    self.btnshowq.setStyleSheet("background: lightgray")
    self.btnshowq.clicked.connect(self.btnshowq_clicked)

    self.btnnext = QPushButton("NEXT", self)
    self.btnnext.setGeometry(self.x + 500, self.y + 400, 150, 30)
    self.btnnext.setStyleSheet("background: lightgray")
    self.btnnext.clicked.connect(self.btnnext_clicked)
    self.btnnext.setEnabled(False)
  
  def createHelpField(self):
    btnhelp = QPushButton(self)
    btnhelp.setGeometry(self.x + 650, 0, 20, 20)
    #btnhelp.setStyleSheet("border: transparent")
    btnhelp.clicked.connect(self.btnhelp_clicked)
    pixmap = QPixmap()
    pixmap.load("res\\help.png")
    icon = QIcon()
    icon.addPixmap(pixmap)
    btnhelp.setIcon(icon)
    btnhelp.setIconSize(QSize(20,20))

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())    

import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = starttest("test_7")
    sys.exit(app.exec_())