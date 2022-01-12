### 표준입출력
print("Python", "Java", sep=",", end="?")   # end로 한 줄에 출력
print("무엇이 더 재밌을까요?")

# 시험성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")  # n칸 확보하고 각 방향 정렬, :로 나눔

# 대기순번표 001, 002 ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))    # zfill로 자리수 채움

#answer = input("아무 값이나 입력하세요 : ")     # input으로 입력받으면 항상 문자열로 저장됨***
#print(type(answer))
#print("입력하신 값은 " + answer + "입니다.")





### 다양한 출력포맷 *****
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보 *****
print("{0: >10}" .format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}" .format(-500))

# 왼쪽 정렬하고, 빈칸으로 _채움
print("{0:_<+10}" .format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}" .format(10000000000000000))

# 3자리 마다 콤마를 찍어주기, +-부호도 추가
print("{0:+,}" .format(10000000000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자리수 확보, 빈자리는 ^로 채움
print("{0:^<+30,}" .format(10000000000000000))

# 소수점 출력
print("{0:f}" .format(5/3))

# 소수점 특정 자리수까지
print("{0:.2f}" .format(5/3))





# ### 파일입출력
# 파일 생성
# score_file = open("score.txt", "w", encoding="utf8")  # w : write
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# 파일 수정
# score_file = open("score.txt", "a", encoding="utf8")    # a : append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# 줄 별로 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 줄 별로 불러오기 2
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end = "")
# score_file.close()

# 줄 별로 불러오기3
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list형태로 모든 라인 저장
for line in lines:
    print(line, end="")
score_file.close()





# ### pickle
import pickle
# profile_file = open("profile.pickle", "wb")     # b: 바이너리, 피클쓰려면 필수, 피클은 인코딩 불필요
# profile = {"이름": "박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close





### with    파일조작이 간편함
import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


for i in range(1,4):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as week_report:
        week_report.write(" - {0} 주차 주간보고 -" .format(i))
        week_report.write("\n부서 : ")
        week_report.write("\n이름 : ")
        week_report.write("\n업무 요약 : ")