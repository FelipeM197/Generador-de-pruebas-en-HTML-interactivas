[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 1 Enunciado: Al evaluar las bases teóricas de la computación, ¿qué característica arquitectónica diferencia invariablemente a un sistema paralelo puro de un sistema distribuido?
Opciones: A) Comparten memoria o disco físico operando bajo un sistema de control centralizado. B) Mantienen memoria propia e independiente usando la red como único recurso compartido. C) Requieren hardware homogéneo estricto para coordinar el procesamiento transaccional. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Ejecutan paralelismo intra-query sin necesidad de interconexión por red de mensajes.
Respuesta Correcta: A Explicación: La arquitectura teórica de sistemas establece que un sistema paralelo se define por compartir físicamente la memoria o el disco bajo un mismo sistema operativo. La opción B define a un sistema distribuido, no al paralelo, fundamentado en la independencia de los elementos de procesamiento (PE).
[TIPO: EMPAREJAMIENTO] Pregunta ID: 2 Enunciado: Correlacione los "Aspectos Distribuibles" de una arquitectura de bases de datos con sus técnicas de implementación axiomáticas. (1: Lógica, 2: Funciones, 3: Datos, 4: Control).
Opciones: A) 1-Inter/intra query, 2-Cliente/servidor, 3-Fragmentación, 4-Recuperación fallos. B) 1-Fragmentación, 2-Inter/intra query, 3-Cliente/servidor, 4-Recuperación fallos. C) 1-Cliente/servidor, 2-Recuperación fallos, 3-Inter/intra query, 4-Fragmentación. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) 1-Recuperación fallos, 2-Fragmentación, 3-Cliente/servidor, 4-Inter/intra query.
Respuesta Correcta: A Explicación: Teóricamente, la Lógica se distribuye en paralelismo de consultas (inter/intra-query); las Funciones especializan nodos lógicamente (ej. Cliente/servidor); los Datos se dividen (Fragmentación/Replicación); y el Control delega la sincronización y Recuperación de fallos en la red.
[TIPO: RESPUESTA CORTA] Pregunta ID: 3 Enunciado: ¿Cuál es el término técnico formal que define la capacidad de los nodos para operar independientemente sin depender del resto, siendo un pilar en el diseño de un DDBMS?
Opciones: A) El término técnico exclusivo y axiomáticamente aceptado en la literatura es SITIO/NODO. B) El término técnico exclusivo y axiomáticamente aceptado en la literatura es DEADLOCKER. C) El término técnico exclusivo y axiomáticamente aceptado en la literatura es AUTONOMIA. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) El término técnico exclusivo y axiomáticamente aceptado en la literatura es COMMIT 2PC.
Respuesta Correcta: C Explicación: La "Autonomía" es la propiedad fundamental de los Elementos de Procesamiento (PE) en la teoría de sistemas distribuidos, dictaminando que cada PE puede tomar decisiones locales sin requerir dependencia continua de un coordinador central.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 4 Enunciado: En la distribución de la Lógica de Procesamiento, ¿qué mecanismo algorítmico define estrictamente la ejecución del paralelismo intra-query?
Opciones: A) Divide una sola consulta en subconsultas procesadas simultáneamente en varios nodos. B) Ejecuta múltiples consultas distintas concurrentemente usando un solo nodo central. C) Delega el control de recuperación distribuida a la capa de red del sistema paralelo. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Consolida las bases de datos heterogéneas mediante independencia de datos absolutas.
Respuesta Correcta: A Explicación: El paralelismo intra-query consiste en descomponer una única consulta global en múltiples subconsultas que se despachan a nodos remotos para ser calculadas simultáneamente. La opción B define parcialmente al paralelismo inter-query.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 5 Enunciado: Desde la teoría de fallos, ¿cuál es el objetivo central subyacente a la Distribución de Control en un DDBMS?
Opciones: A) Delega la recuperación de fallos a un único nodo maestro eliminando cuellos de red. B) Mantiene el catálogo del esquema de datos replicado asíncronamente en discos duros. C) Reparte la responsabilidad de coordinación eliminando los puntos únicos de colapso. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Fragmenta la lógica transaccional para evitar el uso del protocolo de dos fases 2PC.
Respuesta Correcta: C Explicación: Distribuir el control evita el problema del "Punto Único de Fallo" (SPOF) que caracteriza a los sistemas centralizados. La coordinación se reparte equitativamente, garantizando que la caída de un coordinador local no paralice la red global (Resiliencia).
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 6 Enunciado: Respecto a la interdependencia de los aspectos distribuibles, ¿cómo interactúan matemáticamente los pilares en una transacción de área amplia (WAN)?
Opciones: A) Los aspectos operan aislados garantizando que la red nunca sufra cuellos de botella. B) La distribución de datos y lógica se influyen mutuamente requiriendo control global. C) La independencia de datos reemplaza la necesidad de distribuir funciones en el nodo. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) El paralelismo inter-query suprime la fragmentación horizontal en la capa de control.
Respuesta Correcta: B Explicación: Los cuatro aspectos (Datos, Funciones, Lógica y Control) son ineludiblemente interdependientes. Distribuir datos (Fragmentación) exige obligatoriamente distribuir la lógica para leerlos (Paralelismo) y un Control riguroso (Consistencia) para integrar los resultados sin violar ACID.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 7 Enunciado: Cuando un proveedor de nube asume la gestión integral de un DDBMS abstracto listo para su explotación directa, ¿bajo qué modelo evolutivo se enmarca estrictamente?
Opciones: A) Es una plataforma PaaS pues el cliente debe gestionar el sistema operativo subyacente. B) Se clasifica como SaaS ya que el proveedor ofrece la gestión completa como un servicio. C) Opera bajo IaaS limitando la autonomía de los procesadores en clústeres heterogéneos. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Constituye un modelo P2P puro donde clientes y servidores comparten el disco central.
Respuesta Correcta: B Explicación: En la taxonomía del Cloud Computing para DDBMS, cuando el sistema se entrega gestionado (tolerancia a fallos, replicación y administración delegadas), se define académicamente como Software as a Service (SaaS).
[TIPO: EMPAREJAMIENTO] Pregunta ID: 8 Enunciado: Empareje la semántica de transferencia de red con su Modo de Entrega Teórico. (1: Pull-only, 2: Push-only, 3: Híbrido).
Opciones: A) 1-Petición explícita, 2-Envío sin solicitud, 3-Petición inicial y envíos automáticos. B) 1-Envío sin solicitud, 2-Petición inicial y envíos automáticos, 3-Petición explícita. C) 1-Petición inicial y envíos automáticos, 2-Petición explícita, 3-Envío sin solicitud. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) 1-Petición explícita, 2-Envío condicional asíncrono, 3-Ejecución concurrente estricta.
Respuesta Correcta: A Explicación: Pull-only exige que el receptor inicie la transacción de lectura; Push-only emite datos desde el servidor sin petición (Multicast/Broadcast); Híbrido se suscribe con un pull inicial para desatar un flujo de push automatizado.
[TIPO: ORDENAMIENTO] Pregunta ID: 9 Enunciado: Identifique la secuencia cronológica axiomática del progreso arquitectónico de los datos. (1: Archivos, 2: BD central, 3: P2P Temprano, 4: Cliente/Servidor, 5: Cloud).
Opciones: A) La secuencia evolutiva axiomáticamente comprobada en la teoría histórica es: 1,3,2,5,4. B) La secuencia evolutiva axiomáticamente comprobada en la teoría histórica es: 2,1,4,3,5. C) La secuencia evolutiva axiomáticamente comprobada en la teoría histórica es: 1,2,3,4,5. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) La secuencia evolutiva axiomáticamente comprobada en la teoría histórica es: 5,4,3,2,1.
Respuesta Correcta: C Explicación: La computación avanzó de sistemas de archivos redundantes (60s), a bases centralizadas, luego primeros DDBMS geodistribuidos P2P lentos (70s), el auge Cliente/Servidor (80s-90s), culminando en los servicios masivos de Cloud Computing.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 10 Enunciado: Ante la ocurrencia ineludible de un particionamiento de red, ¿cuál es el comportamiento matemático forzoso de un sistema regido por el modelo CP del Teorema CAP?
Opciones: A) Sacrifica la consistencia devolviendo lecturas obsoletas para evitar interrumpir red. B) Sacrifica la partición simulando una red perfecta para operar con alta disponibilidad. C) Sacrifica la disponibilidad cesando de responder hasta restaurar la coherencia total. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Sacrifica la autonomía local requiriendo el protocolo de compromiso de las tres fases.
Respuesta Correcta: C Explicación: El Teorema CAP de Brewer establece que ante una Partición (P), un sistema CP prioriza la Consistencia (C) fuerte. Por ende, la única vía matemática para evitar lecturas divergentes es sacrificar la Disponibilidad (A), bloqueando el servicio.
[TIPO: RESPUESTA CORTA] Pregunta ID: 11 Enunciado: ¿Cuál es el acrónimo que define el postulado matemático que rige el equilibrio forzoso entre consistencia, disponibilidad y tolerancia al particionamiento de red?
Opciones: A) El término técnico exclusivo y axiomáticamente aceptado en la literatura es MODELO. B) El término técnico exclusivo y axiomáticamente aceptado en la literatura es TEOREMA CAP. C) El término técnico exclusivo y axiomáticamente aceptado en la literatura es PRINCIPIO. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) El término técnico exclusivo y axiomáticamente aceptado en la literatura es REPLICA.
Respuesta Correcta: B Explicación: El "Teorema CAP" (Consistency, Availability, Partition tolerance) demostrado por Gilbert y Lynch dicta las limitaciones teóricas fundamentales para el diseño asíncrono y distribuido en bases de datos.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 12 Enunciado: ¿Qué propiedad estructural subyace a la comunicación entre Elementos de Procesamiento (PE) en una topología verdaderamente distribuida?
Opciones: A) Carecen de acceso directo al estado ajeno y dependen estrictamente de los mensajes. B) Mantienen una memoria global centralizada garantizando la transparencia de replicación. C) Ejecutan la sincronización mediante lectura sucia cruzada en bases de datos paralelas. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Reemplazan el control distribuido mediante el uso de directorios totalmente acoplados.
Respuesta Correcta: A Explicación: Por definición axiomática, en un DDBMS ningún PE tiene acceso a la memoria o disco de otro PE (arquitectura Shared-Nothing). La interacción requiere estrictamente el paso de mensajes a través del protocolo de red de comunicación.
[TIPO: EMPAREJAMIENTO] Pregunta ID: 13 Enunciado: Enlace cada promesa teórica de "Transparencia" con la abstracción matemática que facilita al usuario. (1: Red, 2: Fragmentación, 3: Replicación, 4: Datos).
Opciones: A) 1-Oculta servidor, 2-Oculta división, 3-Oculta copias redundantes, 4-Aísla programas. B) 1-Aísla programas, 2-Oculta copias redundantes, 3-Oculta servidor, 4-Oculta división. C) 1-Oculta división, 2-Oculta servidor, 3-Aísla programas, 4-Oculta copias redundantes. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) 1-Oculta copias redundantes, 2-Aísla programas, 3-Oculta división, 4-Oculta servidor.
Respuesta Correcta: A Explicación: La Transparencia de Red oculta la ubicación física (IP/Ciudad); Fragmentación oculta la división horizontal/vertical; Replicación encubre la existencia de copias sincronizadas; la Independencia de Datos aísla la lógica del negocio de alteraciones en disco.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 14 Enunciado: De acuerdo a la literatura fundamental, ¿cuáles son los dos vectores algorítmicos que soportan la promesa de "Rendimiento Mejorado" en entornos distribuidos?
Opciones: A) Depende exclusivamente del control de concurrencia pesimista basado en timestamps 2PL. B) Se logra mediante el escalado vertical del hardware y protocolos de consistencia laxa. C) Se sustenta lógicamente en la localidad de los datos y el paralelismo de subconsultas. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Radica en la propagación ansiosa de réplicas evitando así anomalías como el fantasma.
Respuesta Correcta: C Explicación: El rendimiento optimizado en DDBMS se fundamenta axiomáticamente en acercar los datos a la fuente de consumo (Localidad) para abatir latencia de red, y en dividir cargas transaccionales concurrentemente (Paralelismo).
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 15 Enunciado: Para mitigar cuellos de botella sin incurrir en rediseños monolíticos extremos, ¿qué estrategia teórica aplica la promesa de "Escalabilidad del Sistema"?
Opciones: A) Reemplaza los servidores por máquinas de mayor costo para evitar cuellos en latencia. B) Agrega nuevos nodos a la red distribuyendo la carga transaccional de manera elástica. C) Elimina la necesidad de particionar los datos al mantener directorios centralizados. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Fomenta el uso de catálogos monolíticos para incrementar el paralelismo inter-query.
Respuesta Correcta: B Explicación: La promesa de Escalabilidad en un DDBMS descansa sobre el "Escalado Horizontal" (Scale-out), el cual añade nodos básicos para repartir la carga, contrastando con el costoso "Escalado Vertical" (Scale-up) de entornos centralizados (Opción A).
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 16 Enunciado: Dentro de la promesa de Confiabilidad y Transacciones Distribuidas, ¿qué garantía estructural proporciona la "Transparencia de Concurrencia"?
Opciones: A) Permite la lectura sucia para garantizar un rendimiento óptimo en la red área amplia. B) Oculta la fragmentación forzando el reinicio en cascada de transacciones secundarias. C) Crea la ilusión de que el usuario opera el sistema en solitario sin las interferencias. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Consolida las réplicas mediante propagación perezosa mitigando fallos del coordinador.
Respuesta Correcta: C Explicación: La transparencia de concurrencia, garantizada por las propiedades de aislamiento ACID y la serializabilidad, aísla cada hilo de ejecución de modo que el cliente percibe estar manipulando los recursos sin colisiones con otros usuarios paralelos.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 17 Enunciado: Dada la naturaleza interdependiente de las redes, ¿por qué es matemáticamente imposible satisfacer simultáneamente todas las promesas de un DDBMS en grado máximo?
Opciones: A) Mejorar la consistencia fuerte degrada ineludiblemente los tiempos de la latencia. B) Optimizar la localidad de datos destruye la transparencia de red de forma irreversible. C) Priorizar la tolerancia a particiones anula completamente la autonomía local del nodo. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Implementar escalabilidad horizontal previene totalmente la ocurrencia de los deadlock.
Respuesta Correcta: A Explicación: Las promesas incurren en "Trade-offs" (Compromisos). Priorizar un modelo estricto de Consistencia (como Replicación Ansiosa) penaliza el Rendimiento al forzar transacciones largas sobre latencias de red, validando que el equilibrio absoluto es inalcanzable.
[TIPO: RESPUESTA CORTA] Pregunta ID: 18 Enunciado: ¿Qué término técnico, derivado del inglés, define el sacrificio o concesión ineludible entre múltiples beneficios teóricos contradictorios en el diseño?
Opciones: A) El término técnico exclusivo y axiomáticamente aceptado en la literatura es DEADLOCKS. B) El término técnico exclusivo y axiomáticamente aceptado en la literatura es TRADE-OFF. C) El término técnico exclusivo y axiomáticamente aceptado en la literatura es ALGORITMO. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) El término técnico exclusivo y axiomáticamente aceptado en la literatura es MULTICAST.
Respuesta Correcta: B Explicación: Un "Trade-off" es el concepto que rige las áreas conflictivas en el diseño DDBMS, denotando el costo colateral asumido (ej. perder velocidad) a cambio de optimizar una métrica prioritaria (ej. ganar consistencia transaccional global).
[TIPO: EMPAREJAMIENTO] Pregunta ID: 19 Enunciado: Relacione la violación teórica a la propiedad de Aislamiento con su respectiva Anomalía de Ejecución Concurrente. (1: Perdida, 2: Sucia, 3: No Repetible, 4: Fantasma).
Opciones: A) 1-Sobrescritura destructiva, 2-Estado no consolidado, 3-Valor mutado, 4-Cardinalidad. B) 1-Estado no consolidado, 2-Cardinalidad, 3-Sobrescritura destructiva, 4-Valor mutado. C) 1-Valor mutado, 2-Sobrescritura destructiva, 3-Cardinalidad, 4-Estado no consolidado. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) 1-Cardinalidad, 2-Valor mutado, 3-Estado no consolidado, 4-Sobrescritura destructiva.
Respuesta Correcta: A Explicación: La Actualización Perdida causa sobrescritura (viola atomicidad); la Lectura Sucia lee valores no consolidados; la Lectura No Repetible ve un valor mutado entre dos consultas; los Fantasmas alteran la cardinalidad y conteo de tablas por agregaciones externas.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 20 Enunciado: El Control de Concurrencia basado en Bloqueos de Dos Fases (2PL) preserva el orden serializable. No obstante, ¿qué vulnerabilidad letal introduce en WAN?
Opciones: A) Ocasiona interbloqueos circulares globales que exigen algoritmos de detección estricta. B) Provoca reinicios en cascada por verificaciones fallidas de las marcas de tiempo joven. C) Impide la recuperación autónoma forzando la separación de intenciones con el pre-commit. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Genera lecturas fantasmas al desactivar la fase de encogimiento en nodos geográficos.
Respuesta Correcta: A Explicación: El protocolo 2PL (Two-Phase Locking) retiene candados pesimistas. Su mayor riesgo sistémico es el "Deadlock Global" (Interbloqueo), requiriendo construir y rastrear Grafos de Espera de Transacciones (WFG) a través de la latencia de la red WAN.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 21 Enunciado: Si el administrador decide sustituir 2PL por el algoritmo optimista Timestamp Ordering (TO) para evitar interbloqueos, ¿qué penalización teórica asume?
Opciones: A) Genera grafos de espera cíclicos resolviéndose únicamente mediante consenso de quórum. B) Evita los bloqueos pero penaliza el rendimiento al forzar reinicios masivos en cascada. C) Aplica un esquema pesimista reteniendo candados físicos hasta concluir la transacción. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Sacrifica la consistencia global operando exclusivamente bajo arquitecturas tolerantes AP.
Respuesta Correcta: B Explicación: Timestamp Ordering previene bloqueos (deadlocks) pero ante alta concurrencia de escrituras superpuestas o desordenadas por latencia de red, desata "Reinicios en Cascada" (Cascading Aborts), destruyendo el throughput transaccional.
[TIPO: EMPAREJAMIENTO] Pregunta ID: 22 Enunciado: Distinga el comportamiento de fiabilidad de los Protocolos Transaccionales. (1: 2PC, 2: 3PC, 3: Paxos).
Opciones: A) 1-Síncrono bloqueante, 2-Recuperación autónoma, 3-Decisiones validadas con los quórums. B) 1-Recuperación autónoma, 2-Decisiones validadas con los quórums, 3-Síncrono bloqueante. C) 1-Decisiones validadas con los quórums, 2-Síncrono bloqueante, 3-Recuperación autónoma. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) 1-Síncrono bloqueante, 2-Decisiones validadas con los quórums, 3-Recuperación autónoma.
Respuesta Correcta: A Explicación: 2PC es inherentemente síncrono y bloqueante (vulnerable a caídas del coordinador). 3PC integra el Pre-Commit para recuperación autónoma. Paxos elimina el requerimiento de totalidad apoyándose en mayorías relativas (quórum) para fallos parciales.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 23 Enunciado: En el mantenimiento de consistencia mutua, ¿cuál es el postulado diferencial entre los Modelos de Propagación de Réplicas Ansiosa (Eager) y Perezosa (Lazy)?
Opciones: A) Ansiosa sincroniza inmediatamente bloqueando la red; perezosa permite leer obsoletos. B) Ansiosa sacrifica la consistencia estricta; perezosa garantiza formalmente atomicidad. C) Ambas previenen absolutamente el surgimiento de interbloqueos en transacciones globales. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Perezosa utiliza estrictamente el protocolo de tres fases mitigando demoras y bloqueos.
Respuesta Correcta: A Explicación: Eager Replication bloquea la transacción original integrando todas las copias de forma síncrona, maximizando consistencia pero degradando latencia. Lazy Replication actualiza asíncronamente, mejorando velocidad a costa de permitir visibilidad de datos temporales obsoletos.
[TIPO: RESPUESTA CORTA] Pregunta ID: 24 Enunciado: ¿Cuál es el criterio formal de corrección matemática que exige que un historial concurrente produzca los mismos efectos que un historial secuencial puro?
Opciones: A) El término técnico exclusivo y axiomáticamente aceptado en la literatura es CONCURRENTE. B) El término técnico exclusivo y axiomáticamente aceptado en la literatura es ATOMICIDAD!. C) El término técnico exclusivo y axiomáticamente aceptado en la literatura es SERIALIZABILIDAD. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) El término técnico exclusivo y axiomáticamente aceptado en la literatura es TIMESTAMPING.
Respuesta Correcta: C Explicación: La "Serializabilidad" (1SR) es la piedra angular del control de concurrencia. Un scheduler válido asegura que a pesar del entrelazamiento de las transacciones (paralelismo), el impacto en base de datos equivalga algebraicamente a ejecutarlas una tras otra.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 25 Enunciado: En la taxonomía de la arquitectura DDBMS, ¿cuál es la diferencia semántica formal entre un "Desafío de Diseño" y un "Área Conflictiva"?
Opciones: A) El desafío es la anomalía reactiva transaccional, el conflicto es el diseño preventivo. B) El desafío busca reglas globales preventivas; el conflicto es la falla específica visible. C) Ambos conceptos describen exactamente la imposibilidad matemática del teorema de Brewer. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) El conflicto se suprime totalmente mediante el escalamiento horizontal en la nube IaaS.
Respuesta Correcta: B Explicación: El "Desafío" actúa a nivel estratégico (ej. diseñar mecanismos de aislamiento), operando como reglas preventivas. El "Área Conflictiva" (ej. lectura sucia) es la manifestación operativa reactiva que ocurre cuando el desafío no ha sido mitigado al 100%.
[TIPO: EMPAREJAMIENTO] Pregunta ID: 26 Enunciado: Relacione las 3 Dimensiones de Implementación definidas por M. T. Özsu con el vector de complejidad técnica que introducen. (1: Autonomía, 2: Distribución, 3: Heterogeneidad).
Opciones: A) 1-Control local autónomo, 2-Dispersión física de nodos, 3-Diferencias en software base. B) 1-Diferencias en software base, 2-Control local autónomo, 3-Dispersión física de nodos. C) 1-Dispersión física de nodos, 2-Diferencias en software base, 3-Control local autónomo. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) 1-Control local autónomo, 2-Diferencias en software base, 3-Dispersión física de nodos.
Respuesta Correcta: A Explicación: Según el modelo de Özsu, la Autonomía denota la capacidad del control local independiente; la Distribución marca la expansión topográfica de las bases de datos (Single-site vs WAN); y la Heterogeneidad contempla las discordancias en protocolos, hardware y SQL.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 27 Enunciado: Al evaluar el árbol relacional, ¿por qué la optimización de consultas distribuidas recae inevitablemente en un nivel de complejidad clasificado como NP-Hard?
Opciones: A) Requiere consolidar firmas de veracidad para los datos no estructurados en repositorios. B) Evaluar combinaciones de uniones de fragmentos y latencia de red resulta intratable hoy. C) Depende del protocolo de dos fases para prevenir la lectura sucia en catálogos globales. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Suprime la capacidad de particionamiento horizontal exigiendo escaneos totales de nodos.
Respuesta Correcta: B Explicación: Al existir múltiples nodos y fragmentos (espacio de búsqueda exponencial), sumado al costo asimétrico de transferir datos por red frente a ejecutar localmente, encontrar el plan de consulta de "costo mínimo absoluto" carece de solución en tiempo polinómico.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 28 Enunciado: Frente al desafío del crecimiento dinámico, ¿qué mecanismo formal ampara la aplicación estratégica del Scale-out (Escalamiento Horizontal)?
Opciones: A) Agrega capacidad mediante la expansión de nodos paralelos sin afectar la base operativa. B) Reemplaza procesadores de bajo costo por servidores de gama alta para absorber latencia. C) Modifica el esquema relacional migrando todas las transacciones al modelo híbrido NoSQL. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Consolida las bases de datos en un clúster de disco centralizado limitando fragmentación.
Respuesta Correcta: A Explicación: Scale-out es el enfoque arquitectónico (típicamente Shared-Nothing) que aborda picos de demanda distribuyendo peticiones a través de la adhesión elástica y transparente de hardware comoditizado a la red de clústeres.
[TIPO: EMPAREJAMIENTO] Pregunta ID: 29 Enunciado: Enlace las dimensiones de la ingesta de Big Data (las 4 V's) con el reto arquitectónico específico que interponen al DDBMS. (1: Volumen, 2: Velocidad, 3: Veracidad).
Opciones: A) 1-Gestión de petabytes, 2-Flujos masivos en tiempo real, 3-Curación de los datos sucios. B) 1-Flujos masivos en tiempo real, 2-Curación de los datos sucios, 3-Gestión de petabytes. C) 1-Curación de los datos sucios, 2-Gestión de petabytes, 3-Flujos masivos en tiempo real. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) 1-Gestión de petabytes, 2-Curación de los datos sucios, 3-Flujos masivos en tiempo real.
Respuesta Correcta: A Explicación: El Volumen se sortea con file systems como HDFS; la Velocidad requiere procesamiento de Streams (tiempo real); y la Veracidad exige motores de depuración analítica para mitigar las incertezas en datos crudos recolectados de la web.
[TIPO: RESPUESTA CORTA] Pregunta ID: 30 Enunciado: ¿Qué cualidad teórica en el procesamiento masivo de datos aborda la necesidad intrínseca de depurar fuentes con procedencia incierta o conflictiva?
Opciones: A) El término técnico exclusivo y axiomáticamente aceptado en la literatura es VISIBILIDAD. B) El término técnico exclusivo y axiomáticamente aceptado en la literatura es HETEROGÉNEO. C) El término técnico exclusivo y axiomáticamente aceptado en la literatura es VERACIDAD. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) El término técnico exclusivo y axiomáticamente aceptado en la literatura es AISLAMIENTO.
Respuesta Correcta: C Explicación: La "Veracidad" es la dimensión de Big Data responsable de garantizar la calidad, limpieza y curación de la información de cara a soportar analíticas confiables sin violar la integridad del DDBMS.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 31 Enunciado: Al descentralizar la estructura mediante un Catálogo Distribuido, el sistema agiliza el enrutamiento. Teóricamente, ¿qué Trade-off irresoluble se origina simultáneamente?
Opciones: A) Bloquea el acceso local paralizando la localización de fragmentos en el servidor central. B) Mejora la búsqueda local pero penaliza drásticamente la latencia al actualizar el esquema. C) Suprime por completo la posibilidad de ejecutar paralelismo intra-query en transacciones. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Delega la responsabilidad de consistencia a los relojes lógicos del consenso por quórums.
Respuesta Correcta: B Explicación: Un directorio distribuido mitiga el cuello de botella central porque la localización (búsqueda) se resuelve en réplicas locales, pero exige una sincronización asfixiante de la red WAN para mantener dichas réplicas consistentes ante cualquier actualización de metadatos.
[TIPO: EMPAREJAMIENTO] Pregunta ID: 32 Enunciado: Ordene semánticamente las fases para gestionar las interdependencias mutuas bloqueadas (Deadlocks) en topologías WAN. (1: Detección, 2: Prevención, 3: Resolución).
Opciones: A) 1-Grafos de espera, 2-Reglas de asignación, 3-Cancelar la transacción víctima bloqueante. B) 1-Cancelar la transacción víctima bloqueante, 2-Grafos de espera, 3-Reglas de asignación. C) 1-Reglas de asignación, 2-Cancelar la transacción víctima bloqueante, 3-Grafos de espera. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) 1-Grafos de espera, 2-Cancelar la transacción víctima bloqueante, 3-Reglas de asignación.
Respuesta Correcta: A Explicación: La Detección rastrea el Wait-For-Graph (WFG) en busca de ciclos; la Prevención aplica reglas formales que restringen asignaciones futuras riesgosas; y la Resolución exige un aborto forzado de la transacción "víctima" para romper la circularidad de recursos retenidos.
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 33 Enunciado: Para mitigar violaciones algorítmicas de Consistencia, ¿qué familias de mecanismos implementa axiomáticamente el Control de Concurrencia Distribuido?
Opciones: A) Emplea candados, ordenamiento temporal o verificaciones optimistas previniendo colisión. B) Utiliza exclusivamente propagación ansiosa para mitigar lecturas sucias en red geográfica. C) Delega el control absoluto a los hipervisores anulando la autonomía del procesador local. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Aplica replicación perezosa incondicional para asegurar serializabilidad en las consultas.
Respuesta Correcta: A Explicación: El control de concurrencia despliega candados (2PL Pesimista), marcas cronológicas crecientes (Timestamp Ordering), y/o validaciones a posteriori (Optimistic Concurrency Control) para coordinar sincronizadamente el acceso sobre un mismo ítem.
[TIPO: ORDENAMIENTO] Pregunta ID: 34 Enunciado: Determine el encadenamiento secuencial teórico subyacente al Procesamiento de Consultas Distribuidas. (1: Descomposición, 2: Optimización, 3: Ejecución local, 4: Integración).
Opciones: A) La secuencia algorítmica axiomáticamente demostrada en la teoría formal es: 1, 2, 3, 4. B) La secuencia algorítmica axiomáticamente demostrada en la teoría formal es: 2, 1, 4, 3. C) La secuencia algorítmica axiomáticamente demostrada en la teoría formal es: 4, 3, 2, 1. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) La secuencia algorítmica axiomáticamente demostrada en la teoría formal es: 1, 3, 2, 4.
Respuesta Correcta: A Explicación: La evaluación inicia dividiendo la consulta según fragmentos (Descomposición); se minimiza matemáticamente el plan de transferencia (Optimización); los nodos procesan sus subtareas mediante paralelismo (Ejecución Local); y se ensambla la respuesta final (Integración).
[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 35 Enunciado: En el pilar del diseño centrado en la Confiabilidad (Reliability), ¿cómo logra un DDBMS subsistir a pesar de desconexiones parciales graves?
Opciones: A) Limita el acceso a datos garantizando que las consultas sean estrictamente secuenciales. B) Aprovecha la redundancia y los logs para tolerar fallos manteniendo consistencia estricta. C) Anula las réplicas en favor de un directorio central previniendo los estados bloqueantes. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) Requiere que los nodos posean hardware idéntico para conmutar las transacciones fallidas.
Respuesta Correcta: B Explicación: La Confiabilidad (Tolerancia a fallos) se asegura operativamente mediante la redundancia pasiva/activa (Replicación) junto a la instrumentación de bitácoras de recuperación (Logs transaccionales), manteniendo la consistencia de red.
[TIPO: EMPAREJAMIENTO] Pregunta ID: 36 Enunciado: Relacione la variable adicional de Diseño DDBMS con la métrica técnica que busca salvaguardar. (1: Seguridad, 2: Heterogeneidad, 3: Escalabilidad).
Opciones: A) 1-Protege datos distribuidos, 2-Integra motores dispares, 3-Soporta adición de nodos red. B) 1-Integra motores dispares, 2-Soporta adición de nodos red, 3-Protege datos distribuidos. C) 1-Soporta adición de nodos red, 2-Protege datos distribuidos, 3-Integra motores dispares. D) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto. E) 1-Protege datos distribuidos, 2-Soporta adición de nodos red, 3-Integra motores dispares.
Respuesta Correcta: A Explicación: En arquitecturas modernas (Problemas Adicionales), la Seguridad protege esquemas abiertos; la Heterogeneidad orquesta interoperabilidad entre bases SQL/NoSQL sin alterar la semántica; y la Escalabilidad asegura que la topología reciba dinámicamente nuevos PEs sin colapsar.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 1
Enunciado: En la integración PostgreSQL-Oracle usando oracle_fdw, se lanza un SELECT con cláusula WHERE extensa. ¿Cuál es el comportamiento de red bajo el principio de localidad de datos?
Opciones:
A) Transfiere todos los datos brutos a PG para aplicar el filtrado en memoria local.
B) Traduce la cláusula a OCI y el motor Oracle ejecuta el filtrado remotamente.
C) Carga los bloques físicos WAL del motor Oracle hacia el buffer virtual de PG.
D) Sincroniza la tabla foránea usando un decodificador lógico antes de su lectura.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: El adaptador oracle_fdw aplica el principio de "Pushdown", delegando el procesamiento algebraico de filtrado al nodo remoto (Oracle) para minimizar la transferencia neta y la latencia de red. La opción A viola el principio de localidad de datos.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 2
Enunciado: Relacione la limitación arquitectónica de oracle_fdw con su equivalente mecanismo de resolución estructural en sistemas heterogéneos: 1) Identidad autogenerada con subtipo OCI 0. 2) Intercepción lógica de inserciones. 3) Carencia de tipo de dato nativo remoto. 4) Anulación de secuencias DEFAULT por envíos NULL directos. Elementos: X) Vista Remota, Y) Trigger INSTEAD OF, Z) Mapeo de Usuario, W) Type Cast Forzado.
Opciones:
A) 1-X, 2-Y, 3-Z, 4-W
B) 1-X, 2-Y, 3-W, 4-Y
C) 1-Y, 2-X, 3-Z, 4-W
D) 1-W, 2-Z, 3-Y, 4-X
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Para mantener la Transparencia de Distribución, se enmascara la llave primaria problemática con una Vista Remota (1->X), se intercepta la inserción (2->Y) y se ignora el envío nulo inyectando la función SYSDATE vía el mismo Trigger (4->Y).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 3
Enunciado: Identifique el acrónimo estricto del estándar de la industria (norma ISO) que define el marco abstracto "Management of External Data" implementado nativamente por PostgreSQL para posibilitar el ecosistema FDW.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: SQL/MED
Explicación: SQL/MED es el protocolo ISO formal que gobierna la interoperabilidad de repositorios externos en sistemas gestores de bases de datos de arquitectura abierta.

