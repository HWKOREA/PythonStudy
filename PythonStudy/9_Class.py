##### CHAP9 클래스 #####

# 예) 스타크래프트

### 1. 클래스 ###
# - 서로 연관이 있는 변수와 함수의 집합

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음.
name = "마린"   # 유닛의 이름
hp = 40         # 유닛의 체력
damage = 5      # 유닛의 공격력
print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 : {0}, 공격력 : {1}".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음.(일반 모드 / 시즈 모드)

tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 : {0}, 공격력 : {1}".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35
print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 : {0}, 공격력 : {1}".format(tank2_hp, tank2_damage))

def attack(name, location, damage) :
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))
    
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)
# 이와 같이 복붙으로 유닛을 만들 수야 있지만, 매번 만들기가 힘들다. 그래서 클래스라는 게 필요.

# 일반 유닛
class Unit :
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

# 클래스 쓰는 법
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# 갯수가 안 맞으면 사용불가.
# marine3 = Unit("마린")
# marine3 = Unit("마린", 40)

### 2. __init__ 함수 ###
# - 파이썬에서 쓰이는 생성자, 마린이나 탱크와 같은 객체가 생성될 때 자동으로 호출
# 객체 - 클래스로부터 만들어지는 녀석들

### 3. 멤버변수 ###
# - 위에서 썼던 self.~~ 가 바로 멤버변수
# - 즉, 클래스 내에서 정의된 변수이고, 선언, 초기화, 사용 모두 가능.

# 레이스 : 공중 유닛, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
# 변수 뒤에 . 을 붙여 멤버변수를 클래스 외부에서도 쑬 수 있다.
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것. (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
# 클래스 내에 clocking 이라는 변수가 없는데, 외부에서 추가로 할당가능. (단, 그 객체 한해서만)
wraith2.clocking = True
if wraith2.clocking == True :
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

### 4. 메소드 ###
# - 클래스 안의 함수
# 클래스 안에서 self 를 쓰면 모든 메소드에서 사용 가능.

# 공격 유닛
class AttackUnit :
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
        # location 앞에 self 가 없는 이유는 전달받은 location 을 이 메소드에서만 쓰기 때문.
        
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
# 공격을 두 번 받음.
firebat1.damaged(25)
firebat1.damaged(25)
        
### 5. 상속 ###

# 위의 Unit 클래스와 AttackUnit 클래스를 보면 name, hp, damage 가 겹친다.
class Unit1 :
    def __init__(self, name, hp) :
        self.name = name
        self.hp = hp
        
class AttackUnit1(Unit1) :
    def __init__(self, name, hp, damage) :
        Unit1.__init__(self, name, hp)
        self.damage = damage
        
    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
        # location 앞에 self 가 없는 이유는 전달받은 location 을 이 메소드에서만 쓰기 때문.
        
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))        
# 클래스명 다음에 괄호로 붙여주면 AttackUnit1 은 Unit1 은 상속받아서 만들어지는 것이고
# AttackUnit1 에서는 self.name 과 self.hp 에 대해선 따로 정의해줄 필요가 없이진다.
# 다만, Unit1.__init__(self, name, hp) 이걸 통해 Unit1 의 생성자를 불러와야 한다.
# 이 떄, Unit1 을 부모클래스라고 하고, 상속받는 클래스는 자식클래스라고 부른다.

### 6. 다중상속 ###
# - 부모가 둘 이상, 즉 여러 곳에서 상속을 받는다는 것.

# 드랍쉽 - 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송. (공격 불가)

# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed # 멤버변수 초기화
    
    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
    
# 공중 공격 유닛 클래스 (공격 기능 + 날 수 있는 기능)
class FlyableAttackUnit(AttackUnit, Flyable):
# 이 메소드가 하는 일은 그냥 두 개의 클래스를 상속받아서 초기화시켜주는 것 뿐
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

### 7. 메소드 오버라이딩 ###
# - 부모 클래스에서 정의한 메소드 말고, 자식 클래스에서 정의한 메소드를 쓰는 것

class Unit2 :
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))
        
class AttackUnit2(Unit2) :
    def __init__(self, name, hp, speed, damage) :
        Unit2.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
        
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable2 :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed
    
    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit2(AttackUnit2, Flyable2):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit2.__init__(self, name, hp, 0, damage) # 지상 speed 0.
        Flyable2.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# 벌쳐 : 지상 유닛, 기동성이 좋음.
vulture = AttackUnit2("벌쳐", 80, 10, 20)
# 배틀크루저 : 공중 유닛, 체력, 공격력 좋음.
battlecruiser = FlyableAttackUnit2("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
# 지금 문제는 지상유닛은 move 를, 공중유닛은 fly 를 써줘야 하는데
# 매번 우리가 이 유닛이 지상인지 공중인지 확인을 해줘야 한다는 것이다.
# 이럴 때 쓰는 게 메소드 오버라이딩. -> go to line 195
battlecruiser.move("9시") # 이와 같이 이동 메소드명을 통일시켜줄 수 있음.

### 8. pass ###
# - 아무것도 안하고 일단 넘어간다는 뜻.

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    pass
game_start()
game_over()
# 이와 같이 일단 돌아가게끔 하는 녀석

### 9. super ###
# - 부모 클래스를 불러올 때 사용됨. 단, 다중상속을 받고 있을 땐 불가능. (따로따로 초기화시켜주어야 함.)

# 건물
class BuildingUnit(Unit2):
    def __init__(self, name, hp, location):
        # Unit2.__init__(self, name, hp, 0) # 지금까진 이렇게 했는데
        super().__init__(name, hp, 0) # super() 를 써도 됨. (단, super는 self 를 넣어주면 안됨.)
        self.location = location

# 서플라이 디폿 : 건물, 1개 건물마다 8개 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")