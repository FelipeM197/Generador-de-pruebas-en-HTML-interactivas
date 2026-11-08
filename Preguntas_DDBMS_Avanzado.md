[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 1
Enunciado: En el modelo cliente/servidor con múltiples servidores y servidor home, cada cliente conoce solo su servidor home, el cual se comunica con los demás servidores según se requiera. ¿Cuál es la principal ventaja y el principal desafío de esta configuración respecto al modelo de cliente pesado?
Opciones: A) Ventaja: elimina virtualmente los cuellos de botella del sistema; desafío: exige que el cliente conozca la ubicación de todos los servidores. B) Ventaja: simplifica el cliente ocultando la coordinación entre servidores; desafío: añade complejidad en la comunicación inter-servidor. C) Ventaja: simplifica considerablemente el código interno del servidor; desafío: el cliente gestiona múltiples conexiones simultáneas activas. D) Ventaja: garantiza consistencia fuerte en todas las operaciones; desafío: introduce mayor latencia perceptible en las lecturas locales. E) Ninguna de las anteriores es correcta en este contexto.
Respuesta Correcta: B
Explicación: Este modelo delega la coordinación al servidor home, lo que hace al cliente más ligero y simple, pero transfiere la sobrecarga y complejidad a la comunicación inter-servidor.

[TIPO: RESPUESTA CORTA] Pregunta ID: 2
Enunciado: En el Teorema CAP, ¿cómo se denomina la propiedad que garantiza que el sistema continúa operando aunque fallen enlaces de comunicación entre nodos? Escriba su respuesta en MAYÚSCULAS, sin tildes.
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: AP
Explicación: Un sistema AP prioriza la Disponibilidad (Availability) y Tolerancia a Particiones (Partition tolerance), permitiendo que siga operando ante caídas de red.

[TIPO: RESPUESTA CORTA] Pregunta ID: 3
Enunciado: ¿Cómo se denomina el tipo de fragmentación que divide una relación en subconjuntos de filas almacenados en distintos nodos, de modo que cada nodo maneja solo los registros que le corresponden geográficamente? Escriba su respuesta en MAYÚSCULAS.
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: HORIZONTAL
Explicación: La fragmentación horizontal agrupa subconjuntos de tuplas (filas) basándose en predicados lógicos, distribuyéndolas en los nodos pertinentes.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 4
Enunciado: Relacione cada anomalía de concurrencia con su definición correcta. 1) Actualización perdida. 2) Lectura sucia. 3) Lectura no repetible. 4) Fantasma. Definiciones: a) Alteración del conjunto de resultados de una consulta por inserciones concurrentes. b) Acceso a estados temporales de datos que podrían ser revertidos. c) Una transacción sobrescribe los cambios de otra sin haberlos integrado. d) Inconsistencia en valores leídos sucesivamente debido a modificaciones externas confirmadas.
Opciones: A) 1-c, 2-b, 3-d, 4-a B) 1-a, 2-c, 3-b, 4-d C) 1-b, 2-a, 3-d, 4-c D) 1-c, 2-d, 3-a, 4-b E) 1-d, 2-b, 3-c, 4-a
Respuesta Correcta: A
Explicación: La actualización perdida sobrescribe cambios (1-c), lectura sucia accede a datos no confirmados (2-b), lectura no repetible ve datos modificados entre lecturas (3-d) y fantasma ve nuevas filas insertadas (4-a).

[TIPO: ORDENAMIENTO] Pregunta ID: 5
Enunciado: Ordene la secuencia correcta del proceso de Confirmación en Dos Fases (2PC). 1) El coordinador envía un mensaje PREPARE a todos los sitios. 2) Cada sitio responde READY o ABORT según su estado. 3) Cada sitio participante registra en su log local la intención de confirmar o abortar. 4) El coordinador envía COMMIT o ABORT según las respuestas. 5) Los sitios aplican físicamente el commit o rollback.
Opciones: A) 1, 2, 3, 4, 5 B) 3, 1, 2, 5, 4 C) 1, 3, 4, 2, 5 D) 2, 4, 1, 3, 5 E) 4, 2, 1, 5, 3
Respuesta Correcta: A
Explicación: El flujo inicia con PREPARE del coordinador (1), seguido de la respuesta READY de los sitios (2), escritura en log local (3), decisión final del coordinador (4) y aplicación física de los cambios (5).

[TIPO: RESPUESTA CORTA] Pregunta ID: 6
Enunciado: ¿Cómo se denomina el criterio de corrección para bases de datos replicadas que exige que el resultado de ejecutar transacciones concurrentes sobre múltiples réplicas sea idéntico al de ejecutarlas serialmente sobre una sola copia?
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: 1SR
Explicación: El criterio de One-Copy Serializability (1SR) garantiza que un sistema replicado se comporte lógicamente como si existiera una única copia de los datos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 7
Enunciado: El teorema CAP establece que un sistema distribuido no puede garantizar simultáneamente las tres propiedades C, A y P. En sistemas distribuidos reales, las fallas de red son inevitables. ¿Qué implicación práctica tiene esta inevitabilidad sobre el diseño de un DDBMS?
Opciones: A) Ninguna de las opciones es correcta. B) El diseñador puede elegir libremente entre C, A y P según el presupuesto disponible. C) El teorema CAP no se aplica cuando el sistema utiliza un esquema de replicación ansiosa. D) Los sistemas distribuidos reales siempre garantizan consistencia y disponibilidad total. E) La tolerancia a particiones es inevitable, así que se elige entre consistencia y disponibilidad.
Respuesta Correcta: E
Explicación: Dado que las redes reales siempre sufren particiones (P es obligatorio), las decisiones de diseño se reducen a un compromiso (trade-off) estricto entre Consistencia (C) y Disponibilidad (A).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 8
Enunciado: Relacione cada término de diseño de DDBMS con su descripción correcta. 1) Fragmentación. 2) Replicación. 3) Asignación. 4) Transparencia de red. Descripciones: a) Decisión que determina en qué nodo físico se almacena cada subconjunto. b) División de una relación en subconjuntos de filas o columnas. c) Mantenimiento de copias idénticas de datos en múltiples nodos. d) Mecanismo que oculta al usuario si los datos están divididos entre nodos distintos.
Opciones: A) 1-b, 2-c, 3-a, 4-d B) 1-a, 2-b, 3-c, 4-d C) 1-c, 2-a, 3-d, 4-b D) 1-d, 2-c, 3-b, 4-a E) 1-b, 2-d, 3-a, 4-c
Respuesta Correcta: A
Explicación: Fragmentar es dividir (1-b), replicar es copiar (2-c), asignar es decidir la ubicación (3-a) y la transparencia oculta la ubicación física (4-d).

[TIPO: RESPUESTA CORTA] Pregunta ID: 9
Enunciado: ¿Cuál es el término técnico que designa la propiedad de un sistema distribuido que permite al usuario acceder a datos sin necesidad de conocer en qué nodo están almacenados físicamente ni si están replicados o fragmentados? Escriba su respuesta en MAYÚSCULAS.
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: TRANSPARENCIA
Explicación: La transparencia es el objetivo principal de los DDBMS para ofrecer una vista unificada y simple a los desarrolladores y usuarios.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 10
Enunciado: En PostgreSQL, la extensión postgres_fdw permite explorar y consultar datos externos. ¿Qué categoría de funcionalidad distribuida representa principalmente esta extensión?
Opciones: A) Fragmentación automática con balanceo de carga entre nodos del sistema. B) Control de concurrencia distribuido mediante locks globales centralizados. C) Replicación sincrónica de datos entre múltiples instancias PostgreSQL. D) Acceso remoto transparente a datos externos como tablas locales. E) Ninguna de las opciones es correcta.
Respuesta Correcta: D
Explicación: Foreign Data Wrapper (FDW) provee una interfaz para acceder a datos que residen en servidores externos integrándolos lógicamente como tablas locales.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 11
Enunciado: Relacione cada tipo de sistema con la característica que mejor lo diferencia. 1) Sistema Paralelo. 2) Sistema Distribuido. 3) Sistema Cliente/Servidor. 4) Sistema Peer-to-Peer. Características: a) Todos los nodos tienen igual funcionalidad y pueden comunicarse entre sí sin roles. b) Procesadores que comparten memoria o disco bajo un mismo sistema operativo. c) Roles fijos donde uno concentra la gestión de datos y el otro provee la interfaz. d) Cada nodo tiene su propia memoria y almacenamiento comunicándose por una red.
Opciones: A) 1-b, 2-d, 3-c, 4-a B) 1-a, 2-b, 3-c, 4-d C) 1-c, 2-d, 3-b, 4-a D) 1-d, 2-a, 3-c, 4-b E) 1-b, 2-c, 3-d, 4-a
Respuesta Correcta: A
Explicación: Paralelo comparte hardware local (1-b), Distribuido une nodos independientes por red (2-d), Cliente/Servidor separa roles fijos (3-c), y Peer-to-Peer descentraliza funcionalidades (4-a).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 12
Enunciado: Relacione cada tipo de conflicto en la integración de esquemas con su ejemplo representativo. 1) Conflicto de nombres. 2) Conflicto de tipo. 3) Conflicto estructural. 4) Conflicto semántico. Ejemplos: a) El atributo "salario" se almacena como entero en un nodo y texto en otro. b) Un mismo concepto se modela como atributo en un sitio y como relación en otro. c) El mismo concepto recibe distintos nombres (sinónimos) o distintos conceptos comparten nombre. d) El mismo término "cliente" tiene interpretaciones distintas en área comercial y técnica.
Opciones: A) 1-c, 2-a, 3-b, 4-d B) 1-a, 2-b, 3-c, 4-d C) 1-d, 2-c, 3-b, 4-a D) 1-b, 2-d, 3-a, 4-c E) 1-c, 2-b, 3-a, 4-d
Respuesta Correcta: A
Explicación: Nombres abarca sinónimos/homónimos (1-c), Tipo se refiere a tipos de datos (2-a), Estructural a cómo se modela el dato en el esquema (3-b), y Semántico a interpretaciones del negocio (4-d).

