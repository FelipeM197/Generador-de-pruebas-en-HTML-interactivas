[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 1
Enunciado: En el modelo cliente/servidor con múltiples servidores y servidor home, cada cliente conoce solo su servidor home, el cual se comunica con los demás servidores según se requiera. ¿Cuál es la principal ventaja y el principal desafío de esta configuración respecto al modelo de cliente pesado?
Opciones:
A) Ventaja: elimina completamente los cuellos de botella; desafío: requiere que el cliente conozca todos los servidores.
B) Ventaja: simplifica el cliente al ocultar la complejidad de la coordinación entre servidores; desafío: añade complejidad de coordinación entre servidores.
C) Ventaja: simplifica el código del servidor; desafío: el cliente gestiona múltiples conexiones.
D) Ventaja: garantiza consistencia fuerte en todas las operaciones; desafío: introduce latencia en las lecturas locales.
E) Ninguna de las anteriores es correcta en este contexto.
Respuesta Correcta: B
Explicación: Este modelo delega la coordinación al servidor home, lo que hace al cliente más ligero y simple, pero transfiere la sobrecarga y complejidad a la comunicación inter-servidor.

[TIPO: RESPUESTA CORTA] Pregunta ID: 2
Enunciado: En el Teorema CAP, ¿cómo se denomina la propiedad que garantiza que el sistema continúa operando aunque fallen enlaces de comunicación entre nodos? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: PARTICION
Explicación: La propiedad que describe la pregunta es la Tolerancia a Particiones (Partition tolerance), que en el acrónimo CAP corresponde a la letra P.

[TIPO: RESPUESTA CORTA] Pregunta ID: 3
Enunciado: ¿Cómo se denomina el tipo de fragmentación que divide una relación en subconjuntos de filas almacenados en distintos nodos, de modo que cada nodo maneja solo los registros que le corresponden geográficamente? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: HORIZONTAL
Explicación: La fragmentación horizontal divide una relación por filas (tuplas), asignando subconjuntos a distintos nodos según un predicado lógico.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 4
Enunciado: Relacione cada anomalía de concurrencia con su definición correcta. 1) Actualización perdida. 2) Lectura sucia. 3) Lectura no repetible. 4) Fantasma. Definiciones: X) Alteración del conjunto de resultados de una consulta por inserciones concurrentes entre dos lecturas. Y) Acceso a estados temporales de datos que podrían ser revertidos tras el fallo o el rollback del origen. Z) Una transacción sobrescribe los cambios de otra sin haber leído ni integrado sus modificaciones antes. W) Inconsistencia en valores leídos sucesivamente debido a modificaciones externas confirmadas entre lecturas.
Opciones:
A) 1-Z, 2-Y, 3-W, 4-X
B) 1-X, 2-W, 3-Y, 4-Z
C) 1-Y, 2-Z, 3-X, 4-W
D) 1-W, 2-X, 3-Z, 4-Y
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: La actualización perdida sobrescribe sin integrar cambios ajenos (1-Z), la lectura sucia accede a datos aún no confirmados (2-Y), la lectura no repetible ve valores distintos entre dos lecturas por confirmaciones externas (3-W), y el fantasma altera el conjunto de resultados por inserciones concurrentes (4-X).

[TIPO: ORDENAMIENTO] Pregunta ID: 5
Enunciado: Ordene los pasos del protocolo de Confirmación en Dos Fases (2PC) en la secuencia correcta de ejecución. 1) El coordinador envía un mensaje PREPARE a todos los participantes de la transacción. 2) Cada sitio responde READY si puede confirmar la transacción, o ABORT si detecta algún problema local. 3) Cada sitio participante registra en su log local la intención de confirmar o abortar. 4) El coordinador envía COMMIT a todos los sitios si todos respondieron READY; envía ABORT si alguno respondió ABORT. 5) Los sitios aplican físicamente el commit o rollback según la decisión recibida del coordinador.
Opciones:
A) 1, 2, 3, 4, 5
B) 3, 1, 2, 5, 4
C) 1, 3, 4, 2, 5
D) 2, 4, 1, 3, 5
E) 4, 2, 1, 3, 5
Respuesta Correcta: A
Explicación: El coordinador envía PREPARE (1), los sitios responden READY/ABORT (2), registran su intención en el log local (3), el coordinador decide COMMIT/ABORT (4) y finalmente se aplica físicamente el resultado (5).

[TIPO: RESPUESTA CORTA] Pregunta ID: 6
Enunciado: ¿Cómo se denomina el criterio de corrección para bases de datos replicadas que exige que el resultado de ejecutar transacciones concurrentes sobre múltiples réplicas sea idéntico al de ejecutarlas serialmente sobre una sola copia? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: 1SR
Explicación: One-Copy Serializability (1SR) garantiza que un sistema replicado se comporte lógicamente como si existiera una única copia de los datos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 7
Enunciado: El teorema CAP establece que un sistema distribuido no puede garantizar simultáneamente las tres propiedades C, A y P. En sistemas distribuidos reales, las fallas de red son inevitables. ¿Qué implicación práctica tiene esta inevitabilidad sobre el diseño de un DDBMS?
Opciones:
A) Ninguna de las anteriores es correcta en este contexto.
B) La tolerancia a particiones no es opcional, por lo que el diseñador debe elegir entre consistencia y disponibilidad.
C) El diseñador puede elegir libremente entre C, A y P dependiendo del presupuesto.
D) El teorema CAP no se aplica a sistemas con replicación ansiosa.
E) Los sistemas distribuidos reales siempre garantizan consistencia y disponibilidad.
Respuesta Correcta: B
Explicación: Como P es obligatorio en redes reales, el diseño se reduce a un trade-off estricto entre Consistencia (C) y Disponibilidad (A) cuando ocurre una partición.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 8
Enunciado: Relacione cada término de diseño de DDBMS con su descripción correcta. 1) Fragmentación. 2) Replicación. 3) Asignación. 4) Transparencia de red. Descripciones: X) Decisión que determina en qué nodo físico se almacena cada subconjunto de datos. Y) Propiedad que permite al usuario consultar datos sin conocer el servidor o ciudad donde están almacenados. Z) División de una relación en subconjuntos de filas o columnas almacenados en distintos nodos para mejorar el rendimiento. W) Mantenimiento de copias idénticas de datos en múltiples nodos para mejorar disponibilidad y tolerancia a fallas. V) Mecanismo que oculta al usuario si los datos están divididos entre nodos distintos.
Opciones:
A) 1-Z, 2-W, 3-X, 4-Y
B) 1-X, 2-Z, 3-W, 4-Y
C) 1-W, 2-Y, 3-Z, 4-X
D) 1-Y, 2-X, 3-Z, 4-W
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: Fragmentar es dividir en subconjuntos (1-Z), replicar es mantener copias idénticas (2-W), asignar es decidir la ubicación física (3-X), y la transparencia de red oculta el servidor/ciudad de almacenamiento (4-Y).

