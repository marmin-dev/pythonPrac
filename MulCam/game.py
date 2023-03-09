import tkinter as tk
import random

# 가위바위보 버튼 클릭 이벤트 핸들러
def play_game(user_choice):
    # 컴퓨터가 낼 가위바위보 선택

    choices = ["가위", "바위", "보"]
    computer_choice = random.choice(choices)

    # 승패 계산
    if user_choice == computer_choice:
        result = "비겼다..."
    elif user_choice == "가위" and computer_choice == "보":
        result = "이겼다.."
    elif user_choice == "바위" and computer_choice == "가위":
        result = "이겼다.."
    elif user_choice == "보" and computer_choice == "바위":
        result = "이겼다..!"
    else:
        result = "졌다.."

    # 결과 출력
    result_label.configure(text="결과: " + result + " (컴퓨터: " + computer_choice + ")")

# tkinter 윈도우 생성
window = tk.Tk()

# 윈도우 타이틀 설정
window.title("가위바위보")

# 가위바위보 버튼 생성
rock_button = tk.Button(window, text="바위", command=lambda: play_game("바위"))
paper_button = tk.Button(window, text="보", command=lambda: play_game("보"))
scissors_button = tk.Button(window, text="가위", command=lambda: play_game("가위"))
# 이미지 넣기


# 결과 출력 라벨 생성
start_label = tk.Label(window, text="싸늘하다 가슴에 비수가 날아와 꽂힌다 ")
result_label = tk.Label(window, text="결과: ")

# 위젯 배치
start_label.pack(side=tk.TOP,padx=10)
rock_button.pack(side=tk.LEFT, padx=10)
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button.pack(side=tk.LEFT, padx=10)
result_label.pack(side=tk.BOTTOM, pady=10)



# 윈도우 실행
window.mainloop()