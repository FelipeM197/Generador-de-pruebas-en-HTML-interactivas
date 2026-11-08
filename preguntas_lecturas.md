[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 1
Enunciado: ¿Cuál de las siguientes afirmaciones describe correctamente la función principal de la capa de Localización de Datos?
Opciones:
A) Transforma una consulta algebraica global en una consulta sobre fragmentos físicos usando el esquema de fragmentación.
B) Convierte una consulta en cálculo relacional hacia una consulta algebraica global usando el esquema conceptual único.
C) Genera una estrategia de ejecución cercana al óptimo evaluando estadísticamente el esquema de asignación de datos.
D) Ejecuta las operaciones algebraicas en los nodos locales aplicando algoritmos de optimización de sistemas centrales.
E) Ninguna de las opciones indicadas describe de manera correcta la función exacta de esta etapa de procesamiento.
Respuesta Correcta: A
Explicación: La capa de Localización de Datos transforma una consulta algebraica global en una consulta sobre fragmentos físicos usando el esquema de fragmentación.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 2
Enunciado: Según el programa de materialización, la reconstrucción de una relación global particionada mediante fragmentación vertical requiere aplicar matemáticamente el operador de unión lógica entre sus respectivos fragmentos.
Opciones:
A) Verdadero
B) Falso
C) Solo si la fragmentación es horizontal
D) Depende del número de fragmentos
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: La reconstrucción de una relación fragmentada verticalmente se realiza con el operador de join (reunión natural), no mediante unión lógica.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 3
Enunciado: Durante la etapa de Simplificación de la Consulta sobre Fragmentos, ¿qué técnica algorítmica permite reducir significativamente el volumen de transferencia en la red?
Opciones:
A) La asignación de operadores bloqueantes para forzar la materialización temprana de resultados en el disco del servidor.
B) La eliminación directa de fragmentos vacíos cuando un predicado de selección es incompatible con la definición del fragmento.
C) El cálculo exhaustivo de permutaciones espaciales para encontrar el orden absoluto y perfecto de ejecución de la consulta.
D) El reemplazo secuencial de relaciones globales empleando diccionarios de tipos y atributos del esquema conceptual base.
E) Ninguna de las opciones indicadas describe correctamente la técnica aplicada en esta fase específica del procesamiento.
Respuesta Correcta: B
Explicación: La eliminación de fragmentos vacíos por incompatibilidad del predicado de selección con la definición del fragmento reduce drásticamente los datos a transferir.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 4
Enunciado: A diferencia de las capas de descomposición y localización, la capa de optimización global basa sus decisiones estructurales en el esquema de asignación y en estadísticas de cardinalidad de los fragmentos.
Opciones:
A) Verdadero
B) Falso
C) Solo si la consulta involucra joins
D) Depende del tipo de fragmentación
E) Ninguna de las anteriores
Respuesta Correcta: A
Explicación: La optimización global usa el esquema de asignación y las estadísticas de fragmentos para generar el plan de ejecución distribuida.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 5
Enunciado: ¿En qué capa de la arquitectura del procesamiento de consultas se introducen por primera vez las primitivas algorítmicas de comunicación (send/receive) entre los distintos nodos?
Opciones:
A) En la etapa de Descomposición de Consultas, al analizar analíticamente los grafos semánticos.
B) En la etapa de Localización de Datos, al reestructurar progresivamente los fragmentos lógicos.
C) En la etapa de Optimización Global, al generar la estrategia de ejecución cercana al óptimo.
D) En la etapa de Ejecución Distribuida, al inicializar el modelo de pipeline en nodos locales.
E) Ninguna de las opciones indicadas identifica de manera correcta a la capa del procesamiento.
Respuesta Correcta: C
Explicación: Las primitivas de comunicación se incorporan en la Optimización Global, cuando se define la estrategia de ejecución distribuida.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 6
Enunciado: Dado que encontrar la estrategia de ejecución óptima es un problema matemáticamente intratable (NP-hard), los optimizadores globales emplean heurísticas y búsquedas exhaustivas acotadas.
Opciones:
A) Verdadero
B) Falso
C) Solo en bases de datos relacionales
D) Solo si hay más de tres fragmentos
E) Ninguna de las anteriores
Respuesta Correcta: A
Explicación: La optimización es NP-hard; por eso se recurre a heurísticas y búsquedas restringidas para hallar planes cercanos al óptimo.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 7
Enunciado: ¿Cuáles son los componentes estructurales que cuantifica la función de costo para evaluar y comparar alternativas en la Optimización Global?
Opciones:
A) El tiempo de compilación del motor, el tamaño de la memoria caché y el ancho de banda del canal de red global.
B) La latencia de la memoria principal, los bloqueos transaccionales concurrentes y el tiempo de respuesta del sistema.
C) Los accesos físicos a disco (E/S), el tiempo de procesamiento (CPU) y la transferencia de datos en red (comunicación).
D) La cantidad de usuarios concurrentes activos, la capacidad de almacenamiento disponible y la velocidad del procesador.
E) Ninguna de las opciones indicadas enumera correctamente los factores matemáticos ponderados por la función de costo.
Respuesta Correcta: C
Explicación: La función de costo pondera E/S, CPU y comunicación para estimar el coste de cada plan de ejecución.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 8
Enunciado: El ordenamiento de las operaciones de join se considera un aspecto de baja importancia en la optimización global, ya que las permutaciones generan diferencias de rendimiento imperceptibles.
Opciones:
A) Verdadero
B) Falso
C) Solo si los joins son naturales
D) Depende del tamaño de la memoria
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: El orden de los joins tiene un impacto muy significativo en el rendimiento, por lo que es un aspecto crítico en la optimización.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 9
Enunciado: Según el modelo de procesamiento por capas, ¿qué característica describe correctamente la fase de Optimización Local ejecutada por los sitios participantes?
Opciones:
A) Utiliza el directorio global del sistema para mapear las relaciones distribuidas hacia sus respectivos fragmentos físicos.
B) Aplica algoritmos de optimización de un DBMS centralizado usando exclusivamente su propio esquema local invisible.
C) Genera un plan de ejecución distribuido maestro que coordina las llamadas asíncronas entre múltiples servidores remotos.
D) Transforma la consulta original en cálculo relacional aplicando reglas heurísticas de simplificación semántica del usuario.
E) Ninguna de las opciones indicadas refleja el comportamiento arquitectónico exacto de los nodos durante esta etapa local.
Respuesta Correcta: B
Explicación: En la optimización local cada sitio optimiza su subconsulta como si fuera una consulta local, utilizando su propio esquema y estadísticas.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 10
Enunciado: El Modelo Iterador clásico implementa un paralelismo en pipeline donde las tuplas se materializan obligatoriamente en el disco físico antes de avanzar hacia el operador de mayor jerarquía.
Opciones:
A) Verdadero
B) Falso
C) Solo cuando hay operadores bloqueantes
D) Depende de la configuración del buffer
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: En el modelo iterador con pipeline las tuplas se pasan directamente en memoria sin necesidad de materialización forzosa en disco.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 11
Enunciado: Dentro del flujo operativo del Modelo Iterador en sistemas distribuidos, ¿cuál es la función de la primitiva algorítmica Next()?
Opciones:
A) Inicializa el estado interno del operador relacional, reservando estructuras como tablas hash antes del procesamiento.
B) Libera todos los recursos computacionales y de memoria RAM empleados una vez que han finalizado las operaciones.
C) Produce y retorna de manera continua la siguiente tupla procesada, o un valor nulo al terminar de recorrer los datos.
D) Transforma la consulta expresada en cálculo relacional hacia una estructura de árbol binario de álgebra relacional.
E) Ninguna de las opciones indicadas describe la funcionalidad correcta de esta función dentro del paradigma de pipeline.
Respuesta Correcta: C
Explicación: Next() obtiene la siguiente tupla del operador hijo y la retorna; cuando no hay más tuplas devuelve un valor nulo que indica fin de datos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 12
Enunciado: Un operador de ordenamiento (sort) se clasifica como bloqueante debido a que requiere materializar exhaustivamente toda su entrada de datos antes de poder emitir cualquier tupla de salida.
Opciones:
A) Verdadero
B) Falso
C) Solo si el orden es descendente
D) Solo si se usa disco
E) Ninguna de las anteriores
Respuesta Correcta: A
Explicación: El ordenamiento es bloqueante porque necesita leer y organizar todos los datos de entrada antes de producir la primera tupla de salida.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 13
Enunciado: Al comparar las cuatro capas arquitectónicas del procesamiento de consultas distribuidas, ¿qué combinación relaciona exactamente la etapa con el esquema de metadatos que consume?
Opciones:
A) Descomposición de Consultas y Esquema de Asignación Física.
B) Localización de Datos y Esquema Conceptual Global Central.
C) Optimización Global y Esquema de Fragmentación Horizontal.
D) Ejecución Distribuida y Esquemas Locales del Sistema Gestor.
E) Ninguna de las opciones indicadas asocia correctamente las capas.
Respuesta Correcta: D
Explicación: La capa de Ejecución Distribuida trabaja directamente sobre los esquemas locales de cada sitio gestor de base de datos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 14
Enunciado: En la división estricta de responsabilidades del modelo de procesamiento distribuido, el sitio de control central ejecuta la descomposición, la localización, la optimización global y la ejecución local.
Opciones:
A) Verdadero
B) Falso
C) Solo si el sistema es homogéneo
D) Solo en arquitecturas centralizadas
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: El sitio de control no ejecuta la ejecución local; esta se realiza en cada sitio participante de manera autónoma.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 15
Enunciado: En el recorrido de la consulta sobre el sistema del IESS expuesto en el documento, ¿qué acción algorítmica específica se lleva a cabo durante la fase de Localización de Datos?
Opciones:
A) La sentencia SQL original se normaliza semánticamente mediante grafos y se convierte a su equivalente en álgebra.
B) Se identifica que el fragmento relevante se encuentra en un servidor específico, descartando activamente a los demás.
C) El procesador global decide aplicar heurísticas de selección temprana antes de transmitir datos a la red interconectada.
D) Cada servidor extrae sus registros de forma local mediante sus propios esquemas y los reporta al sitio coordinador.
E) Ninguna de las opciones indicadas ejemplifica de forma rigurosa la operación ejecutada por la etapa de localización.
Respuesta Correcta: B
Explicación: En la localización se determina qué fragmentos son relevantes y en qué servidores residen, descartando los que no participan en la consulta.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 16
Enunciado: Según el modelo de Özsu y Valduriez, las capas de descomposición de consultas y localización de datos garantizan la transparencia al ocultar al usuario la distribución física de la información.
Opciones:
A) Verdadero
B) Falso
C) Solo para fragmentación horizontal
D) Solo si el esquema está normalizado
E) Ninguna de las anteriores
Respuesta Correcta: A
Explicación: Esas capas ocultan la fragmentación y la localización, proporcionando transparencia de distribución al usuario.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 17
Enunciado: De acuerdo con el principio de progresión de la información en el procesamiento distribuido, ¿qué insumos clave se van añadiendo a medida que una consulta avanza a través de las distintas capas?
Opciones:
A) Exclusivamente predicados lógicos provenientes de vistas de seguridad del usuario final para la simplificación relacional.
B) Únicamente información relativa a la capa de red subyacente para gestionar protocolos de control en las transacciones.
C) Detalles progresivos y metadatos, transitando desde el esquema global inicial hasta llegar a la estadística de fragmentos.
D) Solo estructuras de datos navegacionales para la estricta compatibilidad con las bases de datos de jerarquías pasadas.
E) Ninguna de las opciones indicadas describe de manera certera el principio evolutivo de la información a lo largo de las capas.
Respuesta Correcta: C
Explicación: A medida que se desciende en las capas, se agregan metadatos de fragmentación, localización y estadísticas hasta alcanzar el nivel físico.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 18
Enunciado: Durante la capa de ejecución distribuida, la optimización local requiere una validación y dependencia estricta con el sitio de control para elegir adecuadamente el algoritmo de acceso a los índices.
Opciones:
A) Verdadero
B) Falso
C) Solo si los índices son globales
D) Depende del protocolo de commit
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: La optimización local es autónoma; cada sitio decide sus algoritmos de acceso e índices sin intervención del sitio de control.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 19
Enunciado: ¿Cuál de las siguientes operaciones algebraicas se clasifica estrictamente como un operador en pipeline, capaz de emitir resultados de forma continua sin bloquear el flujo de la ejecución general?
Opciones:
A) El ordenamiento topológico global de una relación basada en un conjunto de claves numéricas primarias y foráneas.
B) La operación de hash join ejecutada obligatoriamente sobre dos fragmentos relacionales de cardinalidades dispares.
C) La proyección de atributos específicos sobre una corriente continua de datos que se examina de manera secuencial.
D) La ordenación temporal de registros fragmentados empleando métodos de acceso a discos distribuidos espacialmente.
E) Ninguna de las opciones indicadas enumera de forma matemática a un operador compatible con este paradigma continuo.
Respuesta Correcta: C
Explicación: La proyección sin eliminación de duplicados es un operador no bloqueante que puede emitir tuplas conforme las recibe.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 20
Enunciado: El programa de materialización estipula que cada referencia a una relación global presente en la consulta debe ser reemplazada por la secuencia de álgebra relacional que la reconstruye desde sus fragmentos.
Opciones:
A) Verdadero
B) Falso
C) Solo si hay fragmentación híbrida
D) Depende del optimizador
E) Ninguna de las anteriores
Respuesta Correcta: A
Explicación: El programa de materialización sustituye cada relación global por el plan algebraico que compone los fragmentos correspondientes.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 21
Enunciado: ¿Cuál de las siguientes afirmaciones describe correctamente el objetivo principal del control de concurrencia?
Opciones:
A) Funcionar como un mecanismo que incrementa la velocidad de ejecución frente a los métodos secuenciales.
B) Desempeñar un control exclusivo sobre transacciones optimistas sin modificar historiales de operaciones.
C) Constituir un mecanismo que garantiza que la ejecución simultánea produzca resultados equivalentes a una serial.
D) Asegurar que las bases de datos distribuidas prescindan totalmente de candados de lectura y escritura.
E) Garantizar que todas las operaciones dentro de un historial se validen simultáneamente al finalizar el proceso.
Respuesta Correcta: C
Explicación: El control de concurrencia asegura que el resultado de la ejecución concurrente sea equivalente a alguna ejecución serial de las transacciones.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 22
Enunciado: Dos operaciones concurrentes sobre la misma unidad de datos se consideran en conflicto únicamente si ambas corresponden a operaciones de escritura (WRITE).
Opciones:
A) Verdadero
B) Falso
C) Solo si la unidad es una tupla
D) Depende del nivel de aislamiento
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: Hay conflicto no solo con dos escrituras; también una lectura y una escritura sobre el mismo dato entran en conflicto.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 23
Enunciado: Según el criterio de corrección de bases de datos, ¿qué condición debe cumplir un historial para ser considerado serializable?
Opciones:
A) Sus operaciones sin conflicto deben ser organizadas estrictamente en función de marcas de tiempo.
B) Debe ser equivalente, en el orden de sus operaciones en conflicto, a alguna ejecución serial.
C) Tiene que asegurar la eliminación completa de múltiples reinicios en las transacciones de lectura.
D) Requiere la administración de todas las operaciones mediante una fase única de decrecimiento.
E) Debe evitar por completo la utilización de cualquier forma de bloqueo en un procesador central.
Respuesta Correcta: B
Explicación: Un historial es serializable si el orden de las operaciones conflictivas coincide con el de alguna ejecución serial.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 24
Enunciado: Los mecanismos de control de concurrencia híbridos combinan primitivos de bloqueo y marcas de tiempo, y son los más implementados en los sistemas comerciales actuales.
Opciones:
A) Verdadero
B) Falso
C) Solo en sistemas NoSQL
D) Depende del motor de almacenamiento
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: Los sistemas comerciales suelen implementar mayoritariamente mecanismos basados en bloqueos (2PL) o MVCC, no híbridos como norma principal.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 25
Enunciado: En los fundamentos del bloqueo (locking), ¿cuál es la dinámica correcta respecto a los modos de candado y su compatibilidad?
Opciones:
A) El establecimiento de candados de lectura permite concurrentemente la asignación de escritura exclusiva.
B) El uso de un candado de escritura permite el acceso concurrente únicamente a las operaciones de lectura.
C) La compatibilidad de lectura con lectura se encuentra plenamente garantizada sobre el mismo dato analizado.
D) El requerimiento de un candado de escritura siempre es compatible con el de otro candado de escritura local.
E) Ninguna de las opciones indicadas representa correctamente el comportamiento de la compatibilidad del candado.
Respuesta Correcta: C
Explicación: Varios candados de lectura sobre el mismo dato son compatibles; un candado de escritura es incompatible con cualquier otro.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 26
Enunciado: En el protocolo de Bloqueo en Dos Fases (2PL), el "punto de bloqueo" representa el instante exacto en que la transacción libera el último candado y termina.
Opciones:
A) Verdadero
B) Falso
C) Solo en 2PL estricto
D) Depende del plan de ejecución
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: El punto de bloqueo es el momento en que la transacción adquiere todos los candados necesarios; después de ese punto no se solicitan más.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 27
Enunciado: ¿Qué problema crítico se previene específicamente mediante la implementación de la variante de Bloqueo en Dos Fases Estricto (2PL Estricto)?
Opciones:
A) El cuello de botella masivo generado en coordinadores bajo una arquitectura de sistema centralizado.
B) La formación de interbloqueos causados directamente por las solicitudes superpuestas de operaciones de lectura.
C) El riesgo inminente de abortos en cascada generados al leer datos que posteriormente sufren deshacer (rollback).
D) El almacenamiento redundante e ineficiente generado por el registro de versiones múltiples en cada registro.
E) La demora en las comunicaciones de red al otorgar un nivel de granularidad muy detallado para cada tabla.
Respuesta Correcta: C
Explicación: El 2PL estricto retiene los candados de escritura hasta el final de la transacción, evitando que otras lean datos que luego serán deshechos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 28
Enunciado: En el Bloqueo Centralizado (C2PL), el administrador central es el único encargado de otorgar o rechazar los candados, mientras que los procesadores de datos ejecutan las operaciones.
Opciones:
A) Verdadero
B) Falso
C) Solo para candados de tabla
D) Depende del número de réplicas
E) Ninguna de las anteriores
Respuesta Correcta: A
Explicación: En el bloqueo centralizado hay un único gestor de bloqueos que concede los candados y los nodos de datos ejecutan las operaciones.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 29
Enunciado: ¿Qué característica técnica describe correctamente el funcionamiento del mecanismo de Bloqueo Distribuido (D2PL)?
Opciones:
A) Requiere delegar toda su carga de trabajo hacia un nodo coordinador ubicado geográficamente en otro sitio.
B) Centraliza la asignación de todas las marcas de tiempo para garantizar unicidad y sincronización global.
C) Reemplaza el uso de los candados mediante un modelo de validación tardía apoyado en conjuntos de escritura.
D) Exige que cada sitio asuma de forma autónoma la concesión de candados sobre los datos que almacena localmente.
E) Elimina la necesidad de utilizar mensajes de coordinación entre los administradores de transacciones en la red.
Respuesta Correcta: D
Explicación: En D2PL cada sitio gestiona los candados de los datos que residen en él, de manera distribuida sin un coordinador central único.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 30
Enunciado: En PostgreSQL, utilizar la sentencia SELECT ... FOR UPDATE solicita de manera directa un candado de lectura, lo que permite accesos concurrentes de modificación sin espera.
Opciones:
A) Verdadero
B) Falso
C) Solo en modo serializable
D) Depende de la versión de PostgreSQL
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: SELECT ... FOR UPDATE solicita un candado de escritura (exclusivo) sobre las filas seleccionadas, bloqueando modificaciones concurrentes.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 31
Enunciado: ¿Cuáles son las dos propiedades matemáticas fundamentales que debe cumplir una marca de tiempo generada para una transacción?
Opciones:
A) Sincronicidad absoluta global y variabilidad dependiente de la red.
B) Monotonicidad decreciente local e identificadores alfanuméricos.
C) Unicidad que identifica sin ambigüedad y monotonicidad creciente.
D) Exclusividad operativa centralizada y homogeneidad de asignación.
E) Ninguna de las opciones indicadas.
Respuesta Correcta: C
Explicación: Las marcas de tiempo deben ser únicas (sin ambigüedad) y monótonamente crecientes para establecer un orden total.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 32
Enunciado: La regla fundamental de las Marcas de Tiempo (Timestamp Ordering) establece que, ante operaciones en conflicto, siempre se ejecuta primero la que posee la mayor marca de tiempo.
Opciones:
A) Verdadero
B) Falso
C) Solo en TO multiversión
D) Depende del tipo de operación
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: En el ordenamiento por marcas de tiempo, la operación con menor marca (más antigua) es la que debe ejecutarse primero.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 33
Enunciado: Bajo el esquema de Marcas de Tiempo por Dato, ¿qué condición se exige para aceptar una operación de escritura (WRITE) enviada por una transacción?
Opciones:
A) La marca de la transacción debe ser superior exclusivamente a la variable wts(x) almacenada localmente.
B) La marca de la transacción debe ser inferior tanto al valor de rts(x) como al límite máximo de wts(x).
C) La marca de la transacción debe superar en valor simultáneamente tanto a la marca rts(x) como a wts(x).
D) La marca de la transacción debe forzar de inmediato el reinicio de los valores históricos del reloj físico.
E) La transacción debe certificar haber terminado completamente su etapa de decrecimiento sin errores.
Respuesta Correcta: C
Explicación: Para aceptar una escritura, la marca de la transacción debe ser mayor que la de la última lectura (rts) y que la de la última escritura (wts) sobre el dato.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 34
Enunciado: Al ejecutar sus operaciones sin permitir retrasos o colas de espera, el algoritmo TO Básico (Basic TO) previene por completo la generación de interbloqueos.
Opciones:
A) Verdadero
B) Falso
C) Solo si no hay escrituras ciegas
D) Depende de la topología de red
E) Ninguna de las anteriores
Respuesta Correcta: A
Explicación: Basic TO evita esperas; si una operación no puede ejecutarse se aborta, por lo que no se producen ciclos de espera (interbloqueos).

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 35
Enunciado: ¿Cuál de las siguientes afirmaciones describe la desventaja principal (costo) que introduce el mecanismo TO Conservador (Conservative TO)?
Opciones:
A) Produce un incremento masivo en el número de abortos en cascada en transacciones locales.
B) Introduce demoras de espera intencionales que propician la posible aparición de interbloqueos.
C) Fomenta un esquema en el cual siempre se prioriza a la transacción más joven del procesador.
D) Agota velozmente el almacenamiento disponible por su retención de versiones múltiples de registro.
E) Ninguna de las opciones indicadas.
Respuesta Correcta: B
Explicación: El TO conservador retrasa deliberadamente operaciones para mantener el orden, lo que puede provocar interbloqueos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 36
Enunciado: El protocolo TO Multiversión (Multiversion TO) genera de forma automática una nueva versión temporal cada vez que una transacción realiza una lectura (READ).
Opciones:
A) Verdadero
B) Falso
C) Solo si la lectura es sucia
D) Solo en PostgreSQL
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: En multiversión, las nuevas versiones se crean con las escrituras (WRITE), no con las lecturas.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 37
Enunciado: ¿Qué ventaja principal justifica la adopción de una arquitectura basada en el mecanismo de TO Multiversión (Multiversion TO)?
Opciones:
A) La liberación definitiva de bloqueos causados por las comunicaciones entre nodos del tipo D2PL.
B) La eliminación casi por completo de la necesidad de reinicios generados por intentos de lectura.
C) El abaratamiento general del espacio de almacenamiento necesario para resguardar los historiales.
D) La optimización y reducción de la fase de validación estricta de conflictos mediante conjuntos WS.
E) Ninguna de las opciones indicadas.
Respuesta Correcta: B
Explicación: Al mantener múltiples versiones, las lecturas no se bloquean ni abortan porque acceden a una versión consistente pasada, eliminando reinicios por lectura.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 38
Enunciado: Según las reglas fundamentales del control de concurrencia, el orden de ejecución siempre es relevante y debe regularse incluso entre aquellas operaciones que no entran en conflicto.
Opciones:
A) Verdadero
B) Falso
C) Solo en protocolos optimistas
D) Depende del nivel de aislamiento serializable
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: Las operaciones que no están en conflicto pueden reordenarse libremente sin afectar la serializabilidad del historial.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 39
Enunciado: En relación con los métodos basados en bloqueo, ¿qué efecto genera directamente la elección de la granularidad (registro, página o tabla) del candado?
Opciones:
A) Define automáticamente la compatibilidad inherente entre lectura y escritura del gestor relacional.
B) Asegura la imposibilidad técnica de que ocurran interbloqueos durante la fase de validación tardía.
C) Regula y afecta de manera directa el equilibrio existente entre la alta concurrencia y la sobrecarga.
D) Establece definitivamente el protocolo expropiador que se aplicará en caso de utilizar un WOUND-WAIT.
E) Ninguna de las opciones indicadas.
Respuesta Correcta: C
Explicación: Una granularidad fina permite más concurrencia pero mayor sobrecarga de gestión; granularidad gruesa reduce la sobrecarga pero baja la concurrencia.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 40
Enunciado: La regla del protocolo 2PL establece que en su fase de decrecimiento, una vez liberado el primer candado, la transacción aún tiene permitido solicitar un número limitado de candados nuevos.
Opciones:
A) Verdadero
B) Falso
C) Solo si el candado era de lectura
D) Solo en 2PL básico no estricto
E) Ninguna de las anteriores
Respuesta Correcta: B
Explicación: En 2PL, una vez que la transacción libera un candado (fase de decrecimiento), no puede solicitar ningún candado nuevo.