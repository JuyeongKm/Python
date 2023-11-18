def sum2n(n) :
    total = 0
    for k in range(1,n+1,1) :
        total = total + k
    return total
a = input('음아닌 n값 :')
while not a.isdigit() :
    a = input('음아닌 n 값 :')
a = int(a)

print('1부터 %d까지 합은 %d.' %(a, sum2n(a)))
