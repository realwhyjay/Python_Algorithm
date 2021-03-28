import sys
import heapq

n = int(input())
array = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        # 배열이 비어있는 경우에는 0을 출력한다
        if not array:
            print(0)
        # 배열이 비어있지 않은 경우에는 힙에서 가장 작은 원소를 삭제한 후 출력한다.
        else:
            print(heapq.heappop(array))
    # 입력된 값이 0이 아닐 경우에는 array에 원소를 추가한다.
    else:
        heapq.heappush(array, x)
