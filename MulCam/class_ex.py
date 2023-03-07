class Student:
    def __init__(self, name, number, classroom):
        self.name = name
        self.number = number
        self.classroom = classroom
    def __str__(self):
        return f"저는 {self.name}이고 {self.classroom}반 {self.number}번 학생입니다"

bumsoo = Student('김범수',15,3)
print(bumsoo)
jandi = Student('금잔디',14,4)
print(jandi)

class Calculator:
    result = 0
    def __init__(self):
        print("계산기 생성!")
    def sum(self,n1,n2):
        self.result = n1 + n2
        return self.result
    def multiple(self, n1, n2):
        self.result = n1 * n2
        return self.result
    def subtract(self,n1, n2):
        self.result = n1 - n2
        return self.result
    def divide(self, n1, n2):
        self.result = n1 / n2
        return self.result

cal = Calculator()
print(cal.sum(1,1))
print(cal.subtract(2,1))
print(cal.multiple(3,2))
print(cal.subtract(5,2))