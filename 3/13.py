x = input()
subx = 'h'
cnt = x.count(subx)
t = cnt - 1
y = x.replace('h','H', t)
answ = y.replace('H','h',1)
print(answ)
