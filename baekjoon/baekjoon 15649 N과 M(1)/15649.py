from itertools import permutations

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]

result = list(permutations(num, m))

for k in result:
    for j in k:
        print(j, end=' ')
    print()
