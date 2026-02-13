#ex1:
n = [1, 2, 3, 4, 5, 6]
res = list(filter(lambda x: x % 2 == 0, n))
print(res)  # [2, 4, 6]

#ex2:
n = [5, 12, 7, 20, 3]
res = list(filter(lambda x: x > 10, n))
print(res)  # [12, 20]

#ex3:
s = ["cat", "elephant", "dog", "tiger"]
res = list(filter(lambda x: len(x) > 4, s))
print(res)  # ['elephant', 'tiger']

#ex4:
num = [-3, 5, -1, 7, -9]
res = list(filter(lambda x: x > 0, num))
print(res)  # [5, 7]
