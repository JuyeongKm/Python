outFp = open('outFile.txt','w')
outStr = ''

while True :
    outStr = input('본문 입력 :')
    if outStr != '' :
        outFp.write(outStr + '\n')
    else :
        break

outFp.close()
print('정상적으로 파일쓰기 끝남')
