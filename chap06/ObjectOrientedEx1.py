mylist = [1,2,3]
myset = set()
print(type(mylist))
print(type(myset))

class SampleWord():
    pass

my_sample = SampleWord()
print(type(my_sample))
class Dog():

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots
my_dog = Dog(breed='Lab', name='mars', spots=False)
print(my_dog.breed , ' ' , my_dog.spots)

