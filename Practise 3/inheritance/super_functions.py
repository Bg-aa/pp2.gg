#ex1:
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Alex", 10)
print(s.name, s.grade)

#ex2:
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")

d = Dog()
d.speak()

#ex3:
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")

obj = B()
obj.greet()

#ex4:
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        super().show()
        print("Child")

c = Child()
c.show()
