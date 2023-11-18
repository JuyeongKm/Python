infile = open('article.txt','r')
outfile = open('result.txt','w')

text = infile.read()

key = 'enginnering'
pos = text.find(key)

if pos == -1 :
    outfile.write('%s발견 못함.\n' %key)
else:
    outfile.write('%d에서 %s발견함.\n' %(pos,key))

outfile.close()
infile.close()
