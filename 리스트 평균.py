score = []
for i in range(5):
    score.append(0)

ave, total = 0,0
print('학생들의 점수를 입력하세요.')

for i in range (5):
    score[i] = input(str(i+1) + '번째 점수 :')
    while not score[i].isdigit() :
        score[i] = input(str(i+1) + '번째 점수 :')
    total = total + int(score[i])

print('='*30)
if len(score) != 0 :
    ave = total / len(score)
else :
    ave = 0

print('평균은 %.2f입니다' %ave)
