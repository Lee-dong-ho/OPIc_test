from gtts import gTTS
import random
import os

def MakeVoiceFile(text, name): 
    tts = gTTS(text=text, lang='en')
    tts.save(name + '.mp3')

def MakeComboSet():
    text = ""
    f = open("combo.txt", 'r')
    lines = f.readlines()
    setcnt = len(lines)//3
    set = random.sample(range(0, setcnt), 3)
    for i in set:
        text += str(lines[i])+str(lines[i+1])+str(lines[i+2])
    f.close()
    return text

def MakeRolePlaying():
    text = ""
    f = open("roleplaying.txt", 'r')
    lines = f.readlines()
    setcnt = len(lines)//3
    set = random.randrange(0, setcnt)
    text += str(lines[set])+str(lines[set+1])+str(lines[set+2])
    f.close()
    return text

def MakeSocialIssue():
    text = ""
    f = open("socialissue.txt", 'r')
    lines = f.readlines()
    setcnt = len(lines)//2
    set = random.randrange(0, setcnt)
    text += str(lines[set])+str(lines[set+1])
    f.close()
    return text

def MakeAudioFile():
    # 2,3,4 / 5,6,7 / 8,9,10 :  Combo           3set
    # 11,12,13               :  Role Playing    1set
    # 14,15                  :  Social Issue    1set
    text = "Tell me something about yourself.\n"
    text += MakeComboSet()
    text += MakeRolePlaying()
    text += MakeSocialIssue()
    filelist = os.listdir(".\\")
    filelist = [file for file in filelist if file.endswith('.mp3')]
    if not filelist: vfname = "OPIc5_1" 
    else: vfname = "OPIc5_" + str(int(filelist[-1][6:-4]) + 1)
    MakeVoiceFile(text, vfname)

if __name__ == '__main__':
    MakeAudioFile()