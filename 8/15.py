from bs4 import BeautifulSoup
import math

def getsqr(coordlist):
    baselat = coordlist[0][0]
    baselon = coordlist[0][1]
    degreelen = 111300
    newcoord = []
    for now in coordlist:
        newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.sin(baselat)))
    sqr = 0
    for i in range(len(newcoord) - 1):
        sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
    sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
    return abs(sqr)

xml = open('mapcity.osm', 'r', encoding='utf-8').read()
fout = open('15out.txt', 'w', encoding='utf-8')
soup = BeautifulSoup(xml, 'xml')
cnt = 0
n = []
dct = {}
answ = []
max = 0

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
                if getsqr(answ) > max:
                    max = getsqr(answ)
                    a = way['id']
                print(getsqr(answ), file=fout)
    n = []
    answ = []
print(a)
fout.close()
