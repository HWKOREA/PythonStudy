##### CHAP10 예외처리 #####

### 1. 예외처리 ###
# - 어떤 에러가 발생했을 때 그에 대해서 처리를 해주는 것.

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요. : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요. : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:      # 에러의 한 종류로 잘못된 데이터형이 있을 때
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:    # 0으로 나누었을 때
    print(err)          # 에러가 난 이유를 그대로 출력가능.
# 예를 들어 11번 줄을 안 안적었을 때
except Exception as err:                 # 위에서 작성한 에러종류 외의 모든 에러를 여기서 처리하겠다.
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

### 2. 에러 발생시키기###

try:
    print("한 자리숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요."))
    num2 = int(input("두 번째 숫자를 입력하세요."))
    if num1 >= 10 or num2 >= 10:
        raise ValueError        # 지정한 에러를 발생시키기.
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

### 3. 사용자 정의 예외처리 ###
# - ValueError 나 ZeroDivisionError 는 파이썬에서 제공해주는 에러고 우리가 직접 에러를 지정해줄 수도 있다.

class BigNumberError(Exception):        # Exception 을 상속받음.
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg

try:
    print("한 자리숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요."))
    num2 = int(input("두 번째 숫자를 입력하세요."))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

### 4. finally ###
# - 예외처리 구문에서 정상적으로 수행되건 오류가 발생하건 상관없이 무조건 실행되는 구문.

try:
    print("한 자리숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요."))
    num2 = int(input("두 번째 숫자를 입력하세요."))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")