#ex1:
s = ["apple", "kiwi", "banana"]
res = sorted(s, key=lambda x: len(x))
print(res)  # ['kiwi', 'apple', 'banana']

#ex2:
s = ["cat", "dog", "elephant"]
res = sorted(s, key=lambda x: x[-1])
print(res)

#ex3:
p = [(1, 5), (2, 3), (4, 1)]
res = sorted(p, key=lambda x: x[1])
print(res)  # [(4, 1), (2, 3), (1, 5)]

#ex4:
s = ["apple", "kiwi", "banana"]
res = sorted(s, key=lambda x: len(x), reverse=True)
print(res)  # ['banana', 'apple', 'kiwi']
