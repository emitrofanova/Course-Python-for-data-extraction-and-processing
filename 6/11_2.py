fin = open('11_1.csv', 'r', encoding='utf-8')
fout = open('11out.txt', 'w', encoding='utf-8')
cost = []
shops = []
for line in fin:
    string = line[:(len(line)-1)].split(';')
    if string[1] == 'Грибы-шибальцы':
        products = string
        continue
    shops = string[0:1]
    string = string[1:]
    for i in range(len(string)):
        cost.append((string[i], products[i+1], *shops))
print(sorted(cost)[0][1], sorted(cost)[0][2], file=fout)
fin.close()
fout.close()