[TIPO: ORDENAMIENTO]
Pregunta ID: 4
Enunciado: Determine el orden de dependencias estrictas para que una transacción originada en PostgreSQL culmine exitosamente persistida en los datafiles remotos de Oracle. I: Motor local (pg_class) delega operación al adaptador oracle_fdw. II: Oracle ejecuta transacción y retorna señal de éxito ORA-00000. III: Librería OCI (Instant Client) transporta la trama binaria. IV: Cliente de red enruta y emite COMMIT sistémico.
Opciones:
A) IV -> I -> III -> II
B) I -> III -> II -> IV
C) III -> I -> IV -> II
D) IV -> III -> II -> I
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: De acuerdo con la orquestación distribuida, el gestor local delega en el plugin (I), luego usa OCI (III) para retransmitir a la red, Oracle materializa la durabilidad (II), y el cliente local confirma la atomicidad total del flujo (IV).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 5
Enunciado: Bajo la teoría de control de concurrencia ACID, ¿qué sucede sistemáticamente si se ejecuta un bloque BEGIN; INSERT hacia un nodo oracle_fdw; seguido de un ROLLBACK; manual desde un cliente PostgreSQL?
Opciones:
A) El registro persiste en Oracle, violando el teorema de atomicidad del ecosistema.
B) El adaptador interviene transformando el aborto en un DML inverso tipo DELETE.
C) PostgreSQL aísla la conexión en memoria y detiene el flujo al motor foráneo.
D) El registro se descarta por completo, garantizando una atomicidad distribuida.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: D
Explicación: Gracias a la abstracción de Transacciones ACID, oracle_fdw hereda y propaga algorítmicamente el comando ROLLBACK al motor remoto antes de confirmar el bloque, garantizando el aislamiento (Isolation) y la reversión (Atomicidad).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 6
Enunciado: Al evaluar un sistema FDW frente a una replicación real en un entorno de alta disponibilidad, si el nodo Oracle sufre una partición de red total (caída libre), ¿qué principio matemático delinea el estado resultante del DDBMS en PostgreSQL?
Opciones:
A) El teorema CAP exige que la tabla foránea utilice sus últimos bloques locales.
B) El principio de durabilidad garantiza lecturas parciales desde el WAL residual.
C) La disponibilidad es sacrificada por completo en favor de la consistencia neta.
D) La consistencia eventual congela el estado bloqueando a los clientes directos.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: Según el Teorema CAP (Consistencia, Disponibilidad, Tolerancia a Particiones), al carecer de almacenamiento físico local, el fallo de red suprime instantáneamente la Disponibilidad para priorizar la Consistencia del nodo.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 7
Enunciado: Durante un proceso de replicación lógica unidireccional, el nodo secundario sufre una caída eléctrica. Tras reiniciar, ¿cómo garantiza algorítmicamente el motor primario la recuperación exacta de los datos asíncronos pendientes?
Opciones:
A) El comando pg_basebackup retransmite los bloques binarios del disco faltante.
B) El slot lógico retiene matemáticamente el WAL no confirmado por el suscriptor.
C) El protocolo 2PC bloquea el primario impidiendo divergencias transaccionales.
D) El decodificador pgoutput reconstruye los estados DML desde logs fragmentados.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: La resiliencia asíncrona no usa un Two-Phase Commit (2PC) sino un Replication Slot que actúa como candado de vida útil para el archivo WAL. Esto asegura la Durabilidad y evita que el archivo se recicle antes de que el nodo secundario asimile el Log Sequence Number (LSN).

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 8
Enunciado: Empareje la configuración sistémica con su implicación matemática o de control arquitectónico en un clúster de replicación. 1) wal_level=logical. 2) max_wal_senders. 3) pg_hba.conf. 4) COPY initial data. Elementos: X) Límite duro de concurrencia de streaming. Y) Materialización del snapshot lógico de sincronización. Z) Exposición del álgebra relacional en eventos del log. W) Vector de seguridad de control de acceso.
Opciones:
A) 1-Z, 2-X, 3-W, 4-Y
B) 1-Z, 2-Y, 3-X, 4-W
C) 1-X, 2-Z, 3-W, 4-Y
D) 1-W, 2-X, 3-Y, 4-Z
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: El wal_level=logical permite decodificar las DMLs relacionales (Z), max_wal_senders gestiona los límites asíncronos del proceso emisor (X), pg_hba asegura red (W) y COPY clona estructuralmente el instante cero (Y).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 9
Enunciado: Especifique el identificador exacto del plugin nativo de PostgreSQL 18 responsable funcionalmente de decodificar el WAL y transformarlo en un flujo lógico estructurado para suscripciones.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: PGOUTPUT
Explicación: El plugin pgoutput asume el rol algorítmico vital de traducir los bloques opacos del WAL en operaciones DML puras interpretables (INSERT/UPDATE/DELETE), diferenciándolo del mecanismo de réplica física.

[TIPO: ORDENAMIENTO]
Pregunta ID: 10
Enunciado: Determine la cadena estricta de dependencias procedimentales durante la inicialización de una suscripción lógica asimétrica. I: Aplicación infinita de cambios DML decodificados (worker asíncrono). II: Retención estricta de transacciones vivas en el Replication Slot de red. III: Materialización física en disco del snapshot base (Initial Sync). IV: Reconocimiento sistémico del rol con privilegios REPLICATION.
Opciones:
A) IV -> II -> III -> I
B) II -> IV -> III -> I
C) IV -> III -> II -> I
D) II -> III -> IV -> I
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: El flujo determinista impone: Autenticación inicial del Worker (IV), creación inmediata del Slot en origen para evitar lag de WAL (II), copiado absoluto inicial (III) y finalmente el streaming en tiempo real (I).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 11
Enunciado: En replicación lógica estándar, si un cliente altera directamente una llave primaria preexistente en el nodo suscriptor, ¿qué fallo matemático del teorema de consistencia distribuida ocurre?
Opciones:
A) Generación de bucles infinitos por ausencia de vectores matemáticos de Lamport.
B) Ruptura transaccional inminente por falta de resolución nativa de conflictos.
C) Interbloqueo distribuido gestionado automáticamente por consenso lógico de Raft.
D) Sobreescritura asíncrona delegando control algorítmico al criterio "Last Write".
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: PostgreSQL unidireccional carece de CRDTs (Conflict-free Replicated Data Types). Una colisión en Primary Key destruye la semántica relacional y bloquea fatalmente la replicación, sin aplicar un LWW ("Last Write Wins").

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 12
Enunciado: Al contrastar Replicación Lógica y postgres_fdw en la planificación de una arquitectura distribuida, ¿qué penalidad sistémica o pérdida axiomática asumes deliberadamente al elegir postgres_fdw?
Opciones:
A) El sacrificio absoluto de procesar el álgebra relacional localmente en el nodo.
B) La imposibilidad funcional de ejecutar protocolos Commit para datos concurrentes.
C) La pérdida ineludible de disponibilidad offline ante fluctuaciones y picos de red.
D) La dependencia de algoritmos sincrónicos de propagación de deltas inmutables.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: Según el Teorema CAP, elegir un FDW (sin copia física ni lógica) sacrifica la Availability en favor de mantener el almacenamiento centralizado, penalizando drásticamente la latencia y la resiliencia offline.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 13
Enunciado: En el contexto de replicación física pura (streaming), durante una carga transaccional masiva que excede la capacidad de memoria, ¿qué tipo estricto de información de red inyecta el motor origen al standby?
Opciones:
A) La sentencia del álgebra relacional acoplada con fragmentos de las filas DML.
B) Matrices vectoriales de concurrencia que unifican el estado ACID del clúster.
C) Comandos binarios ciegos indicando un byte-offset físico exacto a sobreescribir.
D) Instantáneas lógicas incrementales que eluden los bloqueos del disco de origen.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: A diferencia del FDW o pub/sub, el mecanismo físico transporta un Write-Ahead Log que no contiene SQL sino instrucciones binarias ciegas y estrictas (Ej: file_ID, offset_byte) dictaminando el bloque de disco de 8KB a modificar.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 14
Enunciado: Correlacione el comportamiento algorítmico del almacenamiento físico con la instrucción que fluye vía WAL hacia el nodo clonado. 1) Datafile < 1GB con capacidad residual de bloques. 2) Datafile < 1GB desprovisto de espacio libre absoluto. 3) Datafile sobrepasa su límite de diseño nativo (1GB). Elementos: X) El Standby invoca la extensión de página virtual en hardware de disco. Y) El Standby materializa un file-segment numérico completamente nuevo. Z) El Standby sobreescribe instantáneamente la traza en la misma página 8KB.
Opciones:
A) 1-Z, 2-X, 3-Y
B) 1-X, 2-Z, 3-Y
C) 1-Z, 2-Y, 3-X
D) 1-Y, 2-X, 3-Z
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: 1: Z (Espacio libre existe), 2: X (Petición de agrandamiento de bloque al OS), 3: Y (Corte duro por límite de PostgreSQL, generando sufijos como "datafile.1").

[TIPO: RESPUESTA CORTA]
Pregunta ID: 15
Enunciado: Identifique el nombre exacto del archivo marcador de presencia binaria, requerido desde PostgreSQL 12 y generado por pg_basebackup (-R), que condiciona la máquina de estados interna al modo Recovery de solo lectura.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: STANDBY.SIGNAL
Explicación: standby.signal funciona como el switch binario estructural que impide al motor ejecutar procesos de asimilación normales o inicializaciones DDL, forzando un loop permanente de stream-recovery (fijando el sistema en solo lectura).

[TIPO: ORDENAMIENTO]
Pregunta ID: 16
Enunciado: Determine la dependencia estricta cronológica del algoritmo implementado por la herramienta pg_basebackup para consolidar una topología de clon físico distribuido. I: Transferencia y validación de bloques de disco comprimidos (Base Backup). II: Inyección asíncrona recurrente de la ventana de WAL concurrente (-X stream). III: Purga o vaciado absoluto de inodos en el volumen físico o carpeta receptora. IV: Inyección paramétrica de banderas sistémicas de configuración de recuperación.
Opciones:
A) III -> I -> II -> IV
B) I -> II -> III -> IV
C) III -> II -> I -> IV
D) II -> I -> III -> IV
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: El sistema aniquila datos huérfanos (III), ejecuta el transporte pesado binario base (I), al mismo tiempo compensa la latencia transaccional procesando el WAL vivo (II) y por último estampa las marcas estáticas "standby.signal" (IV).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 17
Enunciado: ¿Cuál es el fundamento teórico-transaccional por el cual un nodo configurado en recuperación continua restringe axiomáticamente cualquier intento de inserción DML (read-only)?
Opciones:
A) Los candados asíncronos distribuidos en memoria bloquean concurrencia paralela.
B) El motor anula la propagación de llaves foráneas para predecir los nodos activos.
C) Inyectar bytes locales desfasaría instantáneamente los offsets binarios del WAL.
D) Se requiere obligatoriamente una firma matemática GPG en las transacciones DML.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: La replicación física clona basándose en Offsets estrictos de disco (posición byte). Escribir localmente desplazaría las cabeceras lógicas, corrompiendo inmediatamente la consistencia binaria sin posible mitigación del sistema.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 18
Enunciado: ¿Cómo sustenta la arquitectura de PostgreSQL la replicación física asimétrica si el disco origen (NVMe rápido) y el disco destino (HDD magnético lento) operan físicamente de manera heterogénea?
Opciones:
A) Traduciendo dinámicamente las cadenas a formato relacional independiente.
B) Abstrayendo el hardware del OS mediante páginas lógicas unificadas de 8KB.
C) Comprimiendo vectorialmente los deltas para sincronizar con la rotación HDD.
D) Forzando descodificaciones a nivel de kernel utilizando drivers de disco SCSI.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: A nivel arquitectónico, PostgreSQL abstrae la máquina operando sobre sus propias páginas (bloques) virtuales de 8KB. Transfiere direcciones lógicas de archivo y offset hacia el SO destino, resolviendo la asimetría hardware sin corromper ACID.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 19
Enunciado: En la arquitectura fragmentada de YugabyteDB, ¿qué axioma asegura estrictamente la propiedad de disjunción (disjointness) al aplicar una proyección y evaluar colisiones entre fragmentos distribuidos?
Opciones:
A) El conteo total equitativo garantiza uniformidad en la distribución del particionado.
B) Los algoritmos criptográficos anulan divergencias clonando el quorum de los nodos.
C) La función determinista de hash prohíbe mapear una tupla en más de un fragmento.
D) La arquitectura delega el ruteo de transacciones asíncronas a servidores auxiliares.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: La Disjunción (intersección vacía) establece que ningún registro existirá duplicado entre los particionamientos. Como la función Hash de la llave primaria es puramente determinista, es matemáticamente imposible que la misma fila colisione en 2 fragmentos físicos.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 20
Enunciado: Vincule el principio teórico de bases distribuidas con su validación algorítmica y funcional en el entorno particionado: 1) Completitud distributiva. 2) Transparencia al usuario. 3) Consistencia bajo estrés (Raft Consensus). 4) Disjunción estricta distributiva. Elementos: X) Resolución de peticiones a la tabla padre obviando rutas de red. Y) Rechazo de escrituras al fragmentarse el Quorum de los nodos. Z) Ecuación matemática: Suma neta fragmentos = Cardinalidad global. W) Evaluación nula de intersección (JOIN) inter-nodos.
Opciones:
A) 1-Z, 2-X, 3-Y, 4-W
B) 1-Z, 2-Y, 3-X, 4-W
C) 1-W, 2-X, 3-Y, 4-Z
D) 1-W, 2-Z, 3-Y, 4-X
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: Reglas fundamentales de DDBMS: Completitud (la suma agota el universo -> Z), Transparencia (el usuario desconoce topología física -> X), Quorum Raft asegura que N/2+1 aprueben y prevenga split-brain (Y), Disjunción verifica cero duplicados (W).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 21
Enunciado: Identifique la instrucción sintáctica de Data Definition Language (DDL) obligatoria aplicada sobre la relación relacional padre para activar la fragmentación horizontal basada en algoritmos deterministas o de módulo.
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: PARTITION BY HASH
Explicación: PARTITION BY HASH activa el enrutador virtual de inserción en PostgreSQL/YugabyteDB, permitiendo posteriormente que expresiones de MODULUS y REMAINDER canalicen algorítmicamente las tuplas hacia sus fragmentos dependientes.

[TIPO: ORDENAMIENTO]
Pregunta ID: 22
Enunciado: Determine la dependencia de flujos lógicos aplicada por el gestor transaccional distribuido cuando un bloque de inyección (INSERT) impacta sobre la tabla padre virtual de un clúster YugabyteDB. I: Almacenamiento final físico sobre disco de red (Tablet Raft). II: Inyección DML bruta de datos orientada exclusivamente hacia el esqueleto abstracto padre. III: División de módulo (MODULUS) sobre el vector resolviendo el índice de fragmento. IV: Computación de función criptográfica unidireccional procesando la Primary Key.
Opciones:
A) II -> IV -> III -> I
B) II -> III -> IV -> I
C) IV -> II -> III -> I
D) IV -> III -> II -> I
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: El sistema intercepta la inserción en la entidad (II), extrae su PK y la procesa criptográficamente (IV), divide por el peso numérico para seleccionar vía Resto/Remainder (III) y materializa en el nodo físico que hospeda el Tablet (I).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 23
Enunciado: En un clúster asimétrico de YugabyteDB, si sobreviene un colapso físico de un nodo, ¿cuál es el teorema de control de distribución que fuerza la inhabilitación del motor para realizar mutaciones de datos (escrituras)?
Opciones:
A) La asimetría de red anula los candados transaccionales de los relojes lógicos.
B) El protocolo Raft bloquea operaciones al no sumar mayoría estricta de Quorum.
C) El sistema penaliza la consistencia obligando a lecturas sucias en discos residuales.
D) La transcodificación de deltas invierte los nodos causando colisiones de Lamport.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: En sistemas fuertemente consistentes (Teorema CAP: CP), el Consenso Raft rechaza operaciones de escritura si no puede contactar a N/2 + 1 nodos vivos, previniendo condiciones desastrosas de "Split Brain" por bifurcación.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 24
Enunciado: Al modelar esquemas DDBMS modernos, ¿qué límite transaccional subyacente distancia el concepto funcional de "Partición Lógica / Fragmento" del concepto arquitectónico físico de "Tablet"?
Opciones:
A) El fragmento maneja concurrencia paralela, mientras el Tablet clona el offset WAL.
B) El fragmento almacena punteros de red locales, pero el Tablet aísla el caché Raft.
C) El fragmento es un esquema DDL abstracto, pero el Tablet es el archivo subyacente.
D) El fragmento rechaza transacciones ACID puras, pero el Tablet procesa commits LWW.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: Las particiones/fragmentos son construcciones formales lógicas del álgebra relacional controladas por DDL (ej. vehiculos_frag0). Los tablets son las particiones subyacentes de hardware y replicación administradas automáticamente por el DDBMS para consenso Raft.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 25
Enunciado: En implementaciones de integración Active-Active bidireccional heterogéneas, ¿qué principio teórico subyacente fundamenta la aparición sistémica del colapso de red denominado "Efecto Ping-Pong"?
Opciones:
A) Inversión severa de prioridades por Deadlock transaccional distribuido asimétrico.
B) Disparo recursivo incontrolado por incapacidad de identificar el origen del delta.
C) Latencia de colisión entre hilos asíncronos que mutan los registros concurrentemente.
D) Pérdida progresiva de integridad relacional al violar transacciones bloqueantes 2PC.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Sin marcas de procedencia, un nodo origen (A) inyecta tuplas al nodo (B), y el trigger lógico de (B) intercepta este cambio remoto, procesándolo como si fuera un DML local nuevo y rebotándolo erróneamente a (A), destruyendo la Idempotencia.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 26
Enunciado: Relacione la limitación estructural o patrón de diseño de integración DDBMS asimétrica con su vector de resolución ingenieril. 1) Bloqueo recursivo incontrolado. 2) Carencia funcional estricta de entorno FDW inverso. 3) Liberación prioritaria para mitigar Deadlocks paralelos. 4) Procesamiento determinista secuencial asíncrono. Elementos: X) Patrón Outbox de Cola Transaccional Intermedia. Y) Bandera binaria centralizada de Semáforo. Z) Ejecución de bloque de contingencia de fallos EXCEPTION. W) Iterador sistémico de registros lógicos.
Opciones:
A) 1-X, 2-Y, 3-W, 4-Z
B) 1-Z, 2-W, 3-Y, 4-X
C) 1-Y, 2-X, 3-Z, 4-W
D) 1-Y, 2-Z, 3-X, 4-W
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: El flag semáforo detiene loops (Y). MySQL emula su deficiencia de comunicación usando Outbox/Bandeja de red (X). Los bloqueos fallidos previenen desastres soltando banderas en EXCEPTION (Z) y la asimilación asíncrona ordena cursores lógicos (W).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 27
Enunciado: Indique el identificador exacto de motor de almacenamiento embebido nativamente en MySQL, diseñado originalmente para acoplar servidores vinculados pero suplido en la práctica por enfoques de cola asíncrona ("Outbox").
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: FEDERATED
Explicación: El motor FEDERATED es la solución histórica de MySQL para linked-servers, pero su alta deficiencia transaccional comparada con postgres_fdw hace imperativo enrutar las integraciones hacia esquemas Outbox.

