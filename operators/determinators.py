from matrice import Matrices
from operators.arithmatics import Arithmatric
from validators.validator import Valids

class Determinant:
    def __init__(self):
        self.name = "Determinant"
        self.valid = Valids()
        self.arith = Arithmatric()

    def sarrus(self, matr):
        if not isinstance(matr, Matrices):
            raise TypeError("Input must be a Matrices instance.")
        if not Valids.is_square(matr) or matr.rows not in (2, 3):
            raise ValueError("Sarrus' rule is only applicable to 2x2 or 3x3 square matrices.")

        a = matr.data

        # Case: 2x2 matrix
        if matr.rows == 2:
            return a[0][0] * a[1][1] - a[0][1] * a[1][0]

        # Case: 3x3 matrix
        determinant = (a[0][0] * a[1][1] * a[2][2] +
                    a[0][1] * a[1][2] * a[2][0] +
                    a[0][2] * a[1][0] * a[2][1]) - (
                    a[0][2] * a[1][1] * a[2][0] +
                    a[0][0] * a[1][2] * a[2][1] +
                    a[0][1] * a[1][0] * a[2][2])
        return determinant

    def laplace(self, matr):
        if not isinstance(matr, Matrices):
            raise TypeError("Input must be a Matrices instance.")
        if not Valids.is_square():
            raise ValueError("Laplace expansion is only applicable to square matrices.")
        
        def minor(m, i, j):
            return Matrices([row[:j] + row[j+1:] for k, row in enumerate(m.data) if k != i])
        
        def determinant_recursive(m):
            if m.rows == 1:
                return m.data[0][0]
            if m.rows == 2:
                return m.data[0][0] * m.data[1][1] - m.data[0][1] * m.data[1][0]
            
            det = 0
            for c in range(m.cols):
                det += ((-1) ** c) * m.data[0][c] * determinant_recursive(minor(m, 0, c))
            return det
        
        return determinant_recursive(matr)
    
    def minor_cofactor(self, matr, i, j):
        if not isinstance(matr, Matrices):
            raise TypeError("Input must be a Matrices instance.")
        if not matr.is_square():
            raise ValueError("Minor and cofactor are only applicable to square matrices.")
        if i < 0 or i >= matr.rows or j < 0 or j >= matr.cols:
            raise IndexError("Row and column indices must be within matr dimensions.")
        
        def minor(m, i, j):
            return Matrices([row[:j] + row[j+1:] for k, row in enumerate(m.data) if k != i])
        
        minor_matr = minor(matr, i, j)
        minor_det = self.laplace(minor_matr)
        cofactor = ((-1) ** (i + j)) * minor_det
        return minor_det, cofactor
    