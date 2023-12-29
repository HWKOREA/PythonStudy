# Quiz 7) 표준 체중을 구하는 프로그램을 작성하시오.

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째 자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender) :
    if gender == "남자" :
        std_weight = float(height / 100) * float(height / 100) * 22
    elif gender == "여자" :
        std_weight = float(height / 100) * float(height / 100) * 21
    return std_weight

height = 175
gender = "남자"
std_weight = round(std_weight(height, gender), 2) # 소수점 둘째자리 까지만 반올림 해줘.

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, std_weight))