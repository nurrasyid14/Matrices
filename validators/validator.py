#validators

from matrice import Matrices

class Valids:
    def __init__(self):
        self.name = "Validators"

    @staticmethod
    def is_valid_matr(matr):
        if not isinstance(matr, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matr.is_valid()
    
    @staticmethod
    def is_square(matr):
        if not isinstance(matr, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matr.is_square()

    @staticmethod        
    def is_identity(matr):
        if not isinstance(matr, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matr.is_identity()

    @staticmethod    
    def is_symmetric(matr):
        if not isinstance(matr, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matr.is_symmetric()

    @staticmethod    
    def is_orthogonal(matr):
        if not isinstance(matr, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matr.is_orthogonal()

    @staticmethod   
    def has_inverse(matr):
        if not isinstance(matr, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matr.has_inverse()

    @staticmethod    
    def is_row_echelon(matr):
        if not isinstance(matr, Matrices):
            raise TypeError("Input must be a Matrice instance.")
        return matr.is_row_echelon()  
    