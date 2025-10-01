# KH For Loops notes 2nd

nums = [12,4,4,653,6,]

for num in nums:
    div = num/2
    if div > 100:
        print(f"{div} is half of {num}. And it is still a large number!")
    else:
        print(num)

print("We completed all numbers!")

for x in range(1,10):
    print(x)

print("new list")

for x in range(2,11,2):
    print(x)

for x in range(10,0):
    print(x)