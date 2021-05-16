abc = []
for _ in range(3):
    abc.append(int(input()))

ans = list(str(abc[0]*abc[1]*abc[2]))


for i in range(1, 9):
    print(ans.count(str(i)))
