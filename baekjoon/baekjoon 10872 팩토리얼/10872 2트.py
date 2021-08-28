def pactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * pactorial(n-1)


N = int(input())

print(pactorial(N))
