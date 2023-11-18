#간단 계산기 프로그램
#입력 : 두개 숫자
#출력 : 두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈 결과
#작성자 : 김주영(답 참조)

num1=int(input('첫번째 숫자를 입력하세요: '))
num2=int(input('두번째 숫자를 입력하세요: '))

print('=====================================')
print('두 숫자의 연산 결과는 다음과 같습니다.')
print(num1, '+', num2, '=', num1+num2)
print(num1, '-', num2, '=', num1-num2)
print(num1, '*', num2, '=', num1*num2)
print(num1, '/', num2, '=', num1/num2)
print('계산기를 종료합니다.')
