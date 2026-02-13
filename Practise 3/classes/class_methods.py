#ex1:
class Student:
    def greet(self):
        print("Hello!")

s1 = Student()
s1.greet()

#ex2:
class Student:
    def greet(self, name):
        print(f"Hello, {name}!")

s1 = Student()
s1.greet("Bagdat")

#ex3:
class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

c = Counter()
c.increase()
print(c.count)

#ex4:
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def show_balance(self):
        print(self.balance)
acc = BankAccount(100)
acc.deposit(50)
acc.show_balance()