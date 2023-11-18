inList = ''

inFile = open('song.txt','r',encoding='UTF-8')
inList = inFile.readlines()
print(inList)

inFile.close()
