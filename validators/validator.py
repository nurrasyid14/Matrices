#validators

from matrice import Matrices

class Valids:
    def __init__(self):
        self.name = "Validators"

    def is_valid_matrix(self, matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_valid()
    
    def is_square(self, matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_square()
        
    def is_identity(self, matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_identity()
    
    def is_symmetric(self, matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_symmetric()
    
    def is_orthogonal(self, matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_orthogonal()
    
    def has_inverse(self, matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.has_inverse()
    
    def is_row_echelon(self, matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_row_echelon()  
    