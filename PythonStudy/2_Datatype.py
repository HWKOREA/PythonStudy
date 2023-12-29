##### CHAP2 자료형 #####
# - 숫자형 자료, 문자형 자료, 참과 거짓을 의미하는 boolean 자료, ...

### 1. 숫자형 자료 ###

print(5)
print(-10)
print(3.14)
print(1000)
print(5 + 3)
print(2 * 8)
print(3 * (3 + 1))

### 2. 문자형 자료 ###

print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ" * 9)

### 3. boolean 자료형 -> 참 / 거짓 ###

print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

### 4. 변수 ###

# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "이는 어른일까요? " + str(is_adult))
# age 와 is_adult 를 문자형으로 바꿔줘야한다.

print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# 위와 같이 쉼표로도 이을 수 있고, 그럴 경우에 정수형을 문자형으로 안 바꿔줘도 되지만
# 쉼표는 띄어쓰기가 하나씩 포함된다.

### 5. 주석 ###

# 기본적으로 샾으로 한줄 주석을 하고
'''이렇게 작은 따옴표
세개를 하면
여러문장이
주석 처리 된다.'''
# 일괄적으로 할 때엔 선택을 하고 ctrl + / 하면 된다.