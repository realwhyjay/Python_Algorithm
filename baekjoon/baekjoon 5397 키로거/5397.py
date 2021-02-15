num = int(input())
left_count = -1

for _ in range(num):
    pw_input = input()
    pw = []
    for i in range(len(pw_input)):
        if pw_input[i] == '<':
            if pw_input[i+1] == '<':
                left_count += 1
                print("다음 입력 <  left count : {}".format(left_count))
                print(pw)
            else:
                if not pw:
                    left_count = -1
                    print("비어있음 left_count: {}".format(left_count))
                    print(pw)
                    continue
                left_count += 1
                print("이번 < left count: {}".format(left_count))
                print(pw)
        elif pw_input[i] == '>':
            print("다음 입력 <  left count : {}".format(left_count))
            print(pw)
            continue

        elif pw_input[i] == '-':
            pw.pop()
            print("pop함")
            print(pw)
        else:
            if left_count != -1:
                pw.insert(-1 - left_count, pw_input[i])
                print("입력 받음 (커서 이동 상태) {} left_count :  {}".format(
                    pw_input[i], left_count))
                left_count = -1
                print(pw)
            else:
                pw.append(pw_input[i])
                print("입력 받음 {}".format(pw_input[i]))
                print(pw)
                left_count = -1

    print(''.join(pw))
