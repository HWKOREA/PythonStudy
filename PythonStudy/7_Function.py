##### CHAP7 함수 #####

### 1. 함수 ###

# 함수 정의
def open_account() :
    print("새로운 계좌가 생성되었습니다.")
    
# 함수 호출
open_account()

### 2. 전달값과 반환값 ###

# 입금 함수
def deposit(balance, money) :
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

# 출금 함수
def withdraw(balance, money) :
    if balance >= money :
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

# 저녁에 출금 (수수료)
def withdraw_night(balance, money) :
    commission = 100 # 수수료
    if balance >= money + commission:
        print("출금이 완료되었습니다. 수수료는 {0}원이며, 잔액은 {1}원입니다." \
              .format(commission, balance - money - commission))
        return commission, balance - money - commission
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
print(balance)      # 반환값이 balance 변수에 들어간다. = 1000

balance = withdraw(balance, 2000)
print(balance)
balance = withdraw(balance, 500)
print(balance) # 500

balance = deposit(balance, 1000) # 1500
commission, balance = withdraw_night(balance, 1000)
print(balance) # 400

### 3. 기본값 ###

def profile(name, age, main_lang) :
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 같은 학년, 같은 반, 같은 수업 -> 이름만 다름
# 이 때 사용되는 게 기본값

def profile_school(name, age = 17, main_lang = "파이썬") :
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
# 이 프로필 함수가 호출될 때 age 와 main_lang 을 전달받지 않았을 때 기본으로 적용된다.

profile_school("유재석")
profile_school("김태호")

### 4. 키워드값 ###
# - 함수에서 전달받는 매개변수의 값을 키워드를 이용해서 호출해주면 순서가 섞여있어도 대입된다.

def profile2(name, age, main_lang) :
    print(name, age, main_lang)
    
profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "자바", age = 25, name = "김태호")

### 5. 가변인자 ###

def profile3(name, age, lang1, lang2, lang3, lang4, lang5) :
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") 
    # ,end 는 출력문이 끝날 때 개행이 아닌 띄어쓰기로 끝내겠다라는 뜻
    print(lang1, lang2, lang3, lang4, lang5)
    
profile3("유재석", 20, "python", "java", "c", "c++", "c#")
profile3("김태호", 25, "kotlin", "swift", "", "", "") # 얘는 두개밖에 모름

# 위와 같이 5개까지 모르는 사람이 있을 수도 있고 5개 넘게 아는 사람이 있을 수도 있는데
# 코드를 계속 바꿔줄 순 없음
# 이럴 때 쓰는 게 가변인자

def profile4(name, age, *language) :        # *로 시작되는 매개변수 : 가변인자
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language :
        print(lang, end = " ")
    print()         # 이건 그냥 마지막에 줄바꿈 용도
    
profile4("유재석", 20, "python", "java", "c", "c++", "c#", "javascript")
profile4("김태호", 25, "kotlin", "swift")

### 6. 지역변수와 전역변수 ###

gun = 10 # 전역변수

# 경계근무 함수
def checkpoint(soldiers) : 
    global gun # 전역 공간에 있는 gun을 함수 내에서 사용하겠다.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    
def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
    
print("전체 총 : {0}".format(gun)) # 10
checkpoint(2) # 8
print("남은 총 : {0}".format(gun)) # 8

gun = checkpoint_ret(gun, 2)

# 1번과 2번 함수는 결국 똑같은 얘기지만 전역변수를 많이 쓰면 복잡해지므로
# 리턴값으로 넣어주는 2번 방법이 더 선호된다.