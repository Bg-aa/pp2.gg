#1
import math
degree = float(input())
radian = math.radians(degree)
print(radian) 

#2
import math
h = float(input())
a = float(input())
b = float(input())
area = (a+b) * h / 2
print(f"{area:.1f}") 

#3
import math
n = int(input())
a = float(input())
area = (n * a**2) / (4 * math.tan(math.pi / n))
print(f"{area:.1f}") 

#4
a = float(input())
h = float(input())
area = a * h
print(area)