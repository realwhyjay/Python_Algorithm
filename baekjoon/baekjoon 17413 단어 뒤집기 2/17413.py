import sys
input = sys.stdin.readline

word = ''
result = ''
tag = False

S = list(input().strip())

for i in S:
    # 뒤집어서 출력
    if tag == False:
        if i == '<':
            tag = True
            word = word+i
        # ' '로 단어가 구분되는 경우 처리
        elif i == ' ':
            word = word+i
            result = result+word
            word = ''
        else:
            word = i+word

    # 정상적으로 출력 (< > 안에 들어가있는 경우.)
    elif tag == True:
        word = word+i
        if i == '>':
            tag = False
            result = result+word
            word = ''

print(result+word)
