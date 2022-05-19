number = input()
plus = '+'
a = number.count(plus)
if a == 0: 
    if len(number) == 9:
        print('+7', number, sep='')
    else:
        print('+7',number[1:],sep='')
else:
    print(number)
