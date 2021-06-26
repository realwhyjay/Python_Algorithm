N = int(input())

num = [i for i in range(1, N+1)]

result = ''.join(list(map(str, num)))

print(len(result))
