def isPointInSquare(x,y):
    return ((x <= 1) and (x >= -1) and (y <= 1) and (y >= -1))


x = float(input())
y = float(input())
if isPointInSquare(x, y):
    print("YES")
else:
    print("NO")
