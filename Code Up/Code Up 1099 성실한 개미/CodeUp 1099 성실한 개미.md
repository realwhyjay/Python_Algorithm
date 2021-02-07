# CodeUp 1099 : 성실한 개미

#### Date : 21/02/08

#### Lang : Python

#### Question : [CodeUp 1099](https://www.codeup.kr/problem.php?id=1099)


## 답안

```python
maze = []

# 입력값을 이중리스트로 저장해 미로를 생성해준다.
for i in range(10):
    maze.append(list(map(int, input().split())))

# 시작점 세팅
a = 1
b = 1

# 무한루프를 돌다가 일정 조건을 만났을 때만 break해도록 해주었다.
while True:
  	# 애초에 벽에 닿을일이(maza[a][b] == 1) 없게 만들어서 조건에서 제외했다.
  	# 먹이에 도착한 경우
    if maze[a][b] == 2: 
        maze[a][b]=9
        break
    # 먹이가 없는 경우
    elif maze[a][b] == 0:
        maze[a][b] = 9
    
    # 다음 진행 방향이 벽에 막혀 있는 경우나, 한쪽 끝에 도달해 더이상 갈 수가 없는 경우에 break 해준다.
    # 처음에 이 부분을 까먹어서 시간초과가 났다.
    # 주어진 예시에는 오른쪽과 아래쪽이 전부 다 막히는 일이 없어서 (maze[a][b+1] == 1 and maze[a+1][b] == 1)는 빼줘도 되지 않을까 싶었는데, 왜인지 똑같이 시간오류가 났다. 이유를 모르겠다.
    
    if (maze[a][b+1] == 1 and maze[a+1][b] == 1) or (a == 9 and b == 9):
        break
    
    # 오른쪽으로 갈 수 있는 경우에는 해당 index 값을 ++ 해주었다
    if maze[a][b+1] != 1:
            b+=1
    # 오른쪽으로 갈 수 없는 경우에는 아래로 이동하도록 하였다.
    elif maze[a+1][b] !=1:
            a+=1
    
# 미로 프린트    
for i in range(10):
    for j in range(10):
        print(maze[i][j], end=" ")
    print()
```

