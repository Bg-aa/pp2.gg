#ex1:
class Person:
    def __init__(self, name):
        self.name = name
p1 = Person("Alex")
print(p1.name)

#ex2:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Tom", 20)
print(p1.name, p1.age)

#ex3:
class Car:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):
        print(f"{self.brand} is driving")
car1 = Car("BMW")
car1.drive()

#ex4:
class User:
    def __init__(self, name, country="Kazakhstan"):
        self.name = name
        self.country = country

u1 = User("Bagdat")
print(u1.country)
