class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

### 4. 모듈 직접 실행 ###
# - 지금까지는 간단했지만 실제로 패키지나 모듈을 만들 때에는 잘 동작하는지 테스트를 해봐야됨.

if __name__ == "__main__":          # 이 py 파일에서 직접 실행했을 때
    print("Thailand 모듈을 직접 실행.")
    print("이 문장을 모듈을 직접 실행할 때만 실행돼요.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출.") # 즉 11_Module.py 에서 갖다 쓸 때 이 문장이 실행된다.