n = list(map(int,input().split()))
z = set()
for i in range(len(n)):
    if n[i] in z:
        print('YES')
    else:
        print('NO')
        z.add(n[i])
