##### CHAP11 모듈 #####

### 1. 모듈 ###
# - 필요한 것들끼리 부품처럼 잘 만들어진 파일.

import theater_module

theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격. = 30000
theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때. = 24000
theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때. = 20000

# 모듈명이 기니까 별명을 붙여서 간단하게 줄일 수 있다.
import theater_module as mv

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# .을 붙일 필요 없이 그냥 모듈 안의 모든 것을 사용하겠다.
from theater_module import * # 앞에서 from random import * 을 했었다.

price(3)
price_morning(4)
price_soldier(5)

# 내가 필요한 함수만 import 할 수도 있다.
from theater_module import price, price_morning

price(3)
price_morning(4)
# price_soldier(5) # 이거는 오류 남.

# 함수도 별명을 붙여줄 수 있다.
from theater_module import price_soldier as ps
ps(5)

### 2. 패키지 ###
# - 하나의 디렉토리에 여러 모듈 파일들을 모아놓은 것.

# 신규 여행사 프로젝트. 태국과 베트남에 패키지 여행 상품 제공.

# 태국
import travel.thailand # import 하고 . 뒤에는 모듈이나 패키지만 가능 (클래스, 함수는 import 를 바로 할 수 없음.)
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# 하지만 from import 구문에서는 클래스와 함수 import 가능.
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

# 베트남
from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

### 3. __all__ ###

from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail() # * 을 썼는데도 이렇게만 하면 오류남.
# 우리가 실제로는 공개범위를 설정을 해줘야함.
# __all__ = ["vietnam"] -> 이걸 해주면 잘 실행됨.
trip_to = vietnam.VietnamPackage()
trip_to.detail()

### 4. 모듈 직접 실행 ###
# - 지금까지는 간단했지만 실제로 패키지나 모듈을 만들 때에는 잘 동작하는지 테스트를 해봐야됨.

# 43번 줄에서 Thailand 외부에서 모듈 호출. 문장이 실행된다.

### 5. 패키지, 모듈 위치 ###
# - 지금까지는 패키지나 모듈이 현재 작성 중인 파일 내에 있었다.

# 지금 이게 어느 위치에 있는지 확인할 수 있는 방법
import inspect
import random
print(inspect.getfile(random)) # random 모듈이 어느 위치에 있는 지 파일 정보를 알려줌.
print(inspect.getfile(thailand))

### 6. pip install ###
# - 파이썬에서 기본적으로 제공하는 패키지 외의 패키지 설치

# 터미널 창에 pip install ~~ 을 입력해 패키지 설치
# 터미널 창에 pip list 치면 현재 다운로드한 패키지 볼 수 있음.
# 터미널 창에 pip show ~~ 치면 그 패키지의 정보 열람 가능.
# 터미널 창에 pip install --upgrade ~~ 치면 새로운 버전이 나왔을 때 업그레이드 가능.
# 터미널 창에 pip uninstall ~~ 치면 패키지 삭제 가능.

# beautifulsoup 패키지
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

### 7. 내장함수 ###
# - 말 그대로 내장이 되어 있어 따로 import 를 할 필요 없이 바로 사용 가능한 함수.

# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 사용하세요? : ")
print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시해줌.
print(dir())
import random # 외장함수
print(dir())
import pickle
print(dir())
print(dir(random)) # 랜덤 모듈 내에서 쓸 수 있는 것들을 표시해줌.

lst = [1, 2, 3]
print(dir(lst))

name = "Jim"
print(dir(name))

# 이것 말고도 구글에 list of python builtins 를 검색하면
# 파이썬 내에서 쓸 수 있는 내장함수 정보들을 볼 수 있다.

### 8. 외장함수 ###
# - 직접 import 를 해서 사용해야 하는 함수.
# 구글에 list of python modules 를 검색하면 파이썬에서 제공하는 외장함수 목록을 불 수 있다.

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # .py 로 끝나는 모는 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 표시

folder = "sample_dir"

if os.path.exists(folder):      # 만약 sample_dir 이라는 폴더가 있으면은
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)            # 폴더 삭제.
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)         # 폴더를 직접 생성.
    print(folder, "폴더를 생성하였습니다.")
    
print(os.listdir()) # 현재 디렉토리 표시. (glob 과 비슷)

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 2023-09-11 22:45:15 이렇게 출력됨.

# datetime
import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days = 100) # 오늘 날짜로부터 100일 뒤를 알려줌.
print("우리가 만난지 100일은", today + td) # 단순히 + 계산으로 날짜 계산 가능.