#ex1:
class A:
    def method_a(self):
        print("A")

class B:
    def method_b(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.method_a()
obj.method_b()

#ex2:
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()

#ex3:
print(C.__mro__)

#ex4:
class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        super().greet()
        print("B")

class C(B):
    def greet(self):
        super().greet()
        print("C")

obj = C()
obj.greet()
