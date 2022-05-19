fin = open('6.txt', 'r', encoding='utf-8')
fout = open('6out.txt', 'w', encoding='utf-8')
text = fin.readlines()
max_len_string = max(list(map(len, text)))
for line in text:
    if len(line) == max_len_string:
        print(line, end='', file = fout)
fin.close()
fout.close()
