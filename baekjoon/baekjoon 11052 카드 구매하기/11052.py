n = int(input())
cost = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

# 기본 카드의 값을 전부 dp에 넣어준다.
for i in range(n+1):
    dp[i] = cost[i]

# 각 카드별로, 최대 가격을 구해준다.
# n이 4일 경우, 4가 될 수 있는 경우의 수는
# 0 4, 1 3 , 2 2 이다.
# 이를 점화식으로 나타내면
# dp[j]+dp[i-j]와 같다.
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j])

print(dp[n])
