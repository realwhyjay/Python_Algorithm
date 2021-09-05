num = int(input())

check = 2

while (num != 1):
    if num % check == 0:
        print(check)
        num /= check
    else:
        check += 1
