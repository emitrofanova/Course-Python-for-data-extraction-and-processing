n = int(input())
lan = set()
temp = set()
o = set()
lan1 = set()
for i in range(n):
    num = int(input())
    for j in range(num):
        x = input()
        lan.add(x)
        temp.add(x)
    if i == 0:
        lan1 = temp
    else:
        temp = temp & lan1
answ1 = len(o)
answ2 = sorted(o)
answ3 = len(lan)
answ4 = sorted(lan)
if n == 1:
    print(answ3, *answ4, answ3, *answ4, sep='\n')
else:
    print(answ1, *answ2, answ3, *answ4, sep='\n')
