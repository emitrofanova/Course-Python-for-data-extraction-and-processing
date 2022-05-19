n = int(input())
q = []
for i in range(n):
    x = str(input())
    q.append(x)
answ = sorted(q)
print(*answ, sep='\n')
