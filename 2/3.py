X = int(input())
otd = (((X-1) % 3) == 2 or ((X-1) % 3) == 1)
print(not(otd))
