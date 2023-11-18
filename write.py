inFp = open('song.txt','r',encoding='UTF-8')
outFp = open('outFile.txt' , 'w')
inStr = ''

inList = inFp.readlines()
for inStr in inList :
    outFp.write(inStr)
inFp.close()
outFp.close()
