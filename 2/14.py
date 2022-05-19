N = int(input())
i = 0
while i <= N and 2**i <= N:
    print(2**i, end=' ')
    i += 1
