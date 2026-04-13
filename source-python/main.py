# main.py

import sys
import os
from typing import List

# Importaciones equivalentes a los headers de C++
from imagen import Imagen
from fuerza_bruta import encontrar_seam_fuerza_bruta
from backtracking import encontrar_seam_backtracking
from programacion_dinamica import encontrar_seam_pd


def leer_matriz_energia(ruta: str) -> List[List[float]]:
    """
    Lee una matriz de energía desde un archivo de texto.
    Formato esperado:
      filas columnas
      e00 e01 e02 ...
      e10 e11 e12 ...
      ...
    """
    with open(ruta, 'r') as archivo:
        filas, columnas = map(int, archivo.readline().split())
        energia = []
        for _ in range(filas):
            fila = list(map(float, archivo.readline().split()))
            energia.append(fila)
    return energia


def ejecutar_algoritmo(energia: List[List[float]], algoritmo: str) -> List[int]:
    """Ejecuta el algoritmo seleccionado y devuelve el seam encontrado."""
    if algoritmo == "fb":
        return encontrar_seam_fuerza_bruta(energia)
    if algoritmo == "bt":
        return encontrar_seam_backtracking(energia)
    if algoritmo == "pd":
        return encontrar_seam_pd(energia)
    raise ValueError(f"Algoritmo desconocido: {algoritmo}. Usar fb, bt o pd.")


def imprimir_matriz(matriz: List[List[float]]) -> None:
    for fila in matriz:
        print("\t".join(str(val) for val in fila))


def imprimir_seam(seam: List[int], energia: List[List[float]]) -> None:
    print("Seam encontrado: ", end="")
    total = 0.0
    for f, col in enumerate(seam):
        print(f"({f},{col})", end=" ")
        total += energia[f][col]
    print(f"\nEnergía total: {total}")


def modo_numerico(ruta_entrada: str, algoritmo: str) -> None:
    energia = leer_matriz_energia(ruta_entrada)

    print("Matriz de energía:")
    imprimir_matriz(energia)
    print()

    seam = ejecutar_algoritmo(energia, algoritmo)
    imprimir_seam(seam, energia)

    ruta_salida = f"output/numericos/seam_{algoritmo}.txt"
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    with open(ruta_salida, 'w') as salida:
        for f, col in enumerate(seam):
            salida.write(f"fila {f} -> columna {col}\n")
    print(f"Resultado guardado en {ruta_salida}")


def modo_imagen(ruta_imagen: str, algoritmo: str, iteraciones: int) -> None:
    img = Imagen(ruta_imagen)
    print(f"Imagen cargada: {img.ancho()}x{img.alto()} px")

    for i in range(iteraciones):
        seam = ejecutar_algoritmo(img.obtener_matriz_energia(), algoritmo)
        img.eliminar_seam(seam)

        if (i + 1) % 10 == 0 or i == iteraciones - 1:
            print(f"Iteración {i + 1}/{iteraciones} - Ancho actual: {img.ancho()} px")

    ruta_salida = f"output/imagenes/resultado_{algoritmo}.png"
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    img.guardar(ruta_salida)
    print(f"Imagen guardada en {ruta_salida}")


def imprimir_uso() -> None:
    print(
        "Uso:\n"
        "  Modo numérico: python main.py --numerico <archivo> --algoritmo <fb|bt|pd>\n"
        "  Modo imagen:   python main.py --imagen <archivo> --algoritmo <fb|bt|pd> --iteraciones <N>\n"
        "  Modo test:     python main.py --test <archivo> --iteraciones <N>\n"
        "\nEjemplos:\n"
        "  python main.py --numerico input/ejemplo.txt --algoritmo pd\n"
        "  python main.py --imagen img/foto.jpg --algoritmo pd --iteraciones 50\n"
        "  python main.py --test img/foto.jpg --iteraciones 10\n"
    )

import time
import os
import copy

def modo_test(ruta_imagen: str, algoritmo: str, iteraciones: int) -> None:
    img = Imagen(ruta_imagen)
    ancho_original = img.ancho()
    alto_original  = img.alto()
    print(f"Imagen cargada: {ancho_original}x{alto_original} px")

    ruta_csv = "../output/resultados_test.csv"
    os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)
    archivo_existe = os.path.isfile(ruta_csv)

    algoritmos = ["pd", "fb", "bt"] if algoritmo == "todos" else [algoritmo]

    with open(ruta_csv, "a", newline="") as csv:
        if not archivo_existe:
            csv.write("algoritmo,iteracion,tiempo_ms,ancho_original,alto_original,lenguaje\n")

        for algo in algoritmos:
            print(f"\n--- Algoritmo: {algo} ---")

            img_clon = copy.deepcopy(img)

            for i in range(iteraciones):
                inicio = time.perf_counter()
                seam = ejecutar_algoritmo(img_clon.obtener_matriz_energia(), algo)
                fin = time.perf_counter()

                tiempo_iter = (fin - inicio) * 1000

                print(f"  [{algo}] Iteración {i + 1} - Tiempo: {tiempo_iter:.4f} ms")

                csv.write(f"{algo},{i + 1},{tiempo_iter},{ancho_original},{ancho_original},python\n")

    print(f"\nResultados guardados en {ruta_csv}")

def main() -> int:
    args = sys.argv[1:]

    if not args:
        imprimir_uso()
        return 1

    modo = ""
    ruta_archivo = ""
    algoritmo = "pd"
    iteraciones = 1

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--numerico" and i + 1 < len(args):
            modo = "numerico"
            i += 1
            ruta_archivo = args[i]
        elif arg == "--imagen" and i + 1 < len(args):
            modo = "imagen"
            i += 1
            ruta_archivo = args[i]
        elif arg == "--test" and i + 1 < len(args):
            modo = "test"
            i += 1
            ruta_archivo = args[i]
        elif arg == "--algoritmo" and i + 1 < len(args):
            i += 1
            algoritmo = args[i]
        elif arg == "--iteraciones" and i + 1 < len(args):
            i += 1
            iteraciones = int(args[i])
        elif arg in ("--ayuda", "--help"):
            imprimir_uso()
            return 0
        i += 1

    try:
        if modo == "numerico":
            modo_numerico(ruta_archivo, algoritmo)
        elif modo == "imagen":
            modo_imagen(ruta_archivo, algoritmo, iteraciones)
        elif modo == "test":
            modo_test(ruta_archivo, algoritmo, iteraciones)
        else:
            imprimir_uso()
            return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())