[TIPO: RESPUESTA CORTA] Pregunta ID: 9
Enunciado: ¿Cuál es el término técnico que designa la propiedad de un sistema distribuido que permite al usuario acceder a datos sin necesidad de conocer en qué nodo están almacenados físicamente ni si están replicados o fragmentados? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: TRANSPARENCIA
Explicación: La transparencia es el objetivo principal de un DDBMS para ofrecer una vista unificada y simple de los datos, sin exponer su distribución física.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 10
Enunciado: En el Taller 2, los estudiantes ejecutaron el comando SELECT nombre FROM pg_available_extensions WHERE nombre LIKE '%fdw%' para explorar extensiones disponibles en PostgreSQL. ¿Qué categoría de funcionalidad distribuida representa principalmente postgres_fdw?
Opciones:
A) Acceso remoto transparente a datos en instancias PostgreSQL remotas como si fueran tablas locales.
B) Fragmentación automática de tablas en múltiples nodos con balanceo de carga.
C) Control de concurrencia distribuido mediante locks globales entre instancias PostgreSQL.
D) Replicación sincrónica distribuida mediante logs globales entre múltiples instancias PostgreSQL.
E) Ninguna de las anteriores es correcta en este contexto.
Respuesta Correcta: A
Explicación: postgres_fdw (Foreign Data Wrapper) provee acceso remoto transparente a datos de otra instancia PostgreSQL, exponiéndolos como si fueran tablas locales.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 11
Enunciado: Relacione cada tipo de sistema con la característica que mejor lo diferencia. 1) Sistema Paralelo. 2) Sistema Distribuido. 3) Sistema Cliente/Servidor. 4) Sistema Peer-to-Peer. Características: X) Todos los nodos tienen igual funcionalidad y pueden comunicarse entre sí sin distinción de roles. Y) Procesadores que comparten memoria o disco bajo un mismo sistema operativo con control centralizado. Z) Roles fijos donde uno concentra la gestión de datos y el otro provee la interfaz de la aplicación. W) Cada nodo tiene su propia memoria y almacenamiento; la comunicación ocurre a través de una red heterogénea.
Opciones:
A) 1-Y, 2-W, 3-Z, 4-X
B) 1-X, 2-Y, 3-W, 4-Z
C) 1-Z, 2-X, 3-Y, 4-W
D) 1-W, 2-Z, 3-X, 4-Y
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: Paralelo comparte hardware bajo un mismo SO (1-Y), Distribuido tiene nodos independientes por red heterogénea (2-W), Cliente/Servidor separa roles fijos (3-Z), y Peer-to-Peer da igual funcionalidad a todos los nodos (4-X).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 12
Enunciado: Relacione cada tipo de conflicto en la integración de esquemas con su ejemplo representativo. 1) Conflicto de nombres. 2) Conflicto de tipo. 3) Conflicto estructural. 4) Conflicto semántico. Ejemplos: X) El mismo término "cliente" tiene interpretaciones distintas en el área comercial y en el área técnica de la organización. Y) El atributo "salario" se almacena como entero en un nodo y como texto en otro. Z) Un mismo concepto se modela como atributo en un sitio y como relación independiente en otro. W) El mismo concepto recibe distintos nombres en cada sitio (sinónimos) o distintos conceptos comparten el mismo nombre (homónimos).
Opciones:
A) 1-W, 2-Y, 3-Z, 4-X
B) 1-X, 2-W, 3-Y, 4-Z
C) 1-Y, 2-Z, 3-X, 4-W
D) 1-Z, 2-X, 3-W, 4-Y
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: Nombres abarca sinónimos/homónimos (1-W), Tipo se refiere a tipos de datos distintos para el mismo atributo (2-Y), Estructural a cómo se modela el mismo concepto (3-Z), y Semántico a interpretaciones distintas del negocio (4-X).

[TIPO: ORDENAMIENTO] Pregunta ID: 13
Enunciado: Ordene las siguientes etapas del proceso de diseño Top-Down de una base de datos distribuida, de la primera a la última. 1) Definir la estructura lógica única de la base de datos considerando su distribución (GCS). 2) Aplicar fragmentación y asignación para producir esquemas conceptuales locales de cada sitio. 3) Obtener los esquemas locales (LCS), que describen los fragmentos asignados a cada sitio. 4) Traducir cada LCS en un esquema físico optimizado según las capacidades del nodo local. 5) Evaluar el impacto en comunicación y carga de trabajo para validar si el diseño de distribución es adecuado.
Opciones:
A) 1, 2, 3, 4, 5
B) 2, 1, 4, 3, 5
C) 3, 2, 1, 5, 4
D) 5, 4, 3, 2, 1
E) 1, 3, 2, 4, 5
Respuesta Correcta: A
Explicación: El enfoque Top-Down define primero el GCS global (1), luego fragmenta y asigna (2), obtiene los LCS locales (3), diseña el esquema físico por sitio (4) y finalmente evalúa el impacto en comunicación (5).

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 14
Enunciado: En el diseño top-down de una base de datos distribuida, el GCS se define primero y luego se derivan los esquemas locales. Si un arquitecto comete un error en la etapa de diseño de distribución (fragmentación y asignación), ¿cuál es el impacto en el sistema resultante?
Opciones:
A) El error solo afecta al esquema externo, por lo que los usuarios no perciben ningún problema.
B) El error puede corregirse fácilmente en los esquemas locales sin afectar el GCS.
C) Ninguna de las anteriores es correcta en este contexto.
D) El error no tiene impacto porque el optimizador de consultas compensa automáticamente la fragmentación inadecuada.
E) El error se propaga a todos los esquemas físicos locales, afectando el rendimiento global del sistema de forma amplificada.
Respuesta Correcta: E
Explicación: En el modelo top-down, cada capa depende de la anterior; un error en fragmentación/asignación se hereda y amplifica en todos los esquemas físicos locales derivados.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 15
Enunciado: En un sistema de bases de datos distribuido, la fragmentación horizontal divide una relación por filas, mientras que la fragmentación vertical la divide por columnas. Una empresa eléctrica provincial divide su tabla de clientes por cantón. ¿Qué tipo de fragmentación aplica y cuál es su beneficio principal?
Opciones:
A) Ninguna de las anteriores es correcta en este contexto.
B) Fragmentación vertical; permite acceder solo a los atributos necesarios para cada consulta.
C) Fragmentación vertical; reduce el número de nodos necesarios para almacenar la información.
D) Fragmentación mixta; combina criterios de filas y columnas para maximizar localidad.
E) Fragmentación horizontal; permite que cada nodo procese únicamente los clientes de su cantón, mejorando el rendimiento local.
Respuesta Correcta: E
Explicación: Dividir por cantón filtra filas (tuplas), por lo que corresponde a fragmentación horizontal, garantizando localidad de acceso geográfico.

