n = int(input())
i = 1
j = 1
while i <= n:
    while j <= i:
        print(j, end='')
        j += 1
    print()
    j = 1
    i += 1
