class Line():
    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2
    def len(self):
        (a,b) = self.coordinate1
        (c,d) = self.coordinate2
        return (((c-a)**2) + ((d-b)**2)) ** 0.5

myline = Line((2,4),(3,9))
print(myline.len())

class Cylinder:
    pi = 3.14
    def __init__(self, radius = 1, height =1):
        self.radius = radius
        self.height = height
    def volume(self):
        return self.radius**2 * self.pi * self.height

    def surface_areas(self):
        return (self.radius * 2 * self.pi * self.height * 2) + (self.radius ** 2 * self.pi * 2)

mycyl = Cylinder(radius=3, height=3)
print(mycyl.volume())
print(mycyl.surface_areas())