[TIPO: ORDENAMIENTO] Pregunta ID: 16
Enunciado: Ordene los siguientes pasos para desplegar un contenedor PostgreSQL en Windows usando Docker, según la secuencia lógica correcta del Taller 1. 1) Instalar Docker Desktop y verificar su funcionamiento con docker --version. 2) Descargar la imagen oficial de PostgreSQL desde Docker Hub. 3) Ejecutar docker run con los parámetros de nombre, contraseña, puerto y volumen para crear el contenedor. 4) Verificar el estado del contenedor con docker ps y revisar los logs para confirmar que PostgreSQL inició correctamente. 5) Conectarse al contenedor con docker exec -it postgres-container psql -U postgres y ejecutar consultas de verificación. 6) Confirmar la persistencia de datos identificando el volumen pgdata y comprendiendo su rol frente a la eliminación del contenedor.
Opciones:
A) 1, 2, 3, 4, 5, 6
B) 2, 1, 4, 3, 5, 6
C) 1, 3, 2, 5, 4, 6
D) 3, 2, 1, 6, 5, 4
E) 6, 5, 4, 3, 2, 1
Respuesta Correcta: A
Explicación: La secuencia lógica requiere instalar el motor (1), descargar la imagen (2), instanciar el contenedor (3), verificar su ejecución (4), ingresar para operar (5) y validar la persistencia del volumen (6).

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 17
Enunciado: Según las especificaciones de arquitectura ANSI/SPARC, ¿cuál es la limitación fundamental de la extensión postgres_fdw que impide considerarla un SGBDD completo nativo?
Opciones:
A) Requiere que todos los nodos usen la misma versión exacta del software.
B) No soporta el lenguaje SQL estándar para consultas remotas.
C) No gestiona replicación ni control de transacciones distribuidas de forma nativa, es solo un mecanismo de acceso remoto transparente.
D) Solo funciona en arquitecturas de red cerradas y aisladas.
E) Ninguna de las opciones es correcta.
Respuesta Correcta: C
Explicación: postgres_fdw actúa como puente de acceso remoto (wrapper), pero carece del motor interno para coordinar commits distribuidos o gestionar replicación transaccional nativa.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 18
Enunciado: El algoritmo de consenso Paxos requiere solo una mayoría operativa (quórum) para validar decisiones. ¿En qué aspecto fundamental supera Paxos al protocolo 2PC en términos de tolerancia a fallas?
Opciones:
A) Garantiza consistencia fuerte antes de confirmar la transacción.
B) Paxos permite que el sistema continúe operando si la mayoría de nodos puede comunicarse internamente, sin quedar bloqueado ante la caída del coordinador como ocurre en 2PC.
C) Elimina completamente la necesidad de cualquier coordinador temporal.
D) Procesa todas las transacciones de forma serial sin paralelismo.
E) Ninguna de las opciones es correcta.
Respuesta Correcta: B
Explicación: 2PC bloquea el sistema si el coordinador falla (single point of failure); Paxos tolera esa falla mientras exista mayoría de nodos comunicándose.

[TIPO: RESPUESTA CORTA] Pregunta ID: 19
Enunciado: En el Laboratorio 3, la tabla "pacientes" en cada nodo incluye una restricción CHECK que implementa la fragmentación horizontal. ¿Cómo se denomina este tipo de fragmentación cuando el predicado de división se aplica sobre atributos de la propia tabla fragmentada? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: PRIMARIA
Explicación: La fragmentación horizontal primaria basa sus reglas de división en los propios atributos de la relación que se está fragmentando.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 20
Enunciado: En un sistema distribuido, dos transacciones T1 y T2 acceden al mismo ítem de datos X. T1 realiza una lectura y T2 una escritura concurrente sobre X. ¿Bajo qué condición estas operaciones generan un conflicto según el criterio de serializabilidad?
Opciones:
A) Solo si ambas operaciones son escrituras sobre el mismo ítem.
B) Ninguna de las anteriores es correcta en este contexto.
C) Solo si T1 completa su lectura antes de que se repliquen los nodos.
D) Solo si T1 y T2 pertenecen al mismo proceso de usuario ejecutándose concurrentemente.
E) Cuando acceden al mismo ítem, pertenecen a transacciones distintas y al menos una de las dos operaciones es una escritura.
Respuesta Correcta: E
Explicación: Un conflicto ocurre entre transacciones distintas sobre el mismo dato cuando al menos una de las operaciones es de escritura; las lecturas concurrentes puras no conflictúan.

[TIPO: ORDENAMIENTO] Pregunta ID: 21
Enunciado: Ordene las tres fases del diseño de fragmentación vertical, de primero a último, según el flujo de trabajo descrito en clase. 1) Recolección: identificar las consultas críticas del sistema y registrar con qué frecuencia se ejecutan en cada sitio de la red. 2) Procesamiento: calcular la Matriz de Afinidad (AA), aplicar BEA para obtener la Matriz Agrupada (CA) y ejecutar SPLIT para determinar el punto de corte óptimo. 3) Validación: verificar que los fragmentos resultantes cumplen completitud, reconstrucción y disyuntividad.
Opciones:
A) 1, 2, 3
B) 2, 1, 3
C) 3, 2, 1
D) 1, 3, 2
E) 2, 3, 1
Respuesta Correcta: A
Explicación: Se recolecta primero el comportamiento de las consultas (1), luego se aplican los algoritmos matemáticos de afinidad (2), y finalmente se valida que los fragmentos cumplan las propiedades formales (3).

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 22
Enunciado: En un sistema multidatabase, la capa MDBS actúa como software adicional sobre DBMS locales existentes. Desde la perspectiva de cada DBMS local, ¿cómo percibe la capa de MDBS?
Opciones:
A) Ninguna de las anteriores es correcta en este contexto.
B) Como un nodo par con igual funcionalidad dentro del sistema peer-to-peer.
C) Como otra aplicación cliente que envía solicitudes y recibe respuestas de forma ordinaria.
D) Como una extensión interna que modifica su esquema conceptual local para participar en el esquema global.
E) Como el coordinador global que controla todas sus transacciones locales.
Respuesta Correcta: C
Explicación: En un MDBS se preserva la autonomía local; cada motor base percibe al mediador como un cliente estándar que envía consultas SQL por red, sin conciencia de la distribución global.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 23
Enunciado: En el Laboratorio 3, la tabla "pacientes" usa CHECK (tipo_consulta = 'ambulatorio') en el Nodo B. Un estudiante argumenta que esta restricción es suficiente para garantizar que el diseño de fragmentación horizontal es correcto en producción. ¿Es válido este argumento?
Opciones:
A) Sí, porque en PostgreSQL las restricciones CHECK son el mecanismo oficial de distribución y garantizan todas las propiedades formales requeridas.
B) Sí, porque la restricción CHECK garantiza automáticamente completitud, disyuntividad y reconstrucción para la fragmentación horizontal.
C) No, porque la restricción CHECK solo aplica durante INSERT, no durante UPDATE.
D) No, porque la restricción CHECK solo protege la disyuntividad local, pero no garantiza que todos los pacientes correspondientes lleguen al nodo correcto ni que exista enrutamiento automático para cada inserción.
E) No, porque la restricción CHECK solo garantiza disyuntividad, debiéndose verificar la completitud con un algoritmo independiente.
Respuesta Correcta: D
Explicación: Un CHECK rechaza datos inválidos localmente, pero no mueve ni enruta la data hacia el nodo correcto, dejando sin cubrir la completitud y el enrutamiento automático del diseño global.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 24
Enunciado: Relacione cada modelo del Teorema CAP con su implicación cuando ocurre una falla de red. 1) Modelo CP. 2) Modelo AP. 3) Modelo CA. 4) Tolerancia a particiones. Implicaciones: X) Ante una partición, el sistema prioriza la exactitud de los datos, rechazando responder hasta restaurar la consistencia total. Y) El sistema siempre responde pero con datos que podrían estar desactualizados o inconsistentes hasta la sincronización. Z) Solo viable en entornos centralizados o de un único sitio donde se asume una red perfectamente confiable. W) En entornos distribuidos reales, la fragmentación de la red es inevitable, por lo que sacrificarla (como en el modelo CA) no es una opción válida.
Opciones:
A) 1-X, 2-Y, 3-Z, 4-W
B) 1-Y, 2-X, 3-W, 4-Z
C) 1-Z, 2-W, 3-X, 4-Y
D) 1-W, 2-Z, 3-Y, 4-X
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: El modelo CP bloquea el servicio para proteger la consistencia (1-X), el modelo AP acepta datos desactualizados (2-Y), el modelo CA solo es viable sin red real (3-Z), y la tolerancia a particiones es inevitable en la práctica distribuida (4-W).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 25
Enunciado: Relacione cada esquema de ubicación propuesto por Rahimi con su característica principal. 1) No Replicado. 2) Totalmente Replicado. 3) Parcialmente Replicado. Características: X) Todos los datos residen en un único sitio sin divisiones ni copias; ningún fragmento es distribuido remotamente. Y) Existe una copia completa de la base de datos en cada sitio del sistema; cualquier nodo puede responder consultas de forma local. Z) Solo los fragmentos críticos se replican en más de un sitio; combina fragmentación y replicación, siendo el esquema más usado en producción.
Opciones:
A) 1-X, 2-Y, 3-Z
B) 1-Y, 2-Z, 3-X
C) 1-Z, 2-X, 3-Y
D) 1-X, 2-Z, 3-Y
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: No replicado significa un único sitio sin copias (1-X), totalmente replicado duplica todo en cada sitio (2-Y), y parcialmente replicado combina fragmentación con réplicas críticas (3-Z).

