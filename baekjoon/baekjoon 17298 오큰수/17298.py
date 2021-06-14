import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.append(A[-1])
for i in range(N):
    for j in range(i, N+1):
        #print("count i : {} j : {}".format(i, j))
        if A[i] < A[j]:
            print(A[j], end=' ')
            break
        # elif A[i] >= A[-1] and j == N:
        elif j == N:
            print(-1, end=' ')
