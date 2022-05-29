numbers = list(map(int, input().split()))

first = numbers[0]
answ = []
flag = False

for num in numbers[1:]:
    if (first < 0 and num < 0) or (first > 0 and num > 0):
        answ.append(first)
        answ.append(num)
        flag = True
        break
    first = num

if flag:
    print(*answ)
    