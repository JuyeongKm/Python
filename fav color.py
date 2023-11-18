color = {} 
color['빨강'] = 'Red'
color['파랑'] = 'Blue'
color['노랑'] = 'Yellow'
color['보라'] = 'Violet'
color['주황'] = 'Orange'
color['초록'] = 'Green'
color['남색'] = 'Indigo'
color['분홍'] = 'Pink'
color['흰색'] = 'White'
color['검정'] = 'Black'

print('좋아하는 색을 입력하세요. 종료하려면 "끝"을 입력하세요.')

while True :
    fav = input('당신이 좋아하는 색은? :')
    if fav == '끝' :
        print('종료합니다.')
        break
    elif fav in color :
        print('%s --> %s' %(fav, color[fav]))
    else :
        print('그런 색이 없습니다.')
    print('='*30)
