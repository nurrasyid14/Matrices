#linearalgebra.py

from matrice import Matrices
from operators.arithmatics import Arithmatric
from operators.calculus import Calculus
from validators.validators import Validators
from utilities.exceptions import Exceptions

class LinAlgebra(Operators, Validators, Exceptions, Utils, Constants):
    def __init__(self):
        super().__init__()
        self.name = "LinAlgebra"
    
    def dot_product(self, matrix_a, matrix_b):
        if not self.is_valid_matrix(matrix_a) or not self.is_valid_matrix(matrix_b):
            raise ValueError("Invalid matrices provided.")
        if len(matrix_a[0]) != len(matrix_b):
            raise ValueError("Incompatible matrix dimensions for dot product.")
        
        result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
        for i in range(len(matrix_a)):
            for j in range(len(matrix_b[0])):
                for k in range(len(matrix_b)):
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return result
    
    def cross_product(self, vector_a, vector_b):
        if len(vector_a) != 3 or len(vector_b) != 3:
            raise ValueError("Cross product is only defined for 3-dimensional vectors.")
        
        result = [
            vector_a[1]*vector_b[2] - vector_a[2]*vector_b[1],
            vector_a[2]*vector_b[0] - vector_a[0]*vector_b[2],
            vector_a[0]*vector_b[1] - vector_a[1]*vector_b[0]
        ]
        return result
    
    def matrix_inverse(self, matrix):
        if not self.is_valid_matrix(matrix):
            raise ValueError("Invalid matrix provided.")
        if len(matrix) != len(matrix[0]):
            raise ValueError("Only square matrices can be inverted.")
        
        n = len(matrix)
        identity = self.identity_matrix(n)
        augmented = [row[:] + identity_row[:] for row, identity_row in zip(matrix, identity)]
        
        for i in range(n):
            pivot = augmented[i][i]
            if pivot == 0:
                raise ValueError("Matrix is singular and cannot be inverted.")
            for j in range(2*n):
                augmented[i][j] /= pivot
            
            for k in range(n):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2*n):
                        augmented[k][j] -= factor * augmented[i][j]
        
        inverse = [row[n:] for row in augmented]
        return inverse
    
    def identity_matrix(self, size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    
    def transpose(self, matrix):
        if not self.is_valid_matrix(matrix):
            raise ValueError("Invalid matrix provided.")
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
