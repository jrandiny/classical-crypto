import numpy as np
import sympy

from nptyping import NDArray, Int


class MatrixUtil:
    @staticmethod
    def minor_matrix(matrix: NDArray, i: int, j: int) -> NDArray:
        deleted_row = np.delete(matrix, i, 0)
        return np.delete(deleted_row, j, 1)

    @staticmethod
    def inverse_mod_matrix(matrix: NDArray, modulus: int = 26) -> NDArray:
        dim = len(matrix)
        adjoin = np.zeros(shape=(dim, dim), dtype=int)

        for i in range(dim):
            for j in range(dim):
                minor_matrix = MatrixUtil.minor_matrix(matrix, i, j)
                adjoin[i][j] = round(
                    (-1)**(i + j) * np.linalg.det(minor_matrix))

        adjoin = np.transpose(adjoin)
        determinant = round(np.linalg.det(matrix) % modulus)
        det_inverse = round(sympy.mod_inverse(determinant, modulus))
        return det_inverse * (adjoin % modulus) % modulus