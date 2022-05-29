coord = list(map(float, input().split()))
cnt = int(input())
lan = (coord[2]-coord[0]) / cnt
lon = (coord[3]-coord[1]) / cnt
nnlanmax = coord[0] + lan
nnlonmax = coord[1] + lon
for i in range(cnt):
    nlanmin = coord[0] + i * lan
    nlanmax = nnlanmax + i * lan
    for j in range(cnt):
        nlonmin = coord[1] + j * lon
        nlonmax = nnlonmax + j * lon
        print(nlanmin, nlonmin, nlanmax, nlonmax, sep=' ')
