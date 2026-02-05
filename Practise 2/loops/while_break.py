#ex1:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1  #print 1 2 3 each in new line
#ex2:
i = 1
while i <= 10:
    if i == 7:
        print("Find 7")
        break
    i += 1  # i=7 iteration will print Find 7 and break the loop
#ex3:
while True:
    word = input("Введите слово: ")
    if word == "stop":
        break   #loop will break when user input is "stop"
#ex4:
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
        break
    i += 1 #print 2 and break the loop 
#ex5:
tries = 0
while tries < 3:
    password = input("Пароль: ")
    if password == "admin":
        break
    tries += 1   #loop will break if user input is "admin" or after 3 tries
