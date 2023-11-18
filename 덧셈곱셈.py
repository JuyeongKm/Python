def calc(var1, var2, op) :
    result = 0
    if op == '+' :
        result = var1 + var2 
    elif op == '*' :
        result = var1 * var2
    return result

n1 = int(input('첫번째 수: '))
n2 = int(input('두번째 수: '))
v = input('연산자 (+ 또는 *) : ') 
print('=================================')

value = calc(n1, n2, v)
print('%d %c %d = %d' %(n1, v, n2, value))
#=print('%d %c %d = %d' %(n1,v,n2,calc(n1,n2,v)))
