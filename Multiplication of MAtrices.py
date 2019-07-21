A = [[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]] 
      
B = [[1, 4, 7, 11], 
    [2, 5, 8, 12], 
    [3, 6, 9, 13]] 
      
result = [[0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]] 
  
 
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j] 
  
for m in result: 
    print(m) 
