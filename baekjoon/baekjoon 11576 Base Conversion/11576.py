A, B = map(int, input().split())
m = int(input())
before = list(map(int, input().split()))
temp = 0
after = []
before = before[::-1]

for i in range(m):
    temp += before[i]*(A**i)


while (temp != 0):
    after.append(temp % B)
    temp //= B

after = after[::-1]
for i in after:
    print(i, end=" ")
