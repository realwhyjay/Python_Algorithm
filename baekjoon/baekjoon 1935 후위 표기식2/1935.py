n = int(input())
expression = list(input())
num = [0]*n
stack = []
for j in range(n):
    num[j] = int(input())

for i in expression:
    if i.isalpha():
        stack.append(num[ord(i)-ord('A')])
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
print(format(stack[0], ".2f"))
