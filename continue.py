print('점수를 입력하세요. 종료하려면 q를 입력하세요.')
i = 0
total = 0
while True :
    score = input('점수: ')
    if score == 'q' :
        break
    else :
        while not score.isdigit() :
            score = input('점수: ')
        if int(score) < 40 :
            continue
        total = total + int(score)
        i = i + 1
if i != 0 :
    ave = total/i
else :
    ave = 0
print(i,'과목 평균은', str(ave)+'입니다.')
