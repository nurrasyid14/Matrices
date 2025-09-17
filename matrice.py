import numpy as np
import sympy as sp

class Matrices:
    """
    Kelas untuk merepresentasikan objek matriks.
    Mendukung operasi numerik (numpy) dan simbolik (sympy).
    """

    def __init__(self, data):
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise TypeError("Data harus berupa list of lists.")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

        if not all(len(row) == self.cols for row in data):
            raise ValueError("Semua baris harus memiliki jumlah kolom yang sama.")

        # Cek apakah ada elemen simbolik
        self.is_symbolic = any(
            isinstance(el, sp.Basic) for row in data for el in row
        )

    # ------------------------
    # Representasi
    # ------------------------
    def __repr__(self):
        return "\n".join(str(row) for row in self.data)

    def to_numpy(self):
        return np.array(self.data, dtype=complex if self.has_complex() else float)

    def to_sympy(self):
        return sp.Matrix(self.data)

    def has_complex(self):
        return any(isinstance(el, complex) for row in self.data for el in row)

    # ------------------------
    # Operasi dasar
    # ------------------------
    def __add__(self, other):
        if not isinstance(other, Matrices):
            raise TypeError("Penjumlahan hanya didukung antar Matrices.")
        return Matrices(
            [[self.data[i][j] + other.data[i][j] for j in range(self.cols)]
             for i in range(self.rows)]
        )

    def __sub__(self, other):
        if not isinstance(other, Matrices):
            raise TypeError("Pengurangan hanya didukung antar Matrices.")
        return Matrices(
            [[self.data[i][j] - other.data[i][j] for j in range(self.cols)]
             for i in range(self.rows)]
        )

    def __mul__(self, other):
        if isinstance(other, (int, float, complex, sp.Basic)):  # skalar
            return Matrices([[el * other for el in row] for row in self.data])
        elif isinstance(other, Matrices):  # perkalian matriks
            if self.cols != other.rows:
                raise ValueError("Dimensi tidak cocok untuk perkalian matriks.")
            result = [
                [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                 for j in range(other.cols)]
                for i in range(self.rows)
            ]
            return Matrices(result)
        else:
            raise TypeError("Tipe tidak didukung untuk perkalian.")

    # ------------------------
    # Operasi lanjutan (via sympy)
    # ------------------------
    def transpose(self):
        return Matrices([[self.data[j][i] for j in range(self.rows)]
                         for i in range(self.cols)])

    def determinant(self):
        return self.to_sympy().det()

    def inverse(self):
        return Matrices(self.to_sympy().inv().tolist())

    def differentiate(self, symbol):
        """Turunan setiap elemen matriks terhadap variabel tertentu"""
        sym = sp.symbols(symbol) if isinstance(symbol, str) else symbol
        return Matrices([[sp.diff(el, sym) for el in row] for row in self.data])

    def integrate(self, symbol):
        """Integral setiap elemen matriks terhadap variabel tertentu"""
        sym = sp.symbols(symbol) if isinstance(symbol, str) else symbol
        return Matrices([[sp.integrate(el, sym) for el in row] for row in self.data])
