fin = open('2.txt', 'r', encoding='utf8')
s = 0
sumstring = []
for line in fin:
    s = sum(map(int, line.split()))
    sumstring.append(s)
fin.close()
print(*sumstring)
