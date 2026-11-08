"""Motor unificado de lectura y análisis de preguntas para archivos Markdown y de texto."""
import os
import re

PATRON_DIVISION_OPCIONES = re.compile(r'(?<![A-Za-z])([A-Z])[.)\-]\s+')
PATRON_PAR_GENERICO = re.compile(r'^\d+\s*-\s*[^,]+(?:\s*,\s*\d+\s*-\s*[^,]+)*\.?$')
PATRON_ORDEN_NUMEROS = re.compile(r'\d+(?:\s*,\s*\d+){1,}\.?\s*$')
PATRON_ORDEN_ROMANOS = re.compile(r'[IVXLCDM]+(?:\s*(?:->|,)\s*[IVXLCDM]+){1,}\.?\s*$')
VALORES_ROMANOS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

PATRON_COLUMNA_A = re.compile(r'^columna\s*a\b\s*:?', re.IGNORECASE)
PATRON_COLUMNA_B = re.compile(r'^columna\s*b\b\s*:?', re.IGNORECASE)
PATRON_RESPUESTAS = re.compile(r'^respuestas?(\s+correctas?)?\s*:', re.IGNORECASE)
PATRON_EXPLICACION = re.compile(r'^explicaci[oó]n\s*:', re.IGNORECASE)
PATRON_IMAGEN = re.compile(r'^imagen\s*:\s*(.*)$', re.IGNORECASE)
PATRON_ENCABEZADO = re.compile(r'^(Fuente\s+\d+|Pregunta\s*(?:ID:|\d+(\.\d+)?))\s*:', re.IGNORECASE)
PATRON_DIVISION_ITEMS_B = re.compile(r'(?=(?<![A-Za-z0-9])(?:[a-zA-Z]|\d+)[.)]\s)')
PATRON_PREFIJO_ITEM = re.compile(r'^\s*([a-zA-Z0-9]+)[.)\-]\s*(.*)$', re.DOTALL)
PATRON_PAR_RESPUESTA = re.compile(r'(\d+)\s*-\s*([a-zA-Z0-9]+)')


def _limpiar_espacios(cadena):
    return re.sub(r'\s+', ' ', cadena).strip()


def _dividir_opciones(texto_opciones):
    if not texto_opciones:
        return []

    coincidencias = list(PATRON_DIVISION_OPCIONES.finditer(texto_opciones))
    cortes = []
    letra_esperada = 'A'
    for match in coincidencias:
        if match.group(1) == letra_esperada:
            cortes.append(match.start())
            letra_esperada = chr(ord(letra_esperada) + 1)

    if not cortes:
        return []

    cortes.append(len(texto_opciones))
    opciones = []
    for indice in range(len(cortes) - 1):
        fragmento = texto_opciones[cortes[indice]:cortes[indice + 1]]
        fragmento = fragmento.strip().replace('\n', ' ')
        fragmento = re.sub(r'\s+', ' ', fragmento)
        if fragmento:
            opciones.append(fragmento)
    return opciones


def _contenido_opcion(opcion):
    coincidencia = re.match(r'^[A-Za-z][.)\-]\s*(.*)$', opcion)
    texto = coincidencia.group(1) if coincidencia else opcion
    return texto.strip().rstrip('.').lower()


def _es_verdadero_falso(opcion):
    return _contenido_opcion(opcion) in ('verdadero', 'falso')


def _es_opcion_valida(opcion):
    coincidencia = re.match(r'^[A-Z][.)\-]\s*(.*)$', opcion)
    cuerpo = coincidencia.group(1).strip() if coincidencia else opcion.strip()
    return len(cuerpo) > 2 and cuerpo.upper() != 'N/A'


def _quitar_marcador(opcion):
    coincidencia = re.match(r'^[A-Za-z][.)\-]\s*(.*)$', opcion, re.DOTALL)
    return (coincidencia.group(1) if coincidencia else opcion).strip()


def _romano_a_entero(texto):
    cadena = texto.strip().upper()
    if not cadena or any(caracter not in VALORES_ROMANOS for caracter in cadena):
        return None
    acumulado, previo = 0, 0
    for caracter in reversed(cadena):
        valor = VALORES_ROMANOS[caracter]
        acumulado += -valor if valor < previo else valor
        previo = max(previo, valor)
    return acumulado if acumulado > 0 else None


def _es_distractor_residual(contenido):
    return bool(re.match(r'^ninguna de las?\b', contenido.lower()))


