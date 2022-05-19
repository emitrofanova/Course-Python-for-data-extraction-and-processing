string = input().split()
dct = {}
answ = []
for word in string:
    if word not in dct:
        dct[word] = 0
        answ.append(dct[word])
    else:
        dct[word] += 1
        answ.append(dct[word])
print(*answ)
