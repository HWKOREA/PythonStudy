# 극장에서는 현금만 받음. 잔돈을 안 거슬러줌.
# 미리 극장에 가기 전에 사람 수에 따라 가격을 미리 알 수 있는 모듈이다.

# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원입니다.".format(people, people * 10000))
    
# 조조할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인, 할인 가격은 {1}원입니다.".format(people, people * 4000))