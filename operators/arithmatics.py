import math
from matrice import Matrices

class Arithmatric:
    def __init__(self):
        self.matrice = Matrices()
        self.result = None
        self.history = []
        self.history_index = -1

    def multiply(self, a, b):
        self.result = self.matrice.multiply(a, b)
        self._add_to_history(self.result)
        return self.result
    
    def add(self, a, b):
        self.result = self.matrice.add(a, b)
        self._add_to_history(self.result)
        return self.result
    
    def subtract(self, a, b):
        self.result = self.matrice.subtract(a, b)
        self._add_to_history(self.result)
        return self.result
    
    def divide(self, a, b):
        self.result = self.matrice.divide(a, b)
        self._add_to_history(self.result)
        return self.result
    
    def power(self, a, b):
        self.result = self.matrice.power(a, b)
        self._add_to_history(self.result)
        return self.result
    
    