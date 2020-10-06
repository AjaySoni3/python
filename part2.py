class Dog():

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog(breed = "lab",name = "sammy")
otherdog = Dog(breed= "huskie", name = "manish")
print(mydog.breed)
print(mydog.name)
print(otherdog.breed)
print(otherdog.name)

class Circle():

    pi= 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius* self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r

myc = Circle(4)
myc.set_radius(100)
print(myc.area())
