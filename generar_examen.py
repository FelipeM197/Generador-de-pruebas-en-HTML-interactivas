"""Punto de entrada de consola para la generación de exámenes interactivos."""
import os
import sys

DIR_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if DIR_SRC not in sys.path:
    sys.path.insert(0, DIR_SRC)

from generar_examen import generar_desde_archivo, principal


if __name__ == "__main__":
    principal()
