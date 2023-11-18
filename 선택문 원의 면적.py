from math import pi
#함수 정의부분
def area_circle(radius,n):
    if radius>0:
        area=pi*radius**2
        return round(area,n)
    else:
        return 0.0
#메인코드부분
print(area_circle(3,1))
print(area_circle(-3,1))
