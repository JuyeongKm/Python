myList = [30, 10, 20] # 리스트 초기화

myList.append(40)

#리스트 전체 출력은 %s
print('append(40) 후의 리스트 = %s' %myList )

print('pop()으로 추출한 값 = %s' %myList.pop() )
# 정수이므로, %d 해도 됨
print('pop() 후의 리스트 = %s' %myList )

myList('sort()')
print('sort() 후의 리스트 = %s' %myList )

myList.reverse()
print('reverse() 후의 리스트 = %s' %myList )

print('20 값의 위치 = %d' %myList.index(20) )
