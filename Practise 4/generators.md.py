#1
def squares(N):
    for i in range(N+1):
        yield i ** 2
N = int(input())
for x in squares(N):
    print(x, end = ' ') 

#2
def eva(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
n = int(input())
for x in eva(n):
    print(x, end = " ") 

#3
def divisors(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for x in divisors(n):
    print(x, end = " ")

#4
def squares(a,b):
    for i in range(a,b+1):
        yield i ** 2
a, b = map(int, input().split())
for x in squares(a,b):
    print(x, end = " ")

#5
def reverse(n):
    for i in range(n,-1,-1):
        yield i
n = int(input())
for x in reverse(n):
    print(x, end = " ")
