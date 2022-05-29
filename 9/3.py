import json

fin = open('data_3.json', 'r', encoding='utf-8').read()
lst = json.loads(fin)
cnt = 0
for i in lst:
    time1 = i['OnTime']
    hours1 = int(time1[0:2])
    min1 = int(time1[3:5])
    time2 = i['OffTime']
    hours2 = int(time2[0:2])
    min2 = int(time2[3:5])
    if ((1440 - (hours1 * 60 + min1)) + (hours2 * 60 + min2)) >= 720:
        cnt += 1
print(cnt)
