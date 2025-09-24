import numpy as np
import sympy as sp

class Matrices:
    """
    Kelas inti untuk representasi matriks.
    Operasi dasar dipisahkan ke modul di `operations/`.
    """

    def __init__(self, data):
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise TypeError("Data harus berupa list of lists.")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

        if not all(len(row) == self.cols for row in data):
            raise ValueError("Semua baris harus memiliki jumlah kolom yang sama.")

    def __repr__(self):
        return "\n".join(str(row) for row in self.data)

    def to_numpy(self):
        """Konversi ke numpy array"""
        return np.array(self.data, dtype=complex if self.has_complex() else float)

    def to_sympy(self):
        """Konversi ke sympy Matrix"""
        return sp.Matrix(self.data)

    def has_complex(self):
        """Cek apakah ada elemen kompleks"""
        return any(isinstance(el, complex) for row in self.data for el in row)