test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    print(queue)
    queue = [(i, idx) for idx, i in enumerate(queue)]
    print(queue)
    count = 0

    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print("{} kkkkk".format(queue))
                print(count)
                break
            else:
                queue.pop(0)
                print("{} jjjjj".format(queue))

        else:
            queue.append(queue.pop(0))
            print("{} jjjjj".format(queue))
