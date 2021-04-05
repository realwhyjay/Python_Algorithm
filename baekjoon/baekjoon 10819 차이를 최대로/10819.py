from itertools import permutations

n = int(input())
lst = list(map(int, input().split()))
lst2 = list(permutations(lst, n))
result = []
ans = 0


for a in lst2:
    cnt = 0
    for i in range(n-1):
        cnt += abs(a[i]-a[(i+1)])
    ans = max(cnt, ans)

print(ans)
