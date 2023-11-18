#행렬의 각 원소 출력하기
matrix=[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]
size=len(matrix)
for i in range(size):
    for j in range(size):
        print('(%d,%d) : %d' %(i,j,matrix[i][j]))
