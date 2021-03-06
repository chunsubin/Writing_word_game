# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time
import winsound # 사운드 출력 모듈
import datetime
import sqlite3

# db생성 & Auto commit
# DB경로 설정
conn = sqlite3.connect('D:/[패캠] 파이썬 웹 개발 올인원/python실습(1강)/records.db',isolation_level=None)

# Cursor 연결
cursor=conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")


words=[] # 영어 단어 리스트 (1000개)

n=1 # 게임 시도 횟수
cor_cnt = 0 # 정답의 갯수

with open('D:/[패캠] 파이썬 웹 개발 올인원/python실습(1강)/resource/word.txt','r') as f:
    for c in f:
        words.append(c.strip()) # 양쪽 공백 제거

# print(words) 

input("Ready? Press Enter Key!") # Enter Game Start!

start=time.time()

while n<=5:
    random.shuffle(words)
    q=random.choice(words)

    print()

    print("*Question # {}".format(n))
    print(q)

    x=input()

    print()

    if str(q).strip()==str(x).strip():
        print("Pass!")
        # 정답소리 재생
        #winsound.PlaySound('./sound/good.wav',winsound.SND_FILENAME)
        cor_cnt+=1
    else:
        print("Wrong!")
        # 오답소리 재생
        #winsound.PlaySound('./sound/bad.wav',winsound.SND_FILENAME)

    n+=1

end = time.time() # end time
et = end-start # 총 게임시간
et=format(et,".3f")

if cor_cnt>=3:
    print("합격")
else:
    print("불합격")

# 기록 db 출력

cursor.execute("INSERT INTO records('cor_cnt','record','regdate') VALUES (?,?,?)",
    (
        cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
)

# 수행시간 출력
print("게임시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__=='__main__':
    pass