"""Adaptador para análisis de archivos de texto plano."""
from lector_preguntas import parsear_archivo, parsear_bloques_columnas


def parsear_txt(ruta_entrada):
    return parsear_archivo(ruta_entrada)


if __name__ == "__main__":
    import sys
    ruta = sys.argv[1] if len(sys.argv) > 1 else "Preguntas_BigData.txt"
    preguntas, lista_avisos = parsear_txt(ruta)
    print(f"Preguntas de relacion extraidas: {len(preguntas)}")
    for aviso in lista_avisos:
        print("Aviso:", aviso)
