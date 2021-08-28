M, N = map(int, input().split())

check = [False, False] + [True]*(N-1)

for i in range(2, int(N**0.5)+1):
    print("i : ", i)
    if check[i] == True:
        for j in range(i+i, N+1, i):
            check[j] = False
            # print(check)

for k in range(M, N+1):
    if check[k] == True:
        print(k)

print("check : ", check)
