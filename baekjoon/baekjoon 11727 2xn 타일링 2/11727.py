# n - 가짓수
# 0 - 0
# 1 - 1
# 2 - 3
# 3 - 5
# 4 - 11
# 5 - 21
# n = (n-2)*2 + (n-1)

n = int(input())
result = [0, 1, 3]
for i in range(3, 1001):
    result.append(result[i-2]*2+result[i-1])
print(result[n] % 10007)
