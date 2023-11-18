num1 = input('숫자1 :')
num2 = input('숫자2 :')

try :
    num1 = int(num1)
    num2 = int(num2)
    while True :
        res = num1 /num2
        print(res)

except ValueError :
    print('문자열은 나누기 연산할 수 없음')
except ZeroDivisionError :
    print('0으로 나눌 수 없음')
except :
    print('무슨일이 일어났나요')
