inStr = input('문자열을 입력하세요 :')
outStr = ''

for ch in inStr :
    if ch != '' :
        outStr = outStr + ch
        
print('원래 문자열 =', '[' + inStr + ']')
print('공백 삭제 문자열 =', '[' + outStr + ']') 
