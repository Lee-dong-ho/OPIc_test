from gtts import gTTS
from PyQt5.QtWidgets import QMessageBox
import random
import os

def MakeVoiceFile(text, name): 
    tts = gTTS(text=text, lang='en')
    tts.save(name)

def MakeComboSet():
    text = ""
    f = open("res\\combo.txt", 'r')
    lines = f.readlines()
    setcnt = len(lines)//3
    added_topic = []
    while len(added_topic) < 3:
        set = random.randrange(0, setcnt)
        l = lines[set*3].split("+")
        if l[0] not in added_topic:
            added_topic.append(l[0])
            text += str(l[1])+str(lines[set*3+1])+str(lines[set*3+2])
    f.close()
    return text

def MakeRolePlaying():
    text = ""
    f = open("res\\roleplaying.txt", 'r')
    lines = f.readlines()
    setcnt = len(lines)//3
    set = random.randrange(0, setcnt)
    text += str(lines[set*3])+str(lines[set*3+1])+str(lines[set*3+2])
    f.close()
    return text

def MakeSocialIssue():
    text = ""
    f = open("res\\socialissue.txt", 'r')
    lines = f.readlines()
    setcnt = len(lines)//2
    set = random.randrange(0, setcnt)
    text += str(lines[set*2])+str(lines[set*2+1])
    f.close()
    return text

def MakeAudioFile():
    # 2,3,4 / 5,6,7 / 8,9,10 :  Combo           3set
    # 11,12,13               :  Role Playing    1set
    # 14,15                  :  Social Issue    1set
    filelist = os.listdir(".\\")
    filelist = [int(file[5:]) for file in filelist if file.startswith('test_')]
    filelist.sort()
    if not filelist: dirname = "test_1"
    else: dirname = "test_" + str(filelist[-1] + 1)
    os.makedirs(dirname)

    text = "Tell me something about yourself.\n"
    text += MakeComboSet()
    text += MakeRolePlaying()
    text += MakeSocialIssue()
    texts = text.split('\n')
    for i in range(15): MakeVoiceFile(texts[i], f"{dirname}\\{i+1}.mp3")
    f = open(f"{dirname}\\Questions.txt","w")
    f.write(text)
    f.close()
    return dirname

if __name__ == '__main__':
    dirname = MakeAudioFile()