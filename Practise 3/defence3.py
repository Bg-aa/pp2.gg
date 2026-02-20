class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def intoduce(self):
        print(f"{self.name} {self.sound}")


class Dog(Animal):
    def __init__(self,name,sound,age):
        super().__init__(name,sound)
        self.age = age
    def introduce(self):
        print(f"{self.name} {self.sound} {self.age}")

class Cat(Animal):
    def __init__(self,name,sound,age):
        super().__init__(name,sound)
        self.age = age
    def intoduce(self):
        print(f"{self.name} {self.sound} {self.age}")


my_animal = Animal("Cow", "MOO")
my_animal.intoduce()
my_dog = Dog("Lesli", "RAW", 9)
my_dog.intoduce()
my_cat = Cat("Daryn", "MEOEW", 5)
my_cat.intoduce()