[TIPO: ORDENAMIENTO] Pregunta ID: 26
Enunciado: Ordene los siguientes pasos para implementar replicación lógica unidireccional en PostgreSQL 16, de primero a último, según el Laboratorio 5. 1) Configurar wal_level = logical (o superior) en ambos nodos y reiniciar el servicio de PostgreSQL. 2) Crear el usuario "replica" con privilegio REPLICATION en ambos nodos. 3) Crear la publicación en el Nodo A con CREATE PUBLICATION para las tablas que se desean replicar. 4) Crear la suscripción en el Nodo B con CREATE SUBSCRIPTION, especificando la cadena de conexión y el nombre de la publicación. 5) Verificar en pg_stat_replication que el estado sea "streaming" y que el Nodo B esté recibiendo cambios activamente.
Opciones:
A) 1, 2, 3, 4, 5
B) 2, 1, 4, 3, 5
C) 1, 4, 2, 3, 5
D) 4, 1, 3, 5, 2
E) 3, 1, 2, 4, 5
Respuesta Correcta: A
Explicación: Primero se habilita el WAL lógico (1), se crea el usuario de replicación (2), se crea la publicación en el origen (3), la suscripción en el destino (4) y finalmente se verifica el streaming activo (5).

[TIPO: RESPUESTA CORTA] Pregunta ID: 27
Enunciado: En la fragmentación vertical, ¿qué operador del álgebra relacional permite reconstruir la relación original combinando sus fragmentos basándose en sus claves primarias? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: JOIN
Explicación: El operador JOIN permite emparejar las columnas separadas de los fragmentos verticales de vuelta en una sola fila consolidada, usando la clave primaria común.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 28
Enunciado: En el contexto de los DBMS, el término "promesa" se usa en lugar de "garantía". ¿Cuál de las siguientes opciones justifica mejor por qué las características de un DBMS son promesas y no garantías absolutas?
Opciones:
A) Porque su logro está condicionado por la implementación específica, los trade-offs inherentes a la distribución y el contexto del entorno donde se despliega.
B) Ninguna de las opciones indicadas.
C) Porque los usuarios finales no pueden verificar técnicamente si las promesas se cumplen o no.
D) Porque los fabricantes de DBMS no están dispuestos contractualmente con el rendimiento.
E) Porque los DBMS distribuidos son siempre experimentales en la práctica.
Respuesta Correcta: A
Explicación: Las limitaciones físicas de la red, la latencia y los trade-offs de diseño (como los del Teorema CAP) hacen que el cumplimiento de cada propiedad dependa del contexto específico de despliegue, no de una garantía absoluta.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 29
Enunciado: Un arquitecto debe elegir entre replicación física síncrona y replicación lógica asíncrona para el núcleo de un sistema bancario que no puede tolerar pérdidas de datos confirmados. Propone usar replicación lógica asíncrona argumentando mayor flexibilidad y selectividad. ¿Es adecuada esta elección?
Opciones:
A) No, porque la replicación lógica no es compatible con entornos bancarios de producción en PostgreSQL.
B) No, porque la replicación lógica asíncrona no garantiza consistencia mutua fuerte; si el nodo falla antes de propagar los cambios, se pierden escrituras ya confirmadas al cliente, siendo necesaria la replicación física síncrona para este requisito crítico.
C) No, porque la replicación lógica exige que ambos nodos tengan exactamente el mismo wal_level.
D) Sí, porque la replicación lógica puede configurarse para lograr consistencia fuerte equivalente a la física síncrona.
E) Sí, porque la replicación lógica es incompatible únicamente con entornos de alta escritura.
Respuesta Correcta: B
Explicación: Los sistemas bancarios críticos requieren propagación síncrona (eager); la propagación asíncrona (lazy) conlleva riesgo real de pérdida de escrituras confirmadas ante un fallo repentino del nodo.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 30
Enunciado: Relacione cada estrategia de propagación de actualizaciones con su consecuencia de diseño. 1) Eager (Ansiosa). 2) Lazy (Perezosa). Consecuencias: X) La transacción se confirma en una sola réplica y propaga los cambios de forma asíncrona; puede generar réplicas temporalmente divergentes. Y) Las actualizaciones se propagan a todas las réplicas dentro de la misma transacción; al confirmar, todas las copias quedan consistentes, a costa de mayor latencia.
Opciones:
A) 1-Y, 2-X
B) 1-X, 2-Y
C) 1-Y, 2-Y
D) 1-X, 2-X
E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: Eager propaga y confirma en todas las réplicas dentro de la misma transacción (1-Y), mientras que Lazy confirma rápido y propaga después, arriesgando divergencia temporal (2-X).

