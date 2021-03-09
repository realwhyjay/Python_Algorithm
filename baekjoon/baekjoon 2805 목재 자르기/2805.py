n, m = map(int, input().split())

height = list(map(int, input().split()))

height.sort()
start = 1
end = height[-1]


while start <= end:
    mid = (start+end)//2
    result = 0

    for i in height:
        result += (i - mid)
        print(" i : {} mid : {} i % mid : {}".format(i, mid, i % mid))

    if result >= m:
        start = mid+1
        print("result 크다 : {}".format(result))

    else:
        end = mid-1
        print("result 작다 : {}".format(result))

print(start)
