from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

fin = open('18in.html', 'r', encoding='utf-8')
fout = open('19out.csv', 'w', encoding='utf-8')
s = BeautifulSoup(fin)
c = 0
l = ('td', 'th')
r = []
for i in s.find_all(attrs={"class":"wikitable collapsible collapsed"}):
    c += 1
    if c < 4:
        t = i
        for k in t.find_all('tr'):
            for j in k.find_all(l):
                rr = j.get_text()
                if "\n" in rr and c == 1:
                    rr = rr.replace("\n","")
                r.append(rr)
            print(','.join(r),end='', file=fout)
            r = []
            if c == 1: print(file=fout)
        if c < 3: print(file=fout)
    else:
        break
fin.close()
fout.close()
