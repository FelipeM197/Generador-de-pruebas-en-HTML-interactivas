"""Punto de entrada para la generación de exámenes interactivos en formato HTML."""
import os
import sys

from md_parser import parsear_md
from txt_parser import parsear_txt
from html_generator import generar_html


def generar_desde_archivo(ruta_entrada, ruta_salida=None):
    if not os.path.isfile(ruta_entrada):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_entrada}")

    extension = os.path.splitext(ruta_entrada)[1].lower()
    nombre_base = os.path.splitext(os.path.basename(ruta_entrada))[0]

    if extension in (".md", ".markdown"):
        preguntas, avisos = parsear_md(ruta_entrada)
        formato = "Markdown (opción múltiple / respuesta corta / relación)"
    elif extension == ".txt":
        preguntas, avisos = parsear_txt(ruta_entrada)
        formato = "Texto plano (relación / emparejamiento)"
    else:
        raise ValueError(f"Extensión no admitida: {extension} (se requiere .md o .txt)")

    if not preguntas:
        raise ValueError(
            f"No fue posible extraer preguntas de '{ruta_entrada}'. "
            f"Verifique la estructura del archivo para la extensión {extension}."
        )

    # Las referencias de imagen se resuelven de forma absoluta respecto al archivo origen
    # para permitir que el generador HTML incruste los datos correctamente.
    carpeta_origen = os.path.dirname(os.path.abspath(ruta_entrada))
    for pregunta in preguntas:
        ruta_imagen = pregunta.get("imagen")
        if ruta_imagen and not os.path.isabs(ruta_imagen):
            pregunta["imagen"] = os.path.join(carpeta_origen, ruta_imagen)

    ruta_salida = ruta_salida or os.path.join(os.path.dirname(ruta_entrada) or ".", f"{nombre_base}.html")

    titulo = f"Examen: {nombre_base}"
    identificador = generar_html(preguntas, ruta_salida, titulo=titulo, id_examen=nombre_base)

    print(f"Formato procesado   : {formato}")
    print(f"Preguntas obtenidas : {len(preguntas)}")
    conteo_tipos = {}
    for pregunta in preguntas:
        tipo = pregunta["tipo"]
        conteo_tipos[tipo] = conteo_tipos.get(tipo, 0) + 1
    for tipo, total in conteo_tipos.items():
        print(f"  - {tipo}: {total}")
    if avisos:
        print(f"Avisos durante la lectura ({len(avisos)}):")
        for aviso in avisos[:20]:
            print(f"  * {aviso}")
        if len(avisos) > 20:
            print(f"  ... y {len(avisos) - 20} avisos adicionales.")
    print(f"Archivo generado    : {ruta_salida} (identificador: {identificador})")
    return ruta_salida


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python generar_examen.py archivo_entrada.[md|txt] [archivo_salida.html]")
        sys.exit(1)
    entrada = sys.argv[1]
    salida = sys.argv[2] if len(sys.argv) > 2 else None
    generar_desde_archivo(entrada, salida)
