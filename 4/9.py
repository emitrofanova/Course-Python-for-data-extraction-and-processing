x = list(map(int, (input().split())))
y = x[::-1]
max = y[0]
num = 0
for i in range(len(y)):
    if y[i] >= max:
        max = y[i]
        num = i
print(max, len(y)-num-1)
