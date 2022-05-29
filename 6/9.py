fin = open('9in.csv', 'r', encoding='utf-8')
fout = open('9out.csv', 'w', encoding='utf-8')

for line in fin:
    string = list(line.split(';'))
    l = (string[1][0:(len(string[1])-1)], string[0])
    print(';'.join(l), file=fout)

fin.close()
fout.close()
