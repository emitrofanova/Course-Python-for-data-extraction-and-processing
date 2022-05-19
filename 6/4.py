fin = open('4.txt', 'r', encoding='utf8')
text = fin.readlines()
l = len(text)
print()
for string in range(len(text)):
    print(text[l-string-1],end='')
fin.close()
