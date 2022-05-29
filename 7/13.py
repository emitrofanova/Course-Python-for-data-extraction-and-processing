from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def getnum_links(url):
    fin = open(url, 'r', encoding='utf-8')
    s = BeautifulSoup(fin)
    answ_s = set()
    for link in s.find_all('a'):
        if link.has_attr('href'):
            l = link['href']
            if (':' not in l) and (not(l.startswith('#'))) and (not(l.startswith('//'))) and (not(l.startswith('http://'))) and (not(l.startswith('https://'))):
                answ_s.add(l)
    fin.close()
    return answ_s

fout = open('13out.txt', 'w', encoding='utf-8')
answ = sorted(getnum_links('11_1in.html') & getnum_links('11_2in.html'))
print(*answ, sep='\n', file=fout)
fout.close()
