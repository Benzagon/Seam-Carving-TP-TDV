# fuerza_bruta.py

from typing import List


def _fb(energia: List[List[float]], i: int, j: int, n: int, m: int,
        curr: List[int], curr_energia: float,
        best: List[int], best_energia: float) -> float:
    """O(3^n)"""
    # CASO BASE
    if i == n and 0 <= j < m:
        if curr_energia < best_energia:
            best_energia = curr_energia
            best[:] = curr  # equivalente a best = curr en C++ (copia por valor)
    elif 0 <= j < m:
        curr.append(j)
        curr_energia += energia[i][j]

        # BAJO VERTICAL
        best_energia = _fb(energia, i+1, j,   n, m, curr, curr_energia, best, best_energia)
        # BAJO A LA IZQ
        best_energia = _fb(energia, i+1, j-1, n, m, curr, curr_energia, best, best_energia)
        # BAJO A LA DER
        best_energia = _fb(energia, i+1, j+1, n, m, curr, curr_energia, best, best_energia)

        curr.pop()
        curr_energia -= energia[i][j]

    return best_energia


def encontrar_seam_fuerza_bruta(energia: List[List[float]]) -> List[int]:
    """O(3^n * m)"""
    n = len(energia)
    m = len(energia[0])

    curr: List[int] = []
    curr_energia: float = 0.0

    best: List[int] = []
    best_energia: float = float("inf")

    # O(m * 3^n)
    for i in range(m):
        best_energia = _fb(energia, 0, i, n, m, curr, curr_energia, best, best_energia)

    return best