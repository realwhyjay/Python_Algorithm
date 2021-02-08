maze = []

for i in range(10):
    maze[i].append(list(map(int, input().split())))

a = 1
b = 1

while True:
    if maze[a][b] == 0:
        maze[a][b] = 9
        if maze[a][b+1] == 0:
            b+=1
        else:
            a+=1
    else:
        maze[a][b]=9
        break
    
for i in range(10):
    for j in range(10):
        print(maze[i][j], end=" ")
    print()