[TIPO: ORDENAMIENTO]
Pregunta ID: 28
Enunciado: Ordene estricta y cronológicamente la máquina de estados del Patrón de Semáforo Distribuido cuando un bloque DML fluye del motor anfitrión PostgreSQL hacia el esclavo heterogéneo MySQL. I: Liberación sistémica regresando la variable asíncrona a valor libre 0. II: Evaluación transaccional del estado de bandera remota (v_flag). III: Mutación del semáforo a estado restrictivo de barrera (candado). IV: Materialización absoluta de la tupla DML foránea aplicando el plugin FDW.
Opciones:
A) II -> III -> IV -> I
B) IV -> II -> III -> I
C) II -> IV -> I -> III
D) III -> II -> IV -> I
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: La secuencia ineludible de exclusión mutua: Consulta remota de estado de candado (II), captura del recurso cambiando la bandera (III), ejecución asíncrona sin rebote lógico (IV) y restitución de integridad (I). Alterar el orden propiciará violaciones de carrera.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 29
Enunciado: Al estudiar arquitecturas de replicación heterogénea (PG-MySQL), si el motor anfitrión colapsa o pierde red a mitad de la validación del patrón "Outbox", ¿qué implicación de los sistemas paralelos distribuidos se manifiesta explícitamente?
Opciones:
A) Eliminación heurística forzada de la réplica por el recolector de kernel inactivo.
B) Ruptura silenciosa del principio de Consistencia Transaccional (ACID fallido local).
C) Activación de interbloqueos cruzados (Deadlocks) forzando el reseteo por el Raft.
D) Corrupción binaria general aniquilando las directrices de Completitud relacional.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Ante la falta de un Transaction Coordinator de commit de dos fases (2PC Protocol), el colapso a medio flujo rompe la Atomicidad local del "Outbox", resultando en Stale Data temporal y pérdida de Consistencia absoluta entre los dos motores.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 30
Enunciado: Al incrustar PostgreSQL dentro del subsistema virtualizado WSL2 y enlazar la base a la nube de red local (para conexiones desde un MySQL host nativo), ¿cuál es el comportamiento imperativo de topología de protocolos que asume Windows?
Opciones:
A) Restringe la ruta asíncrona a un bucle estático limitando lecturas distribuidas puras.
B) Ejecuta un rol de router transparente enrutando del bus local 172.x hacia la red LAN.
C) Cifra hipervisorialmente los túneles locales anulando escrituras lógicas delegadas.
D) Compila librerías estáticas delegando la capa OSI al motor de disco virtual SSD subyacente.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: WSL2 despliega un entorno Linux NAT en la subred 172.x. Windows asume el rol de router Bridge transparente interceptando el socket TCP 5432 del Host perimetral para encapsular y retransmitir los frames hacia el entorno virtual subyacente.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 1
Enunciado: En el Algoritmo de Corte (Fragmentación Vertical), ¿cuál es el término técnico o variable formal que cuantifica analíticamente a las consultas conflictivas que requieren datos simultáneos de ambos nodos de la partición, penalizando el sistema?

Respuesta Correcta: CAOS MIXTO
Explicación: El Caos Mixto (representado matricialmente como PM) es la estocástica del tráfico cruzado. Según la teoría de bases de datos distribuidas y la Localidad de Referencia, estas consultas violan el principio de aislamiento operativo, obligando al sistema a ejecutar un JOIN distribuido a través de la red, lo cual es altamente costoso.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 2
Enunciado: Al aplicar el algoritmo BEA para fragmentación vertical, ¿cómo calcula el sistema matemáticamente la función de enlace (Bond) que define la afinidad de acceso transaccional estricta entre dos columnas de una relación universal?

Opciones:
A) Multiplica fila a fila las frecuencias de las columnas coincidentes sumando el total de sus productos relacionales.
B) Extrae los logaritmos naturales base de frecuencias puras para asegurar la estabilización estructural por clúster.
C) Ejecuta un producto cartesiano descentralizado ponderado entre todos los fragmentos del disco duro de la red LAN.
D) Procesa la latencia asintótica dividiendo la fuerza neta transaccional superior contra la fluctuación de los buses.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: A
Explicación: La regla formal algorítmica del Bond Energy Algorithm (BEA) dictamina que la atracción matricial se calcula multiplicando escalarmente el primer elemento de la columna X por el de la columna Y, el segundo por el segundo, sumando el resultado total. Esto agrupa clústeres maximizando la localidad; B, C y D incluyen operaciones (logaritmos, productos cartesianos) que violan las reglas del álgebra matricial aplicada.

[TIPO: ORDENAMIENTO]
Pregunta ID: 3
Enunciado: La fragmentación vertical mediante enfoque analítico Top-Down exige una canalización inmutable. Ordene el pipeline algebraico estricto donde la salida matemática de una fase debe alimentar obligatoriamente como input directo a la fase posterior.

Opciones:
1. Consolidar el sumatorio simétrico de los cruces de frecuencias para la construcción de la Matriz de Afinidad.
2. Recolectar estadísticas transaccionales binarias operativas para estructurar la Matriz de Uso de Atributos.
3. Cuantificar el Balance de Fuerzas evaluando penalizaciones de tráfico cruzado usando una tijera algorítmica.
4. Aplicar la función de enlace Bond reordenando columnas para generar la Matriz de Afinidad Clúster global.

Respuesta Correcta: 2, 1, 4, 3
Explicación: El teorema de diseño relacional secuencial establece: (2) Matriz de Uso define las ocurrencias; (1) Matriz de Afinidad cuantifica simetrías conjuntas; (4) Clúster BEA agrupa adyacentemente por alta energía; y (3) Algoritmo de Corte decide el seccionamiento (Evaluación CM). Un orden distinto quiebra las dependencias matemáticas transitivas.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 4
Enunciado: En el modelo analítico del particionamiento distribuido, la fórmula de contribución se define rígidamente como CM = (CT * CB) - PM². ¿Por qué la teoría relacional penaliza algebraicamente la variable PM elevándola a una potencia cuadrática?

Opciones:
A) Porque el tráfico mixto distribuido fuerza a resolver funciones JOIN de red consumiendo hardware de modo logarítmico.
B) Porque la transferencia de bloques serializados a través de TCP consume exponencialmente más ciclos y bus que la RAM.
C) Porque el teorema de particionamiento ACID exige que las transacciones incompletas sumen asimétricamente un error.
D) Porque el algoritmo matemático estructurado BEA multiplica particiones de nodos descentralizados causando contención.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: B
Explicación: La axiomática de costos de Bases de Datos Distribuidas establece que las operaciones que quiebran la barrera de partición (Caos Mixto PM) fuerzan un JOIN distribuido en red (TCP/IP). Este intercambio de tuplas es asintóticamente (exponencialmente) más pesado (RAM, ancho de banda, CPU) que un escaneo de disco local. A, C y D fallan porque usan lógicas y teoremas erróneos como excusa.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 5
Enunciado: Empareje la abstracción matricial del modelo de diseño algebraico con la función teórica exacta que materializa dentro de la canalización analítica de particionamiento (Top-Down).

Opciones:
1. Matriz de Uso de Atributos
2. Matriz de Afinidad Original
3. Matriz de Afinidad Clúster
4. Métrica de Balance de Red
A) Mapea de manera estrictamente binaria la interacción algorítmica entre una transacción global y un solo atributo.
B) Cuantifica la simetría acumulada y frecuente con la que el motor solicita un par de columnas simultáneamente.
C) Representa las columnas matemáticas reordenadas adyacentemente tras maximizar integralmente la energía de enlace.
D) Mide la ganancia o penalidad neta final resultante de trazar geométricamente un corte divisorio de disco local.

Respuesta Correcta: 1-A, 2-B, 3-C, 4-D
Explicación: (1-A) Uso recoge los 1 y 0 primarios. (2-B) Afinidad acumula pares basándose en el uso. (3-C) Clúster reordena las columnas según el BEA (Bond). (4-D) El balance (CM) finaliza dictaminando la viabilidad del particionamiento calculando CT y CB.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 6
Enunciado: Si un optimizador de bases de datos calcula la función de enlace Bond cruzando dos atributos contra una "columna fantasma" (vacía), ¿cuál es el producto algorítmico teóricamente inyectado para evaluar las esquinas de la partición?

Opciones:
A) Transfiere la energía semántica asintótica en un espectro binario invertido para salvaguardar nodos lógicos.
B) El cálculo algorítmico resulta inherentemente en cero puesto que la atracción cruzada transaccional no existe.
C) Provoca un interbloqueo matemático obligando al orquestador a expulsar la tabla fragmentada del catálogo total.
D) Penaliza linealmente el costo asumiendo que los datos irrelevantes migran entre anillos de subred saturando todo.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: B
Explicación: Según el fundamento matemático del Algoritmo BEA, bond(Atributo, Columna Vacía) es forzosamente 0, ya que una de las matrices vectoriales estará llena de ceros (anulando el producto escalar). Esto sirve como tope estructural para calcular las inserciones "opción izquierda" u "opción derecha" extremas sin romper el pipeline matricial.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 7
Enunciado: Identifique el mecanismo lógico-algorítmico interno del motor SGBD que descarta y omite asintóticamente las particiones físicas irrelevantes del disco al evaluar las imposibilidades de las cláusulas WHERE durante un plan distribuido.

Respuesta Correcta: PARTITION PRUNING
Explicación: El "Partition pruning" (poda de particiones) es la técnica del optimizador del motor basada en las reglas matemáticas formales de disyunción. Si el motor verifica que la restricción es ajena a la consulta lógica, descarta escanear el sub-esquema, mitigando el I/O intensivo.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 8
Enunciado: En bases de datos distribuidas con fragmentación derivada, una entidad débil `Pedidos` hereda su distribución de la entidad fuerte `Clientes`. ¿Qué trade-off u optimización rige axiomáticamente esta arquitectura particionada local?

Opciones:
A) Fuerza la serialización redundante de esquemas lógicos para minimizar la degradación del protocolo de Consenso.
B) Garantiza asintóticamente la persistencia de datos sacrificando el encriptamiento de las tuplas en el nodo origen.
C) Destruye la coherencia ACID fragmentando tuplas huérfanas sin reconocer las dependencias foráneas distribuidas.
D) Co-localiza tuplas relacionadas lógicamente en un solo disco previniendo los abrumadores y lentos JOINs de red.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: D
Explicación: El axioma de la Fragmentación Horizontal Derivada es co-localizar la información dependiente. Al forzar que el hijo radique en el mismo volumen de almacenamiento geográfico que el padre, las lecturas combinadas (JOINs) transcurren internamente sin accionar la red (Foreign Data Wrapper), disminuyendo exponencialmente la latencia (Predicate Push-Down interno).

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 9
Enunciado: Empareje el componente estructural relacional abstracto del patrón Foreign Data Wrapper (FDW) con su función metodológica inmutable operada a nivel de diccionario de datos distribuidos.

Opciones:
1. FDW Extension
2. Foreign Server
3. User Mapping
4. Foreign Table
A) Habilita y recompila los binarios lógicos del núcleo del motor para comprender el protocolo de federación de bases.
B) Inyecta la resolución topológica DNS y el socket de hardware determinando las coordenadas de red destino exactas.
C) Desacopla la matriz de autenticación perimetral asimétrica inyectando las credenciales secretas del nodo esclavo.
D) Abstrae estructuralmente la sintaxis DDL proyectando una interfaz espejo sin ocupar bloques magnéticos internos.

Respuesta Correcta: 1-A, 2-B, 3-C, 4-D
Explicación: El patrón de capa Wrapper requiere activar el intérprete lógico (Extension/A), luego anclar la topología de la capa de red (Server/B), luego delegar las credenciales (User Mapping/C), y finalmente proyectar la representación de las tuplas para el optimizador (Foreign Table/D).

[TIPO: ORDENAMIENTO]
Pregunta ID: 10
Enunciado: Para lograr la transparencia de red unificando tablas foráneas a través de un puente FDW, el catálogo del SGBD exige una instanciación jerárquica estricta. Ordene el ciclo de aprovisionamiento de metadatos distribuidos.

Opciones:
1. Invocar el intérprete algorítmico insertando las librerías dinámicas del protocolo distribuido al núcleo anfitrión.
2. Definir las coordenadas matemáticas de enlace (Host/Puerto) instanciando al servidor esclavo en el diccionario.
3. Declarar el contexto de seguridad asimétrico acoplando credenciales mediante enrutamientos a la tabla de accesos.
4. Materializar una interfaz relacional sin almacenamiento (Espejo) importando proyecciones lógicas de los esquemas.

Respuesta Correcta: 1, 2, 3, 4
Explicación: Se deben proveer las dependencias de abajo hacia arriba: (1) Habilitar binario (Extension); (2) Definir capa física (Server); (3) Definir capa seguridad dependiente del Server (User Mapping); (4) Definir capa lógica de presentación de datos (Foreign Table). Alterar esto invoca el error lógico `dependency violation`.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 11
Enunciado: Al instanciar particionamientos nativos (Horizontal Primaria), el motor gestor obliga axiomáticamente a que la columna pivote particionada se aloje dentro de la Primary Key global. ¿Qué colapso estructural previene esta rigidez?

Opciones:
A) Bloquea la concurrencia agresiva asíncrona mitigando el retardo algorítmico provocado por latencia de relojes LSN.
B) Impide que sub-esquemas de discos apartados dupliquen secuencias colisionando identificadores universales totales.
C) Evade el estrangulamiento de los protocolos criptográficos delegando las llaves simétricas hacia nodos dependientes.
D) Preserva el teorema de independencia funcional transitiva forzando la normalización de tuplas al nivel Boyce-Codd.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: B
Explicación: Si el atributo particionado no estuviese incluido en la Llave Primaria, los índices B-Tree de cada partición física actuarían aislados, permitiendo inserciones de claves `ID=1` en múltiples discos de forma legal (localmente). Esta redundancia destruiría el Teorema de Integridad de Entidad (Unicidad) al reconstruir vistas.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 12
Enunciado: Cuando un motor anfitrión proyecta una reconstrucción (UNION ALL distribuida) aplicando predicados de filtrado complejos (WHERE), ¿qué regla algorítmica aplica estrictamente para eludir cuellos de botella en la red?

Opciones:
A) Consenso Paxos: Valida la integridad concurrente mediante coordinadores de transacciones en los clústeres esclavos.
B) Bloqueo Dos Fases: Congela las tablas espejo en RAM forzando envíos asincrónicos para preservar aislamiento ACID.
C) Snapshot Isolation: Crea replicaciones físicas instantáneas transmitiendo bloques binarios en caché para consultar.
D) Predicate Push-Down: Transfiere la cláusula relacional restrictiva obligando al esclavo a computar filtrados físicos.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: D
Explicación: El "Predicate Push-Down" (Delegación de predicados) en FDW transfiere la inteligencia de la consulta relacional directamente al núcleo SGBD donde reside físicamente la data. De esta forma, el esclavo consume su propia CPU aplicando restricciones matemáticas en disco, devolviendo únicamente el resultado optimizado hacia la red LAN.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 13
Enunciado: Identifique el protocolo criptográfico asimétrico inquebrantable, mandatado en el archivo gestor `pg_hba.conf`, que valida los desafíos de autenticación blindando la confidencialidad perimetral LAN contra ataques de intermediario.

Respuesta Correcta: SCRAM-SHA-256
Explicación: En PostgreSQL (v14+ / 18), `SCRAM-SHA-256` es el algoritmo criptográfico nativo por desafío-respuesta. Al operar conexiones por FDW o federación en redes compartidas, previene ataques Man-in-The-Middle y robo de credenciales en texto claro (como ocurriría si se usara `trust` o algoritmos obsoletos MD5).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 14
Enunciado: Durante una fragmentación mixta que involucra un particionamiento puramente vertical, la clave primaria se ancla y repite en todos los bloques físicos de la relación separada. ¿Qué postulado teórico demanda esta duplicación ineludible?

Opciones:
A) Mitiga la degradación exponencial del protocolo 2PC (Two-Phase Commit) en los esquemas altamente transaccionales.
B) Permite materializar transacciones cruzadas de metadatos sirviendo como caché optimista de las particiones red.
C) Garantiza el teorema de Reconstrucción de la relación original inyectando obligatoriamente operadores JOIN exactos.
D) Obliga al planificador del motor a clonar árboles B-Tree paralelos suprimiendo el balance de red geolocalizado.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: C
Explicación: La duplicación de la Llave Primaria responde al axioma formal de "Reconstrucción Vertical" expuesto en los teoremas de C.J. Date para particionamientos de columnas. Sin un atributo llave redundante como vector de interconexión algebraico, un `JOIN` natural generaría un producto cartesiano espurio y caótico, corrompiendo la tabla reconstruida.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 15
Enunciado: Empareje la postulación formal de los teoremas axiomáticos de bases distribuidas con la inyección práctica de sus operadores (DDL/DML) aplicados para gobernar las instancias federadas de los laboratorios.

Opciones:
1. Regla Matemática de Completitud (Totalidad)
2. Regla Formal de Disyunción (Intersección Nula)
3. Operador de Reconstrucción Horizontal Absoluta
4. Operador de Reconstrucción Vertical de Tuplas
A) Implementación algorítmica forzosa del conector relacional JOIN sobre identificadores preservados y redundantes.
B) Despliegue de restricciones asertivas CHECK evaluadas implícitamente por el motor sobre flujos I/O entrantes.
C) Integración algebraica ejecutando proyecciones lógicas unificadas bajo el comando UNION ALL heterogéneo global.
D) Validación estricta del catálogo para constatar que todas las tuplas atómicas coexisten en algún sub-nodo perimetral.

Respuesta Correcta: 1-D, 2-B, 3-C, 4-A
Explicación: La teoría abstracta se materializa así: Completitud verifica que nada se pierde (D). Disyunción usa los CHECKs para asegurar conjuntos disjuntos (B). Unir fragmentos horizontales exige UNION (C), mientras unirlos verticalmente exige JOIN lógico (A).

[TIPO: ORDENAMIENTO]
Pregunta ID: 16
Enunciado: Acoplar un nodo transaccional SGBD monolítico para admitir flujos de consultas desde orígenes distribuidos demanda alterar anillos de encapsulamiento sucesivos en estricto rigor algorítmico. Ordene el pipeline perimetral expuesto.

Opciones:
1. Establecer regulaciones en el Sistema Operativo (OS) definiendo apertura portuaria física TCP (Windows Firewall).
2. Modificar descriptores de memoria central (`postgresql.conf`) ordenando la vinculación local de sockets en LAN.
3. Emitir el reinicio o recarga binaria del demonio SGBD obligando la absorción efectiva de los perfiles cargados.
4. Mapear reglas lógicas de control criptográfico de accesos de red autorizando subredes cifradas (`pg_hba.conf`).

Respuesta Correcta: 2, 4, 3, 1
Explicación: Se reconfigura desde el núcleo hacia el perímetro externo del OS: (2) El motor SGBD es forzado a escuchar red externa; (4) El motor SGBD recibe listas de quién tiene derecho a entrar por esa red; (3) Se recarga RAM (reinicio) para aplicar estos metadatos del núcleo SGBD; y (1) Se abre la puerta exterior del SO (Firewall) para que los paquetes físicos logren ingresar al socket TCP activo.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 17
Enunciado: Cuando la bitácora del planificador emite la directiva "Foreign Scan" sobre proyecciones distribuidas, ¿cuál es la implicación o trade-off algorítmico subyacente entre el Coordinador anfitrión y el servidor físico esclavo?

Opciones:
A) Delega computación pre-filtrando datos en disco para optimizar ancho de banda sacrificando CPU del nodo esclavo.
B) Sacrifica tolerancia a fallos absoluta congelando tablas espejo para forzar concurrencia seriada y asíncrona total.
C) Gana compresión volumétrica de metadatos en memoria sacrificando protocolos criptográficos perimetrales nativos.
D) Delega los flujos de bloqueos transaccionales (2PL) priorizando escritura local pero asumiendo colisiones altas.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: A
Explicación: El "Foreign Scan" es una manifestación del Predicate Push-down. Al enviar la operación relacional hacia el nodo secundario (esclavo), el Coordinador (anfitrión) absorbe menos datos por el cable de red (optimizando ancho de banda) intercambiando ese beneficio por obligar al esclavo a consumir ciclos de reloj (CPU) ejecutando evaluaciones algorítmicas locales en su propio disco.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 18
Enunciado: Al ensamblar una reconstrucción lógica global aplicando fragmentación mixta, los desarrolladores despliegan sentencias de tipo "Casts" NULOS (ej. `NULL::TEXT`). ¿Qué colapso teórico se omite materializar con este artificio?

Opciones:
A) Detiene los algoritmos de codificación del Write-Ahead Log asimétrico para no perder metadatos al cerrar nodos.
B) Previene rupturas asintóticas del álgebra de conjuntos UNION porque todas las proyecciones requieren grados idénticos.
C) Absorbe las iteraciones del protocolo PAXOS estabilizando el tráfico de red de tuplas huérfanas desincronizadas.
D) Omite verificaciones de consistencia de integridad transitiva permitiendo inyectar atributos foráneos abstractos.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: B
Explicación: La regla formal del operador matemático conjuntista de `UNION/UNION ALL` dictamina que las sub-consultas (relaciones) que se unen verticalmente deben poseer asimétricamente el mismo grado o aridad relacional (idéntico número y tipos de columnas). Rellenar atributos verticalmente particionados con `NULL::TIPO` emula este grado universal, mitigando errores del intérprete lógico de SGBD.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 19
Enunciado: Especifique la cláusula matemática inyectada de forma subyacente en el catalogador DDL de un nodo que valida axiomáticamente el "Esquema de Ubicación", repudiando físicamente las escrituras de tuplas ajenas al ámbito asignado.

Respuesta Correcta: CHECK
Explicación: Los esquemas de ubicación locales o particionamientos utilizan la restricción `CHECK (criterio_regional)`. Esto incrusta la lógica de la topología distribuida directamente a nivel del motor relacional, forzando un rechazo del I/O transaccional si un coordinador u operario intenta introducir filas geográficamente incorrectas.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 20
Enunciado: Según el manual formal de dependencias de catálogo, ¿por qué es metodológicamente mandatorio ejecutar `REASSIGN OWNED` seguido inmediatamente de `DROP OWNED CASCADE` previo a emitir la destrucción global de un rol SGBD distribuido?

Opciones:
A) Porque el colector distribuido transaccional corromperá el aislamiento SNAPSHOT si las credenciales de red persisten.
B) Porque los atributos de pertenencia ligan a los objetos impidiendo la purga del usuario sin romper integridad referencial.
C) Porque los servidores esclavos congelarían las rutinas FDW mediante exclusión mutua de bloqueos 2PL asíncronos en RAM.
D) Porque el estándar ACID asimétrico obliga a re-evaluar la consistencia particionada antes de mitigar los usuarios locales.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: B
Explicación: En arquitecturas PostgreSQL (ANSI Catalog Dependency), los Roles operan globalmente en todo el clúster (Cluster-wide), pero las pertenencias sobre tablas/vistas son intrínsecamente locales a la BDD. Destruir un rol genera un colapso semántico de orfandad referencial si este es propietario de metadatos, por lo que el SGBD lo deniega. `REASSIGN` y `DROP` transfieren y disuelven esos enlaces.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 21
Enunciado: Empareje la declaración de capa DCL (Data Control Language) con el estrato del modelo perimetral que vulnera intencionalmente para acoplar la lectura transparente de FDW en arquitecturas distribuidas.

Opciones:
1. GRANT USAGE ON SCHEMA
2. GRANT SELECT ON ALL TABLES
3. GRANT USAGE ON FOREIGN SERVER
4. ALTER DEFAULT PRIVILEGES
A) Supera la barrera semántica superior autorizando al operario a vislumbrar y transitar la matriz jerárquica subyacente de objetos.
B) Faculta el paso y consumo explícito de las tuplas dinámicas contenidas en las proyecciones relacionales presentes.
C) Inyecta la herencia paramétrica lógica para que los objetos de red generados en iteraciones futuras conserven visibilidad.
D) Interviene y aprueba la apertura de sockets delegados autorizando ruteos mediante configuraciones de mapeos preexistentes.

Respuesta Correcta: 1-A, 2-B, 3-D, 4-C
Explicación: (1-A) Esquema como namespace lógico (transitar el cajón). (2-B) Concesión real de lectura de filas/tuplas. (3-D) Otorga derechos para explotar el objeto Server remoto (Proxy TCP). (4-C) Herencia de privilegios sobre proyecciones (`FOREIGN TABLE`) aún no creadas en el espacio de tiempo.

[TIPO: ORDENAMIENTO]
Pregunta ID: 22
Enunciado: El proceso destructivo controlado (Saneamiento) para reconstruir topologías FDW sin generar orfandad referencial requiere la inyección serial de sentencias operativas DDL. Ordene este flujo irrompible.

Opciones:
1. Depurar el ecosistema disolviendo y purgando contenedores de gran escalado (Bases de Datos locales) previas (DROP DATABASE).
2. Transferir obligatoriamente el puente patrimonial de los artefactos persistentes residuales transfiriéndolos (REASSIGN OWNED).
3. Podar en cascada las delegaciones pasivas y herencias asimétricas inyectadas al perfil objetivo subyacente (DROP OWNED).
4. Evaporar el descriptor central DCL e inicializar un contexto nuevo sin ataduras de los diccionarios anteriores (DROP ROLE / CREATE ROLE).

Respuesta Correcta: 1, 2, 3, 4
Explicación: La destrucción en PostgreSQL demanda podar primero macro-objetos que cargan en cascada miles de elementos locales. Luego se transfiere el ownership del resto marginal (REASSIGN). Luego se disuelven (DROP OWNED) para erradicar las delegaciones. Ya huérfano y aislado de referencias en catálogo, el Rol global puede finalmente suprimirse (DROP).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 23
Enunciado: Un ingeniero de sistemas inyecta DCL con sentencias `GRANT SELECT ON ALL TABLES`, pero suprime o falla en desplegar `ALTER DEFAULT PRIVILEGES` durante un pipeline de despliegue de federaciones FDW. ¿Cuál será la falla estructural final del flujo?

Opciones:
A) Las autenticaciones simétricas (SCRAM-SHA) declinarán las rutinas obligando al motor SGBD a desconectar los buses de la red LAN.
B) El enrutador nativo FDW fragmentará artificialmente los objetos virtuales consumiendo memoria RAM del nodo remoto innecesariamente.
C) Las relaciones o tablas espejos importadas subsecuentemente nacerán carentes de asignación lectora, siendo denegadas e inútiles.
D) La arquitectura CAP desencadenará un rollback asíncrono para revertir inserciones foráneas que quiebren la integridad transitiva.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: C
Explicación: La instrucción `GRANT SELECT` tradicional es atómica y no retroactiva, modificando únicamente la matriz de accesos de los objetos que ya coexisten en el diccionario. Si luego se ejecutan imports lógicos (`CREATE FOREIGN TABLE`), estas proyecciones nacerán estériles (sin privilegios lectores), arrojando el célebre error "Permission denied" en el cliente o coordinador.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 24
Enunciado: Durante un proceso inter-nodos asimétrico, el superusuario `postgres` expide sentencias SQL contra una tabla foránea que tiene un mapeo seguro delegado exclusivamente para el rol transaccional `admin_a`. ¿Qué barrera algorítmica detiene su ejecución?

Opciones:
A) El gestor asimila la falta devolviendo nulos, enmascarando estocásticamente las tuplas para defender el catálogo principal maestro.
B) El optimizador falla indicando ausencia de un contexto Mapeado para la credencial ejecutora, rehusándose a suplantar identidades.
C) El puente proxy sobreescribe forzosamente los descriptores asumiendo elevación de privilegios para cruzar bloqueos concurrentes.
D) El demonio suspende el kernel relacional disparando protocolos 2PC (Two-Phase Commit) para impedir interbloqueos de la subred.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: B
Explicación: La abstracción de red FDW usa mapeos de autenticación biunívocos por Rol local (USER MAPPING). Aunque `postgres` sea superusuario local, FDW no adivina credenciales ni suplanta mapeos ajenos (`admin_a -> admin_b`); si `postgres` lanza un query remoto y carece de su propia ficha relacional explícita de USER MAPPING, el motor rechaza construir el socket de enlace (Error 42704).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 25
Enunciado: Escriba el identificador técnico del mecanismo gestor del motor anfitrión estipulado (`max_...`) que funge como anclaje físico sobre disco previniendo activamente el borrado residual asíncrono del historial WAL de los nodos suscriptores.

