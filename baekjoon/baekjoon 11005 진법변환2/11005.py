num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int, input().split())
answer = ''

while (n != 0):
    answer += str(num[int(n % b)])
    n //= b

print(answer[::-1])
