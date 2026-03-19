#ex1
n = int(input())
listt = list(map(int,input().split()))
res = map(lambda x: x**3,listt)
print(list(res))

filt = list(filter(lambda x: x % 2 ==0, listt))
print(filt)

#ex2
from functools import reduce
n = int(input())
listt = list(map(int,input().split()))
sums = reduce(lambda x,y: x+y,listt)
print(sums)
prod = reduce(lambda a,b: a*b, listt)
print(prod)