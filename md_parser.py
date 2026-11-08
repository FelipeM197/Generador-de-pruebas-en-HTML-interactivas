"""Analizador de archivos Markdown con preguntas estructuradas."""
import re

# El patron busca letras aisladas de opciones (A., B), C-). El lookbehind
# evita separar abreviaturas o terminos en medio de oraciones.
PATRON_DIVISION_OPCIONES = re.compile(r'(?<![A-Za-z])([A-Z])[.)\-]\s+')

PATRON_PAR_GENERICO = re.compile(r'^\d+\s*-\s*[^,]+(?:\s*,\s*\d+\s*-\s*[^,]+)*\.?$')
PATRON_ORDEN_NUMEROS = re.compile(r'\d+(?:\s*,\s*\d+){1,}\.?\s*$')
PATRON_ORDEN_ROMANOS = re.compile(r'[IVXLCDM]+(?:\s*(?:->|,)\s*[IVXLCDM]+){1,}\.?\s*$')

VALORES_ROMANOS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def _dividir_opciones(texto_opciones):
    if not texto_opciones:
        return []

    # Validamos que las letras sigan la progresion alfabetica estricta (A, B, C...)
    # para evitar dividir formulas matematicas o expresiones parenteticas.
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
    # Se descartan opciones comodin como 'N/A' utilizadas en plantillas incompletas.
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
    # Detecta variantes de descarte como 'Ninguna de las anteriores' que no forman pares.
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
        # Elimina encabezados anexos al final del item (como 'Definiciones:') sin alterar el punto final.
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

    # Reconstruccion de emparejamiento codificado dentro de opciones de seleccion
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

        # Cuando no hay columna B explicita en el texto, se infiere desde las variantes en las opciones
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

    # Reconstruccion de ordenamientos secuenciales con digitos
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

    # Reconstruccion de secuencias expresadas en numeracion romana
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


def parsear_md(ruta_entrada):
    with open(ruta_entrada, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()

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

        # Recupera texto numerado que haya quedado antes de la opcion A
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
                "id": f"md-{contador}",
                "tipo": "RELACION",
                "tipo_original": tipo_declarado,
                "modo": relacion["modo"],
                "enunciado": relacion["enunciado"],
                "columna_a": relacion["columna_a"],
                "columna_b": relacion["columna_b"],
                "respuesta_correcta": relacion["respuesta_correcta"],
                "explicacion": explicacion,
                "imagen": imagen,
            })
        else:
            preguntas.append({
                "id": f"md-{contador}",
                "tipo": tipo_final,
                "tipo_original": tipo_declarado,
                "enunciado": enunciado,
                "opciones": opciones,
                "respuesta_correcta": respuesta_correcta,
                "explicacion": explicacion,
                "imagen": imagen,
            })

    return preguntas, avisos


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
