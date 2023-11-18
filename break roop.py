print('점수를 입력하세요. (종료하려면 q)')
i = 0
total = 0

while True :
    score = input('점수: ')
    if score == 'q' :
        break
    else :
        while not score.isdigit() :
            score = input('점수: ')
        total += int(score)
        i += 1

if i != 0 :
    ave = total/i
else :
    ave = 0

print('평균은', round(ave,1), '입니다.')
    


        
    
