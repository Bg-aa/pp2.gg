fruits = ["apple", "banana", "cherry"]
prices = [100, 200, 300]

# enumerate — индексы и значения
for index, fruit in enumerate(fruits):
    print(index, fruit)

# zip — параллельная итерация по спискам
for fruit, price in zip(fruits, prices):
    print(f"The price of {fruit} is {price}")