[TIPO: ORDENAMIENTO] Pregunta ID: 13
Enunciado: Ordene las siguientes etapas del proceso de diseño Top-Down de una base de datos distribuida, de la primera a la última. 1) Definir la estructura lógica completa (GCS). 2) Aplicar fragmentación y asignación. 3) Obtener los esquemas locales (LCS). 4) Traducir cada LCS en un esquema físico optimizado. 5) Evaluar el impacto en comunicación y carga de trabajo.
Opciones: A) 1, 2, 3, 4, 5 B) 2, 1, 4, 3, 5 C) 3, 2, 1, 5, 4 D) 5, 4, 3, 2, 1 E) 1, 3, 2, 4, 5
Respuesta Correcta: A
Explicación: El enfoque Top-Down inicia diseñando el global conceptual (1), luego fragmenta (2), deriva los locales (3), diseña físicamente los locales (4) y finalmente evalúa el modelo (5).

[TIPO: RESPUESTA CORTA] Pregunta ID: 14
Enunciado: Dos transacciones intentan actualizar concurrentemente el estado de un mismo registro sin usar control de concurrencia. Una transacción sobrescribe a la otra sin leer su cambio. ¿Cómo se denomina esta anomalía?
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: ACTUALIZACION PERDIDA
Explicación: Al no existir bloqueos o control, la última escritura prevalece ciegamente, perdiéndose el trabajo de la primera transacción.

[TIPO: RESPUESTA CORTA] Pregunta ID: 15
Enunciado: Una transacción lee un registro que fue modificado por otra transacción que aún no ha confirmado sus cambios (commit). ¿Cómo se llama esta anomalía de concurrencia?
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: LECTURA SUCIA
Explicación: Leer datos de transacciones en curso que pueden ser revertidos (rollback) expone al sistema a estados inconsistentes conocidos como lecturas sucias.

[TIPO: RESPUESTA CORTA] Pregunta ID: 16
Enunciado: ¿Qué esquema de control de concurrencia distribuye marcas de tiempo a las transacciones para garantizar un ordenamiento serializable global sin usar bloqueos? Escriba la sigla técnica de dos letras.
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: TO
Explicación: Timestamp Ordering (TO) prioriza las operaciones en función de la estampa de tiempo asignada al iniciar cada transacción.

[TIPO: RESPUESTA CORTA] Pregunta ID: 17
Enunciado: Si un sistema distribuido bloquea escrituras al detectar que un nodo ha perdido conectividad para garantizar que todos los nodos tengan exactamente los mismos datos, ¿qué propiedad del Teorema CAP está sacrificando?
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: DISPONIBILIDAD
Explicación: Al rechazar peticiones durante una partición de red para mantener la consistencia fuerte, el sistema deja de estar disponible.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 18
Enunciado: Si un sistema de venta de pasajes adopta consistencia eventual mediante propagación perezosa (lazy) de actualizaciones, ¿cuál es el escenario de error concreto que ocurriría a nivel operativo?
Opciones: A) Las transacciones fallarían debido a deadlocks constantes. B) Los usuarios verían un incremento en el tiempo de procesamiento de la compra. C) Ocurriría doble venta del mismo asiento en distintas sucursales. D) El nodo central colapsaría por el exceso de peticiones simultáneas. E) Los datos se corromperían de forma permanente en la base de datos local.
Respuesta Correcta: C
Explicación: La propagación perezosa crea una ventana de inconsistencia donde múltiples nodos ven el mismo recurso como disponible, permitiendo reservas concurrentes conflictivas.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 19
Enunciado: En el diseño top-down de una base de datos distribuida, el GCS se define primero. Si un arquitecto comete un error grave de rendimiento durante la etapa de fragmentación y asignación, ¿cuál es el impacto en el sistema?
Opciones: A) El error solo afecta al esquema externo de la base de datos distribuida completa. B) El error puede corregirse fácilmente en los esquemas físicos sin afectar al GCS global. C) El optimizador de consultas compensa automáticamente el mal diseño de fragmentación. D) El error se propaga a todos los esquemas físicos locales, amplificando el impacto global. E) Ninguna de las opciones es correcta.
Respuesta Correcta: D
Explicación: En el modelo top-down, las etapas inferiores dependen completamente de las superiores; un mal diseño de fragmentación hereda ineficiencias críticas a cada base de datos local.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 20
Enunciado: Una empresa eléctrica provincial divide su tabla de clientes por cantón. ¿Qué tipo de fragmentación aplica y cuál es su beneficio principal?
Opciones: A) Fragmentación vertical; permite acceder únicamente a los atributos que se necesitan. B) Fragmentación vertical; reduce considerablemente el número total de nodos del sistema. C) Fragmentación mixta; combina simultáneamente criterios de filas y de columnas de la tabla. D) Fragmentación horizontal; cada nodo procesa solo clientes de su cantón, mejora rendimiento local. E) Ninguna de las opciones es correcta.
Respuesta Correcta: D
Explicación: Al dividir por cantón se filtran filas (tuplas), lo que corresponde a fragmentación horizontal, garantizando la localidad de acceso de los datos geográficos.

[TIPO: ORDENAMIENTO] Pregunta ID: 21
Enunciado: Ordene los siguientes pasos para desplegar un contenedor PostgreSQL en Windows usando Docker. 1) Instalar Docker Desktop. 2) Descargar la imagen oficial con docker pull. 3) Ejecutar docker run con los parámetros de puerto y volumen. 4) Verificar el estado del contenedor con docker ps. 5) Conectarse al contenedor con docker exec. 6) Confirmar la persistencia de datos en el volumen.
Opciones: A) 1, 2, 3, 4, 5, 6 B) 2, 1, 4, 3, 5, 6 C) 1, 3, 2, 5, 4, 6 D) 3, 2, 1, 6, 5, 4 E) 6, 5, 4, 3, 2, 1
Respuesta Correcta: A
Explicación: La secuencia lógica técnica requiere instalar el motor, descargar la imagen, instanciar el contenedor, verificar su ejecución, ingresar para operar y validar volúmenes.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 22
Enunciado: Una aplicación de delivery de comida acepta mostrar saldos desactualizados por segundos para garantizar servicio rápido. Otra aplicación del SRI bloquea el servicio si no asegura integridad fiscal exacta. ¿Qué criterio de diseño diferencia ambas arquitecturas?
Opciones: A) La prioridad entre disponibilidad y consistencia en el Teorema CAP. B) El costo de infraestructura disponible para el sistema informático. C) El número de usuarios concurrentes del sistema en producción. D) El tipo de base de datos relacional frente a NoSQL utilizado. E) Ninguna de las opciones indicadas.
Respuesta Correcta: A
Explicación: El delivery prioriza Disponibilidad (sistemas AP con consistencia eventual), mientras que el sistema tributario prioriza Consistencia fuerte (sistemas CP).