def _cumple_criterio_mayoria(contenidos, patron):
    candidatos = [c for c in contenidos if not _es_distractor_residual(c)]
    return len(candidatos) >= 2 and all(patron.search(c) for c in candidatos)


def _extraer_columnas_desde_enunciado(enunciado):
    partes = re.split(
        r'(?=(?<![A-Za-z0-9])\d+[.)]\s)|(?=(?<![A-Za-z0-9])[A-Za-z][.)]\s)',
        enunciado,
    )
    introduccion = partes[0].strip()
    elementos_numericos, elementos_alfabeticos = [], []

    for segmento in partes[1:]:
        segmento = segmento.strip()
        segmento = re.sub(r'(?<=\.)\s*[A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+){0,2}:\s*$', '', segmento).strip()
        match_numero = re.match(r'^(\d+)[.)]\s*(.*)$', segmento, re.DOTALL)
        match_letra = re.match(r'^([A-Za-z])[.)]\s*(.*)$', segmento, re.DOTALL)

        if match_numero:
            texto = re.sub(r'\s+', ' ', match_numero.group(2)).strip().rstrip('.').strip()
            if texto:
                elementos_numericos.append((int(match_numero.group(1)), texto))
        elif match_letra:
            texto = re.sub(r'\s+', ' ', match_letra.group(2)).strip().rstrip('.').strip()
            if texto:
                elementos_alfabeticos.append((match_letra.group(1).upper(), texto))

    return introduccion, elementos_numericos, elementos_alfabeticos


def _elementos_desde_parentesis(texto):
    coincidencia = re.search(r'\(([^()]*\d+\s*:[^()]*)\)', texto)
    if not coincidencia:
        return []
    pares = re.findall(r'(\d+)\s*:\s*([^,()]+)', coincidencia.group(1))
    return [(int(num), re.sub(r'\s+', ' ', t).strip().rstrip('.').strip()) for num, t in pares]


def _quitar_parentesis_numerado(texto):
    limpio = re.sub(r'\s*\([^()]*\d+\s*:[^()]*\)', '', texto).strip()
    limpio = re.sub(r'\.{2,}$', '.', limpio)
    if limpio and not limpio.endswith('.'):
        limpio += '.'
    return limpio


def _obtener_columna_a(enunciado):
    intro, items_num, items_let = _extraer_columnas_desde_enunciado(enunciado)
    if items_num:
        return intro, items_num, items_let
    items_num = _elementos_desde_parentesis(enunciado)
    if items_num:
        return _quitar_parentesis_numerado(enunciado), items_num, []
    return intro, [], []


def _pares_de_opcion(contenido):
    return [(int(n), v.strip().rstrip('.').strip()) for n, v in re.findall(r'(\d+)\s*-\s*([^,]+)', contenido)]


