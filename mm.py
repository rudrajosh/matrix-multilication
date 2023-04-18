print("welcome to matrix world")
c = int(input("enter 1 or 2 or 3:\n"))
if c==1:
	# same result will be obtained when we use @ operator
# as shown below(only in python &gt;3.5)
import numpy as np

# input two matrices
matrix_A_cols == matrix_B_rows:
    print('Enter values for matrix A')
    matrix_A = [[int(input(f"column {j+1} -> ENter {i+1} element:")) for j in range(matrix_A_cols)] for i in range(matrix_A_rows) ]

    print() 

    print('Enter values for matrix B ')
    matrix_B = [[int(input(f"column {j+1} -> ENter {i+1} element:")) for j in range(matrix_B_cols)] for i in range(matrix_B_rows) ]

    print() 

    print('Matrix-A :')
    for i in matrix_A:
        print(i)

    print() 
    print('Matrix-B :')
    for i in matrix_B:
        print(i)

        result = [[0 for j in range(matrix_B_cols)] for i in range(matrix_A_rows)]


# This will return matrix product of two array
res = matrix_A @ matrix_B

# print resulted matrix
print(res)
elif c == 2:
matrix_A_rows = int(input('ENter number of rows for matrix-A: '))
matrix_A_cols  = int(input('ENter number of columns for matrix-A: '))

print()

matrix_B_rows = int(input('ENter number of rows for matrix-B: '))
matrix_B_cols  = int(input('ENter number of columns for matrix-B: '))

print() 

if matrix_A_cols == matrix_B_rows:
    print('Enter values for matrix A')
    matrix_A = [[int(input(f"column {j+1} -> ENter {i+1} element:")) for j in range(matrix_A_cols)] for i in range(matrix_A_rows) ]

    print() 

    print('Enter values for matrix B ')
    matrix_B = [[int(input(f"column {j+1} -> ENter {i+1} element:")) for j in range(matrix_B_cols)] for i in range(matrix_B_rows) ]

    print() 

    print('Matrix-A :')
    for i in matrix_A:
        print(i)

    print() 
    print('Matrix-B :')
    for i in matrix_B:
        print(i)

        result = [[0 for j in range(matrix_B_cols)] for i in range(matrix_A_rows)]

  
    for i in range(len(matrix_A)):
        for j in range(len(matrix_B[0])):
            for k in range(len(matrix_B)):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]
        
    print() 

    print('Multiplication of Matrix-A and Matrix-B is :')
    for i in result:  
        print(i)
        
else:
    print('Multiplication of matrices is not possible (columns of matrix-A = row of matrix-B)')
if c == 3:
	import numpy as np

# Get the matrix dimensions from the user
n = int(input("Enter the dimension of the matrix: "))

# Initialize the matrix
matrix = np.zeros((n, n))

# Get the matrix elements from the user
print("Enter the matrix elements:")
for i in range(n):
    for j in range(n):
        matrix[i][j] = float(input(f"Enter element [{i+1}][{j+1}]: "))

# Calculate the inverse of the matrix
matrix_inv = np.linalg.inv(matrix)

# Print the original matrix
print("Original matrix:")
print(matrix)

# Print the inverse of the matrix
print("Inverse of the matrix:")
print(matrix_inv)
