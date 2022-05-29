from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://raw.githubusercontent.com/psaleksandrova/HSE-OPENEDU-course/main/task_7_2_3.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', attrs = {'class' : 'wikitable sortable'})
cnt = 0
for tr in soup.find_all('tr'):
    cnt += 1
    for td in tr.find_all(['td', 'th']):
        cnt *= 2
print(cnt)