def _intentar_relacion(enunciado, opciones, letra_correcta):
    contenidos = [_quitar_marcador(opcion) for opcion in opciones]
    indice_correcta = next((i for i, o in enumerate(opciones) if o[:1].upper() == letra_correcta), None)
    if indice_correcta is None:
        return None

    if _cumple_criterio_mayoria(contenidos, PATRON_PAR_GENERICO):
        pares_correcta = _pares_de_opcion(contenidos[indice_correcta])
        if not pares_correcta:
            return None
        claves_a = {n for n, _ in pares_correcta}
        intro, items_num, items_let = _obtener_columna_a(enunciado)
        if not items_num or {n for n, _ in items_num} != claves_a:
            return None

        valores = [v for _, v in pares_correcta]
        son_letras_sueltas = all(len(v) == 1 and v.isalpha() for v in valores)

        if son_letras_sueltas and items_let and {letra for letra, _ in items_let} >= {v.upper() for v in valores}:
            return {
                "modo": "letra",
                "enunciado": intro,
                "columna_a": [{"num": n, "texto": t} for n, t in sorted(items_num)],
                "columna_b": [{"letra": l.lower(), "texto": t} for l, t in sorted(items_let)],
                "respuesta_correcta": {n: v.lower() for n, v in pares_correcta},
            }

        frases, registradas = [], set()
        for opcion_texto in contenidos:
            for _, valor_par in _pares_de_opcion(opcion_texto):
                clave = valor_par.lower()
                if clave and clave not in registradas:
                    registradas.add(clave)
                    frases.append(valor_par)

        if len(frases) < len(items_num) or len(frases) > 26:
            return None

        abecedario = 'abcdefghijklmnopqrstuvwxyz'
        mapa_frase_letra = {frase.lower(): abecedario[i] for i, frase in enumerate(frases)}
        mapa_respuesta = {}
        for num, valor in pares_correcta:
            letra = mapa_frase_letra.get(valor.lower())
            if letra is None:
                return None
            mapa_respuesta[num] = letra

        if set(mapa_respuesta.keys()) != claves_a:
            return None

        return {
            "modo": "letra",
            "enunciado": intro,
            "columna_a": [{"num": n, "texto": t} for n, t in sorted(items_num)],
            "columna_b": [{"letra": mapa_frase_letra[f.lower()], "texto": f} for f in frases],
            "respuesta_correcta": mapa_respuesta,
        }

    if _cumple_criterio_mayoria(contenidos, PATRON_ORDEN_NUMEROS):
        intro, items_num, _ = _obtener_columna_a(enunciado)
        if not items_num:
            return None
        match_secuencia = PATRON_ORDEN_NUMEROS.search(contenidos[indice_correcta])
        if not match_secuencia:
            return None
        secuencia = [int(x) for x in re.findall(r'\d+', match_secuencia.group(0))]
        claves_a = {n for n, _ in items_num}
        if set(secuencia) != claves_a or len(secuencia) != len(items_num):
            return None
        mapa_posiciones = {elemento: str(pos + 1) for pos, elemento in enumerate(secuencia)}
        total = len(items_num)
        return {
            "modo": "numero",
            "enunciado": intro,
            "columna_a": [{"num": n, "texto": t} for n, t in sorted(items_num)],
            "columna_b": [{"letra": str(pos), "texto": f"{pos}ª posición"} for pos in range(1, total + 1)],
            "respuesta_correcta": mapa_posiciones,
        }

    if _cumple_criterio_mayoria(contenidos, PATRON_ORDEN_ROMANOS):
        partes = re.split(r'(?=(?<![A-Za-z0-9])[IVXLCDM]+\s*[:.]\s)', enunciado)
        intro = partes[0].strip()
        items_num = []
        for segmento in partes[1:]:
            coincidencia = re.match(r'^([IVXLCDM]+)\s*[:.]\s*(.*)$', segmento.strip(), re.DOTALL)
            if not coincidencia:
                continue
            numero = _romano_a_entero(coincidencia.group(1))
            if numero is None:
                continue
            texto = re.sub(r'\s+', ' ', coincidencia.group(2)).strip().rstrip('.').strip()
            if texto:
                items_num.append((numero, texto))

        if not items_num:
            return None

        match_secuencia = PATRON_ORDEN_ROMANOS.search(contenidos[indice_correcta])
        if not match_secuencia:
            return None

        secuencia = [_romano_a_entero(t) for t in re.split(r'\s*(?:->|,)\s*', match_secuencia.group(0).rstrip('.'))]
        if any(s is None for s in secuencia):
            return None

        claves_a = {n for n, _ in items_num}
        if set(secuencia) != claves_a or len(secuencia) != len(items_num):
            return None

        mapa_posiciones = {elemento: str(pos + 1) for pos, elemento in enumerate(secuencia)}
        total = len(items_num)
        return {
            "modo": "numero",
            "enunciado": intro,
            "columna_a": [{"num": n, "texto": t} for n, t in sorted(items_num)],
            "columna_b": [{"letra": str(pos), "texto": f"{pos}ª posición"} for pos in range(1, total + 1)],
            "respuesta_correcta": mapa_posiciones,
        }

    return None


