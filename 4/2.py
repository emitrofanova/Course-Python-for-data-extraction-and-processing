N = int(input())
i = 0
st = 10**N
q = N-1
end = 10**q
for i in range(1, st-end+1, 2):
    print(st-i, end=' ')
