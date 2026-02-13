#ex1:
add = lambda a, b: a + b
print(add(3, 5))   # 8

#ex2:
square = lambda x: x ** 2

print(square(4))   # 16

#ex3:
is_even = lambda x: x % 2 == 0

print(is_even(6))  # True
print(is_even(7))  # False

#ex4:
max_num = lambda a, b: a if a > b else b

print(max_num(10, 7))  # 10
