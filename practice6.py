### 모듈
import theater_module as mv
from travel import vietnam
from travel import thailand # as붙이면 이거로만 호출 가능
mv.price(3) # 3명이 영화보러 갔을 때 가격
mv.price_morning(4) # 4명이 조조 영화보러 갔을 때 가격
mv.price_soldier(5) # 5명 군인이 영화보러 갔을 때 가격

# from으로 호출도 가능
from theater_module import *
# from theater_module import price, price_morning   * 대신 쓸거만 명시 가능
# from theater_module import * price_soldier as price   

price(3)
price_morning(4)
price_soldier(5)




### 패키지
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# from으로도 가능
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()





### 패키지, 모듈 위치
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))



