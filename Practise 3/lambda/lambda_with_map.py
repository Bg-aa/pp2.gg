#ex1:
n = [1, 2, 3, 4]
res = list(map(lambda x: x * 2, n))
print(res)  # [2, 4, 6, 8]

#ex2:
n = [1, 2, 3, 4]
res = list(map(lambda x: x ** 2, n))
print(res)  # [1, 4, 9, 16]

#ex3:
nums = ["1", "2", "3"]
result = list(map(lambda x: int(x), nums))
print(result)  # [1, 2, 3]

#ex4:
s = ["apple", "banana", "kiwi"]
result = list(map(lambda x: len(x), s))
print(result)  # [5, 6, 4]
