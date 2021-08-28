def pactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * pactorial(n-1)


N = int(input())
result = str(pactorial(N))
answer = 0

for i in range(len(result)-1, -1, -1):
    if (result[i] == "0"):
        answer += 1
    else:
        print(answer)
        break
