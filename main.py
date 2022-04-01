from time import sleep
import speech_recognition as sr
import playsound as p
import window as w
import make_audio as a
import os

def StartTest(dirname):
   for audio in range(1,16):
      file = dirname + "\\" + str(audio) + ".mp3"
      p.playsound(file)
      sleep(1)

'''
1. 일 경험 없음
2. 학생 - 아니오, 수업 등록 후 5년
3. 독신자로서 개인 주택이나 아파트에 거주
4. (총 8개)
   영화보기, 콘서트 가기, 공연/연극 관람하기
   캠핑, 공원 가기, 해변가기
   카페/커피전문점 가기, 술집/바에 가기
5. (총 1개) 음악감상
6. (총 1개) 신체 운동을 즐기지 않음
7. (총 2개) 국내여행, 해외여행
'''
if __name__ == '__main__':
    #dirname = a.MakeAudioFile()
    StartTest(os.getcwd() + "\\test_1")