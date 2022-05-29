from bs4 import BeautifulSoup

xml = open('map2.osm', 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'xml')
cnt = 0
for way in soup.find_all('way'):
    cnt += 1
print(cnt)
