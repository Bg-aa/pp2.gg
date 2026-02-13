#ex1:
class Dog:
    pass
dog1 = Dog()
print(type(dog1))

#ex2:
class Dog:
    species = "Animal"
dog1 = Dog()
print(dog1.species)   # Animal

#ex3:
class Dog:
    def bark(self):
        print("Woof!")
dog1 = Dog()
dog1.bark()

#ex4:
class Cat:
    def meow(self):
        print("Meow!")
cat1 = Cat()
cat2 = Cat()
cat1.meow()
cat2.meow()
