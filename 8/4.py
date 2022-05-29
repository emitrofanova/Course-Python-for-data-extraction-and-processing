from bs4 import BeautifulSoup

xml = open('map2.osm', 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'xml')
cnt = 0
for node in soup.find_all('node'):
    cnt += 1
print(cnt)
