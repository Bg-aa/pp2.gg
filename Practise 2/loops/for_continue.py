#ex1:
for i in range(1, 6):
    if i == 3:
        continue
    print(i) #skip 3
#ex2:
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i) #skip even numbers and print odd numbers from 1 to 10
#ex3:
numbers = [-1, 4, -3, 7]
for n in numbers:
    if n < 0:
        continue
    print(n)  #skip negative numbers and print positive numbers from the list
#ex4: 
text = "a b c"
for c in text:
    if c == " ":
        continue
    print(c) #skip spaces and print each character in new line
#ex5:
for i in range(1, 11):
    if i <= 5:
        continue
    print(i) #skip num 1 to 5 and print num 6 to 10 

