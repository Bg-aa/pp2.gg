def Powers(n):
    for i in range(n+1):
        yield 2 ** i
n = int(input())
for v in Powers(n):
    print(v, end=' ')