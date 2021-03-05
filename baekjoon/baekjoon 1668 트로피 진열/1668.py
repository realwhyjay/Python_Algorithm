def trophy_count(trophys):
    result = 0
    for i in range(len(trophys)):
        if i == 0:
            result = 1
            max = trophys[i]
        else:
            if trophys[i] > max:
                result += 1
                max = trophys[i]
    return result


num = int(input())
trophy = []


for _ in range(num):
    trophy.append(int(input()))


print(trophy_count(trophy))

trophy.reverse()

print(trophy_count(trophy))
