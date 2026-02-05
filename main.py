n = int(input())
num = input().split()
mx = -10**9
index = 1
pos = 1
for x in num:
    x = int(x)
    if x > mx:
        mx = x
        index = pos 
    pos += 1
print(index)
