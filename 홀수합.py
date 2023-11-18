s = input('음이 아닌 정수를 입력하세요 : ')
while not s.isdigit() :
    s = input('음이 아닌 정수를 입력하세요 : ')
n = int(s)
sum = 0
i = 1
while i <= n :
    sum = sum + i
    i = i + 2
    
print('1에서', n, '까지 홀수의 합계 :', sum)
