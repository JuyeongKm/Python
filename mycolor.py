mycolor = ['빨강','주황','노랑', '초록', '파랑', '남색', '보라']

print(mycolor[:])
print('='*30)
print('리스트의 길이 =',len(mycolor))

print(mycolor[2],'삭제 후 리스트')
del mycolor[2]
print('mycolor =', mycolor[:])
mycolor[4] = 'Indigo'
print('\'노랑\'을', mycolor[4], '로 수정 후 리스트')
for i in mycolor :
    print(i)
