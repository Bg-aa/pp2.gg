#Varibles in Python
#ex1: Get the type
""" x = 5
print(type(x))"""  #this will show that x is of type int 
#ex2: Multiple varibles
x,y,z = "java","c++", "php"
print(x), print(y), print(z)

#ex3: Multiple varibles
x = y = z = "python"
print(x), print(y), print(z)

#ex4: Multiple varibles
x = "I"
y = "like"
z = "coding"
print(x, y, z)

#ex5: Global varibles
"""1)"""    
x = "awesome" #<=  this is global varible

def myfunc():
  print("Python is " + x)

myfunc()
 
"""2)""" 
x = "awesome" #<=  this is global varible

def myfunc():
  x = "fantastic"  #<=  this is local varible
  print("Python is " + x)  #<=  Python is fantastic

myfunc()

print("Python is " + x) #<=  Python is awesome 
 
# "global" - keyword if you want to change a global variable inside a function.
