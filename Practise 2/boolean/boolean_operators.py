#ex1:
x = 5
print(x > 3 and x < 10)    # returns True because 5 is greater than 3 AND 5 is less than 10

#ex2:
x = 5
print(x > 3 or x < 4)       # returns True because one of the conditions are true

#ex3:
x = 5
print(not(x > 3 and x < 10))    # returns False because not is used to reverse the result

#ex4:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)   # returns True because z is the same object as x
print(x is y) #returns False because x is not the same object as y, even if they have the same content'
print(x == y) # returns True because x is equal to y

print(x is not y)  # returns True because x is not the same object as y
print(x is not z)  # returns False because z is the same object as x
print(x != y)     # returns False because x is equal to y
#ex5:
x = ["apple", "banana"]

print("banana" in x) # returns True because "banana" is present in the list
print("cherry" in x) # returns False because "cherry" is not present in the list

