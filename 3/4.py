import math
x = float(input())
if abs((x % 1) - 0.5) < 0.0000001 or x % 1 > 0.5:
    print(math.ceil(x))
else:
    print(int(x))
