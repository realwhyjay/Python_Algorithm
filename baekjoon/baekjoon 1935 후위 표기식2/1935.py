n = int(input())
expression = list(input())
# 입력 받을 수를 저장할 리스트를 선언한다.
num = [0]*n
stack = []
for j in range(n):
    num[j] = int(input())

for i in expression:
    # 입력받은 문자가 알파벳일 경우 stack에 추가를 해준다.
    # ord()는 유니코드 문자를 정수로 변환해주는 파이썬 내장함수이다.
    # A는 무조건 1이 아니고 문자는 반드시 순서대로 사용되기 때문애,
    # i에 해당하는 정수에서 A에 해당하는 정수를 빼서 코드에서 사용할 인덱스를 찾아준다.
    # ex) ord를 사용하면 A는 정수 97을 반환하고 B는 98를 반환한다.
    #     그렇기 떄문에, B의 경우라면 98-97을 해준 1이라는 인덱스 값을 가지게 된다.
    if i.isalpha():
        stack.append(num[ord(i)-ord('A')])
    # 입력받은 문자가 알파벳이 아니라 연산자일 경우에는
    # 연산을 할 수 두개를 pop 하여 계산해준다.
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if i == '+':
            stack.append(n1+n2)
        elif i == '-':
            stack.append(n1-n2)
        elif i == '*':
            stack.append(n1*n2)
        elif i == '/':
            stack.append(n1/n2)
# 소수점 두자리 수까지만 출력
print(format(stack[0], ".2f"))
