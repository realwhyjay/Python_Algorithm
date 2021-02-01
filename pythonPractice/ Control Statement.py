from random import *
from math import *  # math 라이브러리안에 있는 모든 것을 이용하겠다는 의미
print(5)
print(-10)
print(3.14)
print(123124125)
print(5+8)
print(8/3)
print(8 % 3)

print("풍선")
print('풍풍선')
print("v"*9)


print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)


# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + "의 이름은" + name + "에요")
print(name + "는 " + str(age) + "살이며, 산택을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

print(2**3)  # 2의 3승
print(5 % 3)  # 나머지


# 간단한 수식
number = 2+3*4
print(number)

number = number+2
print(number)

number += 2
print(number)
number -= 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number %= 2
print(number)


# 숫자 처리 함수
print(abs(-5))  # 절대값
print(pow(4, 2))  # 4^2 = 16. 제곱이 나옴
print(max(5, 12))  # 최대값
print(min(5, 12))  # 최소값
print(round(3.14))  # 반올림
print(round(4.99))

# math 라이브러리 사용하는 것
print(floor(4.99))  # 내림,4
print(ceil(3.19))  # 올림,4
print(sqrt(16))  # 제곱근을 구하는 것,4


# 랜덤함수(난수)

print(random())  # 0.0이상 1.0 미만의 임의의 값을 생성하는 것.
print(random() * 10)  # 0.0이상 10.0 미만의 임의의 값을 생성하는 것.
print(int(random() * 10))  # 0 이상 10 미만의 임의의 값을 생성하는 것.

print(int(random() * 10) + 1)  # 1 이상 10 이하의 임의의 값을 생성하는 것.

# 로또 값 출력해보자
print(int(random()*45)+1)  # 1~45 의 임의의 값 생성

# 이걸 더 쉽게 작성하는 방법
print(randrange(1, 45))  # 1~45 미만의 임의의 값 생성
print(randrange(1, 46))  # 1~45의 임의의 값 생성

print(randint(1, 45))  # randint는 저 두 값을 모두 포함하는 임의의 값 생성하는 것


# 문자열
sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년입니다.
파이썬은 쉬워요
정말입니다.
"""
print(sentence3)


# 슬라이싱
jumin = "940420-1069210"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # :을 사용해서 0번째부터 2번째 직전 값까지 가져오는 것
print("월 : " + jumin[2:4])  # :을 사용해서 2번째부터 4번째 직전 값까지 가져오는 것
print("월 : " + jumin[4:6])  # :을 사용해서 4번째부터 6번째 직전 값까지 가져오는 것


print("생년월일 : " + jumin[0:6])  # 처음부터 가져오는거니까 0을 지워도 된다.
print("뒤 7자리 : " + jumin[0:14])  # 끝까지 가져오는거니까 14를 지워도 된다.
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])  # 맨 뒤 7번째부터 끝까지


# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())  # 소문자로 출력
print(python.upper())  # 대문자로 출력
print(python[0].isupper())  # 0번째 문자가 대문자인지 파악
print(len(python))  # 전체 길이 반환
# python을 swift로 바꿔서 출력한다. 변수 내용은 바뀐거 아니고 출력만 바꿔서 해주는 것
print(python.replace("Python", "Swift"))

index = python.index("n")  # index를 사용하면 어떤 문자가 어디에 있는지를 알 수 있다.
print(index)

index = python.index("n", index + 1)
# 그 이후에도 더 있는지 찾는다. 뒤에는 어디부터 찾을지를 정해주는 것.
# 원하는 값이 없을 때는 프로그램을 종료해버린다.
print(index)

print(python.find("Swift"))  # index랑 비슷하게 원하는 문자가 어디에 포함되어있는지 위치를 반환
# 근데 지금 Swift라는게 없으니까 반환값은 -1이 된다. 반환값이 있다는 점에서 index와 차이를 가진다

print(python.count("n"))  # 찾는 문자가 몇개나 있는지 세어주는 것


# 문자열 포맷
print("a"+"b")
print("a", "b")

# 출력 방법 1
print("나는 %d살입니다" % 20)  # 정수
print("나는 %s을 좋아해요." % "파이썬")  # 문자열
print("Apple은 %c로 시작해요" % "A")  # 문자
# %s로만 쓰면 정수건 하나의 문자건 상관없이 다 출력이 가능하다.

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 출력 방법 2 중괄호 사용
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# 순서를 임의로 정할수도 있음
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))

# 출력 방법 3 - 이 경우에는 순서와 상관없이 출력이 가능하다.
print("나는 {age}살이며 {color}색을 좋아해요." .format(age=20, color="빨간"))
print("나는 {age}살이며 {color}색을 좋아해요." .format(color="빨간", age=20))

# 출력 방법 4 - 변수를 사용
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 리스트 []
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탔다
subway.append("하하")
print(subway)

# 정형돈이 두번째 칸에 탔다
subway.insert(1, "정형돈")
print(subway)

# 맨 뒤에칸부터 한명씩 내린다면?
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명 있는지 확인
subway = ["유재석", "조세호", "박명수", "하하"]
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 리스트는 정렬도 가능
num_list = [5, 2, 3, 4, 1]
print(num_list)
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 2, 3, 4, 1]
num_list.extend(mix_list)
print(num_list)


# 딕셔너리 {key: value}로 구성. 키는 중복사용 불가능
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

# 키가 없는데 대괄호를 사용하여 반환을 하려는 경우에는 프로그램이 종료된다
# print(cabinet[5])
# 반면 키가 없는데 get을 사용하려 반환하는 경우에는 None를 반환한다.

# 값이 없는 경우에는 원하는 값을 출력할수 있도록 할 수 있다.
print(cabinet.get(5, "사용 가능"))

# 사전 자료형 안에 어떤 값이 있는지 확인하는 방법
print(3 in cabinet)
print(5 in cabinet)
# key를 넣고 그게 cabinet에 있느냐를 물어보는 것

# key는 스트링 값도 사용이 가능하다.
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새로운 값을 추가하는 경우
print(cabinet)
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "최영재"
# 원래 있던 키에 값을 배정하는 경우에는 이전 값대신 새로운 값이 들어간다.
print(cabinet)

# 값을 삭제하는 경우
del cabinet["A-3"]
print(cabinet)

# key들만 출력하는 경우
print(cabinet.keys())

# value들만 출력하는 경우
print(cabinet.values())

# key, value를 쌍으로 출력하는 경우
print(cabinet.items())

# 딕셔너리를 지우는 경우
cabinet.clear()
print(cabinet)


# 튜플 - list와 다르게 내용 변경이나 추가를 할 수가 없다.
# 대신 속도가 빠르다는 장점이 있다.
menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

# 어디서 활용하나?
name = "최영재"
age = 28
hobby = "코딩"
print(name, age, hobby)

# 튜플을 사용하면 한번에 선언이 가능하다
(name, age, hobby) = ("최영재", 28, "코딩")
print(name, age, hobby)


# 집합 (set)
# 중복이 안되고 순서가 없다.
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "최영재"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (자바는 할 수 있지만 파이썬을 할 수 없는 개발자)
print(java-python)
print(java.difference(python))

# 집합에 추가 또는 삭제 가능
python.add("김태호")
print(python)

java.remove("김태호")
print(java)


# 자료구조의 변경
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))
# 현재는 set상태


# 타입을 리스트로 바꿀 수 있다
menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


# if문
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비될 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")


# for문
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6):  # 1부터 6전까지
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:  # 스타벅스라는 리스트에 있는 사람들 한명한명을 출력하는 것
    print("{0}, 커피가 준비되었습니다.".format(customer))


# while문
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다")


customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
print("토르가 커피를 받아갔다!")


# continue와 break
# continue는 이어지는 명령을 실행시키지 않고 그 다음 반복문을 진행시키도록 하는 것
absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와" .format(student))
        break
    print("{0}, 책을 읽어봐" .format(student))


# 한줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [1, 2, 3, 4, 5]
print(students)

students = [i+100 for i in students]
# students라는 list에 있는 요소들을 i로 하나씩 불러 오고, 거기에 100을 더한 값을 리스트로 바꾸어 집어넣으라는 의미
print(students)

# 학생 이름을 길이로 변환
students = ["아이언맨", "토르", "그루트"]
print(students)
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
print(students)
students = [i.upper() for i in students]
print(students)
