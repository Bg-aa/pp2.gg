#ex1: Slicin strings
s = "Happy code"
print(s[1:5]) # output: appy

#ex2: Slice From the Start
print(s[:5]) # output: Happy
# Slice To the End
print(s[5:]) # output:  code
#Negative Indexing
print(s[-5:-1]) # output: cod

#ex3: Concatenate Strings
a = "Hello"
b = "World"
c = a + b
print(c) # output: HelloWorld

#ex4: Modify Strings
a = " dog "
print(a.upper()) # output: DOG
print(a.lower()) # output: dog
print(a.strip()) # output: dog
print(a.replace("d", "b")) # output: bog
print(a.split(",")) # output:'dog'

#ex5: Format Strings
n = "Bagdat"
age = 18
print(f"My name is {n} I'm {age} years old.")  # output: My name is Bagdat I'm 18 years old.