#ex1
footballers =["Messi", "Ronaldo","Barcola","Mbappe","Olise","Haaland"]
goals = [900,965,30,50,340]
for index,players in enumerate(footballers):
    print(index,players)

for footballer,goal in zip(footballers,goals):
    print(footballer,goal)
#ex2
x = "123"
y = 789
print(type(x))
print(isinstance(y,int))

x_int = int(x)
y_str = str(y)
print(x_int+y)
print(x+y_str)