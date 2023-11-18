def c2f(tempC) :
    return (tempC * 1.8) + 32
def f2c(tempF) :
    return (tempF - 32) / 1.8

print('온도 변환기 : 섭씨->화씨, 화씨->섭씨')

temp = float(input('온도를 입력하세요: '))
base = input('베이스를 입력하세요, C 또는 F: ')

if base.upper() == 'C' : 
    print('섭씨온도 %.2f는 %.2f화씨입니다' %(temp, c2f(temp)) )
elif base.upper() == 'F' :
    print('화씨온도 %.2f는 %.2f섭씨입니다' %(temp, f2c(temp)) )
else :
    print('베이스를 잘못 입력했습니다!')