Respuesta Correcta: REPLICATION SLOTS
Explicación: Los *Replication slots* (Ranuras de Replicación) dictaminan un mecanismo estricto donde el motor anfitrión rastrea internamente la posición de lectura (LSN) del suscriptor. Este objeto detiene el proceso Recolector de Basura (VACUUM/WAL recycle), garantizando que un nodo lento retenga el flujo crudo para prevenir la desincronización irremediable (Consistencia ACID).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 26
Enunciado: De acuerdo a la topología distribuida transaccional, ¿cuál es el rasgo definitorio teórico que abstrae la arquitectura de Replicación Lógica PostgreSQL (Pub/Sub) del espectro de una Replicación Binaria (Física de Streaming Asíncrona)?

Opciones:
A) El motor decodifica secuencialmente la bitácora I/O transfiriendo operaciones algebraicas DML por tabla y omitiendo bloques raw.
B) El motor suspende los algoritmos relacionales paralelos inyectando instantáneas congeladas en la caché para replicar sin disco.
C) El gestor comprime la RAM forzando transacciones determinísticas simétricas de lectura prioritaria perdiendo flexibilidad en red.
D) El optimizador enruta páginas magnéticas brutas a través de un puente FDW evadiendo procesos lógicos internos consumiendo CPU.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: A
Explicación: La replicación lógica procesa ("Decodifica") el Write-Ahead Log extrayendo reconstrucciones puestas en sentencias del DML de bases relacionales (`INSERT`, `UPDATE`), habilitando réplicas selectivas ("per-table basis"). La física serializa los bloques binarios del disco (pages), limitando la réplica a un esquema integral monolítico idéntico. A refuta sólidamente las afirmaciones de las demás.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 27
Enunciado: Empareje la abstracción estructural y relacional del mecanismo transaccional de replicación unidireccional (Publicación-Suscripción) con la estocástica operativa de su componente interno.

Opciones:
1. Bitácora de Escritura Previa (WAL)
2. Decodificador Lógico (pgoutput)
3. Objeto Creador PUBLICATION
4. Objeto Suscriptor SUBSCRIPTION
A) Abstracción consumidora que gestiona la captura y acoplamiento matemático inyectando sentencias desde el worker asíncrono en destino.
B) Contenedor de persistencia transaccional primaria base que almacena los cambios físicos del disco para resguardar durabilidad ACID.
C) Algoritmo de traducción acoplado al kernel que desensambla secuencias magnéticas transformándolas en eventos de álgebra DML entendibles.
D) Interfaz restrictiva de exposición que dictamina qué entidades relacionales se proyectan hacia el anillo del clúster de interconexión.

Respuesta Correcta: 1-B, 2-C, 3-D, 4-A
Explicación: (1-B) WAL como ancla de Durabilidad. (2-C) pgoutput decodifica el raw WAL a SQL. (3-D) La publicación delimita el "perímetro" de exposición DDL. (4-A) La suscripción es el hilo "Worker" remoto que extrae e inserta.

[TIPO: ORDENAMIENTO]
Pregunta ID: 28
Enunciado: La inserción y estabilización arquitectónica de una topología de replicación unidireccional tolerante a rupturas obedece una estricta rigidez operacional DDL. Ordene algorítmicamente el ciclo de despliegue lógico Pub/Sub.

Opciones:
1. Habilitar la codificación semántica extendida en el nivel de núcleo transaccional del anfitrión (`wal_level`) y acoplar el socket TCP de escucha de red.
2. Construir la estructura geométrica espejo DDL de forma idéntica inyectando las tablas huérfanas o vacías en la Base de Datos esclava o secundaría.
3. Declarar la interfaz perimetral de exposición relacional invocando el contenedor de la publicación maestro determinando su alcance local (CREATE PUBLICATION).
4. Configurar el túnel receptor en el suscriptor forzando el copiado inicial masivo y abriendo el worker (CREATE SUBSCRIPTION).

Respuesta Correcta: 1, 2, 3, 4
Explicación: Teorema de encadenamiento de Pub/Sub: Primero se altera el motor nativo del publicador para emitir lógica (`wal_level`). Segundo, como la replicación lógica no transporta esquema DDL (solo DML), las tablas destino se clonan idénticas de antemano vacías. Tercero, se publica el canal. Cuarto y último, el esclavo suscribe, acoplando automáticamente el pull inicial.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 29
Enunciado: ¿Qué trade-off u onda residual asume matemáticamente el Nodo Maestro coordinador en un sistema distribuido cuando su parámetro perimetral interno muta desde `replica` hacia el estado transaccional amplificado de `wal_level = logical`?

Opciones:
A) Restringe la transaccionalidad ACID obligando al kernel SGBD a desconectar asíncronamente cachés de escritura provocando fallos geográficos.
B) Disminuye la eficiencia volumétrica de persistencia puesto que inyecta mayor overhead de contexto y metadatos explícitos de los registros DML.
C) Paraliza el particionamiento mixto destruyendo las delegaciones encriptadas para asegurar una replicación binaria síncrona determinística pura.
D) Expande el rango asintótico de los sockets forzando concurrencias optimistas y clonando índices B-Tree indiscriminadamente en la red LAN.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: B
Explicación: Cambiar a `wal_level = logical` aumenta agresivamente el tamaño del Write-Ahead Log (overhead en I/O de disco) pues inyecta atributos internos extras, claves y referencias para que el decodificador de `pgoutput` re-genere posteriormente SQL DML inteligible, penalizando en parte el consumo físico local en favor de la flexibilidad distribuida.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 30
Enunciado: Analizando topologías con flujos asíncronos de Replicación Lógica (Pub/Sub), ¿qué límite estructural y funcional estricto ostenta este modelo matemático si los ingenieros despliegan alteraciones persistentes sobre los esquemas (ej. `ALTER TABLE ADD COLUMN`)?

Opciones:
A) Los clústeres bloquean el 2PC y conmutan al modelo asincrónico perdiendo las bitácoras I/O en cada latido de la red tolerante.
B) El worker procesa la instrucción transfiriendo el catálogo de vistas completo sobre escribiendo todas las métricas en caché asimétrico.
C) La base transaccional esclava desvincula al optimizador forzando la exclusión mutua de los clústeres a nivel geolocalizado paralelo.
D) La replicación captura lógicamente las operaciones DML puras pero es sorda al DDL; si ambos nodos no sincronizan estructura, el worker quiebra e interrumpe el flujo continuo de datos.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: D
Explicación: A diferencia de la replicación física completa o mecanismos DDL Trigger-based, la replicación lógica canónica en PG18 procesa datos transaccionales, pero repudia el catálogo (DDL). Al no transportar cambios de tabla, si el maestro añade columna, el suscriptor (al ser ciego estructuralmente) sufre una asimetría relacional al momento del volcado del INSERT, deteniendo el worker `logical replication`.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 31
Enunciado: En plataformas monolíticas legadas donde el gestor (SGBD) es carente de módulos nativos de enrutadores FDW o particionamientos dinámicos, ¿qué capa DDL se inyecta lógicamente para emular el Esquema Externo (Transparencia) ANSI/SPARC de una base dispersa?

Respuesta Correcta: VISTA
Explicación: La simulación de bases distribuidas en motores legacy (como la práctica 1) exige fraccionar físicamente las relaciones (tablas distintas). Para restituir el "Nivel Externo" que exige la arquitectura ANSI y engañar al programador (Transparencia de Fragmentación), se despliega de manera forzosa una Vista (VIEW) ensamblando la superposición unificada (JOIN).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 32
Enunciado: Al simular rigurosamente una fragmentación vertical dividiendo forzosamente entidades compactas en tablas físicas aisladas (ej. Lab 1), ¿qué sacrificio transaccional (Trade-off) y axiomático acepta ineludiblemente el diseñador relacional?

Opciones:
A) Invalida las rutinas hash paralizando la abstracción lógica obligando transferencias en un espectro binario asimétrico de metadatos.
B) Duplica forzosamente el atributo llavín saturando bloques de disco y carga a la CPU procesando álgebra combinatoria (JOIN) superflua en cada reconstrucción integral solicitada.
C) Transgrede la normalización BCNF creando interbloqueos determinísticos al omitir los protocolos criptográficos asíncronos nativos en la red subyacente.
D) Pierde capacidad de encapsulamiento relacional sacrificando validaciones ACID y migrando la transaccionalidad hacia árboles sintácticos dispersos geográficamente.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: B
Explicación: Simular fragmentación en SGBDs primitivos requiere "tablas clon". Para mantener el teorema de Reconstrucción, es obligatorio duplicar la Primary Key redundante (consumiendo espacio I/O). Además, toda lectura consolidada acciona un JOIN forzado (consumo CPU y caché), una carga computacional masiva que los motores particionados nativamente logran evitar con un planificador distribuido local integrado.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 33
Enunciado: Basándose en el análisis del diseño lógico simulado y empírico para fraccionar verticalmente una estructura de 3 niveles (`VentasVehiculos`), empareje el atributo semántico con su contenedor físico respetando los axiomas de afinidad operativa.

Opciones:
1. Clave relacional VentaID
2. Atributo Sensible ClienteNombre
3. Atributo Descriptivo VehiculoModelo
4. Atributo Financiero VentaMonto
A) Se inyecta redundantemente en todas las particiones como el eje matemático primario asegurando la Regla de Reconstrucción.
B) Se adhiere y emplaza de manera íntegra y mutuamente excluyente al esquema proyectado para variables demográficas (Cliente).
C) Reside estructuralmente anclado a la partición de caracterización de la transacción subordinada material y descriptiva (Detalle).
D) Coexiste paramétricamente junto con las columnas del vehículo anclando variables monetarias de la venta en la entidad de Desglose.

Respuesta Correcta: 1-A, 2-B, 3-C, 4-D
Explicación: Según el diseño Top-Down pedagógico, VentaID (A) funge de PK enlazante iterada en ambos cortes. ClienteNombre (B) aisla lectura demográfica. VehiculoModelo (C) y VentaMonto (D) aglutinan afinidad en el Detalle operativo, minimizando lectura pesada donde se demanda al cliente exclusivamente.

[TIPO: ORDENAMIENTO]
Pregunta ID: 34
Enunciado: Orquestar un experimento de particionamiento fragmentario vertical usando aproximaciones "Bottom-Up" de simulación relacional obedece a un pipeline inmutable. Ordene el flujo para abstraer teóricamente esta anomalía arquitectónica monolítica.

Opciones:
1. Efectuar el volcado DML inyectando un pull estructurado estático y controlado de tuplas en las tablas espejos generadas de manera aislada.
2. Auditar axiomáticamente al SGBD validando su carencia interna frente a motores distribuibles que asimilan y resuelven el álgebra perimetral de red abstracta.
3. Consolidar el paradigma simulado instanciando sobre los discos una proyección externa que enmascara las bifurcaciones relacionales y opera como fachada única.
4. Codificar la arquitectura atómica generando los sub-esquemas DDL paralelos y soldándolos asimétricamente vía restricciones y llaves (FOREIGN KEY).

Respuesta Correcta: 2, 4, 3, 1
Explicación: El modelo teórico dicta: (2) Diagnosticar incapacidad del gestor de Bases de Datos; (4) Emular estructuras (Tablas) ligadas para reemplazarlo; (3) Restablecer el Nivel Externo ANSI (Crear Vista Unificada); y (1) Sembrar data transaccional (`INSERT`) para auditar la reconstrucción final sin anomalías.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 35
Enunciado: Analíticamente, desde un punto de vista asintótico y de arquitectura interna (Kernel OS), ¿qué optimización intrínseca de hardware dictamina la partición vertical y justifica despedazar tuplas amplias en fragmentos estrechos sobre el bloque de disco duro?

Opciones:
A) Retrasa el envío asíncrono evadiendo que la latencia de protocolos LSN comprometa las métricas de replicación física.
B) Omite lecturas pesadas (I/O) al ignorar atributos o columnas periféricas grasas (Ej. binarios o textos largos) evadiendo inyectarlas a la caché del RAM durante consultas locales.
C) Paraliza el bus de red obligando al optimizador a crear colisiones determinísticas estables que aseguren durabilidad ACID sin compresión magnética asimétrica.
D) Traspasa vectores y particiones hash de exclusión mutua para que el catálogo reciba transacciones encapsuladas síncronas evadiendo interbloqueos estocásticos geográficos en la red LAN.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: B
Explicación: En Teoría de SGBDs (Storage Engines), el motor lee por "Pages" (Bloques completos). Si el registro (tupla) es ancho o "graso", el número de bloques transferidos desde el disco rígido lento a la caché de RAM veloz es gigante. Dividir la tupla achica el disco físico escaneado, mitiga cuellos de botella E/S ("I/O Bottlenecks") y economiza costosos ciclos de memoria, haciendo A, C y D justificaciones falaces e irrelacionadas de red.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 36
Enunciado: Si al estructurar de manera teórica (simulación relacional) particiones fragmentadas dependientes se vulneran los principios inyectando un sub-esquema carente de dependencias referenciales lógicas DDL (Ausencia total de Restricciones `FOREIGN KEY`), ¿qué axioma matemático perimetral distribuido padece degradación estocástica?

Opciones:
A) La norma de encriptamiento asimétrico delegando credenciales de validación cruzada y evadiendo cuellos de red en el puente.
B) El teorema determinístico CAP forzando disponibilidad total pero disolviendo la tolerancia a redes colapsadas o aisladas permanentemente.
C) El postulado lógico formal de Reconstrucción de Entidad, ya que permitiría la asimetría semántica en borrados aniquilando las tuplas del JOIN reconstructor final.
D) La asimetría transitiva del control estocástico del árbol B-Tree del gestor relacional de consultas pre-filtrando índices obsoletos nulos al aire.
E) Ninguna de las opciones anteriores describe el comportamiento axiomático/teórico correcto evaluado en este caso.

Respuesta Correcta: C
Explicación: Sin Dependencias de Integridad Referencial DDL (Las Foreign Keys), el motor no impide borrar `ID=X` en el Fragmento 1 y dejarlo existiendo en el Fragmento 2. Esta anomalía aritmética ("Tuplas Huérfanas") imposibilita recomponer la tabla original, violando directamente el dogma axiomático de C.J. Date: El Teorema de Reconstrucción. Toda junta generará fallos o pérdidas silenciosas de datos.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 1
Enunciado: En sistemas distribuidos analíticos, ¿cómo se define teóricamente la divergencia fundamental entre las métricas de evaluación "Costo Total" y "Tiempo de Respuesta"?
Opciones:
A) El costo suma recursos consumidos; el tiempo evalúa la demora real del usuario.
B) El costo mide latencia de red; el tiempo totaliza ciclos de CPU de servidores.
C) El costo ignora lecturas de disco; el tiempo prioriza las operaciones lógicas.
D) El costo penaliza el paralelismo; el tiempo suma el trabajo de la red global.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: El Principio de Paralelismo en Procesamiento establece que dividir tareas entre múltiples nodos (escalabilidad horizontal) incrementa la suma agregada de recursos o Costo Total (CPU, I/O, red), pero paralelamente reduce el cronómetro de espera o Tiempo de Respuesta. Las demás opciones son falsas matemáticamente; el costo jamás ignora factores físicos (disco/red) y el tiempo no suma trabajo, sino que representa el lapso real hasta la emisión del subgrafo resultante.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 2
Enunciado: Empareje el criterio o métrica de optimización con su axioma lógico de comportamiento en el motor relacional:
1. Criterio de Corrección
2. Criterio de Eficiencia
3. Costo Total Distribuido
4. Estrategia Base (Logística)
I. Agregación métrica del esfuerzo físico completo (CPU, memoria, latencia de red).
II. Postulado físico que exige mover programas diminutos hacia datos masivos.
III. Invariancia matemática y preservación estricta de la semántica original.
IV. Minimización del consumo sistémico aplicando heurísticas de filtrado temprano.
Opciones:
A) 1-I, 2-II, 3-III, 4-IV
B) 1-IV, 2-III, 3-II, 4-I
C) 1-III, 2-IV, 3-I, 4-II
D) 1-II, 2-I, 3-IV, 4-III
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: El Teorema de Equivalencia Algebraica rige el Criterio de Corrección (1-III), exigiendo que las transformaciones mantengan identidad de resultados. La Eficiencia (2-IV) se fundamenta en la reducción de complejidad espacial. El Costo Total (3-I) es una función matemática agregada, y la Logística (4-II) obedece a las asimetrías de transferencia en la red, invalidando cualquier otra combinatoria arquitectónica.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 3
Enunciado: Identifique el concepto teórico (en mayúsculas) que describe la capacidad arquitectónica del modelo relacional para separar la declaración lógica del usuario de la estructura y punteros físicos en disco.
Opciones:
A) TRANSPARENCIA DE RED
B) INDEPENDENCIA FISICA
C) LENGUAJE DECLARATIVO
D) NORMALIZACION ESTRICTA
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: La "INDEPENDENCIA FISICA" es el postulado de Codd que asegura que las mutaciones en las estructuras de almacenamiento subyacentes no alteren las aplicaciones de usuario. A diferencia de las otras opciones, es el término unívoco que sustituyó a los modelos navegacionales procedimentales rígidos, mitigando fallas sistémicas por recompilación.

[TIPO: ORDENAMIENTO]
Pregunta ID: 4
Enunciado: Según el modelo de Logística de Datos en entornos distribuidos, ordene las decisiones algorítmicas secuenciales que ejecuta el "Piloto Automático" para coordinar una petición.
I. Selección del sitio de entrega para reunir y presentar el resultado al usuario.
II. Elección del lugar de procesamiento determinando el servidor maestro (Heavy Lifting).
III. Definición estricta de la ruta de viaje para la movilización paralela de relaciones.
Opciones:
A) III, II, I
B) I, II, III
C) II, III, I
D) III, I, II
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: En el marco de asignación de operadores distribuidos, el sistema debe primero determinar la matriz de costos para fijar el nodo de carga pesada (II). Con base en esto, calcula las transferencias mínimas por la red (III) minimizando el consumo de ancho de banda. Por último, coordina la entrega consolidada hacia el proceso cliente (I). Cualquier otro orden rompería las dependencias de cálculo de costos (Bottom-Up).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 5
Enunciado: ¿Cómo modelan los optimizadores modernos el impacto físico de los componentes de hardware según la teoría de sistemas distribuidos actuales?
Opciones:
A) El procesador minimiza la CPU e ignora la red debido a su velocidad infinita.
B) El software calcula ecuaciones donde la CPU, el disco y la red pesan lo mismo.
C) El modelo híbrido asume que el almacenamiento sólido es más veloz que la RAM.
D) El sistema transfiere tablas enteras para evitar evaluar lecturas secuenciales.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Según la Teoría de Costos Híbridos modernos (vs modelos clásicos de los años 80 que sobre-penalizaban la red), las redes LAN ultrarrápidas equilibran la latencia a tal punto que CPU, I/O y Red se evalúan co-dependientemente. La opción A viola las leyes de latencia física. La opción C es falsa axiomáticamente (RAM es órdenes de magnitud más veloz). La opción D representa una estrategia "ingenua" ineficiente.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 6
Enunciado: Según el modelo de procesamiento distribuido, ¿qué axioma matemático rige la "Estrategia Base" o logística de datos para evitar la saturación de canales?
Opciones:
A) Los datos de mayor volumen deben moverse primero hacia las sentencias lógicas.
B) Los programas pequeños siempre deben moverse hacia donde están datos masivos.
C) La red debe transferir relaciones completas para asegurar consistencia estricta.
D) Las consultas complejas demandan el cruce de tablas en un nodo de mediación.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Basado en el Principio de Minimización de Transferencia de Datos, es infinitamente menos costoso serializar un árbol algebraico (programa ligero) y enviarlo al nodo de almacenamiento que trasladar gigabytes hacia un procesador central. Las opciones A, C y D fomentan el "Desperdicio de Ancho de Banda", vulnerando el teorema de límite de canal (Teorema de Shannon-Hartley implícito en latencia de datos).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 7
Enunciado: En algoritmos aleatorios para optimización, ¿cuál es la propiedad estocástica que distingue de manera categórica al Recocido Simulado de la Mejora Iterativa?
Opciones:
A) Rechaza sistemáticamente planes costosos para buscar mínimos locales aislados.
B) Permite saltos probabilísticos hacia rutas peores para escapar de valles falsos.
C) Evalúa el cien por ciento de permutaciones garantizando hallar el camino óptimo.
D) Transforma el álgebra relacional utilizando heurísticas de selectividad inversa.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: El Recocido Simulado implementa el parámetro "Temperatura" que permite probabilísticamente aceptar un QEP de mayor costo al inicial. Esto supera el "Atrapamiento en Mínimos Locales", fallo intrínseco de algoritmos puramente voraces o iterativos (como enuncia la opción A y D). La opción C describe búsqueda exhaustiva, violando el principio NP-Hard en consultas grandes.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 8
Enunciado: Relacione la arquitectura o momento temporal de decisión con su vulnerabilidad matemática subyacente que limita su escalabilidad.
1. Decisión Centralizada
2. Decisión Distribuida (Autónoma)
3. Optimización Estática
4. Optimización Dinámica
I. Consumo crítico de CPU del servidor en tiempo real (sobrecarga inmediata).
II. Alto riesgo de crear cuellos de botella por tráfico masivo de catálogos.
III. Complejidad por asimetría de información, aunque posee alta resiliencia.
IV. Vulnerabilidad letal a la obsolescencia si las cardinalidades varían.
Opciones:
A) 1-III, 2-I, 3-IV, 4-II
B) 1-IV, 2-III, 3-I, 4-II
C) 1-I, 2-IV, 3-II, 4-III
D) 1-II, 2-III, 3-IV, 4-I
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: D
Explicación: La centralizada colapsa por dependencia de metadatos (Teorema del Punto Único de Falla, 1-II). La distribuida evita colapsos pero fragmenta el catálogo (2-III). La estática se precompila violando el ajuste a desviación estadística futura (4-IV). La dinámica sacrifica Tiempo de Respuesta para evaluar planes on-the-fly (4-I).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 9
Enunciado: Identifique la estructura estadística (en mayúsculas) almacenada en catálogos globales que segmenta la cardinalidad de atributos en rangos no uniformes, permitiendo predicciones algorítmicas de muy alta exactitud.
Opciones:
A) PERFILES DE SEGMENTACION
B) ARBOLES DE DECISION BINARIA
C) FACTORES DE SELECTIVIDAD
D) HISTOGRAMAS DE VALORES
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: D
Explicación: Los "HISTOGRAMAS DE VALORES" refutan matemáticamente la asunción errónea de "distribución uniforme". Proveen la densidad estadística requerida para el cálculo preciso del Factor de Selectividad (SF), justificando su costo de memoria frente a los perfiles planos (opción C y A que son incompletos o incorrectos).

[TIPO: ORDENAMIENTO]
Pregunta ID: 10
Enunciado: Ordene estrictamente los pasos de la técnica algorítmica de filtrado "Semijoin" diseñada para minificar transferencias de red bajo el Modelo Híbrido.
I. El nodo destino descarta tuplas que carezcan de coincidencia (filtrado in-situ).
II. Se efectúa una proyección extrayendo el vector unívoco de la llave de enlace.
III. El nodo origen transmite por red únicamente el subconjunto de vectores aislados.
Opciones:
A) II, III, I
B) III, I, II
C) I, II, III
D) II, I, III
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: La Semireunión R ⋉ S dicta operativamente que primero se evalúa la Proyección (II) πA(S), que reduce el tamaño en O(n) operaciones. Luego ocurre la transmisión de comunicación mínima (III). Finalmente, se utiliza ese vector en R para aplicar la Selección condicional matemática (I). Cualquier otro flujo resultaría en envío de relaciones enteras infractoras del cálculo relacional distribuido.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 11
Enunciado: ¿Cuál es el propósito axiomático de aplicar reglas heurísticas durante la evaluación del espacio de búsqueda en consultas de gran escala?
Opciones:
A) Garantizar matemáticamente la selección de la ruta de menor costo en el clúster.
B) Reestructurar predicados semánticos basándose en el grafo de unión relacional.
C) Eliminar ramas ineficientes de inmediato para evitar saturar el cálculo exacto.
D) Materializar datos temporalmente bloqueando el flujo pipeline en nodos locales.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: Dado que el ordenamiento de cruces (joins) es un problema NP-Hard, el número de permutaciones es del orden de n!. Las heurísticas (ej. selección temprana) podan (pruning) ramas subóptimas eludiendo el cómputo total. Las heurísticas no garantizan el óptimo global (descartando la opción A), ni interactúan con grafos de unión (B), ni imponen bloqueos de flujo (D).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 12
Enunciado: ¿Qué vulnerabilidad teórica asume un motor de bases de datos al emplear exclusivamente un esquema de optimización de tipo "Estático"?
Opciones:
A) Interrumpe el flujo continuo de ejecución al depender de parámetros dinámicos.
B) Consume recursos críticos de procesador mientras el usuario aguarda respuestas.
C) Sufre de obsolescencia letal si las cardinalidades varían de forma imprevista.
D) Obliga al nodo de control a coordinar bloqueos distribuidos en dos fases (2PC).
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: La optimización estática se ejecuta en "Tiempo de Compilación". Si los metadatos estadísticos subyacentes varían (ej. crecimiento abrupto de una tabla), el Plan de Ejecución guardado sufre un Desvío Estructural o obsolescencia estática. Las opciones A y B corresponden al modelo dinámico puro (on-the-fly). La opción D refiere a protocolos de control de transacciones (Consenso), no a optimización relacional.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 13
Enunciado: Según la teoría del Modelo Iterador en ejecución, ¿por qué operadores unarios complejos como "Sort" interrumpen el paralelismo de flujo (pipeline)?
Opciones:
A) Procesan tuplas individualmente y las emiten de inmediato hacia la red global.
B) Obligan a materializar toda la entrada en disco antes de emitir un resultado.
C) Generan productos cartesianos involuntarios al omitir grafos de unión locales.
D) Requieren esquemas de asignación globales para instanciar subconsultas puras.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: En el Pipeline Iterador (Open/Next/Close), operadores "Bloqueantes" sufren de dependencia total de cardinalidad (O(n log n)). No pueden emitir ni la primera fila sin haber evaluado absolutamente todas las de la relación (ej. Ordenamiento). Esto destroza el comportamiento asíncrono. La opción A describe un operador puro en pipeline (ej. Selección). Las opciones C y D confunden capas analíticas con motor de ejecución.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 14
Enunciado: Empareje la Capa Estructural de Procesamiento Distribuido con el Esquema o Directorio del cual extrae metadatos topológicos:
1. Descomposición de Consultas
2. Localización de Datos
3. Optimización Global
4. Ejecución Distribuida
I. Esquema de Fragmentos (Mapeo de tuplas a pedazos horizontales/verticales).
II. Esquemas Locales (Estructuras dependientes del DBMS de cada servidor).
III. Esquema de Asignación (Mapeo topológico de fragmentos a nodos de la red).
IV. Esquema Global (Diccionario de tipos, atributos y relaciones conceptuales).
Opciones:
A) 1-IV, 2-I, 3-III, 4-II
B) 1-I, 2-IV, 3-II, 4-III
C) 1-III, 2-II, 3-IV, 4-I
D) 1-II, 2-III, 3-I, 4-IV
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: Ozsu y Valduriez dictan un flujo de abstracción piramidal. Descomposición ignora particiones y usa el Esquema Conceptual Global (1-IV). Localización transforma la consulta algebraíca usando el Esquema de Fragmentos (2-I). Optimización define algoritmos guiándose por la posición en red, usando Asignación (3-III). La máquina final ejecuta en Motores Locales (4-II). Las demás secuencias violan el Principio de Transparencia del usuario.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 15
Enunciado: Indique la denominación técnica exacta (en mayúsculas) de la secuencia pre-procesada de uniones o joins que reconstruye algebraicamente una relación original particionada verticalmente en múltiples sitios.
Opciones:
A) GRAFO DE UNION CONEXO
B) ESQUEMA DE ASIGNACION
C) PROGRAMA DE MATERIALIZACION
D) PLAN DE EJECUCION DISTRIBUIDA
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: El "PROGRAMA DE MATERIALIZACION" es la entidad matemática inyectada durante la Localización de Datos que reemplaza la relación nominal en el árbol por su operador equivalente reconstruido (ej. R = R1 ⋈ R2). Rechazamos la opción A por ser de análisis semántico; la B por ser de metadatos, y la D por pertenecer a la salida de optimización de costos.