def parsear_bloques_tipo(texto):
    bloques = re.split(r'\[TIPO:', texto)
    preguntas = []
    avisos = []
    contador = 0

    for fragmento in bloques[1:]:
        bloque = "[TIPO:" + fragmento

        match_tipo = re.search(r'\[TIPO:\s*(.*?)\]', bloque)
        match_id = re.search(r'Pregunta ID:\s*(\d+)', bloque)
        match_enunciado = re.search(r'Enunciado:\s*(.*?)(?=Imagen:|Opciones:|Respuesta Correcta:)', bloque, re.DOTALL)
        match_imagen = re.search(r'Imagen:\s*(.*?)(?=Opciones:|Respuesta Correcta:)', bloque, re.DOTALL)
        match_opciones = re.search(r'Opciones:\s*(.*?)(?=Respuesta Correcta:)', bloque, re.DOTALL)
        match_respuesta = re.search(r'Respuesta Correcta:\s*(.*?)(?=Explicaci[oó]n:)', bloque, re.DOTALL)
        match_explicacion = re.search(r'Explicaci[oó]n:\s*(.*)', bloque, re.DOTALL)

        tipo_declarado = match_tipo.group(1).strip() if match_tipo else "N/A"
        id_texto = match_id.group(1).strip() if match_id else None
        enunciado = re.sub(r'\s+', ' ', match_enunciado.group(1)).strip() if match_enunciado else ""
        imagen = re.sub(r'\s+', ' ', match_imagen.group(1)).strip() if match_imagen else None
        imagen = imagen or None

        opciones_crudas = _dividir_opciones(match_opciones.group(1)) if match_opciones else []
        opciones = [opcion for opcion in opciones_crudas if _es_opcion_valida(opcion)]
        respuesta_cruda = re.sub(r'\s+', ' ', match_respuesta.group(1)).strip() if match_respuesta else ""
        explicacion = re.sub(r'\s+', ' ', match_explicacion.group(1)).strip() if match_explicacion else ""

        if opciones and not re.match(r'^[A-Za-z][.)\-]\s', opciones[0]):
            enunciado = f"{enunciado} {opciones[0]}".strip()
            opciones = opciones[1:]

        if not id_texto or not enunciado:
            avisos.append(f"Bloque descartado por campos incompletos: {bloque[:80]!r}")
            continue

        match_letra = re.match(r'^([A-Za-z])[.)\-]?$', respuesta_cruda)
        relacion = None

        if match_letra and len(opciones) >= 2:
            opciones_vf = [o for o in opciones if _es_verdadero_falso(o)]
            if len(opciones_vf) >= 2:
                tipo_final = "VERDADERO_FALSO"
                opciones = opciones_vf
            else:
                relacion = _intentar_relacion(enunciado, opciones, match_letra.group(1).upper())
                tipo_final = "RELACION" if relacion else "MULTIPLE"
            respuesta_correcta = match_letra.group(1).upper()
        else:
            tipo_final = "CORTA"
            respuesta_correcta = respuesta_cruda
            opciones = []

        contador += 1
        if tipo_final == "RELACION":
            preguntas.append({
                "id": f"pregunta-{contador}",
                "tipo": "RELACION",
                "tipo_original": tipo_declarado,
                "modo": relacion["modo"],
                "enunciado": relacion["enunciado"],
                "opciones": [],
                "columna_a": relacion["columna_a"],
                "columna_b": relacion["columna_b"],
                "respuesta_correcta": relacion["respuesta_correcta"],
                "explicacion": explicacion,
                "imagen": imagen,
            })
        else:
            preguntas.append({
                "id": f"pregunta-{contador}",
                "tipo": tipo_final,
                "tipo_original": tipo_declarado,
                "modo": None,
                "enunciado": enunciado,
                "opciones": opciones,
                "columna_a": [],
                "columna_b": [],
                "respuesta_correcta": respuesta_correcta,
                "explicacion": explicacion,
                "imagen": imagen,
            })

    return preguntas, avisos


def _dividir_columna_b(texto):
    partes = re.split(PATRON_DIVISION_ITEMS_B, texto)
    elementos = {}
    for segmento in partes:
        segmento = _limpiar_espacios(segmento)
        if not segmento:
            continue
        coincidencia = PATRON_PREFIJO_ITEM.match(segmento)
        if coincidencia:
            clave = coincidencia.group(1).lower()
            elementos[clave] = coincidencia.group(2).strip()
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
        coincidencia = PATRON_PREFIJO_ITEM.match(linea)
        if coincidencia and coincidencia.group(1).isdigit():
            elementos.append((int(coincidencia.group(1)), coincidencia.group(2).strip()))
        else:
            elementos.append((len(elementos) + 1, linea))
    return elementos


