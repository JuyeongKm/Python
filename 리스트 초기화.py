myList = [] # 빈 리스트 생성

for i in range(10) : # 리스트 10개 셀에 0으로 초기화
    myList.append(0)
print('List 출력 : %s' %myList) # 리스트 전체를 출력

for i in range(10) : # 리스트 셀을 출력
    print('List 출력 : %d' %myList[i])
for i in range(10) : 
    myList[i] = i
for i in range(10) : 
    print('List 출력 : %d' %myList[i])
