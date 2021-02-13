num = int(input())
left_count = -1

for _ in range(num):
    pw_input = input()
    pw = []
    for i in range(len(pw_input)):
        if pw_input[i] == '<':
            if pw_input[i+1] == '<':
                left_count += 1
            else:
                if not pw:
                    left_count = 0
                    continue
                left_count += 1

        elif pw_input[i] == '>':
            continue

        elif pw_input[i] == '-':
            pw.pop()

        else:
            if left_count != 0:
                pw.insert(-1-left_count, pw_input[i])
                left_count = 0
            else:
                pw.append(pw_input[i])
                left_count = 0

    print(''.join(pw))
