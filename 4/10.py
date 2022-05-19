x = list(map(int,input().split()))
num = x[0]
y = []
for i in range(len(x)-1):
    if x[i+1] > x[i]:
        y.append(x[i+1])
    num = x[i]
print(' '.join(map(str,y)))
