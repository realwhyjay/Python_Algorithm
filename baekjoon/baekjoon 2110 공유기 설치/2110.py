n, c = map(int, input().split())
house = []

for _ in range(n):
    x = int(input())
    house.append(x)

house.sort()

# 가장 낮은 좌표와 그 다음으로 낮은 좌표의 차이
start = house[1] - house[0]
# 가장 높은 좌표와 가장 낮은 좌표의 차이
end = house[-1] - house[0]

result = 0

while (start <= end):
    # 가장 인접한 두 공유기 사이의 최대 거리를 찾기위해 만든 변수.
    # 중간 값부터 탐색한다.
    mid = (start+end)//2
    value = house[0]
    count = 1

    # 현재의 mid 값을 이용해 공유기를 설치 해본다
    for i in range(1, len(house)):
        if house[i] >= value+mid:
            count += 1
            value = house[i]

    if count >= c:
     # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시킨다.
        start = mid + 1
        result = mid
        # 최적의 결과를 저장한다.
    else:
        # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소시킨다.
        end = mid - 1

print(result)