[TIPO: ORDENAMIENTO]
Pregunta ID: 16
Enunciado: Ordene estrictamente las cuatro capas de abstracción algorítmica por las que muta una petición SQL hasta convertirse en respuestas físicas locales.
I. Localización de datos convirtiendo elementos globales a fragmentos.
II. Descomposición de la consulta convirtiendo cálculo a álgebra relacional.
III. Ejecución distribuida sobre fragmentos materializados en cada nodo.
IV. Optimización global evaluando costos y comunicación inter-nodos.
Opciones:
A) II, I, IV, III
B) I, II, III, IV
C) IV, III, II, I
D) II, IV, I, III
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: La arquitectura procesa de forma Top-Down progresiva (Modelo de Özsu). La traducción (Descomposición, II) precede a la ubicación física de tuplas (Localización, I). Esto produce un árbol algebraico agnóstico a la red que luego se costea métricamente (Optimización, IV). Finalmente las heurísticas se materializan en hardware asíncrono (Ejecución, III).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 17
Enunciado: A diferencia de las capas estructurales iniciales, ¿qué información estricta utiliza la Optimización Global para configurar el árbol algebraico final?
Opciones:
A) Depende exclusivamente del esquema conceptual para evitar redundancia lógica.
B) Analiza el esquema de fragmentación horizontal para eliminar nodos sin datos.
C) Utiliza reglas de idempotencia matemática para reescribir consultas anidadas.
D) Emplea estadísticas de asignación y cardinalidad para evaluar costos reales.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: D
Explicación: Las capas 1 y 2 ejecutan transformaciones meramente lógicas (heurísticas de reescritura, limpieza de redundancia - anulando las opciones A, B y C). La Capa 3 (Optimización Global) es la única capa impulsada por Modelo de Costos; lee la cardinalidad de los nodos y el factor de Asignación (Allocation) para insertar primitivas de red send/receive ponderadas numéricamente.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 18
Enunciado: En la arquitectura formal de procesamiento, ¿cuál es la delimitación teórica de responsabilidades durante la etapa de "Ejecución Distribuida"?
Opciones:
A) El sitio central aplica el recocido simulado para distribuir métricas exactas.
B) Los nodos locales aplican algoritmos centralizados usando sus propios esquemas.
C) El directorio global materializa relaciones verticales mediante join naturales.
D) La capa normaliza predicados booleanos aplicando la ley distributiva unaria.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: El modelo teórico dicta Autonomía Local. La ejecución rompe el QEP en sub-operaciones donde cada DBMS participante (MySQL, PostgreSQL, etc.) utiliza su propio optimizador centralizado y métodos de acceso físico (índices b-tree) (opción B). La opción A y C conciernen al Coordinador (Capa 3 y 2). La opción D ocurre en el Parser (Capa 1).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 19
Enunciado: Al evaluar sintaxis durante la Descomposición, ¿qué inferencia sistémica emite el analizador si halla una desconexión en el Grafo de Unión relacional?
Opciones:
A) Determina que las relaciones generarán cruzamientos cartesianos no intencionados.
B) Reorganiza cuantificadores lógicos hacia formas normales estándares disyuntivas.
C) Reconstruye fragmentos verticales mediante operaciones de reunión equivalentes.
D) Transfiere diccionarios estadísticos hacia nodos adyacentes para evaluar CPU.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: Si un subgrafo carece de aristas conectoras, esto delata ausencia de condiciones Join entre relaciones. Algebraicamente esto resulta en un Producto Cartesiano (O(n^2)), tipificado como "Inconsistencia Semántica", provocando el aborto del proceso por su intratabilidad matemática no explícita. B es la Normalización. C es la Capa 2.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 20
Enunciado: Empareje la subfase interna de la Descomposición de Consultas con el mecanismo lógico-matemático empleado para transformar la solicitud original:
1. Normalización
2. Análisis Semántico
3. Eliminación de Redundancia
4. Reescritura a Álgebra
I. Traducción a un árbol estructural primitivo evaluando conmutatividad operativa.
II. Aplicación estricta de leyes de Idempotencia y absorción sobre los predicados.
III. Mapeo de precedencias (AND/OR) hacia configuraciones conjuntivas estándar.
IV. Expurgo topológico aislando grafos para rechazar tablas o variables espurias.
Opciones:
A) 1-IV, 2-I, 3-II, 4-III
B) 1-III, 2-IV, 3-II, 4-I
C) 1-I, 2-II, 3-III, 4-IV
D) 1-II, 2-III, 3-IV, 4-I
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Se siguen las fases del Parseador SQL riguroso: Normalización reordena operadores lógicos (1-III). Análisis valida grafos y tipos impidiendo colapsos (2-IV). Eliminación usa p ∨ p ≡ p (Idempotencia) (3-II). Finalmente se emite el primer grafo algebraico (4-I).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 21
Enunciado: Identifique el constructo topológico (en mayúsculas) derivado de omitir proyecciones y nodos terminales, el cual visualiza exclusivamente las dependencias de cruce entre atributos para detectar inconsistencias.
Opciones:
A) GRAFO DE DEPENDENCIA TRANSITIVA
B) DICCIONARIO DE DATOS DISTRIBUIDO
C) ARBOL ARBUSTIVO PARALELO
D) GRAFO DE UNION
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: D
Explicación: El "GRAFO DE UNION" (Join Graph) es la única subestructura que representa relaciones como nodos y cruces relacionales como arcos. Se utiliza como filtro primario en validación Semántica (Capa 1). Un árbol arbustivo (opción C) modela orden de ejecución (Capa 3), no validez semántica.

[TIPO: ORDENAMIENTO]
Pregunta ID: 22
Enunciado: Estructure el flujo algorítmico interno que efectúa la capa de Descomposición desde que recibe la sentencia original del usuario.
I. Detección y poda de redundancias lógico-matemáticas (reglas de equivalencia).
II. Verificación sintáctica-semántica bloqueando relaciones huérfanas en el grafo.
III. Reordenamiento lógico hacia Forma Normal Conjuntiva o Disyuntiva.
IV. Modelado algebraico final emitiendo un árbol binario procesable (QEP base).
Opciones:
A) II, III, I, IV
B) I, II, III, IV
C) III, II, I, IV
D) III, I, II, IV
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: El paso 1 requiere estandarizar el cálculo por precedencia (Normalización, III). El paso 2 requiere este estándar para validar tipos y rutas (Análisis Semántico, II). El paso 3 acorta el camino podando repeticiones (Redundancia, I). El paso 4 traduce ese bloque limpio a Álgebra (Reescritura, IV). Invertir esto impediría detectar tautologías.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 23
Enunciado: Durante la fase teórica de Eliminación de Redundancia, ¿cuál es el fundamento matemático estricto que permite simplificar o podar predicados inútiles?
Opciones:
A) La aplicación de heurísticas de costo para evitar cruces lineales exhaustivos.
B) La sustitución de variables basada en perfiles de fragmentación y selectividad.
C) La aplicación de leyes lógicas de idempotencia para absorber rangos repetidos.
D) El rechazo de esquemas globales desconectados en subgrafos de proyecciones.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: Las inyecciones de vistas o de seguridad relacional crean bucles proposicionales (ej. Edad > 18 AND Edad > 18). El optimizador usa Teoría de Conjuntos y Lógica Booleana (Leyes de Idempotencia o Dominación de AND p ∧ falso ≡ falso) para minimizar el tamaño del predicado antes de convertirse a código algebraico. Opciones A y B corresponden a Optimización (Capa 3).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 24
Enunciado: En la reestructuración de cálculo a álgebra, ¿por qué el árbol resultante de esta transformación estructural primaria NO es calificado matemáticamente como "óptimo"?
Opciones:
A) Asume distribución uniforme ignorando las prioridades semánticas del usuario.
B) Evalúa la red pero descarta los ciclos computacionales del servidor principal.
C) Prescinde de información de distribución espacial y fragmentación de los datos.
D) Obliga al motor a emplear búsqueda exhaustiva sobre subconsultas redundantes.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: La Descomposición pertenece al "Sitio de Control" usando un Esquema Global que es totalmente ciego ante la ubicación física (Sitios) o particiones de los datos (Fragmentos). Genera un "plan bueno genérico", pero subóptimo, dado que un costo verdadero depende de la topología de la red (Localización y Asignación, Capas 2 y 3).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 25
Enunciado: ¿Cuál es la implicación matemática en el espacio de búsqueda al admitir primitivas de evaluación cruzada con complejidad algorítmica estricta O(n²)?
Opciones:
A) Asegura paralelismo masivo descentralizando tuplas a través de nodos remotos.
B) Provoca una explosión en el consumo de CPU forzando la poda heurística inminente.
C) Minimiza la saturación de los canales limitando el envío de llaves foráneas.
D) Reduce la cardinalidad intermedia aplicando reglas de selectividad restrictiva.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: El Producto Cartesiano (sin factor join equitativo) posee una tasa de crecimiento de la forma O(n²). Su inclusión sin restricciones colapsaría el cálculo de la Función Objetivo. Es el axioma base de por qué los optimizadores inyectan Heurísticas (Poda) para retrasarlo o eliminarlo tempranamente. Las demás opciones asumen beneficios falsos derivados de un operador prohibido o altamente destructivo.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 26
Enunciado: Asocie cada estrategia de búsqueda algorítmica implementada por los motores de base de datos con su limitación u operador matemático distintivo:
1. Programación Dinámica
2. Algoritmo Voraz (Greedy)
3. Mejora Iterativa
4. Recocido Simulado
I. Acepta anomalías térmicas (costos peores temporales) para salir de barrancos.
II. Sufre amnesia local, realizando descartes irrevocables sin evaluación global.
III. Alcanza atrapamiento cíclico en mínimos locales al buscar sólo mejoras rectas.
IV. Intratabilidad estricta (colapso factorial) frente a espacios n-dimensionales (>6 tablas).
Opciones:
A) 1-IV, 2-I, 3-III, 4-II
B) 1-III, 2-IV, 3-I, 4-II
C) 1-II, 2-I, 3-IV, 4-III
D) 1-IV, 2-II, 3-III, 4-I
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: D
Explicación: La Programación Dinámica explora todos los niveles (garantiza el óptimo) pero es NP-Hard para esquemas masivos (1-IV). Greedy toma la ruta más barata instantánea cayendo en falsos valles por miopía (2-II). Mejora Iterativa solo baja la curva, quedando presa de mínimos locales (3-III). Recocido usa salto estocástico superando dichas barreras (4-I).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 27
Enunciado: Identifique el estimador numérico estadístico (en mayúsculas) entre 0 y 1 que calcula la probabilidad teórica de que las tuplas logren satisfacer exitosamente las restricciones de un predicado algebraico particular.
Opciones:
A) TASA DE MATERIALIZACION
B) CARDINALIDAD ASINTOTICA
C) FACTOR DE SELECTIVIDAD
D) FRAGMENTACION HORIZONTAL
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: El "FACTOR DE SELECTIVIDAD" (SF) es la base del Modelo de Costo. Por ejemplo, SF = 1 / únicos(A) bajo distribución uniforme. Multiplicar SF por la cardinalidad inicial card(R) deduce el tamaño del resultado intermedio y condiciona de forma directa las decisiones operativas y el coste inter-nodal.

[TIPO: ORDENAMIENTO]
Pregunta ID: 28
Enunciado: En el procesamiento algorítmico general de la Capa 3, ¿cuál es el orden estricto de los eventos que culminan con la instanciación de un Plan de Ejecución?
I. Análisis mediante Modelo de Costo para predecir cardinalidad y tamaños de red.
II. Uso de una Estrategia de Búsqueda sobre los planes para capturar el de menor coste.
III. Generación del Espacio de Búsqueda aplicando reglas lógicas de transformación (álgebra).
IV. Emisión final del QEP óptimo parametrizado hacia los sitios en ejecución distribuida.
Opciones:
A) I, III, II, IV
B) III, I, II, IV
C) III, II, I, IV
D) I, II, III, IV
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Acorde a la Arquitectura Funcional del Optimizador, se entra con un árbol nominal y primero se genera el Espacio topológico multiforme (III). Posteriormente el componente probabilístico "Modelo de Costo" dimensiona cada árbol generativo (I). Con esos datos, la "Estrategia" decide iterar o descartar (II) hasta hallar un límite. Se arroja el QEP resultante (IV).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 29
Enunciado: ¿Qué axioma estructural hace que los "árboles arbustivos" (bushy trees) posean ventaja teórica en un pipeline distribuido masivo frente a los modelos lineales puros?
Opciones:
A) Garantizan un ordenamiento secuencial que evita el agotamiento de memoria RAM.
B) Restringen las reuniones operando exclusivamente con resultados materializados.
C) Admiten la ejecución concurrente de múltiples subplanes en sitios diferentes.
D) Disminuyen el espacio de estados posibilitando el uso de programación dinámica.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: En Teoría de Planificación de Consultas, los árboles de procesamiento Lineal exigen que un nodo base entre siempre con un resultado previo, obligando a una secuencia. Los "Bushy Trees" operan en Y o en matrices, admitiendo que (A ⋈ B) se ejecute en el Nodo 1 y simultáneamente (C ⋈ D) en el Nodo 2, mermando radicalmente el Tiempo de Respuesta a costa de agrandar geométricamente el espacio de búsqueda.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 30
Enunciado: En heurísticas voraces (greedy) para sistemas distribuidos, ¿por qué NO es matemáticamente posible retroceder ante el hallazgo empírico de un subplan costoso de red?
Opciones:
A) Evalúa todas las permutaciones posibles construyendo árboles desde las bases.
B) Acepta degradaciones de rendimiento probables para evadir los valles locales.
C) Elige heurísticamente el menor costo inmediato haciendo su decisión irreversible.
D) Depende de histogramas unidimensionales que ocultan dependencias transitivas.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: El Teorema del Algoritmo Voraz dictamina que su toma de decisiones se efectúa "en el momento local" (Local Optimum). Al elegir la arista más barata en su nivel presente, no almacena punteros de retroceso (backtracking state memory), lo que invalida revertir la matriz de cruce. La opción A define el modelo de Programación Dinámica, y la B, el Recocido Simulado (Simulated Annealing).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 1
Enunciado: Özsu y Valduriez identifican objetivos teóricos que justifican el uso de la replicación en bases de datos distribuidas. ¿Cuáles son estos objetivos estructurales que determinan el diseño del sistema?

Opciones:
A) Disponibilidad, balanceo estricto, atomicidad distribuida y tolerancia a la red bizantina.
B) Disponibilidad, rendimiento, escalabilidad y requisitos operativos de la aplicación misma.
C) Equivalencia estructural, fragmentación horizontal, transparencia local y atomicidad base.
D) Rendimiento absoluto, aislamiento transaccional, tolerancia a particiones y balanceo total.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: Según la literatura sobre conceptos de replicación, los cuatro objetivos fundamentales de Özsu y Valduriez son la disponibilidad frente a fallos, el rendimiento mediante acceso local, la escalabilidad frente al crecimiento de solicitudes y los requisitos específicos de cada aplicación. Las otras opciones introducen falacias teóricas (como la red bizantina o el balanceo total estricto) que no pertenecen a los axiomas de diseño para este modelo.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 2
Enunciado: Relacione la configuración teórica de transparencia y consistencia con su definición estructural exacta:
1. Transparencia limitada
2. Transparencia completa
3. Consistencia mutua fuerte
4. Consistencia mutua débil
a. El Gestor de Transacciones local rutea sin revelar la topología.
b. El cliente tiene codificada la ubicación explícita del maestro.
c. Las réplicas pueden divergir temporalmente pero convergen eventualmente.
d. Las réplicas poseen el mismo estado al confirmarse la transacción.

Opciones:
A) 1-b, 2-a, 3-d, 4-c
B) 1-a, 2-b, 3-c, 4-d
C) 1-c, 2-d, 3-b, 4-a
D) 1-d, 2-c, 3-a, 4-b
E) 1-b, 2-a, 3-c, 4-d

Respuesta Correcta: A
Explicación: La arquitectura de un sistema distribuido dicta que en transparencia limitada el cliente rutea sus operaciones (1-b), y en la completa, el Transaction Manager abstrae la red (2-a). La consistencia fuerte implica convergencia síncrona obligatoria al momento del commit (3-d), mientras que la débil relaja este axioma permitiendo ventanas de divergencia (4-c).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 3
Enunciado: ¿Cuál es el concepto teórico que dicta que la replicación debe mantener múltiples copias físicas de un dato, pero haciendo que el sistema opere frente al usuario como si existiera una sola copia en el espacio lógico? Escriba el término completo.

Respuesta Correcta: EQUIVALENCIA DE UNA SOLA COPIA
Explicación: Este axioma de diseño es la abstracción fundamental de la replicación, la cual asegura que los problemas físicos del particionamiento queden ocultos a la semántica de la transacción del usuario.

[TIPO: ORDENAMIENTO]
Pregunta ID: 4
Enunciado: En un entorno distribuido móvil offline que prioriza la disponibilidad sobre la consistencia, el protocolo opera bajo la estrategia "Lazy Distribuida". Ordene cronológicamente el flujo algorítmico de este proceso de replicación:
1. Sincronización asíncrona mediante transacción de refresco.
2. Almacenamiento directo en la base de datos local desconectada.
3. Registro inicial de la operación en el dispositivo.
4. Convergencia y actualización del estado en los demás nodos regionales.

Opciones:
A) 1, 2, 3, 4
B) 2, 3, 1, 4
C) 3, 2, 1, 4
D) 4, 3, 2, 1
E) 3, 1, 2, 4

Respuesta Correcta: C
Explicación: Un protocolo Lazy Distribuido permite la operación autónoma. Primero ocurre el registro local por el usuario (3), se almacena en la réplica autónoma (2). Cuando se reestablece el enlace, ocurre la sincronización (1) y finalmente la convergencia global (4) resolviendo posibles colisiones.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 5
Enunciado: Cuando un sistema distribuido implementa un grado de "Transparencia Completa" para ocultar la topología física, ¿cuál de los siguientes enunciados define estrictamente su comportamiento transaccional?

Opciones:
A) El usuario rutea lógicamente los datos hacia el nodo maestro utilizando reglas embebidas.
B) El Transaction Manager local define la ubicación física, ocultando la red al desarrollador.
C) El Gestor de Transacciones exige que el cliente codifique la ubicación de las particiones.
D) La actualización se aplica asíncronamente mientras el cliente define el nodo coordinador.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: La transparencia completa descarga al cliente/desarrollador de administrar la topología de red; el Gestor de Transacciones (TM) asume todo el enrutamiento lógico hacia el nodo maestro o réplica. La opción A y C describen una transparencia limitada.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 6
Enunciado: Según el modelo teórico de propagación de actualizaciones, el protocolo "Eager" exige sincronía global. ¿Cuál es el comportamiento axiomático que caracteriza a esta estrategia de actualización?

Opciones:
A) Propaga la actualización asíncronamente para asegurar una convergencia eventual inmediata.
B) Reclama bloqueos asíncronos en los esclavos para evitar la degradación del nodo principal.
C) Propaga los datos dentro de la transacción original asegurando consistencia al confirmar.
D) Prioriza la disponibilidad global descartando la confirmación de escrituras concurrentes.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: El protocolo Eager requiere matemáticamente que la confirmación de la transacción no ocurra hasta que las réplicas sean actualizadas, aplicando 2PC. Garantiza consistencia mutua fuerte sacrificando latencia transaccional.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 7
Enunciado: En la replicación basada en un líder, el modo semi-síncrono busca balancear la confiabilidad. ¿Qué comportamiento algorítmico asume frente a un entorno propenso a fallas?

Opciones:
A) Garantiza tolerancia ante la partición bizantina usando un árbol de confirmación estricta.
B) Detiene la escritura global si el único seguidor activo resulta ser el servidor asíncrono.
C) Permite durabilidad en al menos dos nodos, asumiendo el asíncrono el rol en caso de falla.
D) Fuerza un interbloqueo irresoluble si el líder se apaga antes de propagar a sus esclavos.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: El modo semi-síncrono mantiene un nodo estrictamente acoplado (síncrono) para garantizar la persistencia del Write-Ahead Log. Si este falla, el algoritmo promueve a un nodo asíncrono temporalmente para evitar la parálisis global dictada por el Teorema CAP (sacrificio controlado de consistencia por disponibilidad).

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 8
Enunciado: Relacione la topología de replicación multi-líder con su vulnerabilidad o comportamiento teórico matemático:
1. Topología Circular
2. Topología Estrella
3. Topología Todos a Todos
a. Mayor robustez de rutas, pero genera desorden causal en la llegada de mensajes.
b. Genera vulnerabilidad estricta si el nodo raíz intermedio falla, interrumpiendo el árbol.
c. Genera bucles infinitos si las escrituras no incluyen etiquetas con identificadores de paso.

Opciones:
A) 1-b, 2-c, 3-a
B) 1-c, 2-b, 3-a
C) 1-a, 2-b, 3-c
D) 1-c, 2-a, 3-b
E) 1-a, 2-c, 3-b

Respuesta Correcta: B
Explicación: La topología circular (1) requiere identificadores para evitar bucles (c). La estrella (2) colapsa si el nodo central falla (b). Todos a todos (3) provee múltiples caminos mitigando fallos de red, pero los tiempos de enlace variables generan violaciones de precedencia causal (a).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 9
Enunciado: En la topología multi-líder de "Todos a Todos", los relojes físicos (timestamps) son algorítmicamente insuficientes para resolver el problema de los mensajes que se adelantan. ¿Qué estructura de datos abstracta es necesaria para rastrear las dependencias causales exactas entre las escrituras?

Respuesta Correcta: VECTORES DE VERSION
Explicación: Un vector de versión es la estructura estricta empleada en sistemas distribuidos para resolver colisiones y ordenar cronológicamente las dependencias lógicas cuando la red física sufre retrasos asimétricos y los relojes locales carecen de precisión cuántica/atómica.

[TIPO: ORDENAMIENTO]
Pregunta ID: 10
Enunciado: En una arquitectura basada estrictamente en un líder, ordene el flujo de ejecución algorítmica indispensable para procesar una transacción de escritura global manteniendo la consistencia:
1. Los seguidores aplican los cambios respetando la misma secuencia en su máquina de estados local.
2. El cliente emite la operación hacia el líder designado.
3. El líder propaga de manera síncrona o asíncrona la entrada en el log hacia cada seguidor.
4. El líder procesa y aplica la alteración transaccional sobre su almacenamiento persistente.

Opciones:
A) 2, 4, 3, 1
B) 2, 3, 4, 1
C) 4, 2, 3, 1
D) 2, 4, 1, 3
E) 4, 3, 2, 1

Respuesta Correcta: A
Explicación: El protocolo exige el contacto con el coordinador (2), el cambio y persistencia local (4), la creación y propagación del evento por el log (3), y finalmente la asimilación del evento secuencial en los nodos periféricos (1).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 11
Enunciado: En la topología multi-líder circular, existe una falla inherente al diseño que amenaza la escalabilidad de los recursos transaccionales. ¿Cuál es este problema teórico y su mecanismo de mitigación?

Opciones:
A) Requieren la instauración de una fase de validación temporal mediante confirmación doble.
B) Generan un consumo cíclico indefinido, resuelto mediante identificadores únicos por nodo.
C) Bloquean la máquina de estados local utilizando un protocolo de consenso asimétrico total.
D) Obligan al sistema a resolver el ordenamiento mediante vectores de versión bidireccionales.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: Como cada nodo recibe y reenvía, una escritura carente de metadatos daría infinitas vueltas. La mitigación estructural exige agregar etiquetas con los identificadores de los nodos por los que ha transitado, provocando el descarte al coincidir.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 12
Enunciado: En la replicación multi-líder "Todos a Todos", ¿cuál es el impacto algorítmico directo causado por la asimetría en la velocidad de los enlaces de red al transmitir operaciones interdependientes?

Opciones:
A) La llegada desfasada altera el orden lógico, haciéndose vital el uso de vector de versión.
B) Las latencias asimétricas congelan la propagación, mitigado mediante relojes sincronizados.
C) El retraso estructural rompe el anillo virtual, forzando la reconstrucción de la partición.
D) La entrega adelantada corrompe el log de transacciones exigiendo retrocesos asíncronos.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: A
Explicación: Los enlaces de red tienen velocidades distintas, provocando un desorden causal (ej. una actualización llega a un nodo antes que la inserción de la fila afectada). Los timestamps son insuficientes, exigiendo vectores de versión para no romper la integridad relacional.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 13
Enunciado: A diferencia del "WAL shipping" físico que exige consistencia binaria, ¿qué compromiso arquitectónico asume la Replicación Lógica en el ecosistema PostgreSQL 18?

Opciones:
A) Requiere el uso de bloques binarios de WAL garantizando consistencia fuerte nativa estricta.
B) Propaga operaciones en SQL permitiendo subconjuntos e incurriendo en consistencia eventual.
C) Sincroniza datos a nivel de disco, bloqueando temporalmente hasta que el suscriptor confirme.
D) Delega el control transaccional al publicador anulando la probabilidad de estados obsoletos.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: La replicación lógica opera descodificando el flujo a nivel de comandos o filas, lo que otorga la flexibilidad de replicar solo ciertas tablas (subconjuntos) e incluso cruzar versiones de motor, pero introduce por defecto la consistencia débil/eventual y sus inherentes anomalías de retraso.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 14
Enunciado: Relacione la anomalía de consistencia generada por el retraso asíncrono con su estrategia teórica formal de resolución:
1. Read-Your-Writes
2. Monotonic Reads
3. Consistent Prefix Reads
a. Afinidad de réplica basada en hashes del usuario para atarlo a un nodo específico.
b. Forzar que las escrituras causalmente asociadas habiten la misma partición lógica.
c. Controlar el lag leyendo exclusivamente del líder tras una escritura propia.

Opciones:
A) 1-c, 2-a, 3-b
B) 1-a, 2-c, 3-b
C) 1-b, 2-a, 3-c
D) 1-c, 2-b, 3-a
E) 1-b, 2-c, 3-a

