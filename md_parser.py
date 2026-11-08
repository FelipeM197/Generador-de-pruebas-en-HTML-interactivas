"""Adaptador para análisis de archivos Markdown."""
from lector_preguntas import parsear_archivo, parsear_bloques_tipo


def parsear_md(ruta_entrada):
    return parsear_archivo(ruta_entrada)


if __name__ == "__main__":
    import sys
    ruta = sys.argv[1] if len(sys.argv) > 1 else "Preguntas_BDD.md"
    preguntas, lista_avisos = parsear_md(ruta)
    print(f"Preguntas extraidas: {len(preguntas)}")
    resumen_tipos = {}
    for item in preguntas:
        resumen_tipos[item["tipo"]] = resumen_tipos.get(item["tipo"], 0) + 1
    print("Distribucion por tipo:", resumen_tipos)
    for aviso in lista_avisos:
        print("Aviso:", aviso)
