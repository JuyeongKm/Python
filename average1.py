s = input('과목의 개수를 음이 아닌 정수로 입력하세요: ')
while not s.isdigit() :
    s = input('과목의 개수를 음이 아닌 정수로 입력하세요: ')
n = int(s)
total = 0
i = 1
while i <= n :
    score = input('점수를 입력하세요: ')
    while not score.isdigit() :
        score = inpur('점수를 다시 입력하세요: ')
    total = total + int(score)
    i += 1

if n != 0 :
    ave = total/n
else:
    ave = 0

print(n,'과목의 평균점수: ',round(ave,2))
