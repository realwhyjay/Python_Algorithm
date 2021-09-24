import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

result_list = [numbers[0]]

for i in range(n-1):
    result_list.append(max(result_list[i]+numbers[i+1], numbers[i+1]))

print(max(result_list))
