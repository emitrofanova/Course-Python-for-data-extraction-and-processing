fin = open('5.txt', 'r', encoding='utf8')
fout = open('5out.txt', 'w', encoding='utf8')
c_lines = 0
c_letters = 0
c_words = 0
for line in fin:
    c_lines += 1
    for letter in line:
        if letter.isalpha() == False:
            line = line.replace(letter, " ")
        else:
            c_letters += 1
    c_words += len(line.split())
answ = 'Input file contains:\n' + str(c_letters) + ' letters\n' + str(c_words) + ' words\n' + str(c_lines) + ' lines'
print(answ, end='', file=fout)
fin.close()
fout.close()
