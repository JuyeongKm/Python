def c2f(tempC):
    tempF=tempC*1.8+32
    return tempF

cel=float(input('섭씨 온도를 입력하세요 : '))
fahr=c2f(cel)
print(round(cel,2),'섭씨 온도는',round(fahr,2),'화씨입니다.')
