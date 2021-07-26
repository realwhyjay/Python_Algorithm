
while True:
    try:
        str = list(input())
        low, upper, num, blank = 0, 0, 0, 0

        for i in range(len(str)):
            if str[i].isspace():
                blank += 1
            elif str[i].islower():
                low += 1
            elif str[i].isupper():
                upper += 1
            elif str[i].isdigit():
                num += 1
        print(low, upper, num, blank)
    except EOFError:
        break
