from bs4 import BeautifulSoup

xml = open('map2.osm', 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'xml')
cnt = 0
dct = {}
for way in soup.find_all('way'):
    id = way['id']
    for node in way('nd'):
        if id not in dct:
            dct[id] = 0
        dct[id] += 1
answ = list(dct.items())
def mykey(x):
    return(-x[1],x[0])
answ.sort(key=mykey)
print(answ[0][0])
