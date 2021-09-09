t = int(input())
nums = [int(input()) for _ in range(t)]
N = max(nums)

# 에라토스테네스 체
check = [False, False]+[True]*(N-1)
for i in range(2, int((N+1)**0.5)+1):
    if check[i] == True:
        for j in range(2*i, N+1, i):
            check[j] = False

# 골드바흐 파티션 구하기
for num in nums:
    count = 0
    for i in range((num//2)+1):
        if check[i] and check[num-i]:
            count += 1
    print(count)

# num이 2보다 큰 짝수일 때,
# num = i + (num-i) 이다
# i와 (num-i)를 체크해서 둘 다 소수라면 골드바흐에 해당한다.
