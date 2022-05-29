from bs4 import BeautifulSoup

xml = open('mapcity.osm', 'r', encoding='utf-8').read()
fout = open('14out.txt', 'w', encoding='utf-8')
soup = BeautifulSoup(xml, 'xml')
cnt = 0
n = []
dct = {}
answ = []

for node in soup.find_all('node'):
    dct[int(node['id'])] = (float(node['lat']), float(node['lon']))

for way in soup.find_all('way'):
    for nd in way('nd'):
        temp = int(nd['ref'])
        n.append(temp)
    if n[0] == n[len(n) - 1]:
        for tag in way('tag'):
            if tag['k'] == 'building':
                print(way['id'], file=fout)
                for i in n:
                    answ.append(dct[i])
                print(answ, file=fout)
    n = []
    answ = []
fout.close()
