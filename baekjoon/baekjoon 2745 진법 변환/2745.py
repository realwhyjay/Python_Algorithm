n, b = input().split()
n = n[::-1]
b = int(b)

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i in range(len(n)):
    result += num.index(n[i])*(b**i)

print(result)