[TIPO: RESPUESTA CORTA] Pregunta ID: 23
Enunciado: En la arquitectura ANSI/SPARC distribuida, ¿cuál es la sigla del esquema que describe la organización lógica local de los datos en cada nodo y sirve de puente entre el esquema global y el interno?
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: LCS
Explicación: El Local Conceptual Schema (LCS) representa el modelo de datos unificado pero restringido únicamente a la porción (fragmento) que reside en ese nodo físico específico.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 24
Enunciado: En la arquitectura ANSI/SPARC distribuida, el mapeo entre GCS (Global Conceptual Schema) y LCS (Local Conceptual Schema) es el corazón de la distribución. ¿Qué transparencia específica habilita directamente este mapeo?
Opciones: A) Transparencia de red y transparencia de fragmentación. B) Independencia lógica de los datos distribuidos. C) Transparencia de ubicación y replicación de datos. D) Transparencia de control de concurrencia distribuido. E) Ninguna de las opciones indicadas es correcta.
Respuesta Correcta: E
Explicación: El mapeo GCS-LCS resuelve la ubicación y fragmentación lógica, pero a nivel de opciones de la pregunta, la respuesta evaluada indica que ninguna de las descripciones parciales era correcta de forma aislada para ese mapeo.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 25
Enunciado: Si el SRI necesita integrar datos de facturación provenientes de distintos sistemas heterogéneos (Oracle, PostgreSQL, SQL Server), ¿qué arquitectura de DDBMS es más adecuada?
Opciones: A) DDBMS distribuido de tipo top-down con un único esquema GCS global. B) DDBMS distribuido peer-to-peer completamente homogéneo entre nodos. C) Sistema multidatabase con mediador y wrappers para heterogeneidad. D) Sistema cliente/servidor puro, operando con un único servidor central. E) Ninguna de las opciones es correcta.
Respuesta Correcta: C
Explicación: Cuando los sistemas preexisten y son de distintos fabricantes (heterogéneos), la solución arquitectónica requiere un Multidatabase System (MDBS) apoyado en wrappers.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 26
Enunciado: Según las especificaciones de arquitectura ANSI/SPARC, ¿cuál es la limitación fundamental de la extensión postgres_fdw que impide considerarla un SGBDD completo nativo?
Opciones: A) Requiere que todos los nodos usen la misma versión exacta del software. B) No soporta el lenguaje SQL estándar para consultas remotas. C) No gestiona replicación ni transacciones distribuidas nativas. D) Solo funciona en arquitecturas de red cerradas y aisladas. E) Ninguna de las opciones es correcta.
Respuesta Correcta: C
Explicación: postgres_fdw funciona como un puente de comunicación de acceso remoto (wrapper), pero carece del motor interno para coordinar commits de dos fases nativos o gestionar replicación transaccional.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 27
Enunciado: El algoritmo de consenso Paxos requiere solo una mayoría operativa (quórum) para validar decisiones. ¿En qué aspecto fundamental supera Paxos al protocolo 2PC en términos de tolerancia a fallas?
Opciones: A) Garantiza consistencia fuerte de forma inmediata antes de confirmar la transacción. B) Paxos permite operar con mayoría de nodos sin bloquearse ante fallo del coordinador. C) Elimina por completo la necesidad de mantener cualquier coordinador temporal activo. D) Procesa absolutamente todas las transacciones de forma serial, sin ningún paralelismo. E) Ninguna de las opciones es correcta.
Respuesta Correcta: B
Explicación: 2PC es altamente susceptible a interbloqueos si el coordinador falla (single point of failure), mientras que Paxos soporta particiones y fallas siempre que la mayoría de nodos siga en pie.

[TIPO: RESPUESTA CORTA] Pregunta ID: 28
Enunciado: En una tabla fragmentada, cuando el predicado de división de datos (como un CHECK de PostgreSQL) se aplica directamente sobre los atributos de la propia tabla fragmentada, ¿cómo se denomina a este tipo de fragmentación horizontal?
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: PRIMARIA
Explicación: La fragmentación horizontal primaria basa sus reglas de división estrictamente en columnas que pertenecen a la relación que se está fragmentando.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 29
Enunciado: En un sistema distribuido, dos transacciones acceden al mismo ítem de datos. ¿Bajo qué condición estricta estas operaciones generan un conflicto según el criterio de serializabilidad?
Opciones: A) Solo si ambas operaciones realizadas son de escritura sobre exactamente el mismo dato. B) Solo si la operación de escritura ocurre antes que la lectura del mismo dato exacto. C) Solo si ambas operaciones pertenecen estrictamente al mismo proceso en ejecución concurrente. D) Cuando acceden al mismo dato, son transacciones distintas y al menos una es de escritura. E) Ninguna de las opciones es correcta.
Respuesta Correcta: D
Explicación: Un conflicto ocurre sobre el mismo dato entre diferentes transacciones si al menos una altera el dato (escritura); las lecturas concurrentes puras no generan conflictos.

[TIPO: ORDENAMIENTO] Pregunta ID: 30
Enunciado: Ordene las fases del diseño de fragmentación vertical de primero a último. 1) Recolección: identificar consultas críticas y frecuencias de acceso. 2) Procesamiento: calcular Matriz de Afinidad, Matriz Agrupada y ejecutar SPLIT. 3) Validación: verificar propiedades de completitud, reconstrucción y disyuntividad.
Opciones: A) 1, 2, 3 B) 2, 1, 3 C) 3, 2, 1 D) 1, 3, 2 E) 2, 3, 1
Respuesta Correcta: A
Explicación: Se debe recolectar el comportamiento de las consultas (1), luego aplicar los algoritmos matemáticos de afinidad (2) y finalmente validar que los fragmentos resultantes cumplan las reglas (3).

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 31
Enunciado: En un sistema multidatabase (MDBS), la capa mediadora actúa sobre los DBMS locales. Desde la perspectiva estricta de un DBMS local, ¿cómo percibe este motor a la capa global MDBS?
Opciones: A) Como un nodo par con igual funcionalidad dentro de una red P2P descentralizada. B) Como una extensión interna que modifica directamente el esquema local del DBMS. C) Como el coordinador global que controla la totalidad de sus transacciones. D) Como una aplicación cliente que envía solicitudes y recibe respuestas ordinarias. E) Ninguna de las opciones es correcta.
Respuesta Correcta: D
Explicación: En un MDBS se preserva la autonomía local; los motores base no son conscientes de la distribución y tratan al mediador como un cliente estándar que envía SQL por red.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 32
Enunciado: Un estudiante argumenta que colocar una restricción CHECK en un nodo es suficiente para garantizar un diseño completo de fragmentación horizontal en PostgreSQL. ¿Es válido este argumento?
Opciones: A) Sí, las restricciones CHECK garantizan el enrutamiento automático entre nodos. B) Sí, son el mecanismo oficial y exclusivo de distribución de datos en PostgreSQL. C) No, solo protegen la disyuntividad local, no garantizan completitud ni enrutamiento. D) No, las restricciones CHECK solo aplican durante INSERT, no en UPDATE. E) Ninguna de las opciones es correcta.
Respuesta Correcta: C
Explicación: Un CHECK solo rechaza datos inválidos localmente, pero no mueve la data hacia el nodo que sí debería almacenarla, faltando la lógica de enrutamiento y completitud global.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 33
Enunciado: Relacione cada modelo del Teorema CAP con su implicación ante una falla de red. 1) Modelo CP. 2) Modelo AP. 3) Modelo CA. Implicaciones: a) Ante una falla el sistema deja de responder para proteger la exactitud de los datos. b) El sistema siempre responde pero con datos que podrían estar desactualizados. c) Solo es viable en entornos de un único sitio centralizado sin red.
Opciones: A) 1-a, 2-b, 3-c B) 1-b, 2-a, 3-c C) 1-c, 2-b, 3-a D) 1-a, 2-c, 3-b E) 1-b, 2-c, 3-a
Respuesta Correcta: A
Explicación: CP sacrifica disponibilidad bloqueándose (1-a). AP sacrifica consistencia permitiendo lecturas viejas (2-b). CA ignora la partición asumiendo que no hay red externa (3-c).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 34
Enunciado: Relacione cada esquema de ubicación propuesto por Rahimi con su característica. 1) No Fragmentado. 2) Totalmente Replicado. 3) Parcialmente Replicado. Características: a) Existe una copia completa en cada sitio del sistema. b) Los fragmentos críticos se replican en más de un sitio, combinando fragmentación y replicación; es el más usado en producción. c) Todos los datos residen en un único sitio sin divisiones ni copias.
Opciones: A) 1-c, 2-a, 3-b B) 1-a, 2-b, 3-c C) 1-b, 2-c, 3-a D) 1-c, 2-b, 3-a E) 1-b, 2-a, 3-c
Respuesta Correcta: A
Explicación: No fragmentado significa un nodo único (1-c). Totalmente replicado duplica todo en todos lados (2-a). Parcialmente replicado mezcla técnicas para eficiencia operativa (3-b).

