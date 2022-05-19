x = list(map(int,input().split()))
c = 0
for i in range(1, len(x)-1):
    if x[i-1] < x[i] and x[i] > x[i+1]:
        c = c + 1
print(c)
