
def payCal():
    # 딕셔너리 선언
    pay_dict = {"weekly_hour": 0, "pay_rate": 9620, "total": 0.0}
    # 주간 일한 시간 입력
    weekly_hour = int(input('working hours: '))
    # 딕셔너리 업데이트
    pay_dict["weekly_hour"] = weekly_hour

    if 40 <= int(weekly_hour) < 60:
        # 딕셔너리를 업데이트 해서 반환함
        money = pay_dict["pay_rate"] * int(weekly_hour) * 1.5
        pay_dict["total"] = money
        return pay_dict
    elif 60 <= int(weekly_hour):
        # 딕셔너리를 업데이트 해서 반환함
        money = pay_dict["pay_rate"] * int(weekly_hour) * 2
        pay_dict["total"] = money
        return pay_dict
    else:
            # 딕셔너리를 업데이트 해서 반환함
        money = pay_dict["pay_rate"] * int(weekly_hour)
        pay_dict["total"] = money
        return pay_dict

money_dict = payCal()
print(f'{money_dict["weekly_hour"]} : {money_dict["total"]}')