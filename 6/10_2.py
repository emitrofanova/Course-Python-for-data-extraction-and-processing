raskladka = open('10_r.csv', 'r', encoding='utf-8')
spravka = open('10_s.csv', 'r', encoding='utf-8')
fout = open('10out.txt', 'w', encoding='utf-8')
dct_spravka = {}
dct_result = {}

for line in spravka:
    string = line[:(len(line)-1)].replace(',', '.').split(';')
    if string[1] == 'ККал на 100':
        continue
    for i in range(1, len(string)):
        if string[i] == '':
            string[i] = 0
    dct_spravka[string[0]] = list(map(float,string[1:len(string)]))
spravka.close()

for line in raskladka:
    string = line[:len(line)-1].split(';')
    if string[1] == 'Продукт':
        continue
    if string[0] not in dct_result:
        dct_result[string[0]] = []
        for element in dct_spravka[string[1]]:
            dct_result[string[0]].append(element*int(string[2]) / 100)
    else:
        for i in range(len(dct_result[string[0]])):
            dct_result[string[0]][i] += dct_spravka[string[1]][i] * int(string[2]) / 100
for element in dct_result:
    print(*map(int,dct_result[element]), file= fout)
raskladka.close()
fout.close()
