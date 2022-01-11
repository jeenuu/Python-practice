### 자료형, 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
print("" + name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print("" + name + "는 어른일까요? " + str(is_adult) + "")





### 연산자
print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)

print(2 ** 3)   # 2^3 = 8
print(5 % 3)    # 나머지 구하기
print(5 // 3)   # 몫 구하기

print(10 > 3)
print(4 >= 7)
print(3 == 3)
print(1 != 2)
print(not(1 != 3))

print((3 > 0 ) and (3 < 5))
print((3 > 0) & (3 < 5))
print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))
print(5 > 3 > 2)





### 수식
print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number /= 2
print(number)





### 숫자 처리 함수
print(abs(-5))      # 절댓값
print(pow(4, 2))    # 4^2 = 16
print(max(5, 12))
print(min(5, 12))
print(round(3.14))
print(round(4.98))

from math import *
print(floor(4.90))  # 내림
print(ceil(3.14))   # 올림
print(sqrt(16))     # 제곱근





### 랜덤함수
from random import *
print(random())         # 0.0 이상 1.0 미만 임의의 값 생성
print(random() * 10)    # 0.0 이상 10.0 미만 임의의 값 생성
print(int(random() * 10)) # 0 이상 10 미만 임의의 정수 생성
print(int(random() * 10) + 1)   # 1 이상 10 이하 임의의 정수 생성

print(randrange(1, 46)) # 1 ~ 45 임의의 값 생성
print(randint(1, 45))   # 1 ~ 45 임의의 값 생성

day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 %d일로 선정되었습니다." %day)





### 문자열
sentence = "나는 소년입니다"
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)





### 슬라이싱
jumin = "990120 1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에 부터) : " + jumin[-7:])   # 맨 뒤 7번째부터 끝까지





### 문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())

print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)    # 두 번째 n 찾기
print(index)

print(python.find("n"))
print(python.find("Java"))  # -1 나옴
# print(python.index("Java")) # 오류남
print(python.count("n"))





### 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살 입니다." % 20)
print("나는 %s를 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color = "빨간"))

# 방법 4 (v3.6~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")





### 탈출문자
print("백문이 불여일견\n백견이 불여일타") # 줄바꿈
print("저는 '취준생입니다.'")
print("저는 \"취준생입니다.\"")

print("C:\\Study\\PythonPractice> ")    # \\두번

print("Red Apple\rPine")    # \r : 커서를 맨앞으로 이동

print("Redd\bApple")    # \b : 백스페이스 (한 글자 삭제)

print("Red\tApple")     # \t : 탭

# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
site = "http://naver.com"
pw = site[7 : site.index(".")]
pw = pw[:3] + str(len(pw)) + str(pw.count("e")) + "!"
print("{}의 비밀번호는 {} 입니다." .format(site,pw))





### 리스트  (다양한 자료형 함께 사용 가능)
subway = [10, 20, 30]
print(subway)
print(subway.index(20))

subway.append(40)   # 리스트에 추가
subway.insert(2, 25)    # 사이에 추가

subway.pop()    # 뒤에서부터 하나씩 제거

subway.count(20)    # 카운트

num_list = [5,2,4,3,1]
num_list.sort()     # 오름차순 정렬
print(num_list)

num_list.reverse()  # 순서 뒤집기
print(num_list)

# num_list.clear()    # 모두 지우기

mix_list = ["조세호", 20, True]

num_list.extend(mix_list)   # 리스트 합치기
print(num_list)





### 딕셔너리
cabinet = {3:"유재석", 100:"김태호"}  # key:value
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5])   # 오류남
print(cabinet.get(5))   # 오류안나고 None 뜸
print(cabinet.get(5, "사용가능"))   # 오류났을 때 default 값 설정 가능

print(3 in cabinet)     # cabinet에 있는지 확인

cabinet["C-20"] = "조세호"  # 딕셔너리에 추가, 이미 있으면 업데이트
print(cabinet)

del cabinet[3]      # 딕셔너리에서 삭제
print(cabinet)

print(cabinet.keys())   # key 들만 출력
print(cabinet.items())  # key,val 쌍으로 출력

cabinet.clear   # 딕셔너리 모두 제거





### 튜플    (리스트와 다르게 추가삭제 불가, 속도빠름)
menu = ("돈까스", "치즈까스")
print(menu[0])
# menu.add("생선까스")    # 불가능

(name, age, hobby) = ("김종국", 20, "코딩")     # 이렇게 선언가능
print(name, age, hobby)





### 집합(세트)  (중복이 안되고 순서가 없음)
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)    # 교집합
print(java.intersection(python))

print(java | python)    # 합집합
print(java.union(python))

print(java - python)    # 차집합
print(java.difference(python))

python.add("김태호")    # 집합에 추가
print(python)

java.remove("김태호")   # 집합에서 제거
print(java)





### 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


from random import *
id = list(range(1,21))
winners = sample(id, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print(" -- 축하합니다 -- ")