def parsear_bloques_columnas(texto):
    lineas = texto.splitlines()
    preguntas = []
    avisos = []

    lineas_encabezado = []
    fuente_actual = ""
    estado = "BUSCANDO"
    lineas_col_a = []
    lineas_col_b = []
    lineas_resp = []
    lineas_explicacion = []
    imagen_actual = None
    contador = 0

    def cerrar_bloque():
        nonlocal contador, imagen_actual
        if not (lineas_col_a and lineas_col_b and lineas_resp):
            return

        texto_a = "\n".join(lineas_col_a)
        texto_b = "\n".join(lineas_col_b)
        texto_resp = "\n".join(lineas_resp)

        items_a = _dividir_columna_a(texto_a)
        items_b = _dividir_columna_b(texto_b)

        pares = PATRON_PAR_RESPUESTA.findall(texto_resp)
        es_orden_numerico = bool(items_b) and all(k.isdigit() for k in items_b.keys())
        mapa_respuesta = {}
        for num, val in pares:
            clave_resp = str(int(val)) if es_orden_numerico and val.isdigit() else val.lower()
            mapa_respuesta[int(num)] = clave_resp

        if not items_a or not items_b or not mapa_respuesta:
            referencia = lineas_encabezado[-1] if lineas_encabezado else 'posicion no identificada'
            avisos.append(f"Bloque incompleto cerca de: {referencia}")
            return

        numeros_a = {n for n, _ in items_a}
        claves_validas_b = set(items_b.keys())
        faltantes = [n for n in numeros_a if n not in mapa_respuesta or mapa_respuesta[n] not in claves_validas_b]
        if faltantes:
            referencia = lineas_encabezado[-1] if lineas_encabezado else 'posicion no identificada'
            avisos.append(f"Respuestas inconsistentes en '{referencia}' para elementos {faltantes}")

        contador += 1
        enunciado_crudo = lineas_encabezado[-1] if lineas_encabezado else f"Relación {contador}"
        enunciado = re.sub(r'^(instrucci[oó]n|enunciado)\s*:\s*', '', enunciado_crudo, flags=re.IGNORECASE).strip()
        explicacion = _limpiar_espacios(" ".join(lineas_explicacion))
        modo = "numero" if es_orden_numerico else "letra"

        preguntas.append({
            "id": f"pregunta-{contador}",
            "tipo": "RELACION",
            "tipo_original": "ORDENAMIENTO" if modo == "numero" else "RELACION",
            "modo": modo,
            "enunciado": _limpiar_espacios(enunciado),
            "fuente": fuente_actual,
            "opciones": [],
            "columna_a": [{"num": n, "texto": t} for n, t in sorted(items_a, key=lambda x: x[0])],
            "columna_b": [{"letra": l, "texto": t} for l, t in sorted(items_b.items())],
            "respuesta_correcta": mapa_respuesta,
            "explicacion": explicacion,
            "imagen": imagen_actual,
        })
        lineas_explicacion.clear()
        imagen_actual = None

    for linea in lineas:
        linea_limpia = linea.strip()

        if PATRON_ENCABEZADO.match(linea_limpia):
            if linea_limpia.lower().startswith("fuente"):
                fuente_actual = linea_limpia

        match_img = PATRON_IMAGEN.match(linea_limpia)
        if match_img:
            imagen_actual = match_img.group(1).strip()
            continue

        if PATRON_COLUMNA_A.search(linea_limpia) and estado in ("BUSCANDO", "RESP"):
            if estado == "RESP":
                cerrar_bloque()
            estado = "COL_A"
            lineas_col_a = []
            lineas_col_b = []
            lineas_resp = []
            lineas_explicacion = []
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

        if estado == "RESP" and PATRON_EXPLICACION.match(linea_limpia):
            resto_explicacion = PATRON_EXPLICACION.sub('', linea_limpia, count=1).strip()
            if resto_explicacion:
                lineas_explicacion.append(resto_explicacion)
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
            elif lineas_explicacion:
                lineas_explicacion.append(linea_limpia)
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


def parsear_archivo(ruta_entrada):
    if not os.path.isfile(ruta_entrada):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_entrada}")

    try:
        with open(ruta_entrada, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
    except UnicodeDecodeError:
        with open(ruta_entrada, 'r', encoding='latin-1') as archivo:
            texto = archivo.read()

    preguntas_tipo, avisos_tipo = parsear_bloques_tipo(texto)
    preguntas_col, avisos_col = parsear_bloques_columnas(texto)

    preguntas = []
    avisos = list(avisos_tipo) + list(avisos_col)
    firmas_registradas = set()

    for p in preguntas_tipo:
        firma = re.sub(r'\s+', ' ', p.get("enunciado", "")).strip().lower()[:100]
        if firma:
            firmas_registradas.add(firma)
        preguntas.append(p)

    for p in preguntas_col:
        firma = re.sub(r'\s+', ' ', p.get("enunciado", "")).strip().lower()[:100]
        if firma and firma in firmas_registradas:
            continue
        preguntas.append(p)

    for indice, p in enumerate(preguntas, 1):
        p["id"] = f"pregunta-{indice}"

    return preguntas, avisos
