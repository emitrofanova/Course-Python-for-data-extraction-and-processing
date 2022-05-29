from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

fin = open('18in.html', 'r', encoding='utf-8')
fout = open('18out.csv', 'w', encoding='utf-8')
s = BeautifulSoup(fin)
c = 0
l = ('td', 'th')
r = []
for i in s.find_all(attrs={"class":"wikitable collapsible collapsed"}):
    c += 1
    if c == 2:
        t = i
        for k in t.find_all('tr'):
            for j in k.find_all(l):
                rr = j.get_text()
                r.append(rr)
            print(','.join(r).strip(' '),end='', file=fout)
            r = []
        break
fin.close()
fout.close()
