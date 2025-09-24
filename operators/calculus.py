from matrice import Matrices
import numpy as np
import sympy as sp
from operators.trigonometrics import Trigonometric

class Calculus:
    def __init__(self):
        self.matrices = matrices()
        self.x = sp.symbols('x')
        self.y = sp.symbols('y')
        self.z = sp.symbols('z')
        self.t = sp.symbols('t')
        self.e = sp.E
        self.pi = sp.pi
        self.i = sp.I
        self.ln = sp.ln
        self.sin = sp.sin
        self.cos = sp.cos
        self.tan = sp.tan
        self.csc = sp.csc
        self.sec = sp.sec
        self.cot = sp.cot

    def derivative(self, func, var):
        return sp.diff(func, var)
    
    def integral(self, func, var):
        return sp.integrate(func, var)
    
    def limit(self, func, var, point):
        return sp.limit(func, var, point)
    
    def taylor_series(self, func, var, point, order):
        return sp.series(func, var, point, order).removeO()
    
    def hessian(self, func, vars):
        return sp.hessian(func, vars)
    
    def gradient(self, func, vars):
        pass