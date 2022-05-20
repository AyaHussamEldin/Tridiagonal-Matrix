import math
size_matrix = int(input("Enter size the matrix that you want : "))  
if size_matrix <= 3:
    print("Please enter the size that is greater than 3")
    exit()
  
diagonal = []
numbers1 = [[0 for j in range(0, size_matrix)]
            for i in range(0, size_matrix)]
for a in range(size_matrix):
    numbers1 = int(input(f"Enter the numbers for the main diagonal for position[{a}][{a}] : "))
    diagonal.append(numbers1)
diagonalAbove = []
print("-----------------------------------------------------------------------------------")
for k in range(size_matrix-1):
    numbers2 = int(input("Enter the numbers for diagonal above the main diagonal for position[k][k+1]: "))
    diagonalAbove.append(numbers2)
diagonalBelow = []
print("-----------------------------------------------------------------------------------")
for z in range(size_matrix-1):
    numbers3 = int(input("Enter the numbers for diagonal below the main diagonal for position[z+1][z]: "))
    diagonalBelow.append(numbers3)
print("-----------------------------------------------------------------------------------")
result= []
for s in range(size_matrix):
    numbers4 = int(input("Enter the numbers result for position[s+1][s]: "))
    result.append(numbers4)
print("-----------------------------------------------------------------------------------")
def tridiagonal(size_matrix, diagonal, diagonalAbove, diagonalBelow):
    matrix = [[0 for j in range(size_matrix)]
              for i in range(size_matrix)]
    for k in range(size_matrix-1):
        matrix[k][k] = diagonal[k]
        matrix[k][k+1] = diagonalAbove[k]
        matrix[k+1][k] = diagonalBelow[k]
    matrix[size_matrix-1][size_matrix - 1] = diagonal[size_matrix-1]
    for row in matrix:
        print(row)
    return "this is the tridiagonal matrix"
print(tridiagonal(size_matrix, diagonal, diagonalAbove, diagonalBelow))
#Step 1 
diagonal[1] = diagonal[1]-(diagonalBelow[0]/diagonal[0])*diagonalAbove[0]
result[1] = result[1]-(diagonalBelow[0]/diagonal[0])*result[0]
diagonalBelow[0] = diagonalBelow[0]-(diagonalBelow[0]/diagonal[0])*diagonal[0]
#Step 2
diagonal[2] = diagonal[2]-(diagonalBelow[1]/diagonal[1])*diagonalAbove[1]
result[2] = result[2]-(diagonalBelow[1]/diagonal[1])*result[1]
diagonalBelow[1] = diagonalBelow[1]-(diagonalBelow[1]/diagonal[1])*diagonal[1]
#Step 3
diagonal[3] = diagonal[3]-(diagonalBelow[2]/diagonal[2])*diagonalAbove[2]
result[3] = result[3]-(diagonalBelow[2]/diagonal[2])*result[2]
diagonalBelow[2] = diagonalBelow[2]-(diagonalBelow[2]/diagonal[2])*diagonal[2]
#Step 4
print(tridiagonal(size_matrix, diagonal, diagonalAbove, diagonalBelow))
print(" X4 =",result[3]/diagonal[3])
print(" X3 =",(result[2]-((result[3]/diagonal[3])*diagonalAbove[2]))/diagonal[2])
print(" X2 =",(result[1]-(((result[2]-((result[3]/diagonal[3])*diagonalAbove[2]))/diagonal[2])*diagonalAbove[1]))/diagonal[1])
print(" X1 =",(result[0]-(((result[1]-(((result[2]-((result[3]/diagonal[3])*diagonalAbove[2]))/diagonal[2])*diagonalAbove[1]))/diagonal[1])*diagonalAbove[0]))/diagonal[0])