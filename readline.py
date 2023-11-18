inStr = ''
inputFile = open('song.txt','r',encoding='UTF-8')

inStr = inputFile.readline()
print(inStr, end='')

inStr = inputFile.readline()
print(inStr)

inStr = inputFile.readline()
print(inStr)

inputFile.close()
