x = set(map(int, input().split()))
y = set(map(int, input().split()))
set = x & y
set = sorted(set)
print(*set)
