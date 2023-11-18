def print_head() :
    print'\n========== 연산을 선택하세요 ==========')
    print('1. 덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.종료')
    print('======================================')

def calculator(op) :
    op1 = float(input('첫번째 숫자를 입력하세요: '))
    op2 = float(input('두번째 숫자를 입력하세요: '))
    if op == '1' :
        print('두 수의 더하기 결과는', round(op1+op2,2),'입니다.')
    elif op == '2' :
        print('두 수의 빼기 결과는',round(op1-op2,2),'입니다.')
    elif op == '3' :
        print('두 수의 곱하기  결과는',round(op1*op2,2),'입니다.')
    elif op == '4' :
        if op2 != - :
            print('두 수의 나누기 결과는',round(op1/op2,2),'입니다.')
        else :
            print('0으로 나눌 수 없습니다.')

#메인코드부분
on = True
while on :
    print_head()
    comp = input('어떤 연산을 원하세요? : ')
    while not comp.isdigit() :
        comp = input('어떤 연산을 원하세요? : ')
    if comp == '5' :
        print('종료합니다. 이용해주셔서 감사합니다.')
        on = False
    elif 1 <= int(comp) <= 4 : 
        calculator(comp)
    else :
        print('잘못입력하셨습니다. 다시 선택해주세요.') 
