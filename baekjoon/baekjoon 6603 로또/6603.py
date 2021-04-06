from itertools import combinations

while True:
    test_case = list(map(int, input().split()))
    if test_case[0] == 0:
        break
    num = test_case[0]
    lotto = test_case[1:]

    result = list(combinations(lotto, 6))

    for i in result:
        for j in i:
            print(j, end=' ')
        print()

    print()