Respuesta Correcta: A
Explicación: La anomalía "Read-Your-Writes" (1) ocurre cuando el nodo no tiene el último cambio propio; se mitiga leyendo del líder o controlando por timestamp (c). "Monotonic Reads" (2) requiere afinidad por sesión (a) para evitar saltos en el tiempo lógico. "Consistent Prefix Reads" (3) requiere mitigaciones causales (b).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 15
Enunciado: Si un usuario modifica sus datos, recarga la interfaz, y el balanceador de carga dirige su lectura a un seguidor asíncrono rezagado que le entrega los datos antiguos, ¿qué anomalía de retraso de replicación acaba de sufrir?

Respuesta Correcta: READ-YOUR-WRITES
Explicación: La anomalía Read-Your-Writes define la incapacidad del usuario de observar sus propias confirmaciones si la lectura interactúa con un nodo que no ha convergido el log transaccional del líder.

[TIPO: ORDENAMIENTO]
Pregunta ID: 16
Enunciado: En un clúster PostgreSQL 18, para forzar el comportamiento hacia la Consistencia Mutua Fuerte mitigando todo retraso de red, ordene lógicamente los parámetros de configuración exigidos en `postgresql.conf`:
1. Definir que el sistema retenga confirmaciones con `synchronous_commit = on`.
2. Habilitar la transmisión en la capa de red con `wal_level = replica`.
3. Reiniciar el motor de la base de datos `pg_ctl restart`.
4. Especificar las dependencias asimétricas en `synchronous_standby_names`.

Opciones:
A) 1, 2, 4, 3
B) 2, 1, 4, 3
C) 4, 1, 2, 3
D) 2, 4, 1, 3
E) 1, 4, 2, 3

Respuesta Correcta: B
Explicación: Para implementar la consistencia estricta, primero se ajusta el nivel de extracción física (2), se fuerza el bloqueo 2PC simulado (1), se declaran qué nodos dictan este quórum rígido (4), y finalmente se reinicia el sistema para asimilar la parametrización.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 17
Enunciado: Al operar una topología bidireccional asíncrona mediante replicación lógica, surge inevitablemente la colisión en las llaves primarias generadas simultáneamente. ¿Cómo se mitiga lógicamente esta anomalía estructural sin invocar un bloqueo global de red?

Opciones:
A) Requiere un coordinador distribuido estricto para emitir claves transaccionales síncronas.
B) Obliga al motor a emplear vectores de versión para fusionar los números seriales idénticos.
C) Evita la colisión de llaves al inicializar rangos con incrementos numéricos independientes.
D) Suspende el nodo suscriptor inmediatamente hasta que un humano resuelva la clave duplicada.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: La teoría dicta el uso de "esquemas de pasos" o rangos disjuntos lógicos (ej. Nodo 1 genera impares, Nodo 2 genera pares). Esto elimina matemáticamente el conflicto W/W (Write/Write) subyacente a nivel de identificadores sin sacrificar el principio de autonomía local ni exigir mensajes 2PC a través de la red.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 18
Enunciado: Cuando un administrador consulta la vista `pg_stat_replication` y evalúa el retraso de bytes (`pg_wal_lsn_diff`) sobre un seguidor en modo asíncrono, ¿qué dimensión de la teoría de recuperación de fallos está analizando exactamente?

Opciones:
A) Demuestra la violación matemática del protocolo Eager mediante el descarte asíncrono veloz.
B) Mide lógicamente la divergencia de estados, advirtiendo sobre anomalías de prefijo fallido.
C) Cuantifica bytes de retraso físico, evidenciando el riesgo de pérdida si el primario cae.
D) Resuelve colisiones mutuas forzando la reconvergencia de los registros con marcas temporales.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: El análisis del retraso (`lag`) en una replicación asíncrona mide la ventana de vulnerabilidad del sistema; indica el volumen de transacciones ya confirmadas lógicamente al usuario pero que se perderían irremediablemente en un proceso de failover si el nodo primario perece.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 19
Enunciado: En el diseño arquitectónico "Distribuido Eager", múltiples sitios aceptan transacciones requiriendo la ejecución de un Bloqueo de 2 Fases (2PL) Distribuido. ¿Cuál es el compromiso analítico letal que introduce esta combinación?

Opciones:
A) Desvía las transacciones en conflicto mediante el ruteo automático hacia nodos inactivos.
B) Genera dependencias circulares sistémicas resueltas mediante grafos o marcas de prevención.
C) Fuerza la divergencia transaccional, exigiendo que las escrituras se resuelvan con humanos.
D) Permite omitir la fase de confirmación si se garantiza la disponibilidad de una sola réplica.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: Como cualquier nodo puede iniciar escrituras sobre el mismo dato exigiendo cerraduras globales simultáneas, el modelo es matemáticamente susceptible a interbloqueos distribuidos (deadlocks). Se deben aplicar prevenciones cronológicas (wait-die / wound-wait) o grafos de espera (WFG) para salvaguardar la progresión transaccional.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 20
Enunciado: Según las dimensiones ortogonales de Özsu y Valduriez (Propagación / Lugar de Actualización), asocie cada protocolo con su definición operativa de red:
1. Centralizado Eager
2. Distribuido Eager
3. Centralizado Lazy
4. Distribuido Lazy
a. Un único servidor central asimila el cambio y lo propaga mediante componentes encolados.
b. Las transacciones se aplican en cualquier nodo descentralizado, asumiendo colisiones a resolver lógicamente.
c. Aplica en todas las réplicas en una única transacción mediante un nodo líder único usando protocolo 2PC.
d. Exige bloqueos de escritura descentralizados en toda la red para asegurar concurrencia sin líder único.

Opciones:
A) 1-a, 2-b, 3-c, 4-d
B) 1-c, 2-d, 3-a, 4-b
C) 1-d, 2-c, 3-b, 4-a
D) 1-b, 2-a, 3-d, 4-c
E) 1-c, 2-a, 3-b, 4-d

Respuesta Correcta: B
Explicación: Centralizado Eager coordina desde un nodo con sincronía 2PC (1-c). Distribuido Eager descentraliza, pero sincroniza mediante 2PL forzando consistencia (2-d). Centralizado Lazy absorbe en el líder y difiere con colas de propagación (3-a). Distribuido Lazy maximiza disponibilidad permitiendo colisiones (4-b).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 21
Enunciado: Para mitigar el colapso del sistema en un diseño Distribuido Eager por el choque de bloqueos, el algoritmo analiza los ciclos de dependencia globales. Escriba el término formal (o su acrónimo en inglés de 3 letras) de la matriz de estructuras generada para detectar este fenómeno de 'deadlock'.

Respuesta Correcta: WFG
Explicación: WFG (Wait-For Graph) o Grafo de Espera Distribuido. Se construye periódicamente trazando qué transacción bloquea a otra a través de la red, para detectar un círculo vicioso de interbloqueo y abortar sistémicamente una de ellas.

[TIPO: ORDENAMIENTO]
Pregunta ID: 22
Enunciado: En el Protocolo Centralizado Lazy, la arquitectura desacopla el 2PC y utiliza un esquema de software intermedio para transmitir la consistencia eventual. Ordene el flujo operativo de sus componentes lógicos de propagación:
1. El "procesador de réplicas" aplica asíncronamente las transformaciones lógicas en los esclavos.
2. La "cola de propagación" retiene el historial en tránsito de manera resiliente frente a desconexiones.
3. El "capturador de registros" analiza y destila las marcas del log originadas por el nodo maestro.
4. El sitio primario confirma velozmente la transacción al usuario cliente garantizando latencia mínima.

Opciones:
A) 4, 3, 2, 1
B) 3, 4, 1, 2
C) 4, 2, 3, 1
D) 2, 3, 4, 1
E) 1, 2, 3, 4

Respuesta Correcta: A
Explicación: En el desacoplamiento Lazy, el sistema atiende y libera primero al usuario en la capa local (4), posteriormente el daemon de captura extrae la operación del WAL (3), se expone en un búfer o encolador persistente (2), y el último tramo lo realiza el procesador esclavo aplicando los deltas (1).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 23
Enunciado: En el modelo de "Copia primaria con transparencia total", la red desplaza la potestad dictatorial del nodo maestro único. ¿Qué axioma estructural domina esta arquitectura para satisfacer el enrutamiento transaccional?

Opciones:
A) Consolida todas las escrituras en un solo servidor de registro evadiendo cualquier colisión.
B) Fuerza el particionamiento binario del registro WAL suprimiendo bloqueos en las consultas.
C) Exige un directorio sistémico distribuido para rastrear la ubicación del maestro asignado.
D) Bloquea el procesamiento local hasta que los seguidores validen el identificador transferido.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Para mantener la Transparencia Total y eliminar el embudo de un único maestro global, la responsabilidad de "líder" se reparte granularmente por elemento. Para operar, los Transaction Managers requieren estrictamente de un directorio distribuido que informe qué sitio ostenta la maestría de la tupla requerida.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 24
Enunciado: El Protocolo Distribuido Lazy entrega autonomía total descentralizando las escrituras y postergando la propagación, priorizando el Teorema CAP hacia la alta disponibilidad. ¿Qué consecuencia matemática asume sin remedio este diseño?

Opciones:
A) Garantiza consistencia fuerte asimétrica al someter las tuplas a bloqueos mutuos distribuidos.
B) Genera colisiones simultáneas matemáticamente complejas resueltas por el último timestamp.
C) Inhibe la autonomía local deteniendo las operaciones en sitios donde la latencia sea extrema.
D) Suprime transacciones originadas en nodos periféricos para sostener el aislamiento de lectura.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: Al operar bajo un modelo "Escribir en cualquier parte" (Update Anywhere) de forma diferida, se garantiza una alta probabilidad de choque por Divergencia de Estados (Conflicto W/W). Requiere reconciliaciones como "Apply Last" u heurísticas de dominio para fusionar.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 25
Enunciado: El Consenso de Quórum matemático de Gifford es la herramienta formal para proteger la consistencia frente a particiones de red impredecibles. ¿Cuál es el requisito inecuacional obligatorio para prevenir una intersección vacía de lectura-escritura en un universo de nodos $V$?

Opciones:
A) Asegura que Vr sumado a Vw sea estructuralmente inferior a la totalidad de nodos en el grupo.
B) Obliga matemáticamente a que la cuota de lecturas supere la mitad estricta de todos los votos.
C) Requiere que Vr más Vw supere el total de votos de la red y Vw supere la mitad matemática.
D) Flexibiliza la consistencia permitiendo validar la escritura con la minoría activa del sistema.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Gifford define dos inecuaciones para bloquear la formación subyacente de divergencias: la colisión de lectura/escritura exige $V_r + V_w > V$ (asegurando el solapamiento del dato fresco), y la colisión escritura/escritura exige estrictamente $V_w > V/2$.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 26
Enunciado: Ordene y defina las fases matemáticas del "Protocolo de transición de vistas" encargado de construir y abstraer "Particiones Virtuales" ante perturbaciones físicas de red:
1. Fase de sospecha
2. Fase de acuerdo
3. Fase de creación
4. Fase de puesta al día
a. Instauración del grupo aislado validado mediante la asignación de un identificador lógico secuencial único.
b. Mecanismo de clonado donde los nodos periféricos o intermitentes absorben los históricos del segmento regente.
c. Votación transversal donde el enjambre alcanzable discute la legitimidad de aislar la lista de miembros de la topología.
d. Un componente, ante la expiración de la tolerancia de red (heartbeat fail), emite la propuesta formal de fraccionamiento.

Opciones:
A) 1-d, 2-c, 3-a, 4-b
B) 1-a, 2-b, 3-c, 4-d
C) 1-d, 2-a, 3-c, 4-b
D) 1-c, 2-d, 3-b, 4-a
E) 1-c, 2-a, 3-d, 4-b

Respuesta Correcta: A
Explicación: El protocolo de transición en redes inestables se desglosa en la ausencia del latido alertando al sistema (1-d), votando sobre la exclusión del participante (2-c), blindando lógicamente la partición con un ID inmutable temporalmente (3-a) y resincronizando las desactualizaciones (4-b).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 27
Enunciado: La gran mayoría de los teoremas de control distribuido (incluyendo los protocolos ROWA convencionales) asumen un axioma utópico en el cual un nodo moribundo simplemente deja de procesar abruptamente sin emitir tramas de red corruptas, engañosas o padecer demoras intermitentes. ¿Cuál es el nombre técnico de este modelo teórico de fallo?

Respuesta Correcta: FAIL-STOP
Explicación: La falla por parada limpia (Fail-Stop) es el supuesto académico tradicional que permite eludir las complicaciones intrincadas subyacentes a las faltas bizantinas, asumiendo una interrupción pura y determinista del nodo afectado.

[TIPO: ORDENAMIENTO]
Pregunta ID: 28
Enunciado: Cuando un protocolo adopta esquemas flexibilizados (ej. Read-One/Write-All Available) asumiendo disponibilidad excluyente, el commit requiere una fase de Validación adicional. Ordene secuencialmente los eventos de protección de transacciones contra los "falsos positivos de partición":
1. Ejecución atómica: abortar el conjunto si un estado diverge lógicamente.
2. Comprobación cruzada de inactividad: garantizar que los excluidos continúan caídos.
3. Consolidación de red: verificación de vigencia en los nodos operativos intervinientes.

Opciones:
A) 3, 2, 1
B) 1, 2, 3
C) 2, 3, 1
D) 3, 1, 2
E) 1, 3, 2

Respuesta Correcta: A
Explicación: Para sostener la integridad, la fase de validación evalúa primero quién está activo y válido (3), rastrea si algún componente ausente "volvió" inesperadamente (2) y somete esa matriz a una decisión atómica de confirmación o de rollback estricto (1).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 29
Enunciado: El Protocolo ROWA-A Distribuido elimina el nodo de validación maestro permitiendo la reconfiguración tolerante a fallos. ¿Cómo sortea estructuralmente este modelo la amenaza de generar escrituras conflictivas sobre particiones asimétricas?

Opciones:
A) Detiene irremediablemente el procesamiento de escrituras globales al identificar particiones.
B) Mantiene el procesamiento mediante vistas locales numeradas sin usar un coordinador primario.
C) Bloquea el segmento mayoritario para proteger las operaciones del subgrupo de red aislado.
D) Reclama intervención humana obligatoria para fusionar los logs de los árboles de directorios.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: Al descentralizar el manejo de conectividad, ROWA-A Distribuido previene las escrituras de subgrupos aislados forzando a que cada sitio concuerde sobre una matriz descentralizada ("vista" local numerada). Las escrituras sólo prosperan verificando la legitimidad de la vista unificada.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 30
Enunciado: La Votación de Mayoría estática, introducida por el Algoritmo de Thomas, simplifica el consenso demandando un quórum único. ¿Bajo qué arquitectura física este teorema sucumbe inevitablemente hacia un estancamiento del sistema?

Opciones:
A) Descentraliza las transacciones asimétricas habilitando operaciones en los segmentos menores.
B) Produce un riesgo crítico de bloqueo absoluto ante particiones estructuralmente simétricas.
C) Resuelve bloqueos mutuamente excluyentes delegando la confirmación al registro abstracto WAL.
D) Garantiza convergencia eventual fusionando los conflictos según el identificador cronológico.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: El modelo de Thomas exige matemáticamente la "Regla del 50% + 1". Si la topología de la base de datos está compuesta por un total de nodos pares (ej. 4 nodos), y un fallo disecciona la red por la mitad exacta (2 y 2), ambos grupos quedan lógicamente inhabilitados generando un "Riesgo de Empate" (Deadlock global).


[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 1
Enunciado: En la arquitectura de bases de datos, el criterio de optimización diverge teóricamente según la topología subyacente. Frente al dilema axiomático entre sistemas distribuidos y paralelos, ¿cuál premisa dicta el diseño de operaciones?

Opciones:
A) En sistemas paralelos, el riesgo crítico es la latencia de red entre nodos distantes.
B) En sistemas distribuidos, el objetivo principal es balancear la carga computacional.
C) En sistemas distribuidos, la prioridad es que todos los nodos procesen simultáneamente.
D) En sistemas paralelos, el costo dominante es bajo, priorizando el balance de la carga.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: D
Explicación: En el marco teórico de la infraestructura de datos, el criterio de diseño de BD Paralela prioriza balancear la carga porque la comunicación entre nodos tiene un costo bajo (D es correcta). En BD Distribuida, el riesgo principal son los accesos remotos costosos (alta latencia), por lo que busca minimizar comunicación (B y C violan este principio). El principio teórico afectado es el Modelo de Costos de Ejecución Distribuida.

[TIPO: ORDENAMIENTO]
Pregunta ID: 2
Enunciado: La metodología de diseño Top-Down garantiza una transición axiomática desde la abstracción semántica hasta la implementación de hardware. Ordene secuencialmente las fases estrictas de este proceso.

Opciones:
1. Derivación de los Esquemas Conceptuales Locales (LCS).
2. Construcción matemática del Esquema Conceptual Global (GCS).
3. Construcción y optimización algorítmica de los Esquemas Físicos locales.
4. Ejecución del Diseño de Distribución (Fragmentación y Asignación de datos).

Respuesta Correcta: 2, 4, 1, 3
Explicación: El enfoque Top-Down inicia definiendo la estructura lógica completa (GCS). Luego aplica el diseño de distribución (fragmentación y asignación) que resulta en los esquemas locales (LCS). Finalmente, estos se traducen en los esquemas físicos. Principio afectado: Arquitectura ANSI/SPARC distribuida y Metodología Top-Down.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 3
Enunciado: Durante el diseño Bottom-Up de una base de datos federada, la integración de esquemas locales (LCS) produce inconsistencias que rompen el modelo relacional. Empareje cada escenario de anomalía con su clasificación teórica formal.

Elementos:
A) El atributo "Sueldo" es tipo INT en el Sitio 1 y tipo VARCHAR en el Sitio 2.
B) El concepto "Proyecto" es Atributo en el Sitio 1 y es una Relación en el Sitio 2.
C) El término "Factura" significa documento de cobro en S1 y recibo de bodega en S2.
D) El atributo primario se llama "Cod_Cli" en el Sitio 1 e "ID_Cliente" en el Sitio 2.

Opciones:
1. Conflicto Estructural
2. Conflicto de Tipo
3. Conflicto de Nombres (Sinónimo)
4. Conflicto Semántico

Respuesta Correcta: A-2, B-1, C-4, D-3
Explicación: Según la teoría de integración de esquemas heterogéneos, las disparidades en tipos primitivos son Conflictos de Tipo; las diferencias de modelado relacional (atributo vs tabla) son Conflictos Estructurales; el cambio de contexto del mismo término es Conflicto Semántico; y distintos nombres para el mismo dato es Conflicto de Nombres. Principio afectado: Resolución de Heterogeneidad en Diseño Bottom-Up.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 4
Enunciado: El diseño distribuido se rige por un sistema interdependiente de tres ejes de decisión. Si un arquitecto modifica el nivel de fragmentación de un clúster, ¿qué impacto axiomático tiene sobre la topología integral?

Opciones:
A) La replicación minimiza accesos remotos en escrituras, alterando el esquema de control.
B) La fragmentación define ubicación física asumiendo una replicación completa sincrónica.
C) La asignación altera la localidad y balance, perjudicando el paralelismo intra-query.
D) Modificar cualquier decisión altera el óptimo, exigiendo una evaluación de compromiso.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: D
Explicación: El teorema del diseño distribuido dicta que fragmentación, asignación y replicación son variables interdependientes; optimizar una altera las condiciones óptimas de las demás (trade-off de diseño). La ubicación física es tarea de la asignación (B es falsa). La replicación aumenta costo en escrituras, no lo minimiza (A es falsa). Principio afectado: Interdependencia de Decisiones Fundamentales de Diseño.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 5
Enunciado: Escriba el término metodológico que describe el enfoque arquitectónico aplicado cuando el objetivo es construir un Esquema Conceptual Global (GCS) integrando bases de datos locales y autónomas preexistentes.

Respuesta Correcta: BOTTOM-UP
Explicación: El enfoque Bottom-Up invierte el flujo Top-Down, iniciando desde los esquemas locales hacia la consolidación global para resolver la heterogeneidad y sistemas heredados. Principio afectado: Metodología de Integración de Esquemas.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 6
Enunciado: Proporcione las siglas exactas en inglés del esquema resultante que unifica la vista de todos los datos distribuidos tras superar los conflictos de heterogeneidad en el diseño Bottom-Up.

Respuesta Correcta: GCS
Explicación: GCS (Global Conceptual Schema) es el producto final del proceso Bottom-Up que garantiza la transparencia total de distribución hacia las aplicaciones cliente. Principio afectado: Arquitectura de Referencia de Bases de Datos Distribuidas.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 7
Enunciado: Las consultas y transacciones distribuidas enfrentan barreras insalvables de latencia cuando no cumplen con el principio de localización total. Teóricamente, ¿qué factores agravan ineludiblemente la penalización de procesamiento remoto en un Join distribuido?

Opciones:
A) La transferencia masiva de datos y el overhead del protocolo agravan la penalización.
B) La sincronización diferida elimina completamente la latencia del protocolo de red local.
C) El control de integridad local garantiza que no exista un retardo temporal perceptible.
D) La localización parcial permite que todas las consultas se ejecuten sin validación local.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: A
Explicación: La teoría indica que el overhead de protocolo (validar permisos/bloqueos remotos) y la transferencia masiva de datos hacen que una operación distribuida sea órdenes de magnitud más costosa que una local (A es correcta). La sincronización diferida no "elimina" latencia de red, la asume (B es falsa). Principio afectado: Penalización de Rendimiento por Localización Parcial.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 8
Enunciado: En sistemas que aplican fragmentación en sus atributos de restricción de integridad (ej. claves foráneas distribuidas), se produce el riesgo teórico de "Inconsistencia Temporal". ¿Qué describe axiomáticamente este fallo?

Opciones:
A) El retardo de propagación ansiosa obliga a bloquear la restricción local asíncrona.
B) Se valida positivamente en un nodo mientras los datos referenciados mutan en otro nodo.
C) La fragmentación de atributos de integridad garantiza la sincronización entre réplicas.
D) El sistema requiere rediseño estático inmediato para evitar bloqueos en bases de datos.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: La Inconsistencia Temporal ocurre debido a que la evaluación de integridad requiere coordinación global, permitiendo que un nodo confirme una regla basándose en un estado que simultáneamente está siendo alterado por otra transacción en un nodo remoto. Principio afectado: Control de Integridad Distribuida.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 9
Enunciado: Los entornos reales padecen de estaticidad. Relacione cada factor del problema operativo de reconfiguración dinámica con su definición técnica exacta.

Elementos:
A) Migración de datos
B) Detección de cambios
C) Rediseño incremental
D) Penalización de rendimiento

Opciones:
1. Exige ajustes parciales iterativos que minimizan la perturbación del sistema en producción en lugar de empezar de cero.
2. Identifica cuándo el diseño actual ha dejado de ser eficiente requiriendo monitoreo continuo de los patrones de acceso.
3. Incurre en latencia excesiva originada por la comunicación remota en escenarios de fragmentos descentralizados.
4. Mover tuplas físicamente entre nodos para rebalancear la carga, induciendo costos de tráfico y tiempos de indisponibilidad.

Respuesta Correcta: A-4, B-2, C-1, D-3
Explicación: La reconfiguración dinámica ataca la estaticidad mediante el monitoreo constante (Detección), ejecutando ajustes modulares (Rediseño Incremental) y trasladando registros (Migración), para mitigar los costos de latencia (Penalización). Principio afectado: Optimización Adaptativa de DDBMS.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 10
Enunciado: Concepto clave que describe el pilar de diseño distribuido que busca ajustar la arquitectura de forma continua e iterativa basándose en el comportamiento real del flujo de información, para evitar rediseños estáticos completos.

Respuesta Correcta: OPTIMIZACION ADAPTATIVA
Explicación: La Optimización Adaptativa es el contrapeso al problema de estaticidad de los entornos en producción, fundamentada en análisis de workloads en tiempo real. Principio afectado: Ciclo de Vida de Diseño Distribuido.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 11
Enunciado: Fenómeno de red donde el diseño no logra ubicar todos los requerimientos transaccionales o los predicados de una consulta en un solo sitio físico, obligando a emplear protocolos distribuidos.

Respuesta Correcta: LOCALIZACION PARCIAL
Explicación: La Localización Parcial rompe el principio de acceso local puro, desatando la penalización de rendimiento e invocando Joins distribuidos y protocolos como el 2PC. Principio afectado: Teorema de Transparencia de Distribución.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 12
Enunciado: Al adoptar estrategias de replicación para solventar la disponibilidad, el arquitecto enfrenta un balance estricto dictado por la teoría de propagación de datos. ¿Cuál es el compromiso axiomático (trade-off) de esta decisión?

Opciones:
A) Beneficia lecturas reduciendo latencia y perjudica escrituras requiriendo sincronismo.
B) Incrementa radicalmente la latencia local al exigir propagación perezosa ininterrumpida.
C) Disminuye la disponibilidad del sistema al eliminar las dependencias de acceso asíncrono.
D) Permite omitir las verificaciones distribuidas de integridad en todas las transacciones.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: A
Explicación: La replicación permite resolver consultas R(x) en el nodo más cercano reduciendo el tráfico de red, pero impone que toda W(x) asuma la penalización del protocolo de sincronización mutua (Trade-off de Lectura/Escritura). Principio afectado: Modelo de Equivalencia de Copia Única.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 13
Enunciado: El criterio de "Serializabilidad de Copia Única" (1SR) es el estándar formal para validar esquemas de concurrencia replicada. ¿Qué postula matemáticamente su axioma de corrección?

Opciones:
A) Exige que todas las historias locales sean idénticas a una ejecución paralela asíncrona.
B) El resultado de historias globales debe equivaler a una ejecución serial en copia única.
C) Obliga a que la propagación perezosa mantenga la divergencia temporal en sus réplicas.
D) Garantiza consistencia mutua al impedir cualquier operación de lectura sobre nodos locales.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: 1SR (One-Copy Serializability) exige que la unión de las historias locales de ejecución (Historia Global) produzca el mismo resultado matemático que si las transacciones se ejecutaran de manera secuencial (serial) sobre un único servidor no replicado. Principio afectado: Teoría de Control de Concurrencia y Serializabilidad.

[TIPO: ORDENAMIENTO]
Pregunta ID: 14
Enunciado: El protocolo 2PC (Two-Phase Commit) garantiza la atomicidad de transacciones distribuidas en presencia de fallos. Ordene el flujo estricto de mensajes e interacciones entre el Coordinador y los Sitios.

Opciones:
1. El coordinador global emite el mensaje COMMIT a todos los nodos de la topología.
2. Los sitios participantes verifican su estado y responden al coordinador con READY.
3. El coordinador global envía el mensaje PREPARE a todos los sitios participantes.
4. Cada nodo participante aplica los cambios a disco y confirma finalización.

Respuesta Correcta: 3, 2, 1, 4
Explicación: La Fase 1 (Preparación) exige que el coordinador envíe PREPARE (3) y reciba READY de todos (2). La Fase 2 (Decisión) comienza con el envío del COMMIT global (1) seguido de la aplicación física de los bloqueos a disco (4). Principio afectado: Protocolos de Consenso y Atomicidad Global.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 15
Enunciado: En el marco del Teorema CAP, los protocolos de propagación difieren en el manejo de la latencia y la coherencia del estado transaccional. Compare teóricamente la propagación Ansiosa (Eager) frente a la Perezosa (Lazy).