[TIPO: ORDENAMIENTO] Pregunta ID: 31
Enunciado: Evalúe y ordene los siguientes criterios de decisión para elegir una estrategia de ubicación de datos, de mayor a menor prioridad, cuando el objetivo principal es garantizar disponibilidad ante fallas de un nodo en un sistema bancario crítico. 1) Garantizar que al menos una réplica secundaria pueda asumir las operaciones del nodo principal caído. 2) Verificar que el número de réplicas cumpla el quórum mínimo requerido por los protocolos de consistencia del sistema. 3) Aplicar replicación parcial en los fragmentos de mayor criticidad operativa para equilibrar disponibilidad y costo. 4) Ubicar cada fragmento cerca del sitio donde se genera mayor frecuencia de acceso de lectura. 5) Minimizar el costo de sincronización entre nodos para reducir la latencia de escritura.
Opciones:
A) 1, 2, 3, 4, 5
B) 2, 1, 3, 5, 4
C) 3, 1, 2, 5, 4
D) 1, 3, 2, 4, 5
E) 4, 2, 1, 3, 5
Respuesta Correcta: A
Explicación: La prioridad máxima es garantizar el failover (1), seguida del quórum de consistencia (2), la replicación parcial estratégica (3), la localidad de lectura (4) y por último minimizar el costo de sincronización (5).

[TIPO: ORDENAMIENTO] Pregunta ID: 32
Enunciado: Ordene los pasos para crear la fragmentación horizontal primaria de la tabla "clientes" en el Laboratorio 2, de primero a último, según la guía de práctica. 1) Crear en ambos nodos la base de datos con la misma estructura de tabla y llave correcta. 2) Crear la tabla maestra "clientes" con PARTITION BY LIST para definir la partición lógica. 3) Crear la partición local en el nodo correspondiente usando PARTITION OF ... FOR VALUES IN (...). 4) Insertar los datos de clientes; PostgreSQL redirige automáticamente cada fila a la partición correcta. 5) Verificar la distribución consultando las tablas del sistema para confirmar en qué nodo quedó almacenada cada fila.
Opciones:
A) 1, 2, 3, 4, 5
B) 2, 1, 4, 3, 5
C) 3, 2, 1, 5, 4
D) 1, 3, 2, 4, 5
E) 5, 4, 3, 2, 1
Respuesta Correcta: A
Explicación: Primero se preparan las estructuras base en ambos nodos (1), se declara la tabla maestra particionada (2), se crea la partición local (3), se insertan los datos con enrutamiento automático (4) y finalmente se verifica la distribución (5).

[TIPO: RESPUESTA CORTA] Pregunta ID: 33
Enunciado: ¿Cuál es el nombre del protocolo estándar industrial que garantiza la atomicidad global de una transacción distribuida mediante fases de votación y decisión coordinadas por un nodo coordinador? Escriba la sigla en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: 2PC
Explicación: El protocolo Two-Phase Commit (2PC) coordina la decisión de confirmar o abortar entre todos los nodos participantes mediante una fase de votación y una fase de decisión.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 34
Enunciado: El control distribuido elimina cuellos de botella y puntos únicos de falla al repartir la responsabilidad de coordinación entre varios nodos. ¿Cuál de los siguientes beneficios adicionales del control distribuido describe mejor la relación entre escalabilidad y rendimiento?
Opciones:
A) Al agregar nuevos nodos sin reestructurar completamente el sistema, la carga de procesamiento y coordinación se reparte, mejorando el rendimiento global.
B) Al distribuir el control se reduce el número total de nodos necesarios para el sistema.
C) El control distribuido garantiza que todas las transacciones se ejecuten de forma serial sin conflictos.
D) El control distribuido elimina la necesidad de protocolos de coordinación como 2PC o Paxos.
E) Ninguna de las anteriores es correcta en este contexto.
Respuesta Correcta: A
Explicación: La descentralización del control permite escalar horizontalmente, sumando capacidad de cómputo que absorbe cargas adicionales sin rediseñar todo el sistema.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 35
Enunciado: Una consulta involucra 15 relaciones distribuidas y el espacio de búsqueda del optimizador crece de forma explosiva. ¿Qué tipo de estrategia de búsqueda es la más adecuada según el material para evitar saturar el servidor?
Opciones:
A) Revisión manual de todos los planes por parte del DBA.
B) Búsquedas exhaustivas determinísticas sobre todos los planes posibles.
C) Programación dinámica sin ninguna técnica de poda.
D) Ejecución secuencial de la consulta sin ningún optimizador.
E) Estrategias aleatorizadas, como recocido simulado o mejora iterativa.
Respuesta Correcta: E
Explicación: Cuando el espacio de búsqueda es demasiado grande para algoritmos determinísticos exhaustivos, se recurre a estrategias estocásticas como el recocido simulado para hallar planes suficientemente buenos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 36
Enunciado: Un optimizador de consultas aplica la heurística de filtrado temprano y poda del árbol algebraico en lugar de una búsqueda exhaustiva. ¿Qué tipo de estrategia determinística está utilizando?
Opciones:
A) Enfoque heurístico.
B) Mejora iterativa.
C) Enfoque de búsqueda exhaustiva.
D) Recocido simulado.
E) Estrategia aleatorizada pura.
Respuesta Correcta: A
Explicación: Aplicar reglas prácticas pre-codificadas (como filtrar y proyectar lo antes posible) es un enfoque heurístico determinístico, no una búsqueda exhaustiva ni una estrategia aleatorizada.

[TIPO: RESPUESTA CORTA] Pregunta ID: 37
Enunciado: ¿Cómo se denomina la reversión total de los efectos de una transacción ante un fallo, evitando que se genere un "estado perdido" catastrófico como en el ejemplo de la reserva de vuelos? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: ROLLBACK
Explicación: El ciclo de vida transaccional concluye con Commit o con Abort/Rollback; el Rollback revierte totalmente los efectos parciales de una transacción que no puede completarse con éxito.

