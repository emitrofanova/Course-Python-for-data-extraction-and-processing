n = int(input())
dct = {}
dctrev = {}
zapros = []
for i in range(n):
    x = tuple(input().split())
    dct[x[0]] = x[1:]
for country in dct:
    for city in dct[country]:
        dctrev[city] = country
m = int(input())
for i in range(m):
    zapros.append(input())
for i in zapros:
    print(dctrev[i])
    