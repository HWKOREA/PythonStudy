# Quiz 9) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         pass
    
#     # 매물 정보 표시
#     def show_detail(self):
#         pass

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print("{0} {1} {2} {3} {4}"\
        .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

house_for_sale = []
apartment = House("강남", "아파트", "매매", "10억", "2010년")
officetel = House("마포", "오피스텔", "전세", "5억", "2007년")
villa = House("송파", "빌라", "월세", "500/50", "2000년")
house_for_sale.append(apartment)
house_for_sale.append(officetel)
house_for_sale.append(villa)

print("총 3대의 매물이 있습니다.")
for house in house_for_sale:
    house.show_detail()