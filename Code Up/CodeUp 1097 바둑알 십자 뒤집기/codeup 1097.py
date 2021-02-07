
ba = []

for i in range(20):
    ba.append([])
    for j in range(20):
        ba[i].append(0)

for i in range(19):
    num = list(map(int, input().split()))
    for j in range(19):
        ba[i+1][j+1] = num[j]


count = int(input())

for i in range(count):
    a, b = map(int, input().split())
    for j in range(19):
        if ba[a][j+1] == 1:
            ba[a][j+1] = 0
        else:
            ba[a][j+1] = 1

        if ba[j+1][b] == 1:
            ba[j+1][b] = 0
        else:
            ba[j+1][b] = 1


for i in range(19):
    for j in range(19):
        print(ba[i+1][j+1], end=" ")
    print()
