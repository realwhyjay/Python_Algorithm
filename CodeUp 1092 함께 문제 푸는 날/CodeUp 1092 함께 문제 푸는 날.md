# CodeUp 1092 : 함께 문제 푸는 날

#### Date : 21/02/06

#### Lang : Python

#### Question : [CodeUp 1092](https://www.codeup.kr/problem.php?id=1092)


## 답안 1

```python
# 최소공배수를 구하면 되는 문제라서 함수를 만들어 풀었다.

# 주어진 수를 입력받고
a,b,c = map(int,input().split())

# 최대 공약수를 만드는 재귀함수 만들어준다.
def GCD(a,b):
    if b == 0:
        return a
    else :
        return GCD(b,a%b)

# GCD()를 바탕으로 최소공배수를 만들어주는 함수를 만들어주었다.
def LCM(a,b):
    return(a*b/GCD(a,b))

# 이러면 끝!
print(int(LCM(a,LCM(b,c))))
```

## 답안 2

```python
# 아니 라이브러리를 쓸 생각을 못했네 아오
# 재현이가 어떻게 풀었는지 봤다가 라이브러리로 최대공약수를 구하는 함수가 있는걸 보고 적용해보았다.
from math import gcd
a,b,c = map(int,input().split())
        
def LCM(a,b):
    return(a*b/gcd(a,b))
    
print(int(LCM(a,LCM(b,c))))
```



## 답안 3

```python
# 문제에 있는 힌트를 보고 풀었다.
# 코드도 훨씬 짧고 직관적이다... 홀리몰리....
# 애초에 최소공배수를 구할 필요 없이, 무한루프를 돌리고 조건이 맞을때 break 하는 방식
a,b,c = map(int,input().split())
day = 1

while True:
    if day%a != 0 or day%b != 0 or day%c != 0:
        day+=1
    else :
        print(day)
        break
```

