fin = open('7.txt', 'r', encoding='utf-8')
fout = open('7out.txt', 'w', encoding='utf-8')
text = fin.read()
text_rev = text[::-1]
print(text_rev, file = fout)
fin.close()
fout.close()
