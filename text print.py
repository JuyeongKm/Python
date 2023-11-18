inputFile = open('song.txt','r',encoding='UTF-8')
print(inputFile.read(1))
print(inputFile.read(10))

inputFile.close()
