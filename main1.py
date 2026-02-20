n = int(input())
mydict = {}
count = 0
for i in range(n):
    m=input()
    if not m in mydict:
        mydict[m]=1
    else:
        mydict[m]+=1
for i in mydict:
    if mydict[i] == 3:
        count+=1
print(count)