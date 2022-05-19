x = list(map(int,input().split()))
min = 10000
for i in range(len(x)):
    if x[i] < min and x[i] > 0:
        min = x[i]
print(min)
