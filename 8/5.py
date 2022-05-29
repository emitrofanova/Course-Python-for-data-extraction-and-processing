from bs4 import BeautifulSoup

xml = open('map2.osm', 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'xml')
cnt1 = 0
cnt2 = 0
for node in soup.find_all('node'):
    cnt1 += 1
    for tag in node('tag'):
        cnt2 += 1
        break
print(cnt1-cnt2, cnt2, sep=' ')
