# Generador de Pruebas y Exámenes Interactivos en HTML

Sistema ligero para transformar baterías de preguntas estructuradas (generadas a partir de fuentes documentales mediante modelos de lenguaje) en aplicaciones web interactivas autocontenidas en formato HTML, listas para estudio o evaluación diagnóstica sin requerir servidores ni dependencias externas.

---

## Propósito del Proyecto

El objetivo es automatizar la creación de simuladores de evaluación a partir de fuentes académicas o técnicas. El flujo permite cargar bibliografía especializada en herramientas de análisis como NotebookLM, generar preguntas de alta rigurosidad conceptual con plantillas optimizadas y compilar los resultados directamente en archivos HTML interactivos que funcionan en cualquier navegador.

---

## Características Principales

- **Archivos autocontenidos:** Cada examen se compila en un único archivo HTML con estilos CSS, lógica JavaScript e imágenes codificadas en Base64.
- **Variedad de reactivos admitidos:**
  - Opción múltiple (con 4 o más alternativas y barajado dinámico).
  - Verdadero o Falso.
  - Relación y emparejamiento de columnas.
  - Ordenamiento lógico secuencial (numérico y romano).
  - Respuesta corta con normalización de caracteres y tildes.
- **Compatibilidad universal (.md y .txt):** El analizador procesa cualquier tipo de reactivo sin importar si el archivo tiene extensión `.md`, `.txt` o si combina ambos formatos en un solo documento.
- **Persistencia de sesión:** Registro de intentos previos y porcentaje de aciertos en `localStorage` del navegador.
- **Modo de recuperación:** Opción para reiniciar el examen filtrando exclusivamente las preguntas falladas en intentos anteriores.

---

## Formatos de Entrada Admitidos

El sistema admite dos estructuras principales de forma indistinta tanto en archivos `.md` como en `.txt`, e incluso de forma combinada dentro del mismo documento:

### 1. Bloques Estructurados con Etiquetas (`[TIPO: ...]`)
Utilizados para opción múltiple, verdadero/falso, ordenamiento y respuesta corta:

```markdown
[TIPO: OPCION MULTIPLE]
Pregunta ID: 1
Enunciado: ¿Cuál es la propiedad fundamental de un sistema transaccional que asegura que las operaciones se completen totalmente o no se ejecuten?
Imagen: imagenes_examen/diagrama_acid.png
Opciones: A) Consistencia B) Aislamiento C) Atomicidad D) Durabilidad E) Ninguna de las anteriores
Respuesta Correcta: C
Explicación: La atomicidad garantiza que una transacción sea tratada como una unidad indivisible de trabajo.
```

*Nota:* El campo `Imagen:` es opcional y admite rutas relativas a la carpeta donde se encuentra el archivo fuente.

### 2. Bloques de Columnas (Relación y Emparejamiento)
Diseñados para ejercicios de correspondencia u ordenamiento secuencial entre dos columnas:

```text
Fuente 1: Arquitectura de Sistemas Distribuidos
Instrucción: Relaciona cada patrón de particionamiento con su característica principal.
Columna A
1. Fragmentación Horizontal
2. Fragmentación Vertical
3. Fragmentación Híbrida
Columna B
a. División de tuplas en subconjuntos disjuntos.
b. División por proyección de atributos y clave primaria.
c. Combinación anidada de criterios por tupla y atributo.
d. Distractor no aplicable.
Respuestas: 1-a, 2-b, 3-c
Explicación: La fragmentación divide tablas según relaciones horizontales o verticales.
```

---

## Flujo de Trabajo

### Paso 1: Carga de Fuentes en NotebookLM
Crea un cuaderno en Google NotebookLM y sube los documentos, artículos o capítulos bibliográficos sobre los cuales se diseñará la evaluación.

### Paso 2: Generación del Cuestionario con el Prompt Maestro
Ejecuta la siguiente plantilla en el cuadro de consulta de NotebookLM adaptando los parámetros entre corchetes según la disciplina a evaluar:

