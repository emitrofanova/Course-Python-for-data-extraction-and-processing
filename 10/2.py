import xmltodict

fin = open('2.osm', 'r', encoding='utf-8')
fout = open('2out.txt', 'w', encoding='utf-8')
dct = xmltodict.parse(fin.read())
answ = 0
for node in dct['osm']['node']:
    flag = False
    if 'tag' not in node:
        continue
    if 'tag' in node and isinstance(node['tag'], list):
        for tag in node['tag']:
            if tag['@k'] == 'shop':
                flag = True
    elif isinstance(node['tag'], dict):
        for i in node['tag']:
            if node['tag'][i] == 'shop':
                flag = True
    if flag:
        answ += 1
print(answ, file=fout)
