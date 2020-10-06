# inhertanice

class Animal():

    def __init__(self):
        print("Animal Created")

    def whoami(self):
        print("Animal")

    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print("woof")

    def eat(self):
        print("EATING")



mydog =  Dog()
mydog.whoami()
mydog.eat()
mydog.bark()


# special methods

class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return (f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed")

        
b = Book('pyhton','ajay',200)
print(b)
print(len(b))
del b
