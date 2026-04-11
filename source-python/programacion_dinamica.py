# programacion_dinamica.py

import math
from typing import List, Tuple, Optional

# Tipo equivalente a std::pair<std::vector<int>, double>
Carving = Tuple[List[int], float]

INVALIDO: Carving = ([], float("inf"))


def _min_carving(abajo: Carving, izq: Carving, der: Carving) -> Carving:
    if izq[1] <= abajo[1] and izq[1] <= der[1]:
        return izq
    elif der[1] <= abajo[1] and der[1] <= izq[1]:
        return der
    return abajo


def _pd(energia: List[List[float]], i: int, j: int, n: int, m: int,
        memo: List[List[Optional[Carving]]]) -> Carving:

    if not (0 <= j < m):
        return INVALIDO

    # Si ya calculé la pos
    if memo[i][j] is not None:
        return memo[i][j]

    # CASO BASE
    if i == n - 1:
        elem: Carving = ([j], energia[i][j])
        memo[i][j] = elem
        return elem

    # BAJO VERTICAL
    abajo = _pd(energia, i+1, j,   n, m, memo)
    # BAJO A LA IZQ
    izq   = _pd(energia, i+1, j-1, n, m, memo)
    # BAJO A LA DER
    der   = _pd(energia, i+1, j+1, n, m, memo)

    minimo = _min_carving(abajo, izq, der)

    # Equivalente a min.first.insert(min.first.begin(), j)
    seam  = [j] + minimo[0]
    valor = minimo[1] + energia[i][j]
    resultado: Carving = (seam, valor)

    memo[i][j] = resultado
    return resultado


def encontrar_seam_pd(energia: List[List[float]]) -> List[int]:
    """O(n*m)"""
    n = len(energia)
    m = len(energia[0])

    # Popular memo con None (equivalente a NaN en C++)
    memo: List[List[Optional[Carving]]] = [[None] * m for _ in range(n)]

    best: List[int] = []
    best_energia: float = float("inf")

    for i in range(m):
        seam, energia_seam = _pd(energia, 0, i, n, m, memo)
        if energia_seam < best_energia:
            best = seam
            best_energia = energia_seam

    return best