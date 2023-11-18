n = input('음이 아닌 정수를 입력하세요 :')
while not n. isdigit() :
    n = input('음이 아닌 정수를 입력하세요: ')

number = int(n)
sum = 0

for i in range(1,number+1,1) :
    sum += i
    
print('='*25)
print(number,'까지의 합계: ',sum)
