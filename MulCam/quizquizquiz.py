import random as r
# 내 손 로직
def user_hand():
    while True:
        user_hand = input('가위 바위 보 중에서 입력해 주십사')
        if user_hand == '가위' or user_hand =='보' or user_hand == '바위':
            break
        else:
            print("다시 입력해주세요")
            continue
    return user_hand
# 게임 로직
def game_start(user):
    print("싸늘하다.. 가슴에 비수가 날아와 꽂힌다..")
    a = r.randint(0, 2)
    hand = ['가위', '바위', '보']
    if user == hand[a]:
        print(f'나는{user} 상대는 {hand[a]}')
        print("비겼다..")
    elif user=='가위' and hand[a] == '보':
        print(f'나는{user} 상대는 {hand[a]}')
        print('이겼다..')
    elif user=='바위' and hand[a] == '가위':
        print(f'나는{user} 상대는 {hand[a]}')
        print('이겼다..')
    elif user == '보' and hand[a] == '바위':
        print(f'나는{user} 상대는 {hand[a]}')
        print('이겼다..')
    else:
        print(f'나는 {user} 상대는 {hand[a]}')
        print("졌다...")

game_start(user_hand())


