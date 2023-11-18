#지폐 총액 구하기

cash = ([50000, 10000, 5000, 1000], [2,7,0,3])

sum = 0

for i in range(len(cash[0])):
    sum = sum + cash[0][1]*cash[1][i]

print(sum)
