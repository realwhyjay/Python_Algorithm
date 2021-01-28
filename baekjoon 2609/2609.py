a, b = input().split()
a = int(a)
b = int(b)


def GCD(i, j):
    if j == 0:
        return i
    else:
        return GCD(j, i % j)


gcd = GCD(a, b)
lcm = int(a*b/gcd)
print(gcd, lcm)
