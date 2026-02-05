#ex1:
for i in range(1, 10):
    if i == 4:
        break
    print(i) #print 1 2 3 each in new line
#ex2:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break #print apple banana each in new line
#ex3:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #print apple each in new line
#ex4:
numbers = [1, 3, 7, 8, 9]
for n in numbers:
    if n % 2 == 0:
        print(n)
        break #print 8 and break the loop
#ex5:
word = "python"
for ch in word:
    if ch == "h":
        print("Find h")
        break