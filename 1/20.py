A = int(input())
B = int(input())
min = A * 60 + B
chas = min // 60
chas2 = chas % 24
min2 = min % 60
print(chas2, min2)
