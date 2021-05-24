num = int(input())
arr = [0]*(num+1)


def makeOne(n):
    if n == 1:
        return 0

    value = []
    if n % 2 == 0:
        value.append(arr[n//3]+1)
    if n % 3 == 0:
        value.append(arr[n//2]+1)
    value.append(arr[n-1]+1)

    return min(value)


print(makeOne(num))
