print('점수를 입력하세요. 종료하려면 q를 입력하세요.')
i = 0
total = 0
on = True
while on :
    score = input('점수 : ')
    if score == 'q' :
        on = False
    else :
        while not score.isdigit() :
            score = input('점수 : ')
        total = total + int(score)
        i = i + 1
if i != 0 :
    ave = total / i
else :
    ave = 0
    
print('평균은', str(round(ave, 1)) + '입니다.')
