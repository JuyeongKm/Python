#함수 선언부분
def c2f(tempC):
    tempF=tempC*1.8+32
    print(round(tempC,2),'섭씨온도는',round(tempF,2),'화씨입니다.')

#메인코드
cel=float(input('섭씨 온도를 입력하세요: '))
c2f(cel)