[TIPO: RESPUESTA CORTA] Pregunta ID: 38
Enunciado: Según Gray et al. (1976), ¿qué grado numérico de consistencia es el único que no lee ni escribe datos sucios, e impide además que otras transacciones lean sus cambios parciales? Escriba solo el número.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: 3
Explicación: El Grado 3 (Consistencia Máxima) es el único nivel que no lee ni escribe datos sucios e impide que otras transacciones vean sus cambios parciales antes del commit.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 39
Enunciado: Relacione cada grado de consistencia de Gray (los grados van del 0 al 3) con su manejo de datos sucios. 1) Grado tres (máxima). 2) Grado dos (intermedia). 3) Grado uno (mínima). 4) Grado cero (base). Manejo: X) Solo evita sobrescribir datos sucios ajenos, sin restricciones de lectura. Y) No lee ni escribe datos sucios; impide que otros lean sus cambios parciales. Z) Prohíbe leer datos sucios, pero permite que otros vean sus cambios antes del commit. W) Evita sobrescribir datos de terceros (dirty writes), pero puede leer datos sucios.
Opciones:
A) 1-Y, 2-Z, 3-W, 4-X
B) 1-X, 2-Y, 3-Z, 4-W
C) 1-Z, 2-W, 3-X, 4-Y
D) 1-W, 2-X, 3-Y, 4-Z
E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: Grado 3 es consistencia máxima sin lectura ni escritura sucia (1-Y), Grado 2 prohíbe leer sucio pero permite que otros vean cambios propios (2-Z), Grado 1 solo evita dirty writes aunque puede leer sucio (3-W), y Grado 0 solo protege contra sobrescritura ajena (4-X).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 40
Enunciado: Relacione cada nivel de aislamiento ANSI SQL con los fenómenos que permite que ocurran. 1) Read Uncommitted. 2) Read Committed. 3) Repeatable Read. 4) Serializable. Fenómenos permitidos: X) Previene lectura sucia y lectura no repetible, pero permite tupla fantasma. Y) Permite lectura sucia, lectura no repetible y tupla fantasma. Z) Previene los tres fenómenos: lectura sucia, no repetible y tupla fantasma. W) Previene lectura sucia, pero permite lectura no repetible y tupla fantasma.
Opciones:
A) 1-Y, 2-W, 3-X, 4-Z
B) 1-W, 2-Y, 3-Z, 4-X
C) 1-X, 2-Z, 3-W, 4-Y
D) 1-Z, 2-X, 3-Y, 4-W
E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: Read Uncommitted permite todo (1-Y), Read Committed solo previene lectura sucia (2-W), Repeatable Read previene sucia y no repetible pero permite fantasma (3-X), y Serializable previene los tres fenómenos (4-Z).

[TIPO: RESPUESTA CORTA] Pregunta ID: 41
Enunciado: ¿Qué mecanismo de registro estándar exige escribir la operación en almacenamiento persistente antes de aplicarla a los datos, garantizando la durabilidad tras un fallo crítico? Escriba la sigla en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: WAL
Explicación: El Write-Ahead Log (WAL) registra cada operación en la bitácora persistente antes de aplicarla a los datos, habilitando la recuperación por rehacimiento tras un fallo.

[TIPO: ORDENAMIENTO] Pregunta ID: 42
Enunciado: Ordene los cuatro modelos de organización de lectura/escritura de una transacción según su nivel creciente de restricción, del menos al más restrictivo. 1) General: sin restricciones, máxima flexibilidad. 2) Dos Pasos: agrupa todas las lecturas antes de iniciar las escrituras. 3) Restringido: exige que un dato sea leído inmediatamente antes de ser escrito. 4) Modelo de Acción: ejecuta pares atómicos utilizando la notación [R(x), W(x)].
Opciones:
A) 1, 2, 3, 4
B) 4, 3, 2, 1
C) 2, 1, 4, 3
D) 1, 3, 2, 4
E) 3, 1, 2, 4
Respuesta Correcta: A
Explicación: El modelo General no impone restricciones (1), Dos Pasos exige agrupar lecturas antes de escrituras (2), Restringido exige lectura inmediatamente antes de la escritura de ese dato (3), y el Modelo de Acción es el más restrictivo al forzar pares atómicos (4).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 43
Enunciado: Relacione cada tipo de estructura transaccional con su comportamiento. 1) Transacción Plana. 2) Anidamiento Cerrado. 3) Anidamiento Abierto. Comportamiento: X) Estándar de inicio y fin único, sin subtransacciones. Y) Dependencia jerárquica total; si la raíz aborta, todas las subtransacciones se revierten, manteniendo la atomicidad global. Z) Los resultados de las subtransacciones son visibles antes del fin de la raíz, mejorando la concurrencia pero rompiendo la atomicidad clásica.
Opciones:
A) 1-X, 2-Y, 3-Z
B) 1-Y, 2-X, 3-Z
C) 1-Z, 2-Y, 3-X
D) 1-X, 2-Z, 3-Y
E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: La transacción plana es de inicio y fin único (1-X), el anidamiento cerrado revierte todo si la raíz aborta (2-Y), y el anidamiento abierto expone resultados intermedios antes de tiempo (3-Z).

[TIPO: RESPUESTA CORTA] Pregunta ID: 44
Enunciado: ¿Cómo se denomina la secuencia de transacciones abiertas donde, si una falla, se ejecutan acciones inversas para restaurar el equilibrio semántico, usada como alternativa al rollback en procesos de larga duración? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: SAGA
Explicación: Una Saga es una secuencia de transacciones abiertas que, ante un fallo, ejecuta acciones compensatorias inversas en vez de un rollback tradicional.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 45
Enunciado: Relacione cada clasificación de tarea dentro de un Workflow con su comportamiento ante el fallo. 1) Tarea Vital. 2) Tarea No Vital. 3) Tarea de Contingencia. Comportamiento: X) Su fallo aborta todo el flujo del proceso. Y) Su fallo permite continuar el flujo sin interrumpirlo. Z) Ofrece una ruta alternativa estratégica ante el fallo de la tarea original (por ejemplo, reservar un hotel alterno).
Opciones:
A) 1-X, 2-Y, 3-Z
B) 1-Y, 2-X, 3-Z
C) 1-Z, 2-X, 3-Y
D) 1-X, 2-Z, 3-Y
E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: Una tarea Vital detiene el flujo si falla (1-X), una No Vital deja continuar el proceso (2-Y), y una de Contingencia ofrece una ruta alternativa estratégica (3-Z).

[TIPO: RESPUESTA CORTA] Pregunta ID: 46
Enunciado: En el protocolo de Bloqueo en Dos Fases, ¿qué término designa la variante que mantiene todos los candados hasta el fin de la transacción (commit o abort), siendo indispensable para mitigar el riesgo de abortos en cascada? Escriba las dos palabras en MAYÚSCULAS.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: 2PL ESTRICTO
Explicación: El 2PL Estricto retiene todos los candados hasta el commit o abort final, evitando que otras transacciones lean datos no confirmados que podrían revertirse.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 47
Enunciado: Relacione cada condición de la lógica de aceptación/rechazo del protocolo Timestamp Ordering con la operación que rechaza. 1) TS(T) menor que rts(x) o menor que wts(x). 2) TS(T) menor que wts(x). Operación rechazada: X) Rechaza una operación Read(x). Y) Rechaza una operación Write(x).
Opciones:
A) 1-Y, 2-X
B) 1-X, 2-Y
C) 1-Y, 2-Y
D) 1-X, 2-X
E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: Una escritura Write(x) se rechaza si TS(T) es menor que rts(x) o que wts(x) (1-Y); una lectura Read(x) se rechaza solo si TS(T) es menor que wts(x) (2-X).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 48
Enunciado: Relacione cada variante del protocolo de Marcas de Tiempo con su característica distintiva. 1) TO Conservador. 2) TO Multiversión. Características: X) Crea versiones históricas de los datos para que las lecturas nunca bloqueen a las escrituras. Y) Usa colas para evitar reinicios, aunque arriesga parálisis del sistema.
Opciones:
A) 1-Y, 2-X
B) 1-X, 2-Y
C) 1-Y, 2-Y
D) 1-X, 2-X
E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: El TO Conservador encola operaciones para evitar reinicios, a riesgo de parálisis (1-Y); el TO Multiversión mantiene versiones históricas para que las lecturas nunca se rechacen (2-X).

