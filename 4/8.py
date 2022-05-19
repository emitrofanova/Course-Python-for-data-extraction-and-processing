x = list(map(int, (input().split())))
y = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        y.append(x[i])
print(' '.join(map(str,y)))
