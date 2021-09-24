import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

max = min(numbers)
for i in range(n):
    temp = numbers[i]

    for j in range(i, n):
        if i == j:
            if max < temp:
                max = temp
        else:
            temp += numbers[j]
            if max < temp:
                max = temp

print(max)