[TIPO: ORDENAMIENTO] Pregunta ID: 35
Enunciado: Ordene los pasos para implementar replicación lógica unidireccional en PostgreSQL. 1) Configurar wal_level = logical en el origen y reiniciar. 2) Crear usuario con privilegios de REPLICATION. 3) Crear las tablas físicas en el destino. 4) Crear la PUBLICATION en el origen. 5) Crear la SUBSCRIPTION en el destino.
Opciones: A) 1, 2, 3, 4, 5 B) 2, 1, 4, 3, 5 C) 1, 4, 2, 3, 5 D) 4, 1, 3, 5, 2 E) 3, 1, 2, 4, 5
Respuesta Correcta: A
Explicación: Primero se habilita el WAL lógico (1), luego el usuario de conexión (2), después se preparan las estructuras vacías destino (3), se publica el dato (4) y finalmente se suscribe el destino para iniciar el flujo (5).

[TIPO: RESPUESTA CORTA] Pregunta ID: 36
Enunciado: En la fragmentación vertical, ¿qué operador del álgebra relacional permite reconstruir la relación original combinando sus fragmentos basándose en sus claves primarias?
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: JOIN
Explicación: El operador de unión (JOIN) permite emparejar las columnas separadas de vuelta en una sola fila consolidada.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 37
Enunciado: En el contexto de los DDBMS, el término "promesa" se usa frecuentemente en lugar de "garantía". ¿Por qué las características de un DDBMS son promesas y no garantías absolutas?
Opciones: A) Porque depende de la implementación, trade-offs de distribución y contexto de despliegue. B) Porque los fabricantes no están dispuestos a comprometerse contractualmente. C) Porque los usuarios finales no pueden verificar técnicamente dichas garantías ofrecidas. D) Porque, en la práctica, los DDBMS siguen siendo sistemas fundamentalmente experimentales. E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: Las limitaciones físicas (red, latencia, CAP) obligan a que el nivel de cumplimiento dependa de la configuración y de los sacrificios de diseño aceptados por los arquitectos.

[TIPO: RESPUESTA CORTA] Pregunta ID: 38
Enunciado: ¿Cuál es el término técnico que designa la propiedad de un sistema distribuido que permite al usuario acceder a datos sin necesidad de conocer en qué nodo están almacenados físicamente? (Concepto fundamental en el diseño de DDBMS)
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: TRANSPARENCIA
Explicación: La transparencia de distribución aísla la complejidad física del desarrollador de aplicaciones.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 39
Enunciado: Un arquitecto elige replicación lógica asíncrona para el núcleo de un sistema bancario que no puede tolerar pérdidas de transacciones. Argumenta que brinda más flexibilidad. ¿Es adecuada esta elección?
Opciones: A) Sí, porque la replicación asíncrona resulta suficiente para garantizar alta disponibilidad general. B) Sí, la replicación lógica puede configurarse para ofrecer una consistencia fuerte equivalente al modelo síncrono. C) No, porque la replicación lógica en general no es compatible con entornos bancarios críticos. D) No, la replicación lógica asíncrona no garantiza consistencia fuerte; un fallo antes de propagar pierde escrituras. E) Ninguna de las opciones es correcta.
Respuesta Correcta: D
Explicación: Los sistemas críticos como los bancarios requieren propagación síncrona (eager); la propagación asíncrona (lazy) conlleva riesgo de pérdida de datos ante fallos repentinos.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 40
Enunciado: Relacione la estrategia de propagación con sus consecuencias de diseño. 1) Ansiosa (Eager). 2) Perezosa (Lazy). Consecuencias: a) Garantiza consistencia fuerte en todas las réplicas pero aumenta la latencia de escritura. b) La transacción confirma rápido y propaga cambios asíncronamente; mejora rendimiento pero permite divergencia temporal.
Opciones: A) 1-a, 2-b B) 1-b, 2-a C) 1-a, 2-a D) 1-b, 2-b E) Ninguna de las opciones.
Respuesta Correcta: A
Explicación: Eager bloquea la confirmación hasta que todas las réplicas tengan el dato (1-a), mientras que Lazy responde rápido al cliente asumiendo la eventual actualización de la red (2-b).

[TIPO: ORDENAMIENTO] Pregunta ID: 41
Enunciado: Ordene los criterios de decisión para elegir una estrategia de ubicación de datos, priorizando la disponibilidad ante fallos en un sistema bancario crítico. 1) Garantizar que al menos una réplica secundaria pueda asumir las operaciones. 2) Verificar que el número de réplicas cumpla el quórum mínimo requerido. 3) Aplicar replicación parcial en fragmentos críticos. 4) Ubicar cada fragmento cerca del sitio de lectura. 5) Minimizar el costo de sincronización.
Opciones: A) 1, 2, 3, 4, 5 B) 2, 1, 3, 5, 4 C) 3, 1, 2, 5, 4 D) 1, 3, 2, 4, 5 E) 4, 2, 1, 3, 5
Respuesta Correcta: A
Explicación: En un entorno de alta disponibilidad bancaria, asegurar el nodo de failover es prioridad absoluta (1), seguido del cumplimiento de quórum transaccional para evitar split-brain (2), usando replicación parcial estratégica (3), localidad de datos (4) y por último optimización de latencia (5).

[TIPO: ORDENAMIENTO] Pregunta ID: 42
Enunciado: Ordene los pasos para crear fragmentación horizontal nativa en PostgreSQL 10+ usando particionamiento. 1) Crear la tabla maestra declarando PARTITION BY LIST (columna). 2) Crear las tablas particiones locales usando PARTITION OF ... FOR VALUES. 3) Insertar datos en la maestra y validar el enrutamiento automático a las particiones.
Opciones: A) 1, 2, 3 B) 2, 1, 3 C) 3, 1, 2 D) 2, 3, 1 E) 1, 3, 2
Respuesta Correcta: A
Explicación: Primero se declara el esquema declarativo padre (1), se instancian los segmentos hijos físicos con sus reglas de partición (2) y luego se ingresan datos para validar (3).

