# 백준 11576 : Base Conversion

#### Date : 21/09/08

#### Lang : Python

#### Question : [백준 11576](https://www.acmicpc.net/problem/11576)

## 최종 답안 

```python
A, B = map(int, input().split())
m = int(input())
before = list(map(int, input().split()))
temp = 0
after = []
before = before[::-1]

# 입력받은 값을 10진수로 변환해준다. 
for i in range(m):
    temp += before[i]*(A**i)

# 10진수로 변환한 값을 B 진수로 바꾸어준다.
# B로 나눈 나머지를 차례로 after에 append 해주고
while (temp != 0):
    after.append(temp % B)
    temp //= B

# 이를 뒤집어 정답을 출력한다.
after = after[::-1]
for i in after:
    print(i, end=" ")

```

