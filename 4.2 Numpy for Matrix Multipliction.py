import numpy as np

print("Matrix Multiplication: 5x3 matrix × 3x2 matrix")
print("="*50)

# Get input for 5x3 matrix
print("\nEnter elements for 5x3 matrix:")
matrix_5x3 = []
for i in range(5):
    row = []
    for j in range(3):
        element = int(input(f"Enter element at position [{i+1},{j+1}]: "))
        row.append(element)
    matrix_5x3.append(row)

# Convert to numpy array
matrix_a = np.array(matrix_5x3)

# Get input for 3x2 matrix
print("\nEnter elements for 3x2 matrix:")
matrix_3x2 = []
for i in range(3):
    row = []
    for j in range(2):
        element = int(input(f"Enter element at position [{i+1},{j+1}]: "))
        row.append(element)
    matrix_3x2.append(row)

# Convert to numpy array
matrix_b = np.array(matrix_3x2)

# Display input matrices
print("\n" + "="*50)
print("Input Matrices:")
print("\n5x3 Matrix A:")
print(matrix_a)
print("\n3x2 Matrix B:")
print(matrix_b)

# Perform matrix multiplication
product_matrix = np.dot(matrix_a, matrix_b)

# Display the product matrix
print("\n" + "="*50)
print("Product Matrix (5x2):")
print(product_matrix)

# Alternative method using @ operator
print("\nProduct Matrix (using @ operator):")
print(matrix_a @ matrix_b)

# Display dimensions
print(f"\nDimensions of product matrix: {product_matrix.shape}")