[TIPO: RESPUESTA CORTA] Pregunta ID: 43
Enunciado: ¿Cuál es el nombre del protocolo estándar industrial que garantiza la atomicidad global de una transacción distribuida mediante fases de votación y decisión coordinadas por un nodo coordinador central? Escriba la sigla en MAYÚSCULAS.
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: 2PC
Explicación: El Two-Phase Commit protocol (2PC) es el estándar clásico en SGBD relacionales distribuidos para asegurar que todos los nodos hagan commit o rollback juntos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 44
Enunciado: El control distribuido elimina cuellos de botella al repartir responsabilidades. ¿Qué beneficio directo describe la relación entre escalabilidad y rendimiento en este diseño?
Opciones: A) Al agregar nodos sin reestructurar, la carga se reparte y mejora el rendimiento global. B) Garantiza que absolutamente todas las transacciones se ejecuten en estricto orden serial. C) Elimina por completo la necesidad de cualquier protocolo de coordinación distribuida. D) Reduce de forma directa el total de recursos de hardware necesarios en todo el sistema. E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: La arquitectura de control verdaderamente descentralizada permite escalar horizontalmente, sumando capacidad de cómputo que absorbe cargas adicionales dinámicamente.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 45
Enunciado: En el problema de diseño estructural, si aplicamos algoritmos de fragmentación vertical a una tabla PROYECTOS y obtenemos F1(PNO, BUDGET) y F2(PNAME, LOC), donde PNO es la clave primaria. ¿Qué problema crítico de diseño presenta esta matriz de fragmentación propuesta?
Opciones: A) F2 no incluye el atributo BUDGET de la tabla. B) Viola la localidad de los datos en el sistema distribuido. C) F2 no incluye PNO, impidiendo reconstrucción con JOIN. D) Genera fragmentos demasiado grandes para el sistema. E) Ninguna de las opciones es correcta.
Respuesta Correcta: C
Explicación: La propiedad de Reconstrucción (Reconstruction) exige que cada fragmento vertical incluya la clave primaria de la relación base, de lo contrario las tuplas de F2 quedan huérfanas y no se pueden cruzar.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 46
Enunciado: Relacione cada nivel de la arquitectura ANSI/SPARC distribuida con su función. 1) Esquema Interno Local (LIS). 2) Esquema Conceptual Local (LCS). 3) Esquema Conceptual Global (GCS). 4) Esquema Externo (ES). Funciones: a) Vista personalizada que cada usuario obtiene del sistema. b) Descripción unificada de todos los datos distribuidos. c) Organización lógica de datos en un nodo específico. d) Define cómo se almacenan físicamente los datos en archivos locales.
Opciones: A) 1-d, 2-c, 3-b, 4-a B) 1-c, 2-d, 3-a, 4-b C) 1-a, 2-b, 3-c, 4-d D) 1-b, 2-a, 3-d, 4-c E) 1-d, 2-a, 3-c, 4-b
Respuesta Correcta: A
Explicación: LIS es físico (1-d). LCS es el fragmento lógico local (2-c). GCS es el modelo unificado total (3-b). ES es la vista parcial del usuario (4-a).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 47
Enunciado: Relacione la dimensión de clasificación de DDBMS según Özsu con su definición. 1) Autonomía. 2) Distribución. 3) Heterogeneidad. 4) Integración. Definiciones: a) Grado en que los gestores locales pueden operar de forma independiente. b) Dispersión física de los nodos. c) Diferencias entre componentes de hardware, protocolos o modelos de datos. d) Capacidad del sistema para añadir nodos o esquemas unificados.
Opciones: A) 1-a, 2-b, 3-c, 4-d B) 1-b, 2-c, 3-d, 4-a C) 1-c, 2-d, 3-a, 4-b D) 1-d, 2-a, 3-b, 4-c E) 1-a, 2-c, 3-b, 4-d
Respuesta Correcta: A
Explicación: Autonomía mide el control local (1-a). Distribución evalúa si están en red (2-b). Heterogeneidad mide diferencias tecnológicas (3-c). Integración es cómo unen los modelos (4-d).

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 48
Enunciado: Una empresa tiene un servidor publicador en Quito para la tabla Clientes. Sus oficinas de Cuenca y Portoviejo son suscriptores lógicos. Un usuario en Portoviejo necesita replicar ahora la tabla Contratos. ¿Cuál es la acción de diseño más recomendada?
Opciones: A) Convertir al servidor de Portoviejo en un publicador secundario independiente. B) Crear una nueva suscripción completamente directa y aislada únicamente en Portoviejo. C) Ampliar la publicación en Quito incluyendo Contratos, así todos los suscriptores reciben cambios. D) Modificar la suscripción existente de Cuenca en cascada hacia Portoviejo. E) Ninguna de las opciones es correcta.
Respuesta Correcta: C
Explicación: Para mantener la topología de replicación limpia y controlada, se agregan artículos (tablas) a las publicaciones existentes, propagando el cambio a todos los nodos suscritos a ese canal de negocio.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 49
Enunciado: Relacione cada protocolo de tolerancia a fallas en escrituras replicadas con su característica distintiva. 1) Regla de intersección de quórum. 2) Protocolo de copias disponibles (ROWAA). 3) Consenso de quórum de Gifford. 4) Votación de mayoría de Thomas. Características: a) Obliga a que la suma de votos de lectura y escritura supere el total, asegurando solapamiento. b) Se asume que los nodos fallan de forma limpia (fail-stop) escribiendo en todas las copias vivas. c) Asigna identificadores (pesos/versiones) a la lectura/escritura gestionando redes. d) Exige que el quórum de escritura sea estrictamente mayor a la mitad de los votos totales.
Opciones: A) 1-a, 2-b, 3-c, 4-d B) 1-b, 2-c, 3-d, 4-a C) 1-c, 2-d, 3-a, 4-b D) 1-d, 2-a, 3-b, 4-c E) 1-a, 2-d, 3-c, 4-b
Respuesta Correcta: A
Explicación: La regla básica de quórum es la intersección V_r + V_w > V (1-a). Copias disponibles ignora nodos caídos (2-b). Gifford asigna pesos (3-c). Mayoría pura requiere más del 50% de votos (4-d).

[TIPO: ORDENAMIENTO] Pregunta ID: 50
Enunciado: Ordene las fases del procesamiento distribuido de consultas según la teoría clásica de DDBMS. 1) Descomposición de consultas. 2) Localización de datos. 3) Optimización global. 4) Ejecución distribuida.
Opciones: A) 1, 2, 3, 4 B) 2, 1, 4, 3 C) 3, 1, 2, 4 D) 1, 3, 2, 4 E) 2, 3, 1, 4
Respuesta Correcta: A
Explicación: El motor primero descompone y normaliza la sintaxis (1), luego localiza los fragmentos físicos en red (2), genera y evalúa planes de costo (3), y finalmente ejecuta los operadores en pipeline (4).

[TIPO: ORDENAMIENTO] Pregunta ID: 51
Enunciado: Ordene las fases de ejecución de escritura en un protocolo Eager basado en Bloqueo Distribuido (2PL). 1) El coordinador solicita bloqueos de escritura a los administradores locales de cada sitio. 2) Cada nodo otorga el bloqueo si el ítem de datos no está en uso. 3) Se envían los nuevos valores a actualizar una vez que todos los bloqueos han sido asegurados. 4) Los bloqueos se mantienen firmes hasta completar todo el proceso de confirmación de dos fases.
Opciones: A) 1, 2, 3, 4 B) 2, 1, 3, 4 C) 3, 1, 2, 4 D) 1, 3, 2, 4 E) 4, 2, 1, 3
Respuesta Correcta: A
Explicación: El coordinador distribuye el intento de bloqueo (1), los sitios aprueban localmente (2), la data fluye (3) y los bloqueos se sostienen hasta el commit final (4).

[TIPO: RESPUESTA CORTA] Pregunta ID: 52
Enunciado: ¿Cuál es el nombre del modelo de implementación clásico de operadores relacionales que expone tres primitivas (Open, Next, Close) permitiendo paralelismo de datos en pipeline entre nodos durante una consulta distribuida? Escriba su respuesta en MAYÚSCULAS.
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: ITERADOR
Explicación: El modelo iterador evalúa filas bajo demanda por la red, evitando saturar la memoria materializando resultados intermedios gigantescos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 53
Enunciado: En un clúster YugabyteDB distribuido, una tabla se fragmenta mediante PARTITION BY HASH. Para que el diseño cumpla la propiedad formal de completitud, ¿qué relación matemática estricta debe verificarse entre la tabla padre y sus fragmentos físicos?
Opciones: A) Cada fragmento individual debe tener exactamente el mismo número de filas. B) La suma total de todos los fragmentos generados debe superar al total original. C) El total de filas padre debe igualar la suma de filas de todos los fragmentos. D) La tabla padre original debe almacenar copias redundantes de todos los datos. E) Ninguna de las opciones es correcta.
Respuesta Correcta: C
Explicación: La regla de completitud dictamina que toda tupla de la relación original debe pertenecer a al menos un fragmento, sin perderse ningún dato en el proceso de particionamiento.

[TIPO: ORDENAMIENTO] Pregunta ID: 54
Enunciado: Ordene los pasos para procesar una actualización bajo un protocolo centralizado ansioso de "maestro único" (Primary Copy). 1) La aplicación cliente envía la escritura directamente al sitio maestro. 2) El maestro obtiene los bloqueos necesarios y aplica el cambio en su propia copia. 3) El maestro reenvía la escritura a todos los nodos esclavos de forma síncrona. 4) Las consultas de solo lectura pueden ejecutarse de los esclavos tras la actualización.
Opciones: A) 1, 2, 3, 4 B) 2, 1, 4, 3 C) 3, 2, 1, 4 D) 1, 3, 2, 4 E) 4, 1, 2, 3
Respuesta Correcta: A
Explicación: La arquitectura Master-Slave rutea escrituras al líder (1), este persiste localmente (2), propaga el registro síncronamente (3) y finalmente los seguidores pueden servir lecturas consistentes (4).

