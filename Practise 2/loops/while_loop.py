#ex1:
i = 1
while i < 6:
  print(i)
  i += 1 #print 1 2 3 4 5 each in new line
#ex2:
i = 2
while i <= 10:
    print(i)
    i += 2 #print 2 4 6 8 10 each in new line
#ex3:
i = 5
while i > 0:
    print(i)
    i -= 1 #print 5 4 3 2 1 each in new line
#ex4:
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print(total) #print 15
#ex5:
password = ""
while password != "1234":
    password = input("enter password: ")