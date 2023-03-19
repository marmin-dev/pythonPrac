import random
import time
# 단어 개수 입력받기

def word_len_input():
    word_len = ''
    while True:
        try:
            word_len = int(input("몇개의 단어를 외우실 건가요?"))
        except:
            print("숫자가 아닙니다")
            continue
        break
    return word_len
# 리스트 생성, 단어 추가하기
def word_input(n):
    word_li = []
    for i in range(n):
        word_li.append(input("단어를 입력하십시오"))
    return word_li
# 단어 맞추기
def word_quiz(li):
    print("30 초의 시간을 드립니다 외우십쇼")
    time.sleep(30)
    count = 0;
    for i in range(len(li)):
        word = input(f'{i+1}번째로 입력한 단어는?')
        if word == li[i]:
            print("정답")
            count += 1
        else:
            print("오답")
    print(f'당신이 맞춘 갯수는 {count}개 입니다')


num = word_len_input()
lis = word_input(num)
word_quiz(lis)



