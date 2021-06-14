import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
result = [-1]*N

stack.append(0)
i = 1

while stack and i < N:
    while stack and A[stack[-1]] < A[i]:
        result[stack[-1]] = A[i]
        stack.pop()

    stack.append(i)
    i += 1

for i in result:
    print(i, end=' ')
