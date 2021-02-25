num = int(input())
ans = []

for _ in range(num):
    data = list(map(int, input().split()))
    ans.append(data)

ans = sorted(ans, key=lambda x: (x[0], x[1]))

for i in ans:
    print(i[0], i[1])
