def GCD(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return(GCD(b, a % b))


num1, num2 = map(int, input().split())
lcm = int((num1 * num2)/GCD(num1, num2))

print(lcm)
