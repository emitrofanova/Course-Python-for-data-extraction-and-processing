from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

answ = open('7in.html', 'r', encoding='utf-8')
fout = open('7out.txt', 'w', encoding='utf-8')
s = BeautifulSoup(answ)
for link in s.find_all('a'):
    if link.has_attr('href'):
        print(link['href'], file=fout)
answ.close()
fout.close()
