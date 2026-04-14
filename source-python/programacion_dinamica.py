# programacion_dinamica.py

import math
from typing import List, Tuple, Optional

Carving = Tuple[int, float]

INVALIDO: Carving = (-1, float("inf"))


def _min_carving(abajo: Carving, izq: Carving, der: Carving, j: int) -> Carving:
    if izq[1] <= abajo[1] and izq[1] <= der[1]:
        return (j - 1, izq[1])
    elif der[1] <= abajo[1] and der[1] <= izq[1]:
        return (j + 1, der[1])
    return (j, abajo[1])


def _pd(energia: List[List[float]], i: int, j: int, n: int, m: int,
        memo: List[List[Optional[Carving]]]) -> Carving:

    if not (0 <= j < m):
        return INVALIDO

    if memo[i][j] is not None:
        return memo[i][j]

    if i == n - 1:
        elem: Carving = (-1, energia[i][j])
        memo[i][j] = elem
        return elem

    abajo = _pd(energia, i+1, j,   n, m, memo)
    izq   = _pd(energia, i+1, j-1, n, m, memo)
    der   = _pd(energia, i+1, j+1, n, m, memo)

    minimo = _min_carving(abajo, izq, der, j)
    resultado: Carving = (minimo[0], minimo[1] + energia[i][j])

    memo[i][j] = resultado
    return resultado


def _reconstruir(memo: List[List[Optional[Carving]]], best: int, n: int) -> List[int]:
    res = [best]
    prev = best
    for i in range(n - 1):
        prev = memo[i][prev][0]
        res.append(prev)
    return res


def encontrar_seam_pd(energia: List[List[float]]) -> List[int]:
    """O(n*m)"""
    n = len(energia)
    m = len(energia[0])

    memo: List[List[Optional[Carving]]] = [[None] * m for _ in range(n)]

    best: int = -1
    best_energia: float = float("inf")

    for i in range(m):
        col, energia_seam = _pd(energia, 0, i, n, m, memo)
        if energia_seam < best_energia:
            best = i
            best_energia = energia_seam

    return _reconstruir(memo, best, n)