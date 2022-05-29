from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

fin = open('9in.html', 'r', encoding='utf-8')
dct = {}
s = BeautifulSoup(fin)
for code in s.find_all('code'):
    words = code.get_text()
    if words not in dct:
        dct[words] = 1
    else:
        dct[words] += 1
    w = words
max = dct[w]
for words in dct:
    if dct[words] >= max:
        max = dct[words]
for words in dct:
    if dct[words] == max:
        print(words, end=' ')
fin.close()
