from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def getnum_links(url):
    fin = open(url, 'r', encoding='utf-8')
    s = BeautifulSoup(fin)
    answ_s = []
    for link in s.find_all('a'):
        if link.has_attr('href'):
            l = link['href']
            if (':' not in l) and (not(l.startswith('#'))) and (not(l.startswith('//'))) and (not(l.startswith('http://'))) and (not(l.startswith('https://'))):
                answ_s.append(l)
    fin.close()
    return len(answ_s)

print(getnum_links('11_1in.html'),getnum_links('11_2in.html'), sep=' ')
