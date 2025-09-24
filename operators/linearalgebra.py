#linearalgebra.py

from matrice import Matrices
from operators.arithmatics import Arithmatric
from operators.calculus import Calculus
from validators import Valids

class LinAlgebra(Valids, Matrices, Arithmatric, Calculus):
    def __init__(self):
        super().__init__()
        self.name = "LinAlgebra"
    
    def dot_product(self, matr_a, matr_b):
        if not self.is_valid_matr(matr_a) or not self.is_valid_matr(matr_b):
            raise ValueError("Invalid matrices provided.")
        if len(matr_a[0]) != len(matr_b):
            raise ValueError("Incompatible matr dimensions for dot product.")
        
        result = [[0 for _ in range(len(matr_b[0]))] for _ in range(len(matr_a))]
        for i in range(len(matr_a)):
            for j in range(len(matr_b[0])):
                for k in range(len(matr_b)):
                    result[i][j] += matr_a[i][k] * matr_b[k][j]
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
    
    def matr_inverse(self, matr):
        if not self.is_valid_matr(matr):
            raise ValueError("Invalid matr provided.")
        if len(matr) != len(matr[0]):
            raise ValueError("Only square matrices can be inverted.")
        
        n = len(matr)
        identity = self.identity_matr(n)
        augmented = [row[:] + identity_row[:] for row, identity_row in zip(matr, identity)]
        
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
    
    def identity_matr(self, size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    
    def transpose(self, matr):
        if not self.is_valid_matr(matr):
            raise ValueError("Invalid matr provided.")
        return [[matr[j][i] for j in range(len(matr))] for i in range(len(matr[0]))]
