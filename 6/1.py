fin = open('1.txt', 'r', encoding='utf8')
cnt = 0
words = len(set(fin.readline().split()))

#s = sum(map(int, fin.readline().split()))
#s1 = sum(map(int, fin.readline().split()))
fin.close()
print(words)
