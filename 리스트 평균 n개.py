s = input('과목의 개수를 입력하세요 :')
while not s.isdigit() :
    s = input('과목의 개수를 입력하세요 :')
n = int(s)
total,ave = 0,0

score = []
for i in range(n):
    score.append(0)

for i in range(n):
    score[i] = input(str(i+1) + '번째 점수:')
    while not score[i].isdigit():
        score[i] = input(str(i+1) + '번째 점수 :')
    total = total + int(score[i])

print('='*30)
if len(score) != 0:
    ave = total / len(score)
else:
    ave = 0
print('%d과목의 평균은 %.2f입니다' %(n,ave))
