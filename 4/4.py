N = int(input())
i = 0
answ = 1
answ2 = 1
for i in range(2,N+1):
    answ = answ * i
    answ2 = answ + answ2
print(answ2)
