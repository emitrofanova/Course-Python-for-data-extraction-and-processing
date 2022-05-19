def mykey(x):
    return x[1]
def mykey2(x):
    return x[0]

fin = open('3.txt', 'r', encoding='utf8')
fout = open('3out.txt', 'w', encoding='utf8')
dct = {}
fulltxt = []
for line in fin:
    string = line.split()
    fulltxt += string
for i in range(len(fulltxt)):
    if fulltxt[i] in dct:
        dct[fulltxt[i]] += 1
    else:
        dct[fulltxt[i]] = 1
answ = []
for key in dct:
    t = (dct[key], key)
    answ.append(t)
answ1 = sorted(answ, key=mykey)
answ2 = sorted(answ1, key=mykey2, reverse=True)
a = []
for i in range(len(answ2)):
    a.append(answ2[i][1])
print(*a, file=fout, end='')
fout.close()
fin.close()
