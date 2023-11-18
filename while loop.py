s = input('음이 아닌 정수를 입력하세요: ')
while not s.isdigit() :
    s = input('음이 아닌 정수를 입력하세요: ')
i = 1
sum = 0
while i <= n :
    sum=sum+i
    i=i+1

print('1에서',n,'까지의 합계: ',sum)
