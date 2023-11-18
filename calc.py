def calc(values) :
    sum = 0
    try:
        sum = values[0] + values[1] + values[2]
    except IndexError as err :
        print(str(err))
    except Exception as err :
        print(str(err))
    else :
        print('에러 없음')
    finally :
        print(sum)

#메인처리부분
calc([1,2,3,6])
calc([1,2])
