A = [[12,2,6],
    [9 ,5,5],
    [3 ,3,4]]

B = [[3,8,7],
    [9,7,4],
    [0,6,1]]

result=[[A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]

for m in result:
   print(m)
