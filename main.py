with open("nums.txt", "w") as file:
    s = input()
    file.write(s)
with open("nums.txt", "r") as f:
    nums = list(map(int,f.read().split()))
with open("sum.txt", "w") as f:
    f.write(nums)
    print(sum(nums))