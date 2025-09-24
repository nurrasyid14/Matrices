import sympy as sympy
import numpy as np
from matrice import Matrices

class Trigonometric:
    def __init__(self):
        pass

    def sin(self, matrix):
        if isinstance(matrix, matrices.Matrix):
            return matrices.Matrix(np.sin(matrix.data))
        else:
            raise TypeError("Input must be a Matrix instance")

    def cos(self, matrix):
        if isinstance(matrix, matrices.Matrix):
            return matrices.Matrix(np.cos(matrix.data))
        else:
            raise TypeError("Input must be a Matrix instance")

    def tan(self, matrix):
        if isinstance(matrix, matrices.Matrix):
            return matrices.Matrix(np.tan(matrix.data))
        else:
            raise TypeError("Input must be a Matrix instance")
        
    def cot(self, matrix):
        if isinstance(matrix, matrices.Matrix):
            return matrices.Matrix(1/np.tan(matrix.data))
        else:
            raise TypeError("Input must be a Matrix instance")
        
    def sec(self, matrix):
        if isinstance(matrix, matrices.Matrix):
            return matrices.Matrix(1/np.cos(matrix.data))
        else:
            raise TypeError("Input must be a Matrix instance")
        
    def csc(self, matrix):
        if isinstance(matrix, matrices.Matrix):
            return matrices.Matrix(1/np.sin(matrix.data))
        else:
            raise TypeError("Input must be a Matrix instance")