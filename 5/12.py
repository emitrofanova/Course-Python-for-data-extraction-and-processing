string = input().split()
dct = {}
answ = []
max = -1
for word in string:
    if word not in dct:
        dct[word] = 0
    else:
        dct[word] += 1
for word in sorted(dct):
    if dct[word] > max:
        answ = word
        max = dct[word]
print(answ)
