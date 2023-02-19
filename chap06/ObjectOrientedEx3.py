class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")
myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        print("Dog Created")
        self.name = name

    # Override
    def who_am_i(self):
        print("I am a dog {}".format(self.name))
class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        print("Cat Created")
        self.name = name

    # Override
    def who_am_i(self):
        print("I am a cat {}".format(self.name))

niko = Dog('niko')
felix = Cat("felix")

for pet in [niko,felix]:
    print((type(pet)))
def pet_speak(pet):
    pet.who_am_i()

pet_speak(niko)
