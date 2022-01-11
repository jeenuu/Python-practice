### if
weather = "비"
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")





### for
for waiting_no in range(2, 10, 2):
    print("대기번호 : {0}" .format(waiting_no))


starbucks = ["아이언맨", "토트", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다." .format(customer))





### while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요." .format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

# customer2 = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출{1}회". format(customer2, index))
#     index += 1

# customer3 = "그루트"
# person = "Unknown"
# while person != customer3 :
#     print("{0}, 커피가 준비되었습니다." .format(customer3))
#     person = input("이름이 어떻게 되세요 ?")





### countinue, break
absent = [2, 5] # 결석
no_book = [7]   # 책 깜빡
for student in range(1,11) :
    if student in absent :
        continue
    elif student in no_book :
        print("오늘 수업 여기까지. {0}는 교무실로 따라와" .format(student))
        break
    print("{0}, 책을 읽어봐" .format(student))





### 한 줄 for
#출석번호가 1 2 3 4 앞에 100 붙이기로 함 101 102 103 ..
student = [1,2,3,4,5]
student = [i + 100 for i in student]
print(student)

student = ["Iron man", "Thor", "Groot"]
student = [len(i) for i in student]
print(student)

student = ["Iron man", "Thor", "Groot"]
student = [i.upper() for i in student]
print(student)

from random import *



ok = 0
for i in range(5,51) :
    time = randint(5,50)
    if time >= 5 and time <= 15 :
        print("[O] {0}번째 손님 (소요시간 : {1}분)" .format(i, time))
        ok += 1
    else :
         print("[ ] {0}번째 손님 (소요시간 : {1}분)" .format(i, time))       
print("총 탑승 승객 : {0} 분" .format(ok))





### 함수
def open_account() :
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money) :   # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance + money))
    return balance + money

def withdraw(balance ,money) :  # 출금
    if balance >= money :
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다." .format(balance))

def withdraw_night(balance, money) : # 저녁에 출금
    commission = 100 # 수수료
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다." .format(commission, balance))

# 기본값 설정
def profile(name, age = 17, main_lang = "파이썬") :
    print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}" .format(name, age, main_lang))
profile("유재석")   # 이름만 적어도 나머지 다 나옴

# 키워드값
def profile(name, age, main_lang) :
    print(name, age, main_lang)
profile(name = "유재석", main_lang = "파이썬", age = 20)

# # 가변인자
def profile(name, age, *language) :
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end = " ") # 줄 안바꾸기 이어서 쓰기
    for lang in language:
        print(lang, end = " ")
    print()
profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JS")
profile("김태호", 20, "Kotlin", "Swift", "", "", "")





### 지역변수와 전역변수
gun = 10

def checkpoint(soldiers):   # 경계근무
    global gun  # 전역 공간에 있는 gun 사용 ***********
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))



def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))
    return gun

print("전체 총 : {0}" .format(gun))
gun = checkpoint_ret(gun, 2)
#checkpoint(2)
print("남은 총 : {0}" .format(gun))



def std_weight(height, gender):
    if gender == "남자":
        std = height * height * 22
        return std
    elif gender == "여자" :
        std = height * height * 21
        return std

height = 175
gender = "남자"
weight = round(std_weight(height/ 100, gender),2)

print("키 {0} {1}의 표준 체중은 {2}kg 입니다." .format(height, gender, weight))