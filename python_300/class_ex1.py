class Human:
    pass



class Human:
   def __init__(self):
       print("응애응애")
areum = Human()

class Human:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __str__(self):
        return self.name+ str(self.age)+ self.sex
    def who(self):
        print(f'나는 {self.name}이고 {self.age}살입니다')
areum = Human("아름",25,"female")
print(areum)
areum.who()

del areum