```text
Actúa como un profesor universitario riguroso especializado en [ROL O ESPECIALIDAD ACADÉMICA]. Tu objetivo es diseñar un examen sobre [ASIGNATURA O TEMA CENTRAL], basándote estrictamente en los [NÚMERO DE DOCUMENTOS] documentos de la bibliografía proporcionada.

Reglas de diseño del examen:

Falsa Práctica: Utiliza escenarios del mundo real, casos de estudio o tecnologías específicas del área ([EJEMPLOS DE HERRAMIENTAS O CASOS DEL ÁREA]) como "cebo" en los enunciados. La pregunta no debe evaluar comandos o uso operativo básico, sino el fundamento teórico, matemático o algorítmico que sustenta el problema ([EJEMPLOS DE FUNDAMENTOS TEÓRICOS]).

Profundidad Teórica: Evalúa compensaciones técnicas (trade-offs), teoremas, principios fundamentales ([LEYES, PRINCIPIOS O TEOREMAS APLICABLES]) y el comportamiento de sistemas o modelos bajo condiciones límite, estrés o fallos.

Formatos Requeridos:

1. Preguntas de Emparejamiento: Conceptos conceptualmente cercanos donde la diferencia radique en un matiz semántico, formal o arquitectónico clave ([EJEMPLOS DE CONCEPTOS COMPARABLES]).
2. Pregunta de Ordenamiento Lógico: Flujo de proceso, algoritmo o secuencia donde el orden dependa de dependencias estrictas (longitud mínima de 4 fases/pasos).
3. Preguntas de Respuesta Corta Exacta: Solicita acrónimos o términos técnicos unívocos de la materia ([EJEMPLOS DE TÉRMINOS O SIGLAS]).
4. Caso de Desarrollo (Alta complejidad): Expone un escenario crítico o fallo en cadena. Solicita identificar anomalías teóricas y proponer una solución estructurada justificando cada decisión técnica.
5. Preguntas de Opción Múltiple: Mínimo 5 opciones por pregunta, incluyendo obligatoriamente "Ninguna de las anteriores". Distribuye respuestas correctas de forma aleatoria donde dicha opción sea la correcta. Todas las alternativas deben ser plausibles y con similar longitud de texto.

Instrucciones de Salida:
- Incluye una etiqueta clara indicando el tipo de formato al que pertenece cada pregunta.
- Genera un mínimo de [CANTIDAD DE PREGUNTAS] preguntas distribuidas entre todas las fuentes analizadas.
```

### Paso 3: Guardar el Resultado
Guarda las preguntas generadas en un archivo de texto con codificación UTF-8, usando indistintamente la extensión `.md` o `.txt`.

### Paso 4: Generación del HTML Interactivo
Ejecuta el script principal desde la terminal indicando el archivo de entrada:

```bash
python generar_examen.py archivo_entrada.md
```

O si el archivo está en formato de texto plano:

```bash
python generar_examen.py archivo_entrada.txt
```

También es posible especificar una ruta o nombre de salida personalizado:

```bash
python generar_examen.py archivo_entrada.txt evaluacion_final.html
```

Si deseas prescindir de las preguntas de respuesta corta antes de generar el examen interactivo, puedes utilizar la herramienta auxiliar de filtrado:

```bash
python filtrar_respuesta_corta.py cuestionario.md cuestionario_sin_cortas.md
```

---

## Estructura del Repositorio

```text
├── generar_examen.py              # Script principal de ejecucion
├── lector_preguntas.py            # Motor unificado de analisis para formatos .md y .txt
├── html_generator.py              # Ensamblador de la interfaz web interactiva
├── md_parser.py                   # Adaptador de lectura para Markdown
├── txt_parser.py                  # Adaptador de lectura para texto plano
├── filtrar_respuesta_corta.py     # Script auxiliar de filtrado de respuesta corta
├── imagenes_examen/               # Recursos graficos incrustados en los reactivos
├── Preguntas_*.md                 # Baterias de ejemplo en formato Markdown
├── Preguntas_*.txt                # Baterias de ejemplo en formato de texto plano
└── .gitignore                     # Exclusion de temporales, entornos y HTML generados
```

---

## Requisitos de Ejecución

- Python 3.8 o superior (únicamente biblioteca estándar; no requiere instalación de dependencias vía `pip`).
- Cualquier navegador web moderno compatible con ECMAScript 6 y `localStorage`.
