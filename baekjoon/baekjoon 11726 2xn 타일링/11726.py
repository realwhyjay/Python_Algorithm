# n-2 + n-1

n = int(input())
result = [0, 1, 2]
for i in range(3, 1001):
    result.append(result[i-2]+result[i-1])
print(result[n] % 10007)
