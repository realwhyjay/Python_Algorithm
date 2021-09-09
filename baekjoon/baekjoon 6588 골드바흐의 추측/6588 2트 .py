import sys
input = sys.stdin.readline
N = 1000000
# 에라토스테네스 체
check = [False, False]+[True]*(N-1)
for i in range(2, int((N+1)**0.5)+1):
    if check[i] == True:
        for j in range(2*i, N+1, i):
            check[j] = False

# 골드바흐 파티션 구하기
while True:
    n = int(input())
    if n == 0:
        break
    for i in range((n//2)+1):
        if (check[i] and check[n-i]):
            print("{} = {} + {}".format(n, i, n-i))
            break
