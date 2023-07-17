def diagonal_sum(matrix,rows,columns):

    sum=0
    for i in range(rows):
        sum+=matrix[i][i]
    return sum

input_array=list(map(int,input().split()))
r=input_array[0]
c=input_array[1]
matrix=[]
j=2
for i in range(r):
    matrix.append(input_array[j:j+r])
    j+=r
# print(matrix)
print(diagonal_sum(matrix,r,c))

