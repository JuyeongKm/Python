import os
fName = 'score.txt'
if os.path.exists(fName) :
    inFp = open(fName,'r')
    total = 0
    for jumsu in inFp :
        total = total + int(jumsu)
    print('총점 = %d, 평균 = %.2f' %(total, total/20))
    inFp.close()
else:
    print('파일이 없습니다.')
