def diagonal_difference(matrix):
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    n=len(matrix)
    l=0
    r=len(matrix[0])-1
    for i in range(n):
        left_diagonal_sum +=matrix[i][l]
        right_diagonal_sum +=matrix[i][r]
        l +=1
        r -=1
    return abs(left_diagonal_sum - right_diagonal_sum)



print(diagonal_difference([[1,2,3],[4,5,6],[9,8,9]]))