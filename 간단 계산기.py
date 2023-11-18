#간단 계산기 : calculator.py
#입력: 사칙연산과 두개 실수 값, 출력: 연산결과 값(실수)

print('간단 계산기입니다. 연산을 선택하세요.')
print('1. 덧셈, 2. 뺄셈, 3. 곱셈. 4.나눗셈')
comp = input('어떤 연산을 원하세요? :')
op1 = float(input('첫번째 숫자를 입력하세요 : '))
op2 = float(input('두번째 숫자를 입력하세요 : '))

if comp == '1':
    pirnt('두 수의 더하기 결과는', round(op1+op2,2),'입니다.')
elif comp == '2':
    print('두 수의 빼기 결과는', round(op1-op2,2),'입니다.')
elif comp == '3':
    print('두 수의 곱하기 결과는',round(op1*op2,2),'입니다.')
elif comp == '4':
    if op2 != 0:
        pirnt('두 수의 나누기 결과는', round(op1/op2,2),'입니다.')
    else:
        print('0으로 나눌 수 없습니다.')
print('이용해 주셔서 감사합니다.')
                  
