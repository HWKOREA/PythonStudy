##### CHAP8 파일 입출력 #####

### 1. 표준 입출력 ###

# 원래는 콤마로 연결하면 띄어쓰기가 되었는데
print("python", "java", sep = ",") # sep 를 사용하면 띄어쓰기를 할지 다른걸 할지 지정 가능.
print("python", "java", sep = " vs ")
print("python", "java", "javascript", sep = " vs ")

# end 를 사용하면 출력 끝날 때 개행 대신 무엇을 할지 지정 가능
print("python", "java", sep = ",", end = "? ")
print("무엇이 더 재밌을까요?")

import sys
print("python", "java", file = sys.stdout) # 표준출력
print("python", "java", file = sys.stderr) # 표준에러

# 시험 성적
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items() :
    print(subject.ljust(8), str(score).rjust(4), sep = ":")
    # () 숫자만큼의 공간을 확보하고, 왼쪽 오른쪽 정렬

# 은행 대기순번표 001, 002, 003, ...
for num in range(1, 21) :
    print("대기번호 : " + str(num).zfill(3))
    # () 숫자만큼의 공간을 확보하고, 남는 공간 0으로 채우기.
    
# 표준입력
answer = input("아무 값이나 입력하세요. : ")
print("입력하신 값은 " + answer + "입니다.")
print(type(answer)) 
# 사용자의 입력을 통해서 받은 값은 그것이 숫자여도 항상 문자열 형태로 저장된다.

### 2. 다양한 출력포맷 ###

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) # 콜론 빈자리채울것 정렬방향 확보할공간 순으로 입력.

# 양수일 땐 + 로 표시, 음수일 땐 = 로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
print("{0:+,}".format(100000000000))
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3)) # 소수점 둘째자리까지 표시 (셋째자리에서 반올림)

### 3. 파일 입출력 ###

# 쓰기
# score_file 이란 변수를 만들고, open 을 통해서 파일을 열고,
# 처음에는 파일 이름, 그 다음엔 목적 (read / write), 마지막으로 한글이 잘 나오기 위해 encoding.
score_file = open("score.txt", "w", encoding = "utf8")
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close() # 파일을 열었으면 닫아주는 것도 꼭 해줘야 한다.

# w는 덮어쓰기라면 a 는 이미 존재하는 파일 뒤에 이어서 쓸 때 사용.
score_file2 = open("score.txt", "a", encoding = "utf8")
# 위와 같이 print 를 사용해도 되고, 아래와 같이 .write 를 사용해도 된다. (똑같다.)
score_file2.write("과학 : 80")
score_file2.write("\n코딩 : 100") # 다만 print 는 끝날 때 자동 개행이 되는 반면 이건 직접 해줘야함.
score_file2.close()

# 읽기
score_file3 = open("score.txt", "r", encoding = "utf8")
print(score_file3.read())
score_file3.close()

# 한 줄씩 불러오고 싶을 때
score_file4 = open("score.txt", "r", encoding = "utf8")
print(score_file4.readline()) # 줄별로 읽기 동작 실행, 한 줄 읽고 커서는 다음 줄로 자동이동.
print(score_file4.readline())
# print 는 자동으로 줄바꿈이 되기 때문에 한 줄 씩 더 되는 모습을 볼 수 있다.
# 그게 싫으면 이렇게 하면 된다.
print(score_file4.readline(), end = "")
print(score_file4.readline())
score_file4.close()

# 몇 줄인지 모를 때
score_file5 = open("score.txt", "r", encoding = "utf8")
while True :
    line = score_file5.readline()
    if not line :
        break
    print(line, end = "")
print()
score_file5.close()

# 리스트에 값을 넣어 처리하기
score_file6 = open("score.txt", "r", encoding = "utf8")
lines = score_file6.readlines() # 모든 line 을 가지고 와서 list 형태로 저장.
for line in lines :
    print(line, end = "")
print()
score_file6.close()

### 4. Pickle ###
# - 프로그램 상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장해주는 것.

import pickle
# b 는 바어너리이고 pickle 을 사용할 때는 항상 바이너리를 정의해주어야 한다.
profile_file = open("profile.pickle", "wb") # pickle 은 따로 인코딩할 필요 없다.
profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
print(profile)
# 제일 중요한 부분 - pickle 을 이용해서 데이터를 파일에 쓰는 것
pickle.dump(profile, profile_file) # profile 정보를 파일에 저장
profile_file.close()

# 파일에서 데이터를 가져오기
profile_file2 = open("profile.pickle", "rb")
profile2 = pickle.load(profile_file2) # 파일에 있는 내용을 데이터 형태로 저장
print(profile2)
profile_file2.close()

### 5. With ###
# - with 를 쓰면 조금 편하게 작업가능.

import pickle
# close 할 필요 없이 자동으로 종료해줌.
with open("profile.pickle", "rb") as profile_file3 :
    print(pickle.load(profile_file3))

# 단 두 줄에 거쳐서 파일을 읽고 쓸 수 있음.
with open("study.txt", "w", encoding = "utf8") as study_file :
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding = "utf8") as study_file2 :
    print(study_file2.read())