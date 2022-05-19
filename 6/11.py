fin = open('11_1.csv', 'r', encoding='utf-8')
fout = open('11out.txt', 'w', encoding='utf-8')
mini = []
coord = []
shops = []
i = -1
for line in fin:
    i += 1
    string = line[:(len(line)-1)].split(';')
    if string[1] == 'Грибы-шибальцы':
        products = string
        continue
    shops += string[0:1]
    string = string[1:]
    string = list(map(int,string))
    mini.append(min(string))
    coord.append(i-1)
    coord.append(string.index(mini[i-1]))
mini2 = min(mini)
i = 0
answ = []
for element in mini:
    if element == mini2:
        answ.append((products[coord[i*2+1]+1], shops[coord[i*2]]))
    i += 1
print(*min(answ), file=fout)
fin.close()
fout.close()
