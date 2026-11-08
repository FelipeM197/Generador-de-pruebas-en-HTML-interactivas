"""Suite de pruebas automatizadas para verificar compatibilidad universal entre formatos .md y .txt."""
import os
import sys
import tempfile
import unittest

DIR_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if DIR_SRC not in sys.path:
    sys.path.insert(0, DIR_SRC)

from lector_preguntas import parsear_archivo
from md_parser import parsear_md
from txt_parser import parsear_txt
from generar_examen import generar_desde_archivo


BLOQUE_MULTIPLE = """
[TIPO: OPCION MULTIPLE]
Pregunta ID: 1
Enunciado: ¿Cuál es el puerto estándar asignado al protocolo HTTPS?
Opciones: A) 80 B) 443 C) 22 D) 8080
Respuesta Correcta: B
Explicación: El tráfico seguro HTTPS utiliza por defecto el puerto 443.
"""

BLOQUE_VERDADERO_FALSO = """
[TIPO: VERDADERO_FALSO]
Pregunta ID: 2
Enunciado: UDP es un protocolo orientado a conexión que garantiza la entrega ordenada de paquetes.
Opciones: A) Verdadero B) Falso
Respuesta Correcta: B
Explicación: UDP no está orientado a conexión y no garantiza orden ni entrega.
"""

BLOQUE_CORTA = """
[TIPO: RESPUESTA CORTA]
Pregunta ID: 3
Enunciado: ¿Qué sigla identifica al protocolo encargado de traducir nombres de dominio a direcciones IP?
Respuesta Correcta: DNS
Explicación: Domain Name System resuelve nombres legibles a direcciones numéricas.
"""

BLOQUE_COLUMNAS = """
Fuente 1: Arquitectura de Redes
Instrucción: Relaciona cada protocolo con su capa del modelo OSI.
Columna A
1. HTTP
2. TCP
3. IP
Columna B
a. Capa de Aplicación
b. Capa de Transporte
c. Capa de Red
Respuestas: 1-a, 2-b, 3-c
Explicación: HTTP pertenece al nivel 7, TCP al nivel 4 e IP al nivel 3.
"""

BLOQUE_ORDENAMIENTO = """
Fuente 1: Ciclo de Compilación
Instrucción: Ordena secuencialmente las fases principales de compilación.
Columna A
1. Análisis Léxico
2. Análisis Sintáctico
3. Generación de Código
Columna B
1. Primera fase
2. Segunda fase
3. Tercera fase
Respuestas: 1-1, 2-2, 3-3
Explicación: El análisis léxico genera tokens, el sintáctico el árbol y luego se emite código.
"""


