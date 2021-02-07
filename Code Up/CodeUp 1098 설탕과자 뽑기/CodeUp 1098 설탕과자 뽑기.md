# CodeUp 1098 : 설탕과자 뽑기

#### Date : 21/02/08

#### Lang : Python

#### Question : [CodeUp 1098](https://www.codeup.kr/problem.php?id=1098)


## 답안

```python

h,w = map(int,input().split())

# 0으로 이루어진 과자 판을 만든다.
# 이전에 바둑알 문제에서 했던 것과는 달리 입력값에 해당하는 크기의 이중 리스트를 바로 생성해준다.
sugar = [[0]*w for _ in range(h)]
        
n = int(input())

for i in range(n):
    l,d,x,y = map(int,input().split())
    # 가로로 놓을지 세로로 놓을지에 따라 조건을 나누어준다
    if d == 0: # 가로
      # 가로로 설탕과자를 놓는 경우에는 h는 고정시키고 w값만 바뀌어야하기에 주어진 길이만큼 for문을 돌리되, 그때마다 w값에 해당하는 y를 1씩 증가시켜주었다.
        for j in range(l):
            sugar[x-1][y-1] = 1
            y+=1
    else : # 세로
        for j in range(l):
            sugar[x-1][y-1] = 1
            x+=1

# 설탕과자 위치 출력
for i in range(h):
    for j in range(w):
        print(sugar[i][j], end=" ")
    print()

```

