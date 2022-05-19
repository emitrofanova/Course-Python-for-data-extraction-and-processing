def sort3(x, y, z):
    if x >= y and x >= z:
        if y >= z:
            return z, y, x
        else:
            return y, z, x
    elif y >= x and y >= z:
        if x >= z:
            return z, x, y
        else:
            return x, z, y
    elif z >= x and z >= y:
        if x >= y:
            return y, x, z
        else:
            return x, y, z

        
x = int(input())
y = int(input())
z = int(input())
print(' '.join(map(str, sort3(x, y, z))))
