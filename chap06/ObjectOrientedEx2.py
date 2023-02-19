class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

        # OPERATIONS/Actions ---> Methods
    def bark(self, number):
        print('WOOF! My name is {} and the number is {}'.format(self.name,number))
my_dog = Dog(breed='Lab', name='mars', spots=False)
print(my_dog.breed , ' ' , my_dog.spots)
print(my_dog.species)
my_dog.bark(13)

class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius
        self.area = radius * radius * self.pi

    # Method
    def get_circumfrence(self):
        return self.radius * self.pi * 2
mycircle = Circle(6)
print(mycircle.get_circumfrence())
print(mycircle.area)