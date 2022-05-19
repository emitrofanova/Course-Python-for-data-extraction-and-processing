p = int(input())
x = int(input())
y = int(input())
vklad = x * 100 + y
year = vklad * ((100 + p)/ 100)
rub = (year / 100) - (year / 100) % 1
kop = year % 100
print(int(rub), int(round(kop,2)))
