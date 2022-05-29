import xmltodict

fin = open('3.osm', 'r', encoding='utf-8')
fout = open('3out.txt', 'w', encoding='utf-8')
dct = xmltodict.parse(fin.read())
for node in dct['osm']['node']:
    flag = False
    if 'tag' not in node:
        continue
    if 'tag' in node and isinstance(node['tag'], list):
        for tag in node['tag']:
            if tag['@k'] == 'shop':
                flag = True
                answLat = node['@lat']
                answLon = node['@lon']
    elif isinstance(node['tag'], dict):
        for i in node['tag']:
            if node['tag'][i] == 'shop':
                flag = True
                answLat = node['@lat']
                answLon = node['@lon']
    if flag:
        print('L.marker([' + answLat + ', ' + answLon + ']).addTo(mymap);', file=fout)
