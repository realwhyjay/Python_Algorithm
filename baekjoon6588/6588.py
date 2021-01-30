number = 1000000
goldbach = [False, False]+[True]*(number)
for i in range(2, number//2+1):
    if goldbach[i] == True:
        for j in range(i+i, number+1, i):
            goldbach[j] = False


while True:
    check_num = int(input())
    if check_num == 0:
        break

    #first = 0
    #last = check_num

   # for i in range(number):
        if goldbach[first] and goldbach[last]:
            print(f"{check_num} = {first}+{last}")
            break
        first += 1
        last -= 1

    for i in range(2, check_num//2+1):
        if goldbach[i] and goldbach[check_num-i]:
            print("{} = {} + {}".format(check_num, i, check_num-i))
            break
# for i in range(2, number):
 #   if goldbach[i] == True:
  #      print(i)
