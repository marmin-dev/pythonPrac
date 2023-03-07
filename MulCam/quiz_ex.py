# 커피 클래스
class MilkCoffee:
    price = 400
    def __init__(self):
        print('밀크커피 생성!')
class BlackCoffee:
    price = 300
    def __init__(self):
        print('블랙커피 생성!')
# 인간 클래스
class Customer:
    def __init__(self,money):
        self.money = money
        print(f'나는 {self.money}원을 가지고 있다')
# 자판기 클래스
class vendor:
    black_coffee = BlackCoffee
    milk_coffee = MilkCoffee
    def __init__(self):
        print('자판기 생성')
    def get_milk_coffee(self,cust):
        if cust.money >= self.milk_coffee.price:
            cust.money = cust.money - self.milk_coffee.price
            get_milk = MilkCoffee()
            print(f'잔돈은 {cust.money}입니다')
        else:
            print("돈이 없으면 커피는 없지")

    def get_black_coffee(self, cust):
        if cust.money >= self.black_coffee.price:
            cust.money = cust.money - self.black_coffee.price
            get_black = BlackCoffee()
            print(f'잔돈은 {cust.money}입니다')
        else:
            print("돈 더 갖고오십쇼")

# 인간 검증기
def valid_money():
    while True:
        try:
            money = int(input("돈을 넣어봐"))
        except:
            print("돈을 정수형으로 넣어야지")
            continue
        break
    c = Customer(money)
    return c

c = valid_money()
v = vendor()
v.get_milk_coffee(c)
v.get_black_coffee(c)
print(c.money)