Opciones:
A) La propagación ansiosa garantiza consistencia fuerte aplicando los cambios tras el commit.
B) La propagación perezosa disminuye la latencia asumiendo divergencias temporales del dato.
C) La estrategia perezosa bloquea el sistema si un nodo primario interrumpe su conectividad.
D) La técnica ansiosa permite lecturas obsoletas controladas mediante serialización épsilon.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: La propagación Lazy aplica actualizaciones en réplicas mediante transacciones de refresco *después* del commit original, bajando latencia a costa de Consistencia Eventual (B es correcta). Eager aplica *antes* del commit (A es falsa) y causa bloqueos ante fallos de red (C es falsa). Principio afectado: Modelos de Consistencia y Teorema CAP.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 16
Enunciado: En sistemas de consistencia eventual, el gestor de réplicas admite inconsistencias transitorias parametrizables. Relacione la Restricción de Frescura de Datos con su límite formal aplicable.

Elementos:
A) Límite de tiempo
B) Límite de valor
C) Límite de deriva en múltiples ítems
D) Serializabilidad épsilon (ESR)

Opciones:
1. Se tolera un margen de divergencia expresado como diferencia absoluta o porcentual del registro.
2. Define el retraso máximo permitido en unidades cronológicas (ej. 5 minutos) respecto al maestro.
3. Modula el umbral de error máximo basándose en la cantidad de operaciones de escritura concurrentes pendientes.
4. Acota la inconsistencia limitando la diferencia de las marcas de tiempo entre múltiples variables consultadas en un join.

Respuesta Correcta: A-2, B-1, C-4, D-3
Explicación: Las políticas relajan ACID permitiendo lectura de datos obsoletos mediante cotas estrictas: tiempo (cronológico), valor (numérico), deriva (diferencia de timestamps de lectura múltiple) y ESR (error por escrituras en cola). Principio afectado: Relajación de la Consistencia Mutua.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 17
Enunciado: Escriba el acrónimo del protocolo de control de copias que asegura consistencia fuerte mapeando toda operación R(x) a la réplica más cercana, pero forzando que W(x) bloquee y actualice todos los nodos simultáneamente.

Respuesta Correcta: ROWA
Explicación: ROWA (Read-One Write-All) es la base del control síncrono que prioriza latencia de lectura pero penaliza fuertemente el rendimiento de escritura y disponibilidad en presencia de particiones. Principio afectado: Protocolo Quorum y Consistencia Fuerte.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 18
Enunciado: Nombre del grado de abstracción en replicación centralizada donde el gestor de transacciones intercepta las sentencias de escritura y las enruta directamente al nodo maestro sin que la aplicación cliente sepa de la distribución física.

Respuesta Correcta: TRANSPARENCIA TOTAL
Explicación: A diferencia de la Transparencia Limitada (donde la aplicación debe apuntar explícitamente al maestro), la Transparencia Total esconde la complejidad topológica en el motor de bases de datos. Principio afectado: Transparencia de Distribución.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 19
Enunciado: El diseño de la fragmentación vertical enfrenta complejidad exponencial (Número de Bell). Al contrastar heurísticas matemáticas, ¿cuál es el comportamiento axiomático que diferencia al enfoque de Splitting respecto al de Grouping?

Opciones:
A) Grouping parte del esquema global y divide atributos produciendo fragmentos superpuestos.
B) Splitting agrupa atributos desde cero buscando minimizar la redundancia en claves primarias.
C) Splitting divide la relación completa generando fragmentos disjuntos y alineados al acceso.
D) Grouping emplea el algoritmo de Bell para resolver la complejidad exponencial de atributos.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Splitting es un enfoque Top-Down que corta la relación global en fragmentos limpios evitando redundancias de datos no clave (C es correcta). Grouping es Bottom-Up, parte de atributos aislados y genera Overlapping (A y B son falsas). Principio afectado: Algoritmia de Diseño Físico Vertical.

[TIPO: ORDENAMIENTO]
Pregunta ID: 20
Enunciado: El diseño vertical se fundamenta en un flujo analítico lineal para calcular los límites de fragmentación óptimos. Ordene los pasos formales de este algoritmo secuencial de optimización.

Opciones:
1. Reordenar las filas y columnas aplicando el Bond Energy Algorithm (BEA) para formar bloques densos diagonales (CA).
2. Construir la Matriz de Afinidad de Atributos (AA) procesando el uso de datos y frecuencia de consultas por sitio.
3. Evaluar el punto de corte con el algoritmo SPLIT para separar atributos minimizando cruces de red.
4. Auditar las trazas de uso en producción para identificar frecuencias y predicados (Recolección).

Respuesta Correcta: 4, 2, 1, 3
Explicación: El proceso requiere capturar la frecuencia (4), con la cual se calcula la afinidad matricial inicial AA (2). Luego, BEA reordena la matriz agrupando densidades CA (1), permitiendo que SPLIT trace el corte matemático final (3). Principio afectado: Heurística BEA-SPLIT de Diseño Vertical.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 21
Enunciado: Toda estrategia de fragmentación está sometida a un teorema de correctitud que previene pérdida de datos e inconsistencias transaccionales. Empareje la regla formal con su justificación estructural.

Elementos:
A) Regla de Completitud.
B) Regla de Reconstrucción (Horizontal).
C) Regla de Reconstrucción (Vertical).
D) Regla de Disjuntividad (Vertical).

Opciones:
1. Restringe la duplicación de atributos no clave, exigiendo como única redundancia obligatoria la Clave Primaria.
2. Garantiza la recuperación de la tabla global aplicando exclusivamente operadores de UNION lógica.
3. Garantiza la recuperación de la tabla global aplicando exclusivamente operadores relacionales de EQUI-JOIN.
4. Postula que todo elemento discreto (tupla o atributo) de GCS debe estar mapeado en el modelo físico fragmentado.

Respuesta Correcta: A-4, B-2, C-3, D-1
Explicación: Completitud evita fugas mapeando todo dato. Reconstrucción exige UNION para fragmentos horizontales y JOIN (sobre PK compartida) para los verticales. Disjuntividad vertical restringe solapamientos de columnas, tolerando solo la PK. Principio afectado: Reglas de Correctitud de Fragmentación.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 22
Enunciado: Durante el diseño del particionamiento (Sharding), el administrador emplea el algoritmo COM_MIN sobre los filtros de las sentencias WHERE. ¿Qué garantiza teóricamente la salida de este algoritmo?

Opciones:
A) Asegura que cada fragmento vertical contenga obligatoriamente la clave de reconstrucción.
B) Produce un conjunto de predicados completo y mínimo para fragmentación horizontal óptima.
C) Genera el grafo de join para determinar la correspondencia semántica de las tablas hijas.
D) Descompone la tabla aprovechando las contradicciones e implicaciones lógicas redundantes.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: COM_MIN purga filtros redundantes y garantiza que el conjunto final de predicados simples sea Completo (todas las tuplas clasificadas) y Mínimo (cada filtro causa un cambio real en el enrutamiento). Principio afectado: Álgebra Relacional en Fragmentación Horizontal Primaria.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 23
Enunciado: Identifique el nombre del postulado empírico que dicta que en el diseño horizontal no se evalúan todas las consultas de la red, ya que el 20% de las transacciones son responsables de la inmensa mayoría de la carga sistémica.

Respuesta Correcta: REGLA DEL 80/20
Explicación: La regla de Pareto o Regla del 80/20 justifica reducir el universo de análisis transaccional a la muestra estadísticamente dominante de operaciones. Principio afectado: Heurística de Optimización de Carga de Trabajo.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 24
Enunciado: Proporcione el término matemático formal que cuantifica la complejidad combinatoria inmanejable de la fragmentación vertical (ej. 10^23 opciones para m=30 atributos), demostrando que es un problema NP-Duro.

Respuesta Correcta: NUMERO DE BELL
Explicación: El Número de Bell, denotado como B(m), define todas las particiones posibles de un conjunto, obligando a los DDBMS a utilizar heurísticas de agrupamiento/división en vez de fuerza bruta. Principio afectado: Complejidad Computacional del Diseño Físico.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 25
Enunciado: La clasificación arquitectónica difiere drásticamente entre autores. Al comparar el enfoque lógico de Rahimi frente al operativo de Connolly, ¿cuál de las siguientes sentencias representa un contraste riguroso?

Opciones:
A) Rahimi garantiza un balance operativo mediante sincronización diferida y tolerante a fallos.
B) Connolly prioriza la disponibilidad estructural sobre la latencia física en transacciones.
C) Rahimi opera en el nivel lógico-arquitectónico mientras Connolly prioriza costos fijos.
D) Ambos teóricos prohíben explícitamente el uso de réplicas en redes de área amplia lenta.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Rahimi (2010) modela topologías abstractas (nivel lógico, ej. Distribución Mixta), mientras Connolly (2015) traduce estas decisiones en optimización de variables operativas de infraestructura de red como el ancho de banda y el hardware subyacente. Principio afectado: Taxonomías de Alocación de Datos.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 26
Enunciado: Rahimi (2010) clasifica la topología de base de datos en cinco patrones axiomáticos. Relacione la abstracción arquitectónica con su comportamiento ante fallos y carga.

Elementos:
A) No Replicado, No Fragmentado.
B) Totalmente Replicado.
C) Fragmentado o Particionado puro.
D) Parcialmente Replicado.
E) Distribución Mixta.

Opciones:
1. Máxima flexibilidad estructural, integra y balancea simultáneamente múltiples niveles de redundancia y partición.
2. Incurre en joins distribuidos costosos, posee alta localidad y elimina de raíz la sobrecarga transaccional de sincronismo.
3. Máxima disponibilidad y latencia cero de lectura, pero demanda el mayor costo computacional durante las escrituras globales.
4. Genera un cuello de botella sistémico único que condena a la topología si el enlace de red hacia su único nodo colapsa.
5. Permite una tolerancia a fallos selectiva, duplicando exclusivamente los subconjuntos del negocio que son de alta criticidad.

Respuesta Correcta: A-4, B-3, C-2, D-5, E-1
Explicación: El modelo centralizado es un cuello de botella (A-4). Totalmente replicado prioriza la lectura al coste de la escritura (B-3). El particionado puro elimina redundancia (C-2). Parcialmente replicado busca eficiencia de costos (D-5). Mixta combina todo (E-1). Principio afectado: Patrones de Distribución Lógica de Rahimi.

[TIPO: ORDENAMIENTO]
Pregunta ID: 27
Enunciado: El estándar SQL/MED (postgres_fdw) habilita la lectura descentralizada de nodos foráneos simulando transparencia. Ordene el flujo jerárquico estricto requerido para levantar el túnel perimetral en PostgreSQL.

Opciones:
1. Utilizar CREATE USER MAPPING para vincular localmente el perfil de seguridad con la base foránea.
2. Levantar los objetos Proxy del esquema mediante CREATE FOREIGN TABLE o IMPORT.
3. Configurar la infraestructura del canal IP remoto ejecutando CREATE SERVER.
4. Habilitar la librería interna del motor DDBMS mediante CREATE EXTENSION postgres_fdw.

Respuesta Correcta: 4, 3, 1, 2
Explicación: La configuración sigue un principio de anillos de seguridad: Activar módulo binario en memoria (4), configurar infraestructura de red y puerto (3), superar capa de autenticación perimetral (1) y finalmente clonar metadatos lógicos (2). Principio afectado: Arquitectura de Datos Externos (FDW).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 28
Enunciado: Las funciones de costo formalizan el algoritmo de asignación física (Alocación). ¿Qué define el comportamiento teórico diferencial entre alocación Estática y Dinámica de fragmentos?

Opciones:
A) La dinámica reubica datos en tiempo real pero introduce costos de migración y monitoreo.
B) La estática ajusta constantemente las métricas de red para prevenir un punto de fallo.
C) La dinámica requiere replicación completa síncrona para garantizar consistencia eventual.
D) La estática es más compleja de implementar debido a los algoritmos de costos heurísticos.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: A
Explicación: La Alocación Dinámica traslada fragmentos respondiendo a fluctuaciones de carga (migración física y overhead de monitoreo), mientras la Estática es inmutable (B es falsa, D es falsa porque la dinámica es más compleja). Principio afectado: Algoritmos de Alocación y Distribución Óptima.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 29
Enunciado: En la arquitectura física de clústeres PostgreSQL, escriba el nombre completo con extensión del archivo matriz que gestiona la seguridad de red, la validación de sockets TCP y los algoritmos criptográficos permitidos por host.

Respuesta Correcta: PG_HBA.CONF
Explicación: pg_hba.conf (Host-Based Authentication) constituye la barrera principal que el DDBMS usa para validar conexiones externas antes de que el motor de consultas actúe. Principio afectado: Autenticación Perimetral de Gestores de Bases de Datos.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 30
Enunciado: Axioma computacional formulado originalmente por Eric Brewer que demuestra lógicamente la imposibilidad de que un sistema distribuido garantice simultáneamente Consistencia perfecta, Disponibilidad absoluta y Tolerancia a las Particiones de red.

Respuesta Correcta: TEOREMA CAP
Explicación: El Teorema CAP rige todo el diseño de sistemas distribuidos, determinando que los arquitectos siempre deben optar por ceder consistencia inmediata (AP) o disponibilidad (CP) cuando falla la red. Principio afectado: Teorema Fundamental de Bases de Datos Distribuidas.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 31
Enunciado: En el modelo de Fragmentación Horizontal Derivada, ¿qué regla matemática o estructural rige el diseño axiomáticamente para asegurar la resolución de subconsultas sin transferencia entre nodos?

Opciones:
A) La matriz de afinidad determina los predicados simples aplicables a las tablas hijas base.
B) El algoritmo BEA agrupa atributos de join local para asegurar la reconstrucción vertical.
C) La disjuntividad vertical permite solapamiento de claves primarias en los grafos de join.
D) La tabla padre hereda granularidad de la hija garantizando consistencia y alta latencia.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: E
Explicación: En Fragmentación Derivada, la tabla HIJA hereda la partición de la tabla PADRE (basado en el Grafo de Join y claves foráneas), no a la inversa (D es falsa). La matriz de afinidad y el algoritmo BEA son exclusivos de la fragmentación vertical (A y B falsas). La disjuntividad no trata solapamientos en grafos de join horizontales. Principio afectado: Integridad Referencial en Diseño Horizontal Derivado.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 32
Enunciado: En el marco de control de réplicas, al evaluar los perfiles de gestión de actualización distribuida como el modelo "Update Anywhere", ¿qué aserción define el teorema de operaciones correctas?

Opciones:
A) El sitio maestro centraliza las actualizaciones evitando requerir protocolos de consenso.
B) La copia primaria delega todas las actualizaciones a un único sitio para reducir latencia.
C) El modelo "single master" distribuye la carga de escritura equitativamente en la red local.
D) La transparencia limitada intercepta las escrituras dirigiéndolas al maestro de forma local.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: E
Explicación: El modelo "Update Anywhere" no tiene maestros fijos, permite mutaciones en cualquier réplica local forzando a una reconciliación asíncrona global. Las opciones fallan teóricamente: Single master no distribuye carga (C falsa), transparencia limitada NO intercepta automáticamente (D falsa, esa es total), la copia primaria admite distintos maestros por fragmento, no un único sitio global (B falsa). Principio afectado: Modelos de Ejecución y Ubicación de Actualizaciones.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 1
Enunciado: Un administrador altera el agrupamiento físico (clustering) en los discos de un nodo de bases de datos distribuidas. Según la teoría formal ANSI/SPARC extendida para SGBDD, ¿qué esquemas sufren una modificación algorítmica obligatoria?

Opciones:
A) Altera el esquema externo para soportar nuevas estructuras físicas del hardware.
B) Modifica el esquema conceptual global para mantener estricta consistencia lógica.
C) Cambia el esquema conceptual local para evitar severas caídas de rendimiento red.
D) Afecta exclusivamente al esquema interno local sin impactar modelos superiores.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: D
Explicación: Principio de Independencia Física de Datos. La separación estricta entre el Esquema Conceptual y el Esquema Interno garantiza que las alteraciones en el nivel de hardware (clustering, estructuras de archivos) modifiquen únicamente el Esquema Interno Local (LIS), aislando completamente las capas lógicas y las vistas externas (LCS, GCS, ES).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 2
Enunciado: Indique el acrónimo del esquema que, en la extensión distribuida de ANSI/SPARC, describe cómo se dividen o mapean los registros lógicamente en un nodo específico para gestionar la fragmentación local (puente entre el modelo físico y el global).

Respuesta Correcta: LCS
Explicación: El Esquema Conceptual Local (Local Conceptual Schema - LCS) actúa como la capa intermedia que modela la porción local de los datos para posibilitar el mapeo de la fragmentación hacia el Esquema Conceptual Global.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 3
Enunciado: Relacione los esquemas de la arquitectura ANSI/SPARC distribuida con su función formal en el ecosistema.

Opciones:
1. Esquema Interno Local (LIS)
2. Esquema Conceptual Local (LCS)
3. Esquema Conceptual Global (GCS)
4. Esquema Externo (ES)

A) Proporciona vistas adaptadas excluyendo datos no requeridos.
B) Define compresión, gestión de bloques y ubicación en disco.
C) Unión lógica que habilita transparencia de red globalmente.
D) Describe la organización lógica completa del nodo particular.

Respuesta Correcta: 1-B, 2-D, 3-C, 4-A
Explicación: El LIS gestiona el hardware (B). El LCS es el puente lógico local (D). El GCS abstrae y unifica toda la base distribuida (C). El ES filtra y restringe las vistas según roles, brindando independencia lógica (A).

[TIPO: ORDENAMIENTO]
Pregunta ID: 4
Enunciado: Ordene estrictamente el flujo de mapeo de abstracción en una arquitectura distribuida (ANSI/SPARC extendida), desde el nivel más bajo (hardware local) hacia la vista final consumida por el usuario.

Opciones:
1. Esquema Conceptual Global (GCS)
2. Esquema Externo (ES)
3. Esquema Interno Local (LIS)
4. Esquema Conceptual Local (LCS)

A) 3, 4, 1, 2
B) 3, 1, 4, 2
C) 1, 3, 4, 2
D) 4, 3, 1, 2
E) 2, 1, 4, 3

Respuesta Correcta: A
Explicación: La jerarquía estructural se levanta desde el disco físico (LIS), se mapea a la lógica del sitio (LCS), se consolida en el modelo unificado de la red (GCS) y finalmente se proyecta hacia la aplicación o usuario final (ES).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 5
Enunciado: Al desplegar un SGBDD utilizando `postgres_fdw`, se identifican ciertos bloqueos transaccionales a nivel de clúster. Según el análisis teórico, ¿cuál es la limitación axiomática de esta extensión?

Opciones:
A) Impide configurar tablas remotas como instancias lógicas locales en la memoria RAM.
B) Bloquea la fragmentación horizontal declarativa al combinar múltiples nodos de red.
C) Carece de mecanismos nativos para el control de transacciones 2PC y la replicación.
D) Requiere que todos los nodos compartan exactamente el mismo esquema interno local.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Principio de Control Transaccional Distribuido. `postgres_fdw` actúa como un puente de comunicación para acceso remoto transparente, pero no satisface los requisitos de un DBMS Distribuido completo porque no gestiona protocolos de consistencia (como el 2 Phase Commit) ni replicación nativa.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 6
Enunciado: Identifique el acrónimo del esquema que proporciona la visión unificada de todos los datos en una arquitectura Peer-to-Peer, constituyéndose como la unión de todos los esquemas locales para habilitar la transparencia de red.

Respuesta Correcta: GCS
Explicación: El Esquema Conceptual Global (Global Conceptual Schema - GCS) asume la responsabilidad teórica de ocultar la fragmentación y ubicación física para simular un modelo centralizado a nivel lógico.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 7
Enunciado: En un modelo distribuido "Heterogéneo Multilingüe", el nodo de Quito opera sobre Oracle y el de Guayaquil sobre PostgreSQL. Bajo esta configuración teórica, ¿cómo se resuelve formalmente el procesamiento de consultas por parte de los usuarios locales?

Opciones:
A) Los usuarios operan el sistema global con un único lenguaje de consulta estandarizado.
B) Todos los nodos utilizan el mismo modelo relacional garantizando conexión directa.
C) Cada usuario consulta la base global utilizando el lenguaje nativo de su sistema base.
D) El optimizador global bloquea las peticiones que no usan el dialecto predeterminado.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Arquitectura Heterogénea Multilingüe. Este principio establece que el sistema distribudo debe soportar que el usuario envíe la consulta en el dialecto SQL de su propio motor local, obligando a la capa superior a ejecutar los mapeos hacia el Esquema Conceptual Global y a otros dialectos.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 8
Enunciado: Empareje las subdimensiones teóricas de la "Autonomía" con la definición que rige su nivel de independencia en el SGBD local.

Opciones:
1. Autonomía de Diseño
2. Autonomía de Comunicación
3. Autonomía de Ejecución

A) El SGBD procesa las transacciones que recibe según sus propios algoritmos de control.
B) El SGBD determina libremente qué porción de información decide exponer a la red.
C) El SGBD escoge su propio modelo de datos y técnicas de gestión para su estructura.

Respuesta Correcta: 1-C, 2-B, 3-A
Explicación: La autonomía en un SGBD se divide ortogonalmente: Diseño (C - modelo de datos/técnicas), Comunicación (B - integración selectiva/qué exponer), y Ejecución (A - control de transacciones y concurrencia).

[TIPO: ORDENAMIENTO]
Pregunta ID: 9
Enunciado: Según el modelo arquitectónico de un DBMS centralizado genérico, ordene cronológicamente el flujo descendente (Top-Down) de una consulta desde su emisión hasta el soporte de recuperación.

Opciones:
1. Interfaz (Gestión de vistas y cálculo relacional)
2. Control (Integridad semántica y autorización)
3. Compilación (Álgebra relacional y optimización)
4. Ejecución (Sincronización de plan de acceso)
5. Acceso a Datos (Buffers y métodos físicos)
6. Consistencia (Control de concurrencia y logs)

A) 1, 2, 3, 4, 5, 6
B) 1, 3, 2, 5, 4, 6
C) 2, 1, 3, 4, 6, 5
D) 1, 2, 4, 3, 5, 6
E) 1, 3, 4, 2, 6, 5

Respuesta Correcta: A
Explicación: El modelo en cascada de Özsu & Valduriez establece una estricta dependencia algorítmica: la interfaz formula (1), el control valida semántica (2), se compila en álgebra relacional (3), se orquesta la ejecución (4), se ingresa a memoria/disco (5) y se garantizan propiedades ACID en disco (6).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 10
Enunciado: Al mapear un modelo DBMS centralizado genérico con la arquitectura abstracta de ANSI/SPARC, ¿qué capas operativas corresponden intrínseca y biyectivamente al Nivel Conceptual?

Opciones:
A) Corresponde directamente a la capa de interfaz que maneja todas las vistas externas.
B) Corresponde a las capas de acceso a datos y control de consistencia transaccional.
C) Corresponde a las capas de control, compilación algorítmica y ejecución orquestada.
D) Corresponde al enrutador de red que distribuye las consultas entre los servidores BD.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Principio de Mapeo Funcional. La Interfaz mapea al Nivel Externo. El Nivel Conceptual (lógica, estructura y validación) mapea a Control (semántica), Compilación (optimización) y Ejecución. Acceso/Consistencia mapean al Nivel Interno.

[TIPO: RESPUESTA CORTA]
Pregunta ID: 11
Enunciado: Indique el término técnico formal que describe el nivel de autonomía donde cada SGBD opera independientemente, rechaza integraciones y desconoce por completo la existencia de otros sistemas en su entorno.

Respuesta Correcta: AISLAMIENTO TOTAL
Explicación: El "Aislamiento Total" es la configuración de autonomía donde no hay esquemas federados ni comunicación de red compartida para la resolución transaccional distribuida.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 12
Enunciado: ¿Cuál de los siguientes escenarios define formalmente un ecosistema con nivel de autonomía de "Integración Sólida"?

Opciones:
A) Semiautonomía impone un control central para asegurar disponibilidad del repositorio.
B) Aislamiento total exige que el optimizador global gestione los bloqueos distribuidos.
C) Integración sólida centraliza el procesamiento eliminando la independencia operativa.
D) Semiautonomía prohibe compartir datos para preservar la privacidad interinstitucional.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Dimensión de Autonomía de Control. En la integración sólida, un único DBMS controla por completo el procesamiento lógico y transaccional, suprimiendo la capacidad de los nodos para actuar de forma independiente ante la red.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 13
Enunciado: Al desacoplar servidores implementando un "Servidor de Base de Datos" dedicado (Modelo C/S), el sistema elimina cuellos de botella de hardware. Sin embargo, ¿qué sacrificio teórico (trade-off) se asume estructuralmente?

Opciones:
A) Obliga a los clientes a asumir la carga de enrutamiento hacia diferentes sub-sistemas.
B) Elimina el cuello de botella físico pero crea inevitablemente un único punto de red.
C) Exige que el manejador de interfaz traduzca el SQL a álgebra relacional pura siempre.
D) Añade latencia de red que solo se justifica con consultas de alto costo computacional.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: D
Explicación: Principio de Overhead de Comunicación. Desacoplar la aplicación y la base de datos incrementa las transferencias por red. Este costo arquitectónico solo se amortiza teóricamente si el motor asume cargas intensivas o paralelismo que compensen dicha latencia.

[TIPO: ORDENAMIENTO]
Pregunta ID: 14
Enunciado: En el software interno del SERVIDOR de una arquitectura de referencia Cliente/Servidor, ordene el flujo de procesamiento de una orden recibida de arriba hacia abajo.

Opciones:
1. Controlador Semántico de Datos
2. Optimizador de Consultas
3. Gestor de Transacciones
4. Gestor de Recuperación
5. Procesador de Soporte en Tiempo de Ejecución (Runtime)

A) 2, 1, 3, 5, 4
B) 1, 2, 3, 4, 5
C) 3, 1, 2, 4, 5
D) 2, 3, 1, 5, 4
E) 1, 3, 2, 4, 5

Respuesta Correcta: B
Explicación: La pila del servidor evalúa semántica (1), luego optimiza a álgebra (2), administra la transacción y bloqueos lógicos (3), coordina su registro de logs/recuperación (4) y finaliza delegando las llamadas físicas al sistema operativo (5).

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 15
Enunciado: Relacione la variación del modelo Cliente/Servidor con su característica técnica definitoria.

Opciones:
1. Múltiples clientes, Servidor único
2. Múltiples clientes, Múltiples servidores - Cliente pesado
3. Múltiples clientes, Múltiples servidores - Servidor home

A) Cada terminal soporta mayor carga lógica al gestionar su conexión a múltiples nodos.
B) Simplifica el terminal forzándolo a conectarse a un nodo que asume la coordinación.
C) Centralización total que se convierte arquitectónicamente en punto único de fallo.

Respuesta Correcta: 1-C, 2-A, 3-B
Explicación: El servidor único es un SPOF (C). El cliente pesado asume latencias y lógicas de enrutamiento (A). El servidor home actúa como proxy/coordinador para aliviar al cliente (B).

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 16
Enunciado: De acuerdo con la arquitectura de referencia Cliente/Servidor para bases de datos relacionales, ¿qué elementos transitan estrictamente desde el módulo cliente hacia el sistema operativo del servidor?

