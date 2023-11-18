#반지름 입력받아 계산하기
from math import pi
radius=int(input('반지름을 입력하세요:'))

if radius>0:
           area=pi*radius**2
else:
    area=0.0

print(round(area,1))
