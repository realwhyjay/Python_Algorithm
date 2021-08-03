num1, num2 = map(int, input().split())


def GCD(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


gcd = GCD(num1, num2)
lcm = int(num1*num2/gcd)

print(gcd)
print(lcm)

# 최대 공약수 => 유클리드 호제법을 사용
# 두 수 중 큰 수를를 작은 수로 나누고, 나머지가 생긴다면
# 그 나누어준 작은 수를 아까 나온 나머지로 다시 나누어준다.
# 나머지가 0이될 떄 까지 반복한뒤, 마지막으로 나온 나머지가 바로 최대공약수!
# 최소 공배수 = (두 자연수의 곱 / 최대공약수)
