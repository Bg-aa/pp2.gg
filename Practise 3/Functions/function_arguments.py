#ex1:
def fun(fname):
  print(fname + " Refsnes")

fun("Emil")
fun("Tobias")
fun("Linus")
#ex2:
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

#ex3:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#ex4:
def func(name = "friend"):
  print("Hello", name)

func("Emil")
func("Tobias")
func()
func("Linus")

#ex5:
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")