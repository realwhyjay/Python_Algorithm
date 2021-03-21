N, M = map(int, input().split())
lesson = list(map(int, input().split()))

start = max(lesson)
end = sum(lesson)

while start <= end:
    mid = (start + end)//2
    time = 0
    count = 1

    for i in lesson:
        if time+1 >= mid:
            time = 0
            count += 1
        time += i

    if time:
        count += 1

    if count > M:
        start = mid+1
    else:
        end = mid-1

print(start)
