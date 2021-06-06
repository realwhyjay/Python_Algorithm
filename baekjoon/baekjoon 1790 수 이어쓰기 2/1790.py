N, K = map(int, input().split())

num = [i for i in range(1, N+1)]

result = ''.join(list(map(str, num)))

print(result[K])
