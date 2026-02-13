#ex1:
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()

#ex2:
class Shape:
    def area(self):
        print("Calculating area")

class Square(Shape):
    def area(self):
        print("Square area")

#ex3:
class Animal:
    def speak(self):
        print("Sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Dog(Animal):
    def speak(self):
        print("Woof")

animals = [Cat(), Dog()]

for animal in animals:
    animal.speak()

#ex4:
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    pass

c = Child()
c.show()
