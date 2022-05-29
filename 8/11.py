from bs4 import BeautifulSoup

xml = open('mapcity.osm', 'r', encoding='utf-8').read()
fout = open('11out.txt', 'w', encoding='utf-8')
soup = BeautifulSoup(xml, 'xml')
cnt = 0
for node in soup.find_all('node'):
    cnt += 1
    if cnt == 101:
        break
    print(node['id'], node['lat'], node['lon'], sep=' ', file=fout)
fout.close()
