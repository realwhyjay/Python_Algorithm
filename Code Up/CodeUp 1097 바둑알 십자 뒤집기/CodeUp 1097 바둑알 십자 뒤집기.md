# CodeUp 1097 : 바둑알 십자 뒤집기

#### Date : 21/02/07

#### Lang : Python

#### Question : [CodeUp 1097](https://www.codeup.kr/problem.php?id=1097)


## 답안 1

```python
ba = []

# 처음에 이중 리스트를 이용하여 20x20 사이즈의 바둑판을 만들어준다.
# 19x19 사이즈가 아닌 이유는, 주어진 문제에서 제일 첫번째 칸의 인덱스가 [0,0]이 아닌 [1,1]이기 때문에 나중에 편하게 이를 계산하기 위해서다
for i in range(20):
    ba.append([])
    for j in range(20):
        ba[i].append(0)

# 사용자에게 입력된 값을 바둑판에 입력한다.
for i in range(19):
        num = list(map(int, input().split()))
        for j in range(19):
            ba[i+1][j+1] = num[j]


count = int(input())

for i in range(count):
    a, b = map(int, input().split())
    for j in range(19):
      # 입력받은 값과 같은 열의 숫자를 바꿔준다.
        if ba[a][j+1] == 1:
            ba[a][j+1] = 0
        else:
          ba[a][j+1] = 1

      # 입력받은 값과 같은 행의 숫자를 바꿔준다.
        if ba[j+1][b] == 1:
            ba[j+1][b] = 0
        else:
            ba[j+1][b] = 1

# 바둑판 출력
for i in range(19):
    for j in range(19):
        print(ba[i+1][j+1], end=" ")
    print()

```

## 답안 2

```python

ba = []

# 처음에 0으로 가득찬 바둑판을 미리 만들어두는게 비효율적이라고 생각했다.입력하는대로 바둑판을 만들도록 해주었다.


# 이전의 경우는 0으로 가득찬 20x20 바둑판을 만든 뒤, 19x19 크기에 해당하는 값들을 입력받아 만들어둔 바둑판에 넣어주었던 것. 마지막 출력할 때는 0에 해당하는 행과 열을 빼주고 출력했다. 
# 이 경우에는 기존과는 달리 애초에 19x19 바둑판을 입력받으면서 만들게되니 index 값을 새로 계산해주어야했다.

for i in range(19):
    ba.append([int(num) for num in input().split()])

count = int(input())

for i in range(count):
    a, b = map(int, input().split())
    for j in range(19):
        if ba[a-1][j-1] == 1:
            ba[a-1][j-1] = 0
        else:
          ba[a-1][j-1] = 1

        if ba[j-1][b-1] == 1:
            ba[j-1][b-1] = 0
        else:
            ba[j-1][b-1] = 1

# 바둑판 출력
for i in range(19):
    for j in range(19):
        print(ba[i][j], end=" ")
    print()


```

