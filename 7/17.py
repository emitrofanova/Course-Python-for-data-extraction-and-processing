from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

fin = open('17in.html', 'r', encoding='utf-8')
fout = open('17out.html', 'w', encoding='utf-8')
s = BeautifulSoup(fin)
c = 0
for i in s.find_all(attrs={"class":"wikitable collapsible collapsed"}):
    c += 1
    if c == 2:
        print(i, file=fout)
        break
fin.close()
fout.close()
