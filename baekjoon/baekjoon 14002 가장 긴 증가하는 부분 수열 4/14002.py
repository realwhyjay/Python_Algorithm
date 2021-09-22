n = int(input())
a = list(map(int, input().split()))

dp = [1]*n
result = []

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)


# for i in range(len(dp)):
#     if i == 0:
#         result.append(a[i])
#         temp = dp[i]
#     elif dp[i] > temp:
#         temp = dp[i]
#         result.append(a[i])

# print(max(dp))
# for i in result:
#     print(i, end=' ')

value = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == value:
        result.append(a[i])
        value -= 1

print(max(dp))
for i in reversed(result):
    print(i, end=' ')
