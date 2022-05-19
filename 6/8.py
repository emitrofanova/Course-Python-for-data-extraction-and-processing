fin = open('input_6_3_1.csv', 'r', encoding='utf-8')
fout = open('8out.txt', 'w', encoding='utf-8')
dct = {}
for line in fin:
    string = list(line.split(';'))
    if string[0] in dct:
        dct[string[0]][0] += int(string[1])
        dct[string[0]][1] += 1
    else:
        dct[string[0]] = [int(string[1]),1]
list = []
for company in dct:
    list.append(((dct[company][0] / dct[company][1]), company))
answ = []
for i in sorted(list):
    answ.append(i[1])
print(*answ,  sep='\n', file=fout)
fin.close()
fout.close()
