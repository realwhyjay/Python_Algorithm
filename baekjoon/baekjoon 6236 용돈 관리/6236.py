n, m = map(int, input().split())
money = []

for _ in range(n):
    money.append(int(input()))

start = max(money)
end = sum(money)
result = sum(money)

while start <= end:
    mid = (start+end)//2
    count = 0
    sum = 0

    for i in money:
        sum += i
        if sum > mid:
            count += 1
            sum = i

    if sum > 0:
        count += 1

    if count > m:
        start = mid+1
    else:
        if mid < result:
            result = mid
        end = mid-1

print(result)