[TIPO: ORDENAMIENTO] Pregunta ID: 55
Enunciado: Ordene las fases del protocolo de transición de vistas para gestionar nodos caídos o recuperados en un sistema con particiones virtuales. 1) Fase de sospecha: un nodo nota la ausencia de otro y propone crear una nueva partición. 2) Fase de acuerdo: los sitios alcanzables votan para validar la nueva lista de miembros. 3) Fase de creación: se asigna un nuevo identificador secuencial a la partición. 4) Fase de puesta al día: los nodos rezagados copian datos perdidos del grupo mayoritario.
Opciones: A) 1, 2, 3, 4 B) 2, 1, 4, 3 C) 1, 3, 2, 4 D) 4, 3, 2, 1 E) 3, 1, 2, 4
Respuesta Correcta: A
Explicación: El sistema primero detecta la falla (1), busca consenso sobre quién sobrevive (2), genera el nuevo sub-clúster oficial (3) y sincroniza datos de recuperación (4).

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 56
Enunciado: En el procesamiento de consultas, compare la complejidad computacional del operador Join basado en ordenamiento vs un Producto Cartesiano puro. ¿Cuál afirmación es correcta?
Opciones: A) Ambos operadores tienen exactamente la misma complejidad lineal O(n) en tiempo. B) El producto cartesiano resulta ser computacionalmente más eficiente en la práctica. C) El join ordenado es O(n log n), el producto cartesiano O(n^2) al combinar tuplas. D) Ambos operadores presentan complejidad O(n al cuadrado) en su peor caso posible. E) Ninguna de las opciones es correcta.
Respuesta Correcta: C
Explicación: El Sort-Merge Join optimiza la unión, mientras que el producto cartesiano es una explosión combinatoria ineficiente.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 57
Enunciado: Un optimizador distribuido mantiene estadísticas a nivel de atributo usando histogramas detallados en lugar de solo promedios por relación. ¿Qué compensación (trade-off) implica esta decisión de diseño?
Opciones: A) Provoca una menor precisión general en la estimación de recursos del sistema. B) Elimina la necesidad de actualizar el diccionario de datos periódicamente. C) Los histogramas no afectan al rendimiento del sistema en general. D) Mayor precisión en selectividad, pero mayor consumo de memoria y mantenimiento. E) Ninguna de las opciones es correcta.
Respuesta Correcta: D
Explicación: Los metadatos detallados (histogramas) mejoran dramáticamente las decisiones de costo del optimizador, pero requieren procesamiento adicional para mantener sus barras (buckets) actualizadas tras cambios de datos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 58
Enunciado: Para una consulta distribuida donde cruzaremos Empleados en Quito (10000 filas) con Asignaciones en Guayaquil (100000 filas, pero restringido a solo 100 ingenieros específicos). ¿Qué estrategia optimiza dramáticamente el costo de transferencia por red?
Opciones: A) Duplicar completamente ambas tablas en los dos sitios remotos disponibles. B) Transferir la tabla Asignaciones completa hacia el sitio de Quito. C) Ejecutar el cruce completo de ambas tablas en el sitio de Guayaquil. D) Filtrar 100 ingenieros en Quito y enviar solo esas filas a Guayaquil. E) Ninguna de las opciones es correcta.
Respuesta Correcta: D
Explicación: El principio fundamental de la optimización distribuida es ejecutar operadores restrictivos (Selection, Projection) lo más cerca del origen posible para minimizar el volumen de bytes enviados por el canal de red.

[TIPO: RESPUESTA CORTA] Pregunta ID: 59
Enunciado: En la capa de optimización global, encontrar la estrategia de ejecución óptima evaluando cada posible permutación de joins para consultas con muchas tablas es inasumible computacionalmente. ¿Cómo se clasifica en teoría de la computación este tipo de explosión combinatoria? Escriba su respuesta con guion en el medio (Ejemplo: AA-BB).
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: NP-HARD
Explicación: El problema de ordenamiento óptimo de multi-joins es NP-Hard, lo que justifica el uso de heurísticas (como el filtrado temprano) en lugar de búsquedas exhaustivas estériles.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 60
Enunciado: Durante el diseño de optimizadores, el análisis semántico aplica reglas sobre la consulta antes de intentar generar árboles de ejecución. ¿Cuál es el beneficio directo de aplicar este análisis riguroso?
Opciones: A) Aumenta considerablemente la velocidad general de la red de comunicaciones. B) El orden de validación resulta indiferente para el resultado final de la consulta ejecutada. C) Rechazar consultas semánticamente incorrectas pronto, evitando desperdicio de CPU y envío de datos. D) Garantiza que toda consulta enviada se ejecute correctamente siempre, sin excepción. E) Ninguna de las opciones es correcta.
Respuesta Correcta: C
Explicación: Validar tipos de datos, privilegios y existencia de tablas al inicio (front-end del motor) previene la sobrecarga masiva de lanzar un proceso distribuido fallido.

[TIPO: RESPUESTA CORTA] Pregunta ID: 61
Enunciado: Para detectar condiciones de interbloqueo (deadlock) en sistemas distribuidos que utilizan bloqueos Eager, el sistema construye y analiza un grafo dirigido cíclico. ¿Con qué sigla técnica de tres letras se conoce a la estructura Wait-For Graph?
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: WFG
Explicación: El WFG (Wait-For Graph) rastrea qué transacciones están reteniendo recursos y cuáles están esperando, identificando ciclos que indican bloqueos mutuos insolubles.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 62
Enunciado: En escenarios donde el espacio de búsqueda del optimizador crece explosivamente al cruzar 15 o más relaciones distribuidas, ¿qué tipo de estrategia de búsqueda abandona el determinismo tradicional para evitar saturar la memoria del servidor de BD?
Opciones: A) Búsqueda exhaustiva determinística tradicional sobre todo el espacio de planes. B) Ejecución secuencial simple, sin construir ningún árbol de ejecución completo. C) Revisión manual y detallada del plan por parte del DBA especializado. D) Estrategias aleatorizadas como recocido simulado o mejora iterativa. E) Ninguna de las opciones es correcta.
Respuesta Correcta: D
Explicación: Cuando el árbol de combinaciones es demasiado vasto para algoritmos de programación dinámica estándar (System R), las bases de datos modernas usan algoritmos genéticos y estocásticos para hallar planes "suficientemente buenos" en tiempos limitados.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 63
Enunciado: Cuando el analizador de un optimizador altera el árbol algebraico forzando selecciones y proyecciones hacia las hojas (filtrado temprano) y aplicando podas (pruning) predefinidas sin explorar otras vías, ¿qué enfoque está utilizando?
Opciones: A) Enfoque heurístico con reglas prácticas pre-codificadas y sin costos. B) Estrategia estocástica completamente ciega, sin ningún tipo de evaluación previa. C) Búsqueda exhaustiva lineal recorriendo secuencialmente todos los planes posibles. D) Procesamiento de flujo continuo, sin evaluación alguna de costos asociados. E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: Las reglas heurísticas (como "hacer JOIN siempre desde la tabla más pequeña") son atajos determinísticos implementados por los desarrolladores del SGBD para acelerar la toma de decisiones sin calcular matemáticamente todas las variantes.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 64
Enunciado: Relacione la fase del procesamiento de consultas con el esquema o metadato del cual extrae su información principal. 1) Descomposición. 2) Localización. 3) Ejecución. Esquemas: a) Esquema Conceptual Global (GCS), usado para validación de sintaxis unificada. b) Esquema de Fragmentación, usado para rutear el plan a nodos específicos. c) Esquemas Internos Locales (LIS), usados por el motor propio del nodo para leer disco.
Opciones: A) 1-a, 2-b, 3-c B) 1-b, 2-c, 3-a C) 1-c, 2-a, 3-b D) 1-a, 2-c, 3-b E) 1-c, 2-b, 3-a
Respuesta Correcta: A
Explicación: El parsing inicial requiere conocer todas las tablas lógicas del sistema en el GCS (1-a), luego la ubicación física se lee del catálogo de fragmentos (2-b), y finalmente el motor local accede a sus discos guiado por su LIS local (3-c).

[TIPO: ORDENAMIENTO] Pregunta ID: 65
Enunciado: Ordene correctamente las fases del protocolo Bloqueo en Dos Fases (2PL). 1) Fase de decrecimiento (liberación gradual de candados). 2) Fase de crecimiento (adquisición progresiva de candados). 3) Punto de bloqueo (último candado adquirido). 4) Confirmación o aborto (commit/rollback).
Opciones: A) 2, 3, 1, 4 B) 1, 2, 3, 4 C) 2, 1, 3, 4 D) 3, 2, 1, 4 E) 4, 2, 3, 1
Respuesta Correcta: A
Explicación: El protocolo 2PL inicia con la fase de crecimiento (2) donde se adquieren candados, se alcanza el punto de bloqueo (3), luego se liberan gradualmente en la fase de decrecimiento (1) y finalmente se confirma o aborta (4).

