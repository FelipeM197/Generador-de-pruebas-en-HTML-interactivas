"""Analizador para archivos de texto con preguntas de relacion y emparejamiento."""
import re

PATRON_COLUMNA_A = re.compile(r'^columna\s*a\b\s*:?', re.IGNORECASE)
PATRON_COLUMNA_B = re.compile(r'^columna\s*b\b\s*:?', re.IGNORECASE)
PATRON_RESPUESTAS = re.compile(r'^respuestas?(\s+correctas?)?\s*:', re.IGNORECASE)
PATRON_ENCABEZADO = re.compile(r'^(Fuente\s+\d+|Pregunta\s+\d+(\.\d+)?)\s*:', re.IGNORECASE)

PATRON_DIVISION_LETRAS = re.compile(r'(?=(?<![A-Za-z])[a-z]\.\s)')
PATRON_PREFIJO_NUMERICO = re.compile(r'^\s*(\d+)[.)\-]\s*(.*)$', re.DOTALL)
PATRON_PAR_RESPUESTA = re.compile(r'(\d+)\s*-\s*([a-zA-Z])')


def _limpiar_espacios(cadena):
    return re.sub(r'\s+', ' ', cadena).strip()


def _dividir_columna_b(texto):
    partes = re.split(PATRON_DIVISION_LETRAS, texto)
    elementos = {}
    for segmento in partes:
        segmento = _limpiar_espacios(segmento)
        if not segmento:
            continue
        coincidencia = re.match(r'^([a-zA-Z])[.)\-]\s*(.*)$', segmento)
        if coincidencia:
            elementos[coincidencia.group(1).lower()] = coincidencia.group(2).strip()
    return elementos


def _dividir_columna_a(texto):
    texto = texto.strip()
    if not texto:
        return []
    lineas = texto.split('|') if '|' in texto else texto.split('\n')

    elementos = []
    for linea in lineas:
        linea = _limpiar_espacios(linea)
        if not linea:
            continue
        coincidencia = PATRON_PREFIJO_NUMERICO.match(linea)
        if coincidencia:
            elementos.append((int(coincidencia.group(1)), coincidencia.group(2).strip()))
        else:
            elementos.append((len(elementos) + 1, linea))
    return elementos


def parsear_txt(ruta_entrada):
    with open(ruta_entrada, 'r', encoding='utf-8') as archivo:
        lineas = archivo.read().splitlines()

    preguntas = []
    avisos = []

    lineas_encabezado = []
    fuente_actual = ""
    estado = "BUSCANDO"
    lineas_col_a = []
    lineas_col_b = []
    lineas_resp = []
    contador = 0

    def cerrar_bloque():
        nonlocal contador
        if not (lineas_col_a and lineas_col_b and lineas_resp):
            return

        texto_a = "\n".join(lineas_col_a)
        texto_b = "\n".join(lineas_col_b)
        texto_resp = "\n".join(lineas_resp)

        items_a = _dividir_columna_a(texto_a)
        items_b = _dividir_columna_b(texto_b)
        mapa_respuesta = {int(n): l.lower() for n, l in PATRON_PAR_RESPUESTA.findall(texto_resp)}

        if not items_a or not items_b or not mapa_respuesta:
            referencia = lineas_encabezado[-1] if lineas_encabezado else 'posicion no identificada'
            avisos.append(f"Bloque incompleto cerca de: {referencia}")
            return

        numeros_a = {n for n, _ in items_a}
        letras_validas = set(items_b.keys())
        faltantes = [n for n in numeros_a if n not in mapa_respuesta or mapa_respuesta[n] not in letras_validas]
        if faltantes:
            referencia = lineas_encabezado[-1] if lineas_encabezado else 'posicion no identificada'
            avisos.append(f"Respuestas inconsistentes en '{referencia}' para elementos {faltantes}")

        contador += 1
        titulo = lineas_encabezado[-1] if lineas_encabezado else f"Relación {contador}"
        preguntas.append({
            "id": f"txt-{contador}",
            "tipo": "RELACION",
            "enunciado": _limpiar_espacios(titulo),
            "fuente": fuente_actual,
            "columna_a": [{"num": n, "texto": t} for n, t in sorted(items_a, key=lambda x: x[0])],
            "columna_b": [{"letra": l, "texto": t} for l, t in sorted(items_b.items())],
            "respuesta_correcta": mapa_respuesta,
            "explicacion": "",
        })

    for linea in lineas:
        linea_limpia = linea.strip()

        if PATRON_ENCABEZADO.match(linea_limpia):
            if linea_limpia.lower().startswith("fuente"):
                fuente_actual = linea_limpia

        if PATRON_COLUMNA_A.search(linea_limpia) and estado in ("BUSCANDO", "RESP"):
            if estado == "RESP":
                cerrar_bloque()
            estado = "COL_A"
            lineas_col_a = []
            lineas_col_b = []
            lineas_resp = []
            resto = PATRON_COLUMNA_A.sub('', linea_limpia, count=1).strip()
            if resto:
                lineas_col_a.append(resto)
            continue

        if PATRON_COLUMNA_B.search(linea_limpia) and estado == "COL_A":
            estado = "COL_B"
            resto = PATRON_COLUMNA_B.sub('', linea_limpia, count=1).strip()
            if resto:
                lineas_col_b.append(resto)
            continue

        if PATRON_RESPUESTAS.search(linea_limpia) and estado == "COL_B":
            estado = "RESP"
            resto = PATRON_RESPUESTAS.sub('', linea_limpia, count=1).strip()
            if resto:
                lineas_resp.append(resto)
            continue

        if estado == "COL_A":
            if linea_limpia:
                lineas_col_a.append(linea_limpia)
        elif estado == "COL_B":
            if linea_limpia:
                lineas_col_b.append(linea_limpia)
        elif estado == "RESP":
            if not linea_limpia or linea_limpia == "." or PATRON_ENCABEZADO.match(linea_limpia):
                cerrar_bloque()
                estado = "BUSCANDO"
                lineas_encabezado = []
                if PATRON_ENCABEZADO.match(linea_limpia):
                    lineas_encabezado.append(linea_limpia)
            else:
                lineas_resp.append(linea_limpia)
        else:
            if linea_limpia:
                lineas_encabezado.append(linea_limpia)
                if len(lineas_encabezado) > 3:
                    lineas_encabezado = lineas_encabezado[-3:]

    if estado == "RESP":
        cerrar_bloque()

    return preguntas, avisos


if __name__ == "__main__":
    import sys
    ruta = sys.argv[1] if len(sys.argv) > 1 else "Preguntas_BigData.txt"
    preguntas, lista_avisos = parsear_txt(ruta)
    print(f"Preguntas de relacion extraidas: {len(preguntas)}")
    for aviso in lista_avisos:
        print("Aviso:", aviso)
