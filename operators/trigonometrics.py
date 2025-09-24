import sympy as sympy
import numpy as np
from matrice import Matrices

class Trigonometric:
    def __init__(self):
        pass

    def sin(self, matr):
        if isinstance(matr, matrices.Matrix):
            return matrices.Matrix(np.sin(matr.data))
        else:
            raise TypeError("Input must be a Matrix instance")

    def cos(self, matr):
        if isinstance(matr, matrices.Matrix):
            return matrices.Matrix(np.cos(matr.data))
        else:
            raise TypeError("Input must be a Matrix instance")

    def tan(self, matr):
        if isinstance(matr, matrices.Matrix):
            return matrices.Matrix(np.tan(matr.data))
        else:
            raise TypeError("Input must be a Matrix instance")
        
    def cot(self, matr):
        if isinstance(matr, matrices.Matrix):
            return matrices.Matrix(1/np.tan(matr.data))
        else:
            raise TypeError("Input must be a Matrix instance")
        
    def sec(self, matr):
        if isinstance(matr, matrices.Matrix):
            return matrices.Matrix(1/np.cos(matr.data))
        else:
            raise TypeError("Input must be a Matrix instance")
        
    def csc(self, matr):
        if isinstance(matr, matrices.Matrix):
            return matrices.Matrix(1/np.sin(matr.data))
        else:
            raise TypeError("Input must be a Matrix instance")