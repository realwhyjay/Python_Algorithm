import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_numbers = [0] * N

for i in range(N):
    if i == 0:
        sum_numbers[i] = arr[i]
    else:
        sum_numbers[i] = sum_numbers[i-1] + arr[i]


for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(sum_numbers[j-1])
    else:
        print(sum_numbers[j-1]-sum_numbers[i-2])
