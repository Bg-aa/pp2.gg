#ex1:
class Dog:
    species = "Animal"

dog1 = Dog()
dog2 = Dog()

print(dog1.species)
print(dog2.species)

#ex2:
class Dog:
    species = "Animal"

Dog.species = "Mammal"

dog1 = Dog()
print(dog1.species)

#ex3:
class User:
    count = 0

    def __init__(self):
        User.count += 1

u1 = User()
u2 = User()
print(User.count)   # 2

#ex4:
class Example:
    class_var = 10

    def __init__(self):
        self.instance_var = 20

obj = Example()

print(obj.class_var)      # 10
print(obj.instance_var)   # 20
