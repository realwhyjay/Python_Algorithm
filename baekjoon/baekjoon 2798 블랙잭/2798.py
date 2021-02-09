N, M = map(int, input().split())
card = list(map(int, input().split()))
sum = 0
max = 0

for i in card:
    for j in card:
        for t in card:
            if i == j or i == t or j == t:
                continue
            else:
                sum = i + j + t
                if max < sum <= M:
                    max = sum

print(max)
