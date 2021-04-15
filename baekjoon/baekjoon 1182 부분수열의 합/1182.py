from itertools import combinations

n, s = map(int, input().split())
lis = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
    comb = list(combinations(lis, i))
    for j in comb:
        if sum(j) == s:
            count += 1

print(count)
