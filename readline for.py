inList, inStr = [],''

inFile = open('song.txt','r',encoding='UTF-8')
inList = inFile.readlines()

for inStr in inList :
    print(inStr, end = '')

inFile.close()
