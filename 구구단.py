def multiplication(dan) :
    for i in range(1, 10) :
        print('%d x %d = %2d' %(dan, i, dan*i))

a = input('구구단 출력하기. 단을 입력하세요 : ')
while not a.isdigit() :
    a = input('구구단 출력하기. 단을 입력하세요 : ')
dan = int(a)
multiplication(dan)
