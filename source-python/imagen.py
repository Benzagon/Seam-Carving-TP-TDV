# imagen.py

import os
import math
from typing import List
from PIL import Image as PILImage


class Imagen:

    def __init__(self, ruta: str = None):
        self._ancho: int = 0
        self._alto: int = 0
        # _pixeles[fila][col] = [R, G, B]
        self._pixeles: List[List[List[int]]] = []

        if ruta is not None:
            self.cargar(ruta)

    def cargar(self, ruta: str) -> None:
        img = PILImage.open(ruta).convert("RGB")
        self._ancho, self._alto = img.size  # PIL: (ancho, alto)

        self._pixeles = [
            [list(img.getpixel((c, f))) for c in range(self._ancho)]
            for f in range(self._alto)
        ]

    def guardar(self, ruta: str) -> None:
        if self.esta_vacia():
            raise RuntimeError("La imagen está vacía.")

        ext = os.path.splitext(ruta)[1].lower().lstrip(".")

        img = PILImage.new("RGB", (self._ancho, self._alto))
        for f in range(self._alto):
            for c in range(self._ancho):
                img.putpixel((c, f), tuple(self._pixeles[f][c]))

        if ext == "png":
            img.save(ruta, format="PNG")
        elif ext in ("jpg", "jpeg"):
            img.save(ruta, format="JPEG", quality=90)
        elif ext == "bmp":
            img.save(ruta, format="BMP")
        else:
            raise RuntimeError(f"Formato no soportado: {ext}. Usar .png, .jpg o .bmp")

    def ancho(self) -> int:
        return self._ancho

    def alto(self) -> int:
        return self._alto

    def esta_vacia(self) -> bool:
        return self._ancho == 0 or self._alto == 0

    def _pixel(self, fila: int, col: int) -> List[int]:
        """Devuelve el píxel con clamp en los bordes (equivalente al lambda en C++)."""
        fila = max(0, min(self._alto - 1, fila))
        col  = max(0, min(self._ancho - 1, col))
        return self._pixeles[fila][col]

    def calcular_energia_pixel(self, fila: int, col: int) -> float:
        energia = 0.0
        for canal in range(3):
            dx = float(self._pixel(fila, col + 1)[canal]) - float(self._pixel(fila, col - 1)[canal])
            dy = float(self._pixel(fila + 1, col)[canal]) - float(self._pixel(fila - 1, col)[canal])
            energia += dx * dx + dy * dy
        return math.sqrt(energia)

    def obtener_matriz_energia(self) -> List[List[float]]:
        return [
            [self.calcular_energia_pixel(f, c) for c in range(self._ancho)]
            for f in range(self._alto)
        ]

    def eliminar_seam(self, seam: List[int]) -> None:
        if len(seam) != self._alto:
            raise RuntimeError("El seam debe tener exactamente una entrada por fila.")

        for f in range(self._alto):
            col = seam[f]
            del self._pixeles[f][col]

        self._ancho -= 1