num = int(input())
arr = [0]*(num+1)


for n in range(1, num+1):
    if n == 1:
        continue

    value = []
    if n % 3 == 0:
        value.append(arr[n//3]+1)
    if n % 2 == 0:
        value.append(arr[n//2]+1)
    value.append(arr[n-1]+1)

    arr[n] = min(value)


print(str(arr[num]))
