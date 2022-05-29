from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

fin = open('15in.html', 'r', encoding='utf-8')
s = BeautifulSoup(fin)
n = 0
for num in s.find_all('td'):
    n += int(num.get_text())
print(n)
fin.close()
