inStr = ''
inFile = open('song.txt','r',encoding='UTF-8')

while True :
    inStr = inFile.readline()
    if inStr == '' :
        break
    print(inStr, end='')

inFile.close()