class TestCompatibilidadFormatos(unittest.TestCase):

    def setUp(self):
        self.archivos_temporales = []

    def tearDown(self):
        for ruta in self.archivos_temporales:
            if os.path.exists(ruta):
                try:
                    os.remove(ruta)
                except OSError:
                    pass

    def _crear_archivo_temporal(self, contenido, extension):
        fd, ruta = tempfile.mkstemp(suffix=extension, text=True)
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(contenido)
        self.archivos_temporales.append(ruta)
        return ruta

    def _verificar_esquema_pregunta(self, p):
        claves_esperadas = {
            "id", "tipo", "tipo_original", "enunciado", "opciones",
            "respuesta_correcta", "explicacion", "imagen", "modo",
            "columna_a", "columna_b"
        }
        self.assertTrue(claves_esperadas.issubset(p.keys()), f"Faltan claves en pregunta: {p.keys()}")
        self.assertIsInstance(p["opciones"], list)
        self.assertIsInstance(p["columna_a"], list)
        self.assertIsInstance(p["columna_b"], list)
        self.assertIsInstance(p["explicacion"], str)

    def test_opcion_multiple_en_archivo_txt(self):
        contenido = BLOQUE_MULTIPLE + "\n" + BLOQUE_VERDADERO_FALSO + "\n" + BLOQUE_CORTA
        ruta = self._crear_archivo_temporal(contenido, ".txt")

        preguntas, avisos = parsear_archivo(ruta)
        self.assertEqual(len(preguntas), 3)
        self.assertEqual(preguntas[0]["tipo"], "MULTIPLE")
        self.assertEqual(preguntas[1]["tipo"], "VERDADERO_FALSO")
        self.assertEqual(preguntas[2]["tipo"], "CORTA")

        for p in preguntas:
            self._verificar_esquema_pregunta(p)

    def test_columnas_en_archivo_md(self):
        contenido = BLOQUE_COLUMNAS
        ruta = self._crear_archivo_temporal(contenido, ".md")

        preguntas, avisos = parsear_archivo(ruta)
        self.assertEqual(len(preguntas), 1)
        p = preguntas[0]
        self.assertEqual(p["tipo"], "RELACION")
        self.assertEqual(p["modo"], "letra")
        self.assertEqual(len(p["columna_a"]), 3)
        self.assertEqual(len(p["columna_b"]), 3)
        self.assertEqual(p["respuesta_correcta"], {1: 'a', 2: 'b', 3: 'c'})
        self.assertTrue("HTTP" in p["explicacion"])
        self._verificar_esquema_pregunta(p)

    def test_ordenamiento_numerico_en_txt(self):
        contenido = BLOQUE_ORDENAMIENTO
        ruta = self._crear_archivo_temporal(contenido, ".txt")

        preguntas, avisos = parsear_archivo(ruta)
        self.assertEqual(len(preguntas), 1)
        p = preguntas[0]
        self.assertEqual(p["tipo"], "RELACION")
        self.assertEqual(p["modo"], "numero")
        self.assertEqual(p["respuesta_correcta"], {1: '1', 2: '2', 3: '3'})
        self._verificar_esquema_pregunta(p)

    def test_documento_mixto_en_md(self):
        contenido = "\n".join([BLOQUE_MULTIPLE, BLOQUE_COLUMNAS, BLOQUE_CORTA])
        ruta = self._crear_archivo_temporal(contenido, ".md")

        preguntas, avisos = parsear_archivo(ruta)
        self.assertEqual(len(preguntas), 3)
        tipos = [p["tipo"] for p in preguntas]
        self.assertIn("MULTIPLE", tipos)
        self.assertIn("RELACION", tipos)
        self.assertIn("CORTA", tipos)

        for p in preguntas:
            self._verificar_esquema_pregunta(p)

    def test_documento_mixto_en_txt(self):
        contenido = "\n".join([BLOQUE_COLUMNAS, BLOQUE_MULTIPLE, BLOQUE_ORDENAMIENTO])
        ruta = self._crear_archivo_temporal(contenido, ".txt")

        preguntas, avisos = parsear_archivo(ruta)
        self.assertEqual(len(preguntas), 3)

        for p in preguntas:
            self._verificar_esquema_pregunta(p)

    def test_intercambiabilidad_md_parser_y_txt_parser(self):
        ruta_txt = self._crear_archivo_temporal(BLOQUE_MULTIPLE, ".txt")
        ruta_md = self._crear_archivo_temporal(BLOQUE_COLUMNAS, ".md")

        # parsear_md debe ser capaz de procesar archivos .txt con cualquier formato
        preguntas_desde_md, _ = parsear_md(ruta_txt)
        self.assertEqual(len(preguntas_desde_md), 1)
        self.assertEqual(preguntas_desde_md[0]["tipo"], "MULTIPLE")

        # parsear_txt debe ser capaz de procesar archivos .md con cualquier formato
        preguntas_desde_txt, _ = parsear_txt(ruta_md)
        self.assertEqual(len(preguntas_desde_txt), 1)
        self.assertEqual(preguntas_desde_txt[0]["tipo"], "RELACION")

    def test_generacion_html_completa(self):
        contenido = "\n".join([BLOQUE_MULTIPLE, BLOQUE_VERDADERO_FALSO, BLOQUE_COLUMNAS])
        ruta_entrada = self._crear_archivo_temporal(contenido, ".txt")
        ruta_salida = ruta_entrada.replace(".txt", ".html")
        self.archivos_temporales.append(ruta_salida)

        resultado = generar_desde_archivo(ruta_entrada, ruta_salida)
        self.assertTrue(os.path.isfile(resultado))

        with open(resultado, 'r', encoding='utf-8') as f:
            html = f.read()

        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("pregunta-card", html)
        self.assertIn("HTTPS", html)
        self.assertIn("Capa de Aplicación", html)
        self.assertIn("modo-oscuro", html)
        self.assertIn("alternarTema", html)
        self.assertIn("btn-tema", html)

    def test_exclusion_preguntas_desarrollo(self):
        bloque_desarrollo = """
[TIPO: DESARROLLO]
Pregunta ID: 99
Enunciado: Explique el Teorema CAP y describa un escenario de particionamiento.
Respuesta Correcta: Rúbrica oficial del teorema CAP.
Explicación: Un sistema distribuido no puede garantizar consistencia estricta y disponibilidad ante particiones.
"""
        contenido = BLOQUE_MULTIPLE + "\n" + bloque_desarrollo + "\n" + BLOQUE_CORTA
        ruta = self._crear_archivo_temporal(contenido, ".md")
        preguntas, _ = parsear_archivo(ruta)
        tipos = [p["tipo"] for p in preguntas]
        self.assertNotIn("DESARROLLO", tipos)
        self.assertEqual(len(preguntas), 2)

    def test_archivos_reales_del_repositorio(self):
        # Valida que todos los archivos reales existentes en el repositorio se procesen sin error
        archivos_existentes = [
            ("Preguntas_BDD.md", 244),
            ("Preguntas_BigData.txt", 36),
            ("Preguntas_Infraestructura_BigData.md", 36),
            ("Preguntas_Compiladores.md", 85),
            ("Preguntas_Animaciones_Regresion_GIS.md", 69),
            ("Preguntas_DDBMS_Avanzado.md", 84),
            ("Preguntas_Lean_XP_Testing.md", 35),
            ("Preguntas_Repaso_Transacciones.md", 65),
            ("preguntas_lecturas.md", 40),
        ]

        dir_preguntas = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "preguntas"))
        for nombre, cantidad_esperada in archivos_existentes:
            ruta = os.path.join(dir_preguntas, nombre) if os.path.isfile(os.path.join(dir_preguntas, nombre)) else nombre
            if not os.path.isfile(ruta):
                continue
            preguntas, _ = parsear_archivo(ruta)
            self.assertEqual(
                len(preguntas),
                cantidad_esperada,
                f"Discrepancia en cantidad para {nombre}: esperadas {cantidad_esperada}, obtenidas {len(preguntas)}"
            )
            for p in preguntas:
                self._verificar_esquema_pregunta(p)


if __name__ == "__main__":
    unittest.main()
