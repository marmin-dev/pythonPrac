import re
def payCal(t):
    pay_time = 9620
    if 40 <= t < 60:
        return pay_time * t * 1.5
    elif 60 <= t:
        return pay_time * t * 2
    else:
        return pay_time * t

def validator():
    while True:
        try:
            work_time = int(input("일한 시간은?"))
        except:
            print("시간은 정수입니다")
            continue
        break
    return work_time


money = validator()
weekly_pay = payCal(money)
pattern = '(\d)(?=(\d{3})+(?!\d))'
formatted_pay = re.sub(pattern, r'\1,', str(weekly_pay))

print(f'{formatted_pay}원을 주급으로 받습니다')
