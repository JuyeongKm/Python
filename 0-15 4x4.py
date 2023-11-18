list=[]
for i in range(4):
    sub=[]
    for j in range(4):
        sub.append(0)
    list.append(sub)

value = 0
for i in range(4) :
    for j in range(4) :
        list[i][j] = value
        value += 1

for i in range(4) :
    for j in range(4) :
        print('%4d' %list[i][j], end='')
    print('')