[TIPO: ORDENAMIENTO] Pregunta ID: 49
Enunciado: Ordene las tres fases de ejecución de un mecanismo de control de concurrencia optimista, de la primera a la última. 1) Lectura: la transacción opera sobre su espacio de trabajo local. 2) Validación: se comparan los conjuntos de lectura y escritura (RS/WS) contra transacciones concurrentes. 3) Escritura: se aplican los cambios de forma global a la base de datos.
Opciones:
A) 1, 2, 3
B) 2, 1, 3
C) 3, 2, 1
D) 2, 3, 1
E) 1, 3, 2
Respuesta Correcta: A
Explicación: El control optimista lee primero en el espacio local (1), valida comparando conjuntos RS/WS (2), y solo si la validación es exitosa aplica los cambios globalmente (3).

[TIPO: RESPUESTA CORTA] Pregunta ID: 50
Enunciado: ¿Cómo se denomina el mecanismo que implementa PostgreSQL para el control de concurrencia optimista, optimizando el rendimiento en entornos donde los conflictos son la excepción y no la regla? Escriba la sigla en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: SSI
Explicación: PostgreSQL implementa el control optimista mediante Serializable Snapshot Isolation (SSI), diseñado para entornos de baja conflictividad.

[TIPO: RESPUESTA CORTA] Pregunta ID: 51
Enunciado: ¿Cómo se denomina la estructura utilizada para diagnosticar interbloqueos que rastrea, dentro de un mismo nodo, qué transacción espera a cuál? Escriba la sigla en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: LWFG
Explicación: El Local Wait-For Graph (LWFG) rastrea las dependencias de espera entre transacciones dentro de un único nodo, aunque por sí solo es insuficiente para detectar ciclos que solo se manifiestan a nivel global (GWFG).

[TIPO: EMPAREJAMIENTO] Pregunta ID: 52
Enunciado: Relacione cada estrategia de evitación de interbloqueos basada en antigüedad con su comportamiento. 1) Wait-Die. 2) Wound-Wait. Comportamiento: X) Es expropiador: si la transacción solicitante es más antigua, aborta a la más joven para tomar el recurso. Y) No es expropiador: si la transacción solicitante es más antigua, espera; si es más joven, se aborta a sí misma.
Opciones:
A) 1-Y, 2-X
B) 1-X, 2-Y
C) 1-Y, 2-Y
D) 1-X, 2-X
E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: Wait-Die no es expropiador: la transacción antigua espera y la joven muere (1-Y). Wound-Wait sí es expropiador: la antigua "hiere" y aborta a la joven para tomar el recurso (2-X).

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 53
Enunciado: En la estrategia de Detección de interbloqueos, una vez identificado un ciclo en el grafo de espera (WFG), ¿qué acción se ejecuta a continuación?
Opciones:
A) Se selecciona una transacción víctima basándose en heurísticas como el esfuerzo invertido o el costo de rollback, y se la aborta.
B) Se predeclaran todos los datos que la transacción utilizará antes de ejecutarla.
C) Se ordena a todas las transacciones esperar indefinidamente hasta que el ciclo se resuelva por sí solo.
D) Se aplica automáticamente la regla Wound-Wait para expropiar a la transacción más antigua.
E) Ninguna de las anteriores describe el comportamiento correcto de esta estrategia.
Respuesta Correcta: A
Explicación: La Detección permite que ocurra el interbloqueo y, al identificarlo mediante un ciclo en el WFG, selecciona una transacción víctima según criterios heurísticos (esfuerzo invertido, costo de rollback) para abortarla y romper el ciclo.

[TIPO: RESPUESTA CORTA] Pregunta ID: 54
Enunciado: ¿Cómo se denomina la estrategia de manejo de interbloqueos que exige predeclarar todos los datos que una transacción utilizará, siendo segura pero extremadamente costosa en términos de concurrencia? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: PREVENCION
Explicación: La estrategia de Prevención exige predeclarar todos los datos que se usarán, garantizando que nunca ocurra un interbloqueo, a costa de una concurrencia muy reducida.

[TIPO: ORDENAMIENTO] Pregunta ID: 55
Enunciado: Ordene la escala de rigurosidad de los niveles de aislamiento ANSI SQL, del menos al más estricto en cuanto a los fenómenos de concurrencia que previenen. 1) Read Uncommitted. 2) Read Committed. 3) Repeatable Read. 4) Serializable.
Opciones:
A) 1, 2, 3, 4
B) 4, 3, 2, 1
C) 2, 1, 4, 3
D) 1, 3, 2, 4
E) 3, 1, 2, 4
Respuesta Correcta: A
Explicación: Read Uncommitted es el nivel menos estricto (no previene ningún fenómeno) y Serializable es el más estricto (previene los tres fenómenos), quedando en medio Read Committed y Repeatable Read en ese orden creciente.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 56
Enunciado: Relacione cada tipo de fallo bajo la propiedad de Atomicidad con el mecanismo de respuesta correspondiente. 1) Fallo de Transacción. 2) Fallo del Sistema. Mecanismos: X) Colapsos de hardware o del sistema operativo que eliminan la memoria volátil; se resuelve con procesos de recuperación ante caídas (crash recovery). Y) Provocado por errores lógicos o interbloqueos; se resuelve mediante la recuperación de la transacción (aborto manual o automático).
Opciones:
A) 1-Y, 2-X
B) 1-X, 2-Y
C) 1-Y, 2-Y
D) 1-X, 2-X
E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: El fallo de transacción (errores lógicos o interbloqueos) se resuelve abortando la transacción (1-Y); el fallo del sistema (colapso de hardware/SO) requiere recuperación ante caídas para restaurar la coherencia (2-X).

