x = list(map(int, input().split()))
min = x[0]
max = x[0]
min_pos = 0
max_pos = 0
for i in range(len(x)):
    if x[i] < min:
        min = x[i]
        min_pos = i
    if x[i] > max:
        max = x[i]
        max_pos = i
x[min_pos] = max
x[max_pos] = min
print(' '.join(map(str,x)))
