#ex1:
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1  #skip 3 
#ex2:
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1 #skip even numbers and print odd numbers from 1 to 10
#ex3:
numbers = [-2, 3, -1, 5]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1   #skip negative numbers and print positive numbers from the list
#ex4:
while True:
    text = input("Введите текст: ")
    if text == "":
        continue
    print(text) #loop will continue if user input is empty string, otherwise it will print the input
#ex5:
i = 1
while i <= 10:
    if i <= 5:
        i += 1
        continue
    print(i)
    i += 1 #skip numbers from 1 to 5 and print numbers from 6 to 10 each in new line
    