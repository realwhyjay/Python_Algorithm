
while True:
    str = list(input())
    if not str:
        break
    low, upper, num, blank = 0, 0, 0, 0
    for i in range(len(str)):
        if str[i] == ' ':
            blank += 1
        elif ord('a') <= ord(str[i]) <= ord('z'):
            low += 1
        elif ord('A') <= ord(str[i]) <= ord('Z'):
            upper += 1
        elif 0 <= int(str[i]) <= 9:
            num += 1
    print(low, upper, num, blank)
