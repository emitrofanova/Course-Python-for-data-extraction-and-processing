n = int(input())
lan = set()
o = []
for i in range(n):
    num = int(input())
    for j in range(num):
        x = str(input())
        lan.add(x)
    o.append(lan)
    lan = set()    
answ2 = set.intersection(*o)
answ4 = set.union(*o)
answ1 = len(answ2)
answ3 = len(answ4)
print(answ1, *sorted(answ2), answ3, *sorted(answ4), sep='\n')
