str = input()
subs = "f"
cnt = str.count(subs)
pos = str.find(subs)
if cnt == 1:
    print(str.find(subs))
elif cnt > 1:
    print(str.find(subs), str.rfind(subs))
else:
    print
