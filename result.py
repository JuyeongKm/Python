inFp = open('score.txt', 'r',encoding='UTF-8')
outFp = open('result.txt','w')

total, count = 0,0

for jumsu in inFp :
    count += 1
    total = total + int(jumsu)

outFp.write('총점 = %d \n' %total)
outFp.write('평균 = %.2f \n' %(total/count))

inFp.close()
outFp.close()