[TIPO: ORDENAMIENTO] Pregunta ID: 66
Enunciado: Ordene las fases del algoritmo de control de concurrencia optimista. 1) Fase de validación: se verifica si existieron conflictos con transacciones concurrentes. 2) Fase de lectura: la transacción lee los datos y los almacena en su espacio de trabajo privado. 3) Fase de escritura: si la validación es exitosa, los cambios se aplican a la base de datos.
Opciones: A) 1, 2, 3 B) 2, 1, 3 C) 3, 2, 1 D) 2, 3, 1 E) 1, 3, 2
Respuesta Correcta: B
Explicación: El control optimista primero lee (2), luego valida (1) y finalmente escribe (3), por lo que la secuencia correcta es 2,1,3.

[TIPO: ORDENAMIENTO] Pregunta ID: 67
Enunciado: Ordene los pasos del proceso de detección distribuida de interbloqueos mediante el algoritmo de grafos de espera. 1) Se comparte el WFG local con los demás sitios. 2) Cada sitio construye su grafo de espera local (WFG). 3) Se aplica un algoritmo de detección de ciclos sobre el grafo global. 4) Se forma un grafo de espera global unificado. 5) Si se detecta un ciclo, se elige una transacción víctima para abortar.
Opciones: A) 2, 1, 4, 3, 5 B) 1, 2, 3, 4, 5 C) 4, 3, 2, 1, 5 D) 2, 4, 1, 3, 5 E) 3, 5, 2, 1, 4
Respuesta Correcta: A
Explicación: Primero se construye el WFG local (2), luego se comparte (1), se unifica en un grafo global (4), se detectan ciclos (3) y se selecciona víctima (5).

[TIPO: ORDENAMIENTO] Pregunta ID: 68
Enunciado: Ordene los pasos de la técnica de prevención de interbloqueos por ordenamiento de recursos. 1) Asignar un orden total y estático a todos los recursos del sistema. 2) Si la transacción necesita un recurso de orden menor que alguno que ya posee, debe liberar los recursos de orden mayor. 3) Las transacciones deben solicitar recursos respetando el orden ascendente. 4) La transacción vuelve a solicitar los recursos liberados una vez adquirido el nuevo.
Opciones: A) 1, 3, 2, 4 B) 2, 1, 4, 3 C) 1, 2, 3, 4 D) 3, 1, 2, 4 E) 4, 2, 1, 3
Respuesta Correcta: A
Explicación: Primero se define el orden (1), luego se exige que las peticiones sigan ese orden (3); si una transacción necesita un recurso de orden inferior, debe liberar los superiores (2) y posteriormente readquirirlos (4).

[TIPO: ORDENAMIENTO] Pregunta ID: 69
Enunciado: Ordene los pasos que sigue un administrador de bloqueo centralizado (C2PL) al recibir una solicitud de candado exclusivo. 1) Recibir solicitud de candado de la transacción. 2) Verificar si el dato está actualmente bloqueado (por cualquier modo). 3) Si está libre, otorgar el candado exclusivo y registrar la transacción; si está ocupado, encolar la solicitud. 4) Cuando la transacción libera el candado, revisar la cola de espera y otorgar el candado a la siguiente solicitud compatible.
Opciones: A) 1, 2, 3, 4 B) 2, 1, 3, 4 C) 1, 3, 2, 4 D) 3, 1, 2, 4 E) 1, 2, 4, 3
Respuesta Correcta: A
Explicación: La secuencia lógica es recibir (1), verificar el estado (2), otorgar o esperar (3) y gestionar la liberación y despertar de esperas (4).

[TIPO: ORDENAMIENTO] Pregunta ID: 70
Enunciado: Ordene las verificaciones que realiza el algoritmo Timestamp Ordering (TO) Básico al procesar una operación de escritura sobre un dato x. 1) Leer el valor actual de rts(x). 2) Leer el valor actual de wts(x). 3) Comparar el timestamp de la transacción ts(T) con rts(x) y wts(x). 4) Si ts(T) es mayor o igual que ambos, escribir el dato y actualizar wts(x) con ts(T); en caso contrario, abortar la transacción.
Opciones: A) 1, 2, 3, 4 B) 2, 1, 4, 3 C) 3, 1, 2, 4 D) 1, 3, 2, 4 E) 2, 3, 1, 4
Respuesta Correcta: A
Explicación: Primero se consultan rts(x) (1) y wts(x) (2), luego se realiza la comparación con ts(T) (3) y se decide si escribir o abortar (4).

