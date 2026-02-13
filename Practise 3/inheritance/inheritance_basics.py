#ex1:
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()

#ex2
class Animal:
    def eat(self):
        print("Eating...")

class Cat(Animal):
    def meow(self):
        print("Meow!")

c = Cat()
c.eat()
c.meow()

#ex3:
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Bagdat")
print(s.name)

#ex4:
class A:
    def method_a(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.method_a()
