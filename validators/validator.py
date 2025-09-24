#validators

from matrice import Matrices

class Valids:
    def __init__(self):
        self.name = "Validators"

    @staticmethod
    def is_valid_matrix(matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_valid()
    
    @staticmethod
    def is_square(matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_square()

    @staticmethod        
    def is_identity(matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_identity()

    @staticmethod    
    def is_symmetric(matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_symmetric()

    @staticmethod    
    def is_orthogonal(matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_orthogonal()

    @staticmethod   
    def has_inverse(matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.has_inverse()

    @staticmethod    
    def is_row_echelon(matrix):
        if not isinstance(matrix, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matrix.is_row_echelon()  
    