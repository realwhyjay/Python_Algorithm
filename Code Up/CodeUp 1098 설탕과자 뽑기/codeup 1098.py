
h, w = map(int, input().split())

sugar = [[0]*w for _ in range(h)]

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            sugar[x-1][y-1] = 1
            y += 1
    else:
        for j in range(l):
            sugar[x-1][y-1] = 1
            x += 1

for i in range(h):
    for j in range(w):
        print(sugar[i][j], end=" ")
    print()
