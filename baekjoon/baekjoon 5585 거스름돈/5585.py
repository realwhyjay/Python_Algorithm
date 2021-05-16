pay = int(input())
money = 1000-pay
count = 0
change = money
kind = [500, 100, 50, 10, 5, 1]

for i in kind:
    if change == 0:
        break
    else:
        count += int(change/i)
        change = int(change % i)


print(count)
