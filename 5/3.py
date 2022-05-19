def mykey(list1):
    return list1[1]

n = int(input())
list1 = []
for i in range(n):
    s = tuple(map(str,input().split()))
    list1.append(s)
answ = sorted(list1, key=mykey)
for i in range(len(answ)):
    print(answ[i][0], answ[i][1], sep=' ')
