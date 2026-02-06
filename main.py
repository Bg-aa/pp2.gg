n = int(input())
num = map(int,input().split())
s = set()
for x in num:
        if x in s:
            print("NO")
        else:
            print("YES")
            s.add(x)