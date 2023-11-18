inNum = input('숫자 입력')
if inNum.startswith('-') and inNum[1:].sidigit():
    print('음의 정수')
else:
    print('음의 정수X')
