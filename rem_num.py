inStr = input('문자열을 입력하세요: ')
outStr = ''
i = 0
while i < len(inStr) :
    if (not inStr[i].isdigit()) :
        outStr = outStr +inStr[i]
    i = i + 1

print('숫자제거 문자열 =',outStr)
