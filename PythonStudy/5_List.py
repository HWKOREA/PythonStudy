##### CHAP5 리스트 #####
# - 순서를 가지는 객체의 집합

### 1. 리스트 ###

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
subway = [10, 20, 30]
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇번쨰 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # append 는 맨 뒤에 추가하는 것
print(subway)

# 정형돈씨를 유재석과 조세호 사이에 태워봄
subway.insert(1, "정형돈") # insert 는 입력한 숫자인덱스 자리에 하나 추가하는 것
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # pop 은 맨 뒤에서 하나씩 제거하는 것
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 리스트는 다양한 자료형과 함께 섞어서 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)

### 2. 사전 (Dictionary) ###
# - key 와 value 로 구성 (중복허용 X)

cabinet = {3 : "유재석", 100 : "김태호"} # 사전은 중괄호로 여닫는다,  key : value 로 구성.

print(cabinet[3]) # key 값을 넣어주면 "유재석" 을 출력함.
print(cabinet[100]) # 김태호
print(cabinet.get(3)) # .get(key 값) 을 사용해도 똑같이 나온다.

# print(cabinet[5]) # 이와 같이 key 가 존재하지 않으면 에러 난다.
print(cabinet.get(5)) # 반면에 .get 은 NONE 이 출력된다.
print(cabinet.get(5, "사용가능")) # NONE 대신에 출력하고 싶은 문구도 출력 가능.

print(3 in cabinet) # key in 변수 로 들어있는 키의 유무 파악 가능. = True
print(5 in cabinet) # False

# key 의 자료형이 문자열도 가능하다.
cabinet = {"A - 3" : "유재석", "B - 100" : "김태호"}
print(cabinet["A - 3"]) # 유재석
print(cabinet["B - 100"]) # 김태호

# 새 손님
print(cabinet)
cabinet["C - 20"] = "조세호" # cabinet 에 C - 20 이라는 key 를 만들고 조세호를 대입.
cabinet["A - 3"] = "김종국" # 값을 업데이트하는 것도 가능.
print(cabinet)

# 간 손님
del cabinet["A - 3"] # del 를 이용해 원하는 key 를 넣어주면 삭제 가능.
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 둘 다 출력
print(cabinet.items())

# 모두 지우기
cabinet.clear()
print(cabinet)

### 3. 튜플 (Tuple) ###
# - 리스트와는 다르게 내용변경이나 추가 불가능.

menu = ("돈까스", "치즈까스") # 소괄호로 묶으면 튜플
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스
# menu.add("생선까스") # 내용변경 X 에러 남.

# 튜플의 사용
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name,age, hobby) = ("김종국", 20, "코딩") # 이와 같이 한꺼번에 선언 가능.
print(name, age, hobby)

### 4. 집합 (Set) ###
# - 중복이 안되고, 순서 없음.

my_set = {1, 2, 3, 3, 3} # 사전과 비슷하게 중괄호로 여닫지만, 콜론 X -> Set
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 이와 같이 리스트를 set 으로 감싸주어도 Set

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python)) # 둘 다 교집합 출력

# 합집합 (java 도 할 수 있거나, python 도 할 수 있는 개발자)
print(java | python)
print(java.union(python)) # 둘 다 합집합 출력

# 차집합 (java 는 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python)) # 둘 다 차집합 출력

# 내용 변경
python.add("김태호") # add 로 세트에 값을 추가 가능.
print(python)
java.remove("김태호") # remove 로 세트의 값을 빼는 것도 가능.
print(java)

### 5. 자료구조의 변경 ###

menu = {"커피", "우유", "주스"} # 집합
print(menu, type(menu))

menu = list(menu) # list 로 감싸면 자료구조가 변경된다.
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))