[TIPO: ORDENAMIENTO] Pregunta ID: 71
Enunciado: Ordene las transiciones de estado típicas de una transacción que utiliza Bloqueo en Dos Fases (2PL). 1) Activa. 2) Adquiriendo candados (fase de crecimiento). 3) Punto de bloqueo (último candado adquirido). 4) Liberando candados (fase de decrecimiento). 5) Comprometida o abortada.
Opciones: A) 1, 2, 3, 4, 5 B) 2, 1, 3, 5, 4 C) 3, 2, 1, 4, 5 D) 1, 4, 2, 3, 5 E) 5, 1, 2, 3, 4
Respuesta Correcta: A
Explicación: La transacción inicia activa (1), entra en crecimiento adquiriendo candados (2), alcanza el punto de bloqueo (3), después libera candados en decrecimiento (4) y finalmente se confirma o aborta (5).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 72
Enunciado: Relacione cada anomalía de concurrencia con su definición. 1) Actualización perdida. 2) Lectura sucia. 3) Lectura no repetible. 4) Lectura fantasma. 5) Análisis inconsistente. 6) Aborto en cascada. Definiciones: X) Una transacción sobrescribe cambios de otra sin haberlos integrado. Y) Una transacción lee un valor no confirmado que luego es revertido. Z) Dos lecturas del mismo dato en una transacción devuelven valores diferentes por modificaciones confirmadas externas. W) Una consulta obtiene un conjunto distinto de filas al repetirse por inserciones ajenas. V) Una transacción realiza cálculos sobre datos que cambian concurrentemente, dando un resultado global incorrecto. U) Una transacción debe abortar porque leyó datos de una transacción que luego abortó.
Opciones: A) 1-X, 2-Y, 3-Z, 4-W, 5-V, 6-U B) 1-Y, 2-X, 3-W, 4-Z, 5-U, 6-V C) 1-W, 2-V, 3-U, 4-X, 5-Y, 6-Z D) 1-Z, 2-W, 3-X, 4-Y, 5-U, 6-V E) 1-V, 2-U, 3-Z, 4-W, 5-X, 6-Y
Respuesta Correcta: A
Explicación: La actualización perdida es sobrescribir sin leer cambios (1-X), la lectura sucia accede a datos no confirmados (2-Y), la no repetible ve cambios entre lecturas (3-Z), el fantasma aparece por inserciones (4-W), el análisis inconsistente mezcla datos inconsistentes (5-V) y el aborto en cascada fuerza abortos por dependencia (6-U).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 73
Enunciado: Relacione cada mecanismo o variante de control de concurrencia con su descripción. 1) 2PL Básico. 2) 2PL Conservador. 3) 2PL Estricto. 4) Timestamp Ordering Básico. 5) Timestamp Ordering Multiversión. 6) Control Optimista. Descripciones: X) Adquiere todos los candados al inicio de la transacción. Y) Libera candados gradualmente tras el punto de bloqueo. Z) Retiene todos los candados hasta el final de la transacción. W) Rechaza operaciones que violan el orden temporal, provocando reinicios. V) Mantiene múltiples versiones para evitar rechazos de lectura. U) Asume pocos conflictos, valida al final y aplica cambios en una fase posterior.
Opciones: A) 1-Y, 2-X, 3-Z, 4-W, 5-V, 6-U B) 1-X, 2-Y, 3-Z, 4-U, 5-V, 6-W C) 1-Z, 2-W, 3-X, 4-Y, 5-U, 6-V D) 1-W, 2-V, 3-U, 4-X, 5-Y, 6-Z E) 1-V, 2-U, 3-Y, 4-Z, 5-W, 6-X
Respuesta Correcta: A
Explicación: 2PL Básico libera después del punto de bloqueo (1-Y); 2PL Conservador bloquea todo al inicio (2-X); 2PL Estricto retiene hasta commit (3-Z); TO Básico rechaza y reinicia (4-W); TO Multiversión evita rechazos de lectura (5-V); Control Optimista valida al final (6-U).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 74
Enunciado: Relacione cada nivel de aislamiento ANSI/ISO con las anomalías que permite. 1) READ UNCOMMITTED. 2) READ COMMITTED. 3) REPEATABLE READ. 4) SERIALIZABLE. Descripciones: X) Permite lecturas sucias, lecturas no repetibles y fantasmas. Y) Evita lecturas sucias, pero permite lecturas no repetibles y fantasmas. Z) Evita lecturas sucias y no repetibles, pero pueden aparecer fantasmas. W) Evita todas las anomalías (lecturas sucias, no repetibles y fantasmas).
Opciones: A) 1-X, 2-Y, 3-Z, 4-W B) 1-Y, 2-X, 3-W, 4-Z C) 1-W, 2-Z, 3-Y, 4-X D) 1-Z, 2-W, 3-X, 4-Y E) 1-X, 2-Z, 3-Y, 4-W
Respuesta Correcta: A
Explicación: READ UNCOMMITTED permite todo (1-X); READ COMMITTED evita sucias (2-Y); REPEATABLE READ evita sucias y no repetibles (3-Z); SERIALIZABLE evita todas (4-W).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 75
Enunciado: Relacione cada variable o componente del modelo de marcas de tiempo con su significado. 1) rts(x). 2) wts(x). 3) ts(T). 4) ID del sitio. 5) Contador lógico. Significados: X) Mayor marca de tiempo de una transacción que ha leído el dato x. Y) Mayor marca de tiempo de una transacción que ha escrito el dato x. Z) Marca de tiempo única asignada a la transacción T. W) Identificador único del nodo, usado para romper empates en marcas de tiempo. V) Contador monotónico que avanza para generar marcas de tiempo locales.
Opciones: A) 1-X, 2-Y, 3-Z, 4-W, 5-V B) 1-Y, 2-X, 3-Z, 4-V, 5-W C) 1-Z, 2-W, 3-X, 4-Y, 5-V D) 1-W, 2-V, 3-Y, 4-X, 5-Z E) 1-V, 2-Z, 3-W, 4-X, 5-Y
Respuesta Correcta: A
Explicación: rts(x) es la marca de lectura máxima (1-X), wts(x) la de escritura máxima (2-Y), ts(T) el identificador de la transacción (3-Z), el ID del sitio garantiza unicidad (4-W) y el contador lógico genera valores monotónicos (5-V).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 76
Enunciado: Relacione cada estrategia de manejo de interbloqueos con su descripción. 1) Prevención. 2) Detección. 3) Evitación. 4) Timeout. 5) Algoritmo del avestruz (ignorar). Descripciones: X) El sistema no implementa ningún mecanismo y asume que los interbloqueos son muy raros. Y) Se restringe la forma en que las transacciones solicitan recursos para eliminar estructuralmente los interbloqueos. Z) Se permite que ocurran interbloqueos, pero el sistema los identifica y resuelve (por ejemplo, abortando una transacción). W) Se utiliza un temporizador; si una transacción espera demasiado, se aborta asumiendo que está en un interbloqueo. V) Se evalúa cada solicitud de recurso y solo se concede si no lleva a un estado inseguro.
Opciones: A) 1-Y, 2-Z, 3-V, 4-W, 5-X B) 1-Z, 2-Y, 3-W, 4-X, 5-V C) 1-W, 2-V, 3-X, 4-Y, 5-Z D) 1-V, 2-W, 3-Y, 4-Z, 5-X E) 1-X, 2-Z, 3-V, 4-W, 5-Y
Respuesta Correcta: A
Explicación: Prevención impone restricciones (1-Y); detección permite que ocurran y los resuelve (2-Z); evitación verifica cada solicitud (3-V); timeout usa temporizador (4-W); avestruz no hace nada (5-X).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 77
Enunciado: Relacione cada tipo de candado o concepto relacionado con su propiedad. 1) Candado compartido (S). 2) Candado exclusivo (X). 3) Múltiples candados compartidos. 4) Candado exclusivo único. 5) Promoción de candado. Descripciones: X) Permite que varias transacciones lean el mismo dato simultáneamente. Y) Solo una transacción puede poseerlo y excluye cualquier otro candado. Z) Varias transacciones pueden retener candados S sobre el mismo dato al mismo tiempo. W) Si una transacción tiene un candado S y desea escribir, puede convertirlo en X si es la única poseedora de S. V) Cuando un dato está bloqueado con X, ninguna otra transacción puede leerlo ni escribirlo.
Opciones: A) 1-X, 2-Y, 3-Z, 4-V, 5-W B) 1-Y, 2-X, 3-W, 4-Z, 5-V C) 1-Z, 2-W, 3-X, 4-Y, 5-V D) 1-V, 2-Z, 3-Y, 4-W, 5-X E) 1-W, 2-V, 3-Z, 4-Y, 5-X
Respuesta Correcta: A
Explicación: S permite lectura concurrente (1-X); X es exclusivo (2-Y); múltiples S pueden coexistir (3-Z); un solo X excluye todo (4-V); la promoción convierte S a X si es posible (5-W).

[TIPO: RESPUESTA CORTA] Pregunta ID: 78
Enunciado: ¿Cómo se denomina la propiedad que asegura que la ejecución concurrente de varias transacciones produce el mismo resultado que una ejecución en serie de las mismas? Escriba su respuesta en MAYÚSCULAS.
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: SERIALIZABILIDAD
Explicación: La serializabilidad es el criterio de corrección fundamental en el control de concurrencia, exigiendo equivalencia con algún orden secuencial.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 79
Enunciado: En un sistema que utiliza bloqueo en dos fases, ¿cuál de las siguientes situaciones puede desencadenar un interbloqueo?
Opciones: A) Dos transacciones solo realizan operaciones de lectura simultáneas. B) Dos transacciones retienen recursos que la otra necesita y esperan. C) Se emplea timestamp ordering en lugar de candados locales. D) La transacción libera todos los candados al hacer commit final. E) Ninguna de las opciones es correcta.
Respuesta Correcta: B
Explicación: Un interbloqueo se produce cuando dos o más transacciones se bloquean entre sí esperando recursos que la otra posee, formando un ciclo de espera.

[TIPO: RESPUESTA CORTA] Pregunta ID: 80
Enunciado: ¿Cuál es el principal inconveniente del algoritmo Timestamp Ordering Básico debido a su política de rechazo inmediato de operaciones fuera de orden? Escriba su respuesta en MAYÚSCULAS (una o dos palabras).
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: REINICIOS FRECUENTES
Explicación: El TO Básico aborta y reinicia la transacción cada vez que una operación llega tarde, lo que puede provocar un número elevado de reinicios y bajo rendimiento.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 81
Enunciado: En el control de concurrencia optimista, ¿en qué fase se aplican realmente las modificaciones a la base de datos?
Opciones: A) Fase de lectura. B) Fase de validación. C) Fase de escritura. D) Fase de preparación. E) Fase de crecimiento.
Respuesta Correcta: C
Explicación: Tras la lectura y la validación exitosa, la fase de escritura es la que materializa los cambios locales en el almacenamiento persistente.

[TIPO: RESPUESTA CORTA] Pregunta ID: 82
Enunciado: ¿Qué estructura de datos dirigida se utiliza para representar las dependencias entre transacciones y detectar ciclos que indican un interbloqueo? Escriba la sigla de tres letras en MAYÚSCULAS.
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: WFG
Explicación: El Wait-For Graph (WFG) modela qué transacción espera a cuál, y la existencia de un ciclo en este grafo señala un interbloqueo.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 83
Enunciado: ¿Qué ventaja principal ofrece el método de control de concurrencia por múltiples versiones (multiversionado) sobre el Timestamp Ordering básico?
Opciones: A) Requiere menos espacio en disco para almacenar datos. B) Elimina por completo la necesidad de timestamps. C) Reduce drásticamente los abortos por rechazos de lectura. D) Es más sencillo de implementar que otros métodos. E) No necesita ningún tipo de sincronización de relojes entre nodos.
Respuesta Correcta: C
Explicación: Al mantener versiones antiguas, las lecturas siempre pueden satisfacerse con una versión consistente, evitando los rechazos y reinicios típicos del TO básico.

[TIPO: RESPUESTA CORTA] Pregunta ID: 84
Enunciado: En PostgreSQL, ¿cuál es el nivel de aislamiento predeterminado? Escriba la respuesta en MAYÚSCULAS y con el nombre exacto del nivel.
Opciones: A) N/A B) N/A C) N/A D) N/A E) N/A
Respuesta Correcta: READ COMMITTED
Explicación: PostgreSQL utiliza por defecto el nivel READ COMMITTED, que evita lecturas sucias pero permite lecturas no repetibles y fantasmas.