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
    for i in range(15): MakeVoiceFile(texts[i], dirname + "\\" + str(i+1))
    return dirname

if __name__ == '__main__':
    dirname = MakeAudioFile()