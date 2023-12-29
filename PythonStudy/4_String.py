##### CHAP4 문자열 #####

### 1. 문자열 ###

sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3) # """ 는 개행

### 2. 슬라이싱 ###
# - 정보 중에서 우리가 필요한 만큼을 잘라서 사용하는 것.

jumin = "990524-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0 : 2]) # 0번째부터 2번쨰 직전까지 = 99
print("월 : " + jumin[2 : 4])
print("일 : " + jumin[4 : 6])
print("생년월일 : " + jumin[: 6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7 :]) # 7번째부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7 :]) # 맨 뒤에서 7번쨰부터 끝까지

### 3. 문자열 처리 함수 ###

python = "Python is Amazing"

print(python.lower()) # 모든 문자를 소문자로.
print(python.upper()) # 모든 문자를 대문자로.
print(python[0].isupper()) # 0번쨰 인덱스가 대문자인지 아닌지 판별. = True
print(len(python)) # 문자열의 길이를 알려줌.
print(python.replace("Python", "Java")) # 문자열의 값들을 손쉽게 바꿀 수 있다.

index = python.index("n") # 어떤 문자가 어느 위치에 있는지 확인가능.
print(index) # 5
index = python.index("n", index + 1) # 쉼표 뒤에서 시작 위치를 정할 수 있음.
print(index) # 15
print(python.index("yth")) # 문자열도 찾을 수 있음. = 1

print(python.find("n")) # .index 랑 비슷하지만
print(python.find("Java")) # .find 는 못 찾을 때 -1 을 반환하지만
# print(python.index("Java")) # .index 는 못 찾으면 에러를 내버린다.

print(python.count("n")) # python 이란 변수에서 n 이 총 몇 번 등장하는지 알려준다.

### 4. 문자열 포맷 ###

print("a" + "b")
print("a", "b")
# 지금까지는 문자열들을 여러 개 출력할 때 위와 같이 출력을 했었다.

# 방법 1
print("나는 %d살입니다." % 20) # % 뒤에 있는 값을 %d 위치에 넣겠다. (d 는 정수형)
print("나는 %s을 좋아해요." % "파이썬") # s 는 문자열
print("Apple 은 %c로 시작해요." % "A") # c 는 문자

# %s 를 쓰게 되면 사실 다 가능하다.
print("나는 %s살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %s로 시작해요." % "A")

print("나는 %s색과 %s색을 좋아해요." % ("파랑", "빨강")) # 두 개 넣는 것은 괄호로 묶어서 사용가능.

# 방법 2
print("나는 {}살입니다.".format(20)) # .format 안의 값을 {} 안에 넣겠다.
print("나는 {}색과 {}색을 좋아해요.".format("파랑", "빨강"))
# 이거 역시 두개 이상 넣는 것이 가능하다.
print("나는 {0}색과 {1}색을 좋아해요.".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파랑", "빨강"))
# 중괄호 안에 인덱스를 대입해 순서를 설정해주는 것도 가능하다.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨강"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨강", age = 20))
# 마치 변수처럼도 사용가능.

# 방법 4
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
# f를 먼저 치면 미리 선언한 변수들을 쓸 수 있다.

### 5. 탈출 문자 ###

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "정환욱"입니다. 를 출력하고 싶을 때
print("저는 '정환욱'입니다.") # 작은 따옴표를 쓰거나
print('저는 "정환욱"입니다.') # 작은 따옴표로 문장 전체를 감싼 후, 큰 따옴표를 쓰거나
print("저는 \"정환욱\"입니다.") # 탈출 문자를 사용한다.

# \\ : 문장 내에서 \
print("C:\\woogi\\PythonStudy>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\tApple") # Red   Apple