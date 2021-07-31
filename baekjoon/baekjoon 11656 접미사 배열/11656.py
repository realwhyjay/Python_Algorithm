S = list(input())
temp = ""
result = []

for i in range(len(S)):
    temp = "".join(S)
    result.append(temp)
    S.pop(0)


for j in sorted(result):
    print(j)
