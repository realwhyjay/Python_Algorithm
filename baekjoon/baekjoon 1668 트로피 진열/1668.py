num = int(input())
trophy = []


for _ in range(num):
    trophy.append(int(input()))


for i in range(len(trophy)):
    if i == 0:
        result = 1
        max = trophy[i]
    else:
        if trophy[i] > max:
            result += 1
            max = trophy[i]


print(result)

trophy.reverse()

for i in range(len(trophy)):
    if i == 0:
        result = 1
        max = trophy[i]
    else:
        if trophy[i] > max:
            result += 1
            max = trophy[i]

print(result)
