"""Filtro para excluir preguntas de respuesta corta en archivos de preguntas (.md, .txt)."""
import re
import sys


def filtrar(ruta_entrada, ruta_salida=None):
    with open(ruta_entrada, "r", encoding="utf-8") as f:
        texto = f.read()

    bloques = re.split(r"(?=\[TIPO:)", texto)
    conservados = []
    descartados = 0

    for bloque in bloques:
        coincidencia = re.match(r"\[TIPO:\s*(.*?)\]", bloque.strip())
        if coincidencia and "RESPUESTA CORTA" in coincidencia.group(1).upper():
            descartados += 1
            continue
        if bloque.strip():
            conservados.append(bloque.strip())

    salida = "\n\n".join(conservados) + "\n"
    ruta_salida = ruta_salida or ruta_entrada
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(salida)

    return descartados, len(conservados)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python filtrar_respuesta_corta.py entrada.[md|txt] [salida.[md|txt]]")
        sys.exit(1)
    entrada = sys.argv[1]
    destino = sys.argv[2] if len(sys.argv) > 2 else None
    descartadas, restantes = filtrar(entrada, destino)
    print(f"Preguntas de respuesta corta excluidas: {descartadas}")
    print(f"Preguntas conservadas: {restantes}")
