n = int(input())
dct = {}
dctrev = {}
for i in range(n):
    n = list(map(str, input().split()))
    dct[n[0]] = n[1]
    dctrev[n[1]] = n[0]
word = str(input())
if word in dct:
    print(dct[word])
else:
    print(dctrev[word])
