### 예외처리
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}" .format(nums[0], nums[1], int(nums[0]/nums[1])))    # 이상한거 넣으면 오류남
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)



### 에러 발생시키기, 사용자 정의 에러
class BigNumberError(Exception):    # 사용자 정의 에러
    # pass
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:    # 의도적으로 필요할 때 어떤 에러를 발생시켜서 except로 내려오게 가능
        raise BigNumberError("입력값 : {0}, {1}" .format(num1, num2))
    print("{0} / {1} = {2}" .format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

### finally 예외처리구문에서 정상적으로 처리되던 오류가 나던 무조건 실행
finally:
    print("계산기를 이용해주셔서 감사합니다.")