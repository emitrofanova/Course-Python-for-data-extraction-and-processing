x = int(input())
max = x
i = 0
while x != 0:
    if x > max:
        max = x
        i = 0
    if x == max:
        i +=1
    x = int(input())
print(i)
