N = int(input())
i = 0
dct = {}
answ = []
while i < N:
    s = list(input().split())
    dct[s[0]] = ''
    for element in s:
        if element == 'R':
            dct[s[0]] += 'read'
        if element == 'W':
            dct[s[0]] += 'write'
        if element == 'X':
            dct[s[0]] += 'execute'
    i += 1

M = int(input())
i = 0
while i < M:
    s = list(input().split())
    if s[0] in dct[s[1]]:
        answ.append(1)
    else:
        answ.append(0)
    i += 1

for element in answ:
    if element == 1:
        print('OK')
    else:
        print('Access denied')
