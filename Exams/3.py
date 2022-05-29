s = input()
inv_s = s[::-1]
cnt1 = 0
cnt2 = 0
for element in s:
    if element == 'h':
        break
    cnt1 += 1

for element in inv_s:
    if element == 'h':
        break
    cnt2 += 1

print(s[:cnt1] + inv_s[cnt2:(len(s)-cnt1)] + s[len(s)-cnt2:])
