from matrice import Matrices
import sympy as sp
from operators import Arithmatric, Calculus, Trigonometric, Determinant, LinAlgebra
import math
import sympy as sp

A = Matrices([[8, 2], [3, 4]])
B = Matrices([[5, 6], [7, 8]])

det = Determinant()
calc = Calculus()
arith = Arithmatric()
trig = Trigonometric()
lin = LinAlgebra()

determinant = det.sarrus(A)
print(f"Determinant of A using Sarrus' rule: {determinant}")