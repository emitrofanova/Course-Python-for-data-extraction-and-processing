fin1 = open('10_r.csv', 'r', encoding='utf-8')
fin2 = open('10_s.csv', 'r', encoding='utf-8')
fout = open('10out.txt', 'w', encoding='utf-8')
dct_r = {}
dct_s = {}
i = 0
for line in fin1:
    string = line.split(';')
    if string[0] in dct_r:
        dct_r[string[0]] += (string[1], string[2])
    else:
        dct_r[string[0]] = (string[1], string[2])
for line in fin2:
    string = line[:(len(line)-1)].replace(',', '.').split(';')
    i += 1
    if string[2] == '': string[2] = 0
    if string[3] == '': string[3] = 0
    if string[4] == '': string[4] = 0
    dct_s[i] = (string[0],string[1], string[2], string[3], string[4])
print(dct_r, file=fout)
print(dct_s, file=fout)
i = 0
sum_kkal = 0
sum_bel = 0
sum_zh = 0
sum_ugl = 0
for day in dct_r:
    prod_day = list(dct_r[day])
    i = 0
    for product in prod_day:
        if '\n' in product:
            continue
        else:
            for cal in dct_s:
                if product == dct_s[cal][0]:
                    gramms = int(prod_day[i+1])
                    kkals = float(dct_s[cal][1])
                    bel = float(dct_s[cal][2])
                    zh = float(dct_s[cal][3])
                    ugl = float(dct_s[cal][4])
                    sum_kkal += gramms * kkals
                    sum_bel += gramms * bel
                    sum_zh += gramms * zh
                    sum_ugl += gramms * ugl
                    i += 2
    if sum_kkal != 0:
        print(int(sum_kkal // 100), int(sum_bel // 100), int(sum_zh // 100), int(sum_ugl // 100))
    sum_kkal = 0
    sum_bel = 0
    sum_zh = 0
    sum_ugl = 0
fin1.close()
fin2.close()
fout.close()