[TIPO: RESPUESTA CORTA] Pregunta ID: 57
Enunciado: ¿Qué acrónimo designa al grafo que rastrea las dependencias de espera entre transacciones a través de toda la red distribuida, siendo indispensable porque un ciclo puede no existir en un solo nodo pero manifestarse solo a este nivel? Escriba la sigla en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: GWFG
Explicación: El Global Wait-For Graph (GWFG) unifica las dependencias de espera de todos los nodos; ignorar este nivel global compromete la detección correcta de interbloqueos distribuidos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 58
Enunciado: Una empresa de transporte interprovincial opera un sistema de venta de boletos distribuido con terminales en Quito, Guayaquil, Cuenca, Ambato y Loja, cada una con su propio nodo PostgreSQL. Ocurren simultáneamente: T1 (desde Quito) lee el asiento 15 del bus B-202 en estado DISPONIBLE y lo actualiza a VENDIDO; T2 (desde Guayaquil) lee todos los asientos de junio, incluido el 15, para evaluar una reserva; T3 (desde Quito) genera un reporte de ocupación de junio sin tocar el asiento 15. ¿Qué par de transacciones presenta un conflicto real según el criterio de serializabilidad?
Opciones:
A) T1 y T3, porque ambas se originan en el mismo terminal de Quito.
B) T2 y T3, porque ambas son operaciones de lectura sobre el mismo rango de fechas.
C) T1 y T2, porque comparten el mismo ítem de datos (asiento 15) y al menos una de las dos es una escritura.
D) Ninguna de las tres genera conflicto porque cada transacción proviene de un nodo distinto.
E) Ninguna de las anteriores es correcta en este contexto.
Respuesta Correcta: C
Explicación: T1 y T2 acceden al mismo ítem (asiento 15) y T1 lo escribe, lo que constituye un conflicto real. T3 no toca el asiento 15, por lo que no conflictúa con T1 ni con T2, sin importar el terminal de origen.

[TIPO: RESPUESTA CORTA] Pregunta ID: 59
Enunciado: En la solución 2PL distribuida para el escenario de venta de boletos, ¿qué tipo de candado debe adquirir T1 sobre el asiento 15 antes de poder cambiar su estado de DISPONIBLE a VENDIDO? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: EXCLUSIVO
Explicación: Toda operación de escritura bajo 2PL exige un candado exclusivo (X) sobre el dato modificado, ya que este modo no permite que ninguna otra transacción lo lea ni lo escriba simultáneamente.

[TIPO: RESPUESTA CORTA] Pregunta ID: 60
Enunciado: En el mismo escenario, T2 necesita leer el estado del asiento 15 (entre otros) únicamente para consultar su disponibilidad, sin modificarlo. ¿Qué tipo de candado sería suficiente para esa operación de T2 bajo 2PL? Escriba su respuesta en MAYÚSCULAS, sin tildes, sin espacio al inicio ni al final.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: COMPARTIDO
Explicación: Una operación de solo lectura requiere únicamente un candado compartido (S), que es compatible con otros candados compartidos, aunque incompatible con uno exclusivo ya otorgado sobre el mismo dato.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 61
Enunciado: Si T1 adquiere el candado exclusivo sobre el asiento 15 antes de que T2 intente leerlo, ¿qué ocurre con T2 bajo el protocolo 2PL?
Opciones:
A) T2 se ejecuta sin restricciones porque los candados compartidos y exclusivos siempre son compatibles entre sí.
B) T2 debe esperar hasta que T1 libere el candado exclusivo, ya que un candado compartido es incompatible con uno exclusivo ya otorgado.
C) T2 aborta automáticamente en cuanto detecta que T1 tiene un candado sobre el mismo dato.
D) T2 puede leer el valor antiguo del asiento sin ningún tipo de espera ni bloqueo.
E) Ninguna de las anteriores describe correctamente el comportamiento del protocolo.
Respuesta Correcta: B
Explicación: El candado exclusivo de T1 bloquea cualquier otro candado (compartido o exclusivo) sobre el mismo dato; T2 queda en espera hasta que T1 confirme o aborte y libere el candado.

[TIPO: ORDENAMIENTO] Pregunta ID: 62
Enunciado: Ordene las fases que atraviesa la transacción T1 al vender el asiento 15 bajo el protocolo 2PL, de la primera a la última. 1) Solicitar y obtener el candado exclusivo sobre el asiento 15 (fase de crecimiento). 2) Leer el estado actual del asiento y verificar que sea DISPONIBLE. 3) Actualizar el estado del asiento a VENDIDO. 4) Confirmar la transacción (commit) y liberar el candado (fase de decrecimiento).
Opciones:
A) 1, 2, 3, 4
B) 2, 1, 3, 4
C) 1, 3, 2, 4
D) 4, 1, 2, 3
E) 1, 2, 4, 3
Respuesta Correcta: A
Explicación: T1 primero adquiere el candado exclusivo (1), luego lee el estado para verificarlo (2), aplica la actualización (3), y finalmente confirma liberando el candado en la fase de decrecimiento (4).

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 63
Enunciado: Como alternativa a 2PL, se aplica Timestamp Ordering (TO) al mismo escenario. T1 confirma su escritura sobre el asiento 15, actualizando wts(asiento15) con su marca de tiempo. Si T2 posee una marca de tiempo TS(T2) menor que wts(asiento15), ¿qué ocurre con la operación de lectura de T2 sobre ese asiento?
Opciones:
A) T2 se acepta sin restricciones porque su timestamp es menor.
B) T2 se rechaza porque su timestamp es menor que wts(asiento15), ya que leería un valor "del futuro" respecto a su propio orden temporal.
C) T2 se acepta y sobrescribe automáticamente el valor escrito por T1.
D) T2 y T1 se ejecutan en paralelo sin ningún tipo de validación de marcas de tiempo.
E) Ninguna de las anteriores es correcta en este contexto.
Respuesta Correcta: B
Explicación: Bajo TO, una operación Read(x) se rechaza si TS(T) es menor que wts(x); T2 llegaría "tarde" respecto a una escritura ya confirmada con una marca de tiempo mayor.

[TIPO: RESPUESTA CORTA] Pregunta ID: 64
Enunciado: En este escenario de venta de boletos, donde es crítico evitar la doble venta de un mismo asiento, ¿qué modelo del Teorema CAP debería priorizar el arquitecto: CP o AP? Escriba solo la sigla del modelo, en MAYÚSCULAS.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: CP
Explicación: Frente al riesgo de doble venta, el sistema debe priorizar la Consistencia (C) sobre la Disponibilidad (A) ante una partición de red, aceptando bloquear temporalmente el servicio antes que mostrar un asiento como disponible cuando ya fue vendido.

[TIPO: EMPAREJAMIENTO] Pregunta ID: 65
Enunciado: Relacione cada estrategia de propagación de actualizaciones con el riesgo o garantía que representa para el sistema de venta de boletos del escenario. 1) Propagación perezosa (Lazy). 2) Propagación ansiosa (Eager). Riesgos: X) El asiento podría mostrarse como disponible en otra terminal después de haber sido vendido, permitiendo una doble venta. Y) Se garantiza que ninguna terminal muestre el asiento como disponible una vez vendido, a costa de mayor latencia en la confirmación de la venta.
Opciones:
A) 1-X, 2-Y
B) 1-Y, 2-X
C) 1-X, 2-X
D) 1-Y, 2-Y
E) Ninguna de las opciones es correcta.
Respuesta Correcta: A
Explicación: La propagación perezosa confirma en un nodo y propaga después, abriendo una ventana de riesgo de doble venta (1-X). La propagación ansiosa garantiza consistencia en todas las terminales antes de confirmar, a costa de latencia (2-Y).