Opciones:
A) Fluyen árboles lógicos de álgebra relacional completamente optimizados por los nodos.
B) Fluyen los comandos de control de concurrencia para bloquear las tablas a distancias.
C) Fluyen consultas estructuradas en SQL puro sin compilar hacia el motor centralizado.
D) Fluyen relaciones materializadas temporales para renderizar toda la interfaz gráfica.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Delimitación de Roles C/S. En el modelo relacional, la compilación y optimización de consultas se ejecutan enteramente en el servidor. El cliente es responsable de enviar el SQL crudo (cálculo relacional) y recibe la "relación resultado".

[TIPO: RESPUESTA CORTA]
Pregunta ID: 17
Enunciado: Indique el nombre del módulo en la arquitectura Cliente/Servidor que corre en la terminal de usuario y es responsable exclusivo de administrar la caché local y los bloqueos de transacciones del lado de la aplicación.

Respuesta Correcta: CLIENT DBMS
Explicación: El Client DBMS (o módulo DBMS local en el cliente) es el artefacto lógico en la capa del usuario encargado de la interacción preliminar, el manejo del estado local (caché) y la gestión de la sesión.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 18
Enunciado: Migrar un entorno hacia múltiples "Servidores de Bases de Datos Distribuidas" eleva la escalabilidad horizontal. ¿Cuál es la implicación teórica directa que se activa como coste de diseño en este escenario?

Opciones:
A) Simplifica extremadamente la recuperación de datos ante caídas de red asíncronas.
B) Exige sincronización altamente compleja para garantizar la consistencia distribuida.
C) Impide escalar el ecosistema horizontalmente debido a los bloqueos de los clientes.
D) Restringe la arquitectura a utilizar estrictamente el modelo jerárquico de base datos.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: Propiedades ACID en Sistemas Distribuidos. La partición y replicación de datos en varios servidores introduce la obligación de ejecutar protocolos de sincronización y consenso (como 2PC) para garantizar la consistencia transaccional global.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 19
Enunciado: La evolución de los sistemas P2P evidencia una divergencia profunda. A nivel de fundamentos, ¿cuál es el postulado arquitectónico que diferencia el P2P "Moderno" del P2P "Clásico"?

Opciones:
A) El modelo moderno exige nodos completamente homogéneos para operar algoritmos BD.
B) El modelo clásico carece de esquemas globales unificados para la red distribuida local.
C) El modelo moderno maneja altísima heterogeneidad sin asumir acuerdos inter-sistemas.
D) El modelo clásico utiliza un diseño topológico estrictamente centralizado en su entorno.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Autonomía P2P Moderna vs Clásica. El P2P clásico operaba con escasos nodos homogéneos y preacuerdos de consistencia; el P2P moderno introduce miles de nodos intermitentes sin acuerdos previos, elevando radicalmente la heterogeneidad y dificultando el control global.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 20
Enunciado: En un sistema P2P, los componentes coexisten en el mismo nodo físico divididos en el "Procesador de Usuario" y el "Procesador de Datos". Clasifique la pertenencia de los siguientes submódulos.

Opciones:
1. Optimizador Global de Consultas
2. Monitor de Ejecución Distribuida
3. Procesador Local de Consultas
4. Gestor Local de Recuperación

A) Procesador de Datos
B) Procesador de Usuario

Respuesta Correcta: 1-B, 2-B, 3-A, 4-A
Explicación: La capa de Usuario atiende el ecosistema lógico distribuido (optimizando la petición y coordinando con la red). La capa de Datos gestiona las instrucciones directas contra el disco, optimizando internamente y recuperando logs locales.

[TIPO: ORDENAMIENTO]
Pregunta ID: 21
Enunciado: Detalle la secuencia algorítmica por la que atraviesa una consulta global distribuida dentro de la máquina del Procesador de Usuario en P2P.

Opciones:
1. Validación (Revisión semántica y permisos vs GCS)
2. Recepción (Captura del SQL por manejador de interfaz)
3. Ejecución (Monitor distribuido coordina subconsultas)
4. Optimización (Descomposición basada en costos)
5. Integración (Ensamblaje de resultados de nodos)

A) 2, 4, 1, 3, 5
B) 2, 1, 4, 3, 5
C) 1, 2, 4, 3, 5
D) 2, 1, 3, 4, 5
E) 4, 2, 1, 3, 5

Respuesta Correcta: B
Explicación: El SQL entra a Interfaz (2), el Controlador avala la consistencia contra el GCS (1), el Optimizador Global divide en un plan algebraico fragmentado (4), el Monitor lo envía por la red (3), y finalmente los fragmentos convergen (5).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 22
Enunciado: ¿Cómo se denomina el tipo de abstracción que asegura que el usuario no deba conocer los criterios matemáticos con los que se han dividido las tablas (gracias a la resolución que efectúa el mapeo GCS-LCS)?

Respuesta Correcta: TRANSPARENCIA DE FRAGMENTACION
Explicación: La Transparencia de Fragmentación abstrae el diseño de particionamiento, ocultando si un registro se cortó horizontal o verticalmente para residir en distintos nodos.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 23
Enunciado: Durante el procesamiento de una transacción en un nodo P2P, ¿cuál es la responsabilidad teórica ineludible del Controlador Semántico de Datos antes de invocar al optimizador?

Opciones:
A) Descompone la consulta global en múltiples fragmentos de álgebra relacional validada.
B) Verifica restricciones de integridad y autorización definidas en el modelo global lógico.
C) Interactúa directamente con el log del sistema para resolver caídas de hardware de red.
D) Ensambla resultados parciales entregados por los procesadores locales para la interfaz.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: Responsabilidad Semántica. En el modelo formal de P2P, el controlador semántico compara la sentencia contra el Esquema Conceptual Global (GCS) exclusivamente para corroborar la integridad de reglas de dominio y los roles de seguridad de red.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 24
Enunciado: Ante la falla eléctrica de un nodo en el clúster P2P, ¿cuál es el comportamiento axiomático del "Gestor Local de Recuperación" al reiniciar el nodo?

Opciones:
A) Coordina la ejecución distribuida de transacciones entre todos los nodos involucrados.
B) Garantiza consistencia local frente a fallos analizando de inmediato el log del sistema.
C) Optimiza los árboles de consulta aplicando heurísticas estrictas de fragmentación datos.
D) Provee las vistas externas personalizadas ocultando la ubicación local de la base nodos.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: B
Explicación: Propiedades de Recuperación (Durability). El Gestor Local pertenece al procesador de datos, cuya única misión de tolerancia a fallos es usar el "System Log" para aplicar Rollback/Commit sobre las operaciones interrumpidas a nivel físico (disco), protegiendo la autonomía local.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 25
Enunciado: La integración de arquitecturas difiere drásticamente según el nivel de autonomía. ¿Qué axioma diferencia el diseño del GCS en un Sistema Multidatabase (MDBS) frente a un DBMS Distribuido Clásico?

Opciones:
A) El MDBS requiere que su esquema global englobe todos los registros locales de la red.
B) El DDBMS distribuye los datos integrando nodos de forma estricta de abajo a arriba.
C) El MDBS define un esquema global parcial integrando esquemas existentes bottom-up.
D) El DDBMS obliga a que todos sus clientes utilicen arquitecturas P2P centralizadas hoy.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Metodología Bottom-Up. A diferencia de un DDBMS (Top-Down, donde el GCS dicta todo), el MDBS se construye desde nodos heterogéneos y autónomos ya operativos que exportan una porción (esquema parcial) hacia arriba, consolidando un diseño Bottom-Up.

[TIPO: EMPAREJAMIENTO]
Pregunta ID: 26
Enunciado: En la arquitectura MDBS (Enfoque Mediador/Wrapper), relacione cada componente del diseño modular con su responsabilidad de abstracción funcional.

Opciones:
1. Capa MDBS
2. Mediador
3. Wrapper
4. DBMS Local

A) Subsistema base, ejecuta transacciones de manera autónoma como si fueran externas.
B) Traduce código canónico hacia dialectos T-SQL, PL/pgSQL específicos del motor base.
C) Estructura no invasiva superior que provee interacción global al cliente corporativo.
D) Abstrae el GCS global, divide las lógicas complejas y recibe datos de unificaciones.

Respuesta Correcta: 1-C, 2-D, 3-B, 4-A
Explicación: El MDBS envuelve sin invadir (C). El mediador gestiona el plan GCS (D). El wrapper aisla las disparidades del dialecto SQL mapeando al motor nativo (B). El DBMS subyacente mantiene su aislamiento (A).

[TIPO: ORDENAMIENTO]
Pregunta ID: 27
Enunciado: Determine el orden correcto en el que se estructuran y ensamblan las capas de esquemas en un entorno Multidatabase (MDBS) aplicando un diseño estricto de Abajo hacia Arriba (Bottom-up).

Opciones:
1. LIS (Local Internal Schema)
2. LCS (Local Conceptual Schema)
3. LES (Local External Schema o Export Schema)
4. GCS (Global Conceptual Schema)
5. GES (Global External Schema)

A) 1, 2, 4, 3, 5
B) 1, 2, 3, 4, 5
C) 5, 4, 3, 2, 1
D) 2, 1, 3, 4, 5
E) 1, 3, 2, 4, 5

Respuesta Correcta: B
Explicación: El disco define el físico (1), que define la lógica local (2), que filtra la porción a compartir (3), la cual se une con la de otros nodos en un consolidado global (4), sobre el que finalmente se proyectan interfaces al usuario final (5).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 28
Enunciado: ¿Qué esquema en la teoría MDBS representa exclusivamente el subconjunto de datos que un nodo autónomo decide voluntariamente "exportar" hacia la federación global, reteniendo privacidad sobre el resto?

Respuesta Correcta: LES
Explicación: El Local External Schema (LES o Esquema de Exportación) es la piedra angular del "Control Selectivo" en MDBS, permitiendo que la autonomía se mantenga inquebrantable al no exponer todo el esquema LCS.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 29
Enunciado: En un entorno MDBS heterogéneo donde coexisten motores SQL Server y NoSQL, la Capa Multi-DBMS sufre incompatibilidad de modelos. ¿Qué regla arquitectónica solventa de inmediato este choque?

Opciones:
A) Bloquea peticiones de nodos que implementan modelos de bases de datos relacionales.
B) Obliga a que todos los nodos exporten absolutamente toda su información almacenada.
C) Exige que el esquema interno local se reconstruya utilizando un dialecto SQL unificado.
D) Requiere la definición de un modelo canónico común para edificar el esquema global.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: D
Explicación: Teorema del Modelo Canónico. Para solucionar discrepancias estructurales (relacional vs objetos), el MDBS impone la construcción de un "Modelo Canónico" abstracto e intermediario en el Mediador, el cual absorbe y traduce las heterogeneidades de la red inferior.

[TIPO: OPCIÓN MÚLTIPLE]
Pregunta ID: 30
Enunciado: La "Capa MDBS" se diferencia estructuralmente de un orquestador transaccional típico de un DDBMS. ¿Cuál de las siguientes afirmaciones describe rigurosamente su principio operativo?

Opciones:
A) Invade el gestor local para modificar su algoritmo de procesamiento de concurrencia.
B) Suplanta el esquema interno local para controlar directamente el acceso a la memoria.
C) Actúa como software no invasivo proveyendo acceso sin alterar al sistema original.
D) Transforma todos los nodos distribuidos en servidores home para reducir la latencia.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.

Respuesta Correcta: C
Explicación: Principio No Invasivo. La capa Multi-DBMS reside por encima de los motores locales sin requerir que estos alteren su código fuente, sus técnicas de gestión ni su formato de disco. Para el motor local, las consultas del MDBS parecen emitidas por un usuario común más.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 1
Enunciado: En el contexto de los sistemas de bases de datos distribuidas, ¿cuál es la fundamentación axiomática del control de concurrencia respecto a la ejecución simultánea de transacciones?
Opciones:
A) Operar exclusivamente sobre las escrituras para generar historiales asíncronos.
B) Garantizar que la ejecución simultánea produzca resultados de ejecución serial.
C) Reemplazar totalmente las propiedades ACID con algoritmos de compensación global.
D) Eliminar de forma absoluta la necesidad de aislamiento aislando ramas completas.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Según el principio de serializabilidad matemática en el control de concurrencia, se asegura que la asincronía de un historial concurrente produzca resultados estrictamente equivalentes a una ejecución en serie (secuencial), preservando así el Aislamiento del Teorema ACID ante lecturas/escrituras cruzadas.

[TIPO: RESPUESTA CORTA] Pregunta ID: 2
Enunciado: ¿Qué término formal define el escenario en el que dos operaciones de transacciones concurrentes acceden a la misma unidad de datos y al menos una de ellas es de escritura (WRITE)?
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: CONFLICTO
Explicación: Acorde a la teoría de historiales, el axioma de "operaciones en conflicto" se satisface únicamente cuando comparten el mismo dato en memoria/disco y existe al menos una operación de modificación, dictaminando por ende que el orden temporal relativo de ejecución afecta ineludiblemente al estado final de la base de datos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 3
Enunciado: De acuerdo con la regla fundamental de los historiales de transacciones, ¿qué implicación teórica tiene la existencia de operaciones concurrentes que NO entran en conflicto sobre una misma unidad de datos?
Opciones:
A) Su orden de ejecución es irrelevante y no afecta en absoluto la corrección global.
B) Requieren forzosamente sincronización mediante un candado exclusivo distribuido.
C) Deben generar obligatoriamente una versión nueva de lectura para la consistencia.
D) Exigen la implementación de un protocolo en dos fases para la validación global.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: La regla fundamental establece axiomáticamente que el orden temporal en un historial solo tiene repercusiones cuando hay conflicto. Dos lecturas concurrentes (operaciones sin conflicto) sobre el mismo registro pueden entrelazarse y procesarse libremente sin violar jamás el teorema de serializabilidad final.

[TIPO: RESPUESTA CORTA] Pregunta ID: 4
Enunciado: Según la taxonomía de mecanismos de control de concurrencia, ¿cómo se denominan conceptualmente a los algoritmos que combinan primitivos de bloqueo y marcas de tiempo, pero carecen de implementación comercial práctica?
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: HÍBRIDOS
Explicación: La arquitectura teórica clasifica a los algoritmos que amalgaman candados (locking) y marcas de tiempo (timestamp ordering) como mecanismos "Híbridos". Esta hibridación permanece como una construcción académica referenciada, dado que no presentan escalabilidad ni adopción en motores SGBD distribuidos reales.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 5
Enunciado: En la capa de mecanismos pesimistas basados en bloqueo, ¿cuál es la restricción teórica universal que gobierna la matriz de compatibilidad entre los modos de candado de lectura (rl) y de escritura (wl)?
Opciones:
A) El de escritura permite concurrencia ilimitada con lecturas sin causar demoras.
B) La de lectura es compatible consigo misma, pero la escritura repele a las demás.
C) Ambos modos de candado son plenamente compatibles en sistemas de validación real.
D) Los candados limitan el acceso concurrente a lectores previniendo tuplas fantasma.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Apoyado en el teorema básico de "Locking", la exclusividad impuesta por un candado de escritura (wl) decreta matemáticamente incompatibilidad frente a cualquier otro intento de bloqueo (sea de lectura o escritura). Por el contrario, múltiples transacciones adquiriendo candados (rl) coexisten armónicamente.

[TIPO: RESPUESTA CORTA] Pregunta ID: 6
Enunciado: En la topología procedimental del protocolo Bloqueo en Dos Fases (2PL), ¿cómo se denomina técnicamente al instante temporal exacto en que la transacción adquiere su último candado necesario?
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: PUNTO DE BLOQUEO
Explicación: El teorema principal de 2PL (Eswaran et al.) estipula formalmente al "punto de bloqueo" como la frontera algorítmica que separa la fase inicial de crecimiento (exclusiva a la reserva y adquisición de recursos) de la subsecuente fase de decrecimiento (proceso exclusivo de liberación sistemática).

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 7
Enunciado: ¿Qué vulnerabilidad transaccional específica que padece el modelo de Bloqueo en Dos Fases (2PL) regular es resuelta categóricamente y de manera matemática mediante la variante 2PL Estricto?
Opciones:
A) El interbloqueo irresoluble generado por la reserva innecesaria en la fase inicio.
B) La escasez de identificadores al delegar control a un nodo único muy congestionado.
C) El encadenamiento de abortos causado al exponer estados no confirmados intermedios.
D) El sobrecosto computacional generado por el almacenamiento de versiones múltiples.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: El protocolo 2PL Estricto exige blindar todos los candados adquiridos reteniendo su liberación hasta el final transaccional (COMMIT/ROLLBACK). Este principio evita axiomáticamente los "abortos en cascada" (cascading aborts) pues aísla en su totalidad el acceso concurrente hacia estados inconsistentes no confirmados.

[TIPO: RESPUESTA CORTA] Pregunta ID: 8
Enunciado: En la orquestación distribuida del Bloqueo Centralizado (C2PL), ¿qué vulnerabilidad crítica en materia de disponibilidad y rendimiento se instaura en el nodo centralizador al canalizar el 100% de la carga del bloqueo?
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: CUELLO DE BOTELLA
Explicación: Al designar la otorgación, denegación y evaluación de concurrencia exclusivamente en un "administrador central", dicho nodo sufre saturación computacional degradándose arquitectónicamente en un embudo ("cuello de botella") y configurando un "Punto Único de Falla", socavando las ventajas de descentralización de la base de datos.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 9
Enunciado: Al evaluar las compensaciones algorítmicas del modelo de Bloqueo Distribuido (D2PL) comparado con su contraparte Centralizada (C2PL), ¿cuál es el costo inherente principal para salvaguardar la consistencia global?
Opciones:
A) Imposibilita la detección de interbloqueos debido a la falta total de comunicación.
B) Reduce de manera irreversible el nivel de aislamiento en todos los nodos de la red.
C) Exige una mayor cantidad de mensajes de coordinación entre administradores locales.
D) Delega el control de lectura a un nodo esclavo y la escritura al de coordinación.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: La descentralización topológica que provee D2PL otorga a cada servidor la potestad de administrar sus propios datos. Sin embargo, esto acarrea el sobrecosto de generar una inmensa volumetría de mensajes a través de los enlaces de red para mantener sincronizada la confirmación (coordinación TM-LM), impactando la latencia en protocolos de consistencia.

[TIPO: RESPUESTA CORTA] Pregunta ID: 10
Enunciado: En el entorno operativo del motor relacional PostgreSQL, ¿qué sentencia complementaria directa al final de una consulta de lectura previene modificaciones concurrentes imponiendo un candado de escritura explícito?
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: FOR UPDATE
Explicación: A nivel de ingeniería de bases de datos, el apéndice de consulta relacional "FOR UPDATE" bloquea el registro interceptado a nivel de fila comportándose lógicamente como una adquisición prematura de un candado (wl). Desplaza el control al sistema de control pesimista interno garantizando aislamiento en pre-escritura.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 11
Enunciado: Para que el algoritmo heurístico de Marcas de Tiempo (Timestamp Ordering) garantice un historial sin colisiones globales, ¿cuáles son los dos determinantes matemáticos obligatorios con los que se asigna cada métrica?
Opciones:
A) Replicabilidad sincrónica y varianza temporal adaptativa al balanceo de las redes.
B) Unicidad matemática sin ambigüedades y monotonicidad creciente del identificador.
C) Exclusividad de operaciones y total aleatoriedad predecible algorítmicamente.
D) Variabilidad asíncrona adaptativa lograda a través de protocolos del nivel físico.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Bajo la teoría de serializabilidad por cronología de operaciones de origen concurrente (Timestamp Ordering), es axiomático que la marca posea "Unicidad" (prohibir dos transacciones gemelas en valor) y una estricta "Monotonicidad" (orden cronológico perpetuo y positivo) permitiendo discernir qué transacción es precursora a otra con exactitud.

[TIPO: RESPUESTA CORTA] Pregunta ID: 12
Enunciado: En la especificación per-variable del modelo de Marcas de Tiempo por Dato, ¿cuál es el descriptor formal que registra la mayor marca de tiempo transaccional que ejecutó satisfactoriamente una escritura del recurso?
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: WTS(X)
Explicación: En TO, la validación se rige por variables inyectadas a nivel de cada campo de información. El valor límite de "Write Timestamp" o "wts(x)" guarda celosamente el reloj lógico de la transacción modificadora más tardía validada, bloqueando así futuras operaciones concurrentes obsoletas sobre "x".

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 13
Enunciado: Apelando al control pesimista del Timestamp Ordering (TO) Básico, ¿bajo qué condiciones lógicas irreductibles se certifica sin rechazo un mandato de escritura (WRITE) desde el procesador de transacciones hacia la bitácora?
Opciones:
A) Solo si la marca de la transacción es inferior al rts(x) y superior a la de wts(x).
B) Si la transacción culmina correctamente una validación optimista frente a sus pares.
C) Únicamente cuando la petición logra adquirir antes un candado exclusivo distribuido.
D) Exclusivamente si la marca de la transacción supera ambos históricos, rts(x) y wts(x).
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: D
Explicación: La regla transaccional algorítmica para inyectar una escritura sin deshacer el historial es rígida: la transacción proponente debe evidenciar ser matemáticamente más joven (una marca de tiempo netamente superior) tanto a la lectora más reciente "rts(x)" como a la última escritora "wts(x)".

[TIPO: RESPUESTA CORTA] Pregunta ID: 14
Enunciado: Debido a que su semántica procesa rechazos inmediatos y reinicios continuos antes de encolar operaciones en memoria, ¿qué falla topológica se previene y prohíbe enteramente en el motor mediante el TO Básico?
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: INTERBLOQUEOS
Explicación: Al prescindir categóricamente del mecanismo de retención o bloqueo, las directrices del TO Básico jamás posicionan a una operación en colas "esperando" por recursos bloqueados por otra. Esta agresividad resolutiva erradica estructuralmente los "deadlocks" o interbloqueos, previniendo los grafos WFG de ciclo cerrado.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 15
Enunciado: ¿Qué alteración estructural de funcionamiento impone intencionalmente la variante TO Conservador para remediar la principal debilidad (abortos continuos o efecto de latigazo de reinicios) inherente a su versión TO Básica?
Opciones:
A) Aumenta exponencialmente los candados, sacrificando la unicidad de las operaciones.
B) Expropia las lecturas a secundarios, mitigando así problemas de la red distribuida.
C) Introduce demoras intencionales asegurando cronología pero permitiendo interbloqueo.
D) Emplea bitácora única central que procesa asíncronamente las solicitudes entrantes.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: A diferencia de los rechazos inmediatos, el TO Conservador somete las peticiones a colas de amortiguamiento (buffers en sitios de origen) que dilatan y ralentizan intencionadamente la resolución para corroborar la recepción del flujo ordenado. El efecto colateral adverso de estas "colas preventivas" es el resurgimiento del riesgo matemático de sufrir interbloqueos.

[TIPO: RESPUESTA CORTA] Pregunta ID: 16
Enunciado: En el sofisticado mecanismo adaptado del modelo TO Multiversión, ¿qué construcción lógica se genera directamente a expensas de la capacidad de almacenamiento por cada solicitud de modificación exitosa?
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: VERSIÓN
Explicación: Para mantener la coherencia en la línea temporal requerida por lectores de edad cronológica variada, el sistema sacrifica disco y RAM reteniendo el valor original sin sobreescritura (non-destructive write) y habilitando una nueva "Versión" adyacente del objeto de datos, rotulada independientemente.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 17
Enunciado: Desde una perspectiva probabilística y analítica en bases de datos analíticas pesadas, ¿cuál es el beneficio sustancial que fomenta la implementación del mecanismo TO Multiversión por sobre sus precursores básicos?
Opciones:
A) La eliminación concluyente de cuellos de botella presentes en topologías en estrella.
B) La erradicación casi por completo de reinicios causados por rechazos en la lectura.
C) La compatibilidad ininterrumpida de red con plataformas de control descentralizado.
D) La supresión permanente de las validaciones de conflictos por interbloqueos ocultos.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: B
Explicación: Las bases de datos dotadas de un mecanismo Multiversión eliminan funcionalmente los cuellos causados por contención en consultas lentas. Dado que una lectura jamás colisiona contra un sobre-registro destructivo (siempre halla una versión histórica cronológicamente consistente a su marca TS), el modelo inhibe al borde absoluto la posibilidad de sufrir "Read Rejections".

[TIPO: RESPUESTA CORTA] Pregunta ID: 18
Enunciado: En caso de operar sobre una topología descentralizada que carece de un reloj físico garantizado, ¿qué componente lógico se debe añadir estáticamente al sufijo del contador de tiempo transaccional para dotar de unicidad al nodo?
Opciones:
A) N/A
B) N/A
C) N/A
D) N/A
E) N/A
Respuesta Correcta: IDENTIFICADOR DEL SITIO
Explicación: El teorema estipula que en escenarios donde los cronómetros de clústeres no cuenten con sincronía sub-milisegundo, se acude a contadores monotónicos lógicos internos. En presencia de empate por tiempo virtual de operaciones concurrentes, el motor concatenará el "Identificador del sitio" rompiendo el empate y reteniendo la unicidad transaccional obligatoria.

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 19
Enunciado: ¿Bajo qué axioma predictivo o heurístico los motores optimistas (Optimistic Concurrency Control) se permiten omitir toda capa de validación perimetral transfiriéndola enteramente hasta la culminación del proceso lógico en RAM?
Opciones:
A) Asumen algorítmicamente que los conflictos son estadísticamente raros o infrecuentes.
B) Postulan que fallos son inexistentes bajo topologías fuertemente acopladas y estables.
C) Asumen que todo nodo posee la memoria infinita para resolución de grafos de espera.
D) Dictaminan que el interbloqueo es estado natural del cluster distribuyendo la carga.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: A
Explicación: La familia de control Optimista diseña sus algoritmos fundamentándose empíricamente sobre el axioma "los conflictos son eventos raros". Por tanto, descartan el uso costoso e intenso de candados a lo largo de las peticiones en vivo para maximizar concurrencia; confiando en atrapar y resolver las eventuales anomalías cruzadas durante la corta fase técnica perimetral final de "Validación".

[TIPO: OPCIÓN MÚLTIPLE] Pregunta ID: 20
Enunciado: En el ciclo lógico terminal (Fase de Validación) de un protocolo optimista, ¿qué métrica o condición booleana certifica irrefutablemente la violación de consistencia, expropiando obligatoriamente a la transacción entrante?
Opciones:
A) Si el volumen escalar del conjunto local supera a su registro de modificaciones.
B) Si la transacción más joven no logra asegurar sus candados con un límite óptimo.
C) Si existe intersección matemática entre su Read Set y el Write Set de las previas.
D) Si la fase de pre-escritura local excede el tiempo estipulado por los secundarios.
E) Ninguna de las anteriores describe el comportamiento axiomático/teórico correcto.
Respuesta Correcta: C
Explicación: La validación asíncrona se efectúa mediante teoría de conjuntos. Una transacción certificará una anomalía y deberá abortarse irrevocablemente si durante las comparaciones el motor detecta una intersección activa (elemento en común) entre el Conjunto de Lectura (Read Set) local y un Conjunto de Escritura (Write Set) finalizado, delatando que los datos absorbidos están desactualizados y sucios.
