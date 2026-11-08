# Módulo 1: Paradigmas de Clústeres Distribuidos, Dimensiones de Estrés y Modelos de Escalabilidad

[TIPO: OPCION MULTIPLE]
Pregunta ID: 1
Enunciado: Una corporación financiera despliega un clúster de procesamiento analítico sobre la infraestructura elástica de AWS EMR para ejecutar un algoritmo paralelo sobre un volumen de datos masivo. Durante la fase de escalamiento, el equipo de ingeniería decide incrementar el número de nodos trabajadores de 10 a 100 servidores. Sin embargo, observan que la aceleración global del tiempo de ejecución se estabiliza rápidamente y no logra reducir el tiempo total por debajo de una cota mínima. Desde la perspectiva de las leyes matemáticas de escalamiento distribuido, ¿cuál de las siguientes afirmaciones explica correctamente la barrera técnica observada?
Opciones: A) La aceleración total alcanzada se encuentra restringida linealmente por la saturación física del ancho de banda del conmutador central (Core Switch). B) El algoritmo ejecutado viola la Ley de Gustafson-Barsis al no escalar la capacidad de memoria RAM volátil proporcionalmente al número de procesadores. C) La aceleración máxima esperada está limitada asintóticamente por la fracción estrictamente secuencial e indivisible del algoritmo, conforme a la Ley de Amdahl. D) El clúster Shared Nothing experimenta una degradación exponencial del rendimiento debido a la falta de un bus de memoria física compartida (SMP). E) Ninguna de las anteriores.
Respuesta Correcta: C
Explicación: La Ley de Amdahl establece que la aceleración máxima está limitada asintóticamente por la fracción secuencial e indivisible de un algoritmo, S_máx = 1 / ((1 - p) + (p / N)), imponiendo un techo independientemente del número N de procesadores.

Fuente 1: Paradigmas de Clústeres Distribuidos, Dimensiones de Estrés y Modelos de Escalabilidad
Instrucción: Asocie cada dimensión o pilar de diseño de sistemas distribuidos (Columna A) con la característica estructural o formal que define su comportamiento en la arquitectura (Columna B):
Columna A
1. Fiabilidad (Reliability)
2. Escalabilidad Horizontal (Scale-Out)
3. Operabilidad (Mantenibilidad)
4. Arquitectura Shared Nothing (SN)
Columna B
a. Incorporación modular de nodos commodity donde la complejidad migra exponencialmente hacia el software de red y sincronización.
b. Capacidad del sistema para continuar operando correctamente y sin pérdida de datos pese a la falla recurrente de componentes físicos.
c. Ausencia de recursos centrales compartidos de memoria o disco; los nodos operan como islas computacionales coordinadas por red.
d. Viabilidad técnica para monitorizar la telemetría, estado de salud y aplicar parches operativos sin detener el servicio.
Respuestas: 1-b, 2-a, 3-d, 4-c
Explicación: 1-b (Fiabilidad: tolerancia a fallas sin pérdida de datos), 2-a (Escalabilidad Horizontal: nodos commodity con complejidad en software), 3-d (Operabilidad: monitoreo y parches sin caída de servicio), 4-c (Shared Nothing: sin recursos centrales compartidos).

Fuente 1: Paradigmas de Clústeres Distribuidos, Dimensiones de Estrés y Modelos de Escalabilidad
Instrucción: Ordene cronológicamente los componentes y barreras de red que atraviesa una petición analítica realizada por un científico de datos desde una red pública externa hasta alcanzar los bloques binarios en los nodos de cómputo, garantizando el aislamiento perimetral:
Columna A
1. El cortafuegos interno (Internal Firewall) inspecciona la legitimidad de las instrucciones y autoriza el tráfico hacia la red privada del clúster.
2. El científico de datos se autentica a través del cortafuegos externo (External Firewall) e ingresa al Nodo Borde (Edge Node) ubicado en la DMZ.
3. El proceso cliente consulta los metadatos al Nodo Maestro (NameNode) a través de la Red de Servicio para resolver el mapa de ubicaciones.
4. El cliente establece sockets TCP de alta velocidad en la Red Privada de Datos con los DataNodes para canalizar el flujo de bytes.
Columna B
1. 1ª posición
2. 2ª posición
3. 3ª posición
4. 4ª posición
Respuestas: 1-3, 2-1, 3-2, 4-4
Explicación: Secuencia correcta: 2 -> 3 -> 1 -> 4. El cliente primero ingresa por el cortafuegos externo al Nodo Borde en DMZ (2), consulta metadatos al NameNode (3), el cortafuegos interno autoriza el tráfico (1) y finalmente establece sockets TCP con los DataNodes (4).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 4
Enunciado: ¿Cuál es el término técnico formal que designa la métrica evaluada en percentiles críticos (p95, p99, p99.9) utilizada para medir el tiempo de respuesta de las consultas de cola lenta bajo condiciones de alta concurrencia de carga?
Respuesta Correcta: Latencia / Tiempo de respuesta / Latencia de cola
Explicación: Latencia o tiempo de respuesta, evaluada en percentiles para medir la dispersión y el comportamiento de la cola lenta.

[TIPO: DESARROLLO]
Pregunta ID: 5
Enunciado: Un clúster de almacenamiento NoSQL distribuido procesa transacciones bancarias utilizando particionamiento por rango de clave primaria. Durante un evento de alta demanda (Black Friday), se detecta que el 90% de las solicitudes de escritura convergen hacia un único nodo trabajador, provocando un colapso por sobresaturación de disco y memoria (nodo caliente / hotspot), mientras los 50 nodos restantes permanecen ociosos.

Requerimiento:
1. Identifique y explique la anomalía teórica presente en la estrategia de particionamiento por rango.
2. Proponga una solución fundada en un protocolo formal de particionamiento que elimine los hotspots y minimice la reubicación masiva de datos cuando se añaden o retiran nodos del clúster. Justifique cada paso.
Respuesta Correcta: 1. Anomalía: El particionamiento por rango agrupa claves consecutivas (ej. marcas de tiempo o IDs correlativos). Ante ráfagas de datos con claves crecientes, una sola partición recibe todo el flujo, creando un hotspot.
2. Solución: Implementar Hashing Consistente (o Hash Partitioning). El hashing distribuye las claves uniformemente asignando el hash de la clave a un anillo de nodos (H(k) mod N), eliminando la concentración espacial y permitiendo añadir o retirar nodos con una reubicación mínima de datos (1/N).
Explicación: 1. Anomalía: El particionamiento por rango agrupa claves consecutivas (ej. marcas de tiempo). Ante ráfagas de datos con claves crecientes, una sola partición recibe todo el flujo, creando un hotspot.
2. Solución: Implementar Hashing Consistente (o Hash Partitioning). El hashing distribuye las claves uniformemente asignando el hash de la clave a un anillo de nodos (H(k) mod N), eliminando la concentración espacial y permitiendo añadir/retirar nodos con una reubicación mínima de datos (1/N).

# Módulo 2: Resiliencia Física, Dominios de Fallo y Plano de Control (YARN vs JobTracker)

[TIPO: OPCION MULTIPLE]
Pregunta ID: 6
Enunciado: En las arquitecturas históricas de Apache Hadoop (versión 1.x), la gestión de recursos de cómputo y la coordinación de tareas MapReduce recaían exclusivamente en un componente centralizado denominado JobTracker. Al evaluar la transición hacia la arquitectura YARN en Hadoop 2.x/3.x, ¿cuál fue el cambio estructural fundamental en el plano de control que permitió superar el cuello de botella de escalabilidad en clústeres de más de 4,000 nodos?
Opciones: A) La conversión de los slots rígidos de Map y Reduce en máquinas virtuales dedicadas gestionadas dinámicamente por un hipervisor KVM. B) El desacoplamiento del JobTracker en un ResourceManager para el arbitraje global de recursos y ApplicationMasters independientes por aplicación. C) La eliminación de los mensajes de latido (heartbeats) entre los trabajadores y el plano de control para evitar la saturación de memoria RAM. D) La migración del almacenamiento de metadatos de espacio de nombres desde la memoria RAM del NameNode hacia una base de datos NoSQL. E) Ninguna de las anteriores.
Respuesta Correcta: B
Explicación: YARN desacopló el JobTracker centralizado en dos entidades: un ResourceManager para el arbitraje global de recursos y ApplicationMasters independientes dedicados por aplicación.

Fuente 2: Resiliencia Física, Dominios de Fallo y Plano de Control (YARN vs JobTracker)
Instrucción: Relacione cada etapa evolutiva del desarrollo de infraestructuras distribuidas (Columna A) con el foco operativo y nivel de automatización que la caracteriza (Columna B):
Columna A
1. Etapa de Limitación (Monolítica)
2. Etapa de Aprendizaje
3. Etapa de Crecimiento
4. Etapa de Madurez
Columna B
a. Coordinación de clústeres en expansión; surge el dilema de saturación de conmutadores y balanceo de carga supervisado por latidos.
b. Infraestructura auto-sanadora total (Full Self-Healing) capaz de sobrevivir a múltiples fallas concurrentes en dominios de fallo independientes.
c. Centralización en servidor único con escalabilidad vertical; ausencia de automatización y administración artesanal.
d. Distribución de tareas lógicas en pequeños grupos de nodos; automatización manual mediante scripts básicos y supervisión reactiva.
Respuestas: 1-c, 2-d, 3-a, 4-b
Explicación: 1-c (Monolítica: servidor único), 2-d (Aprendizaje: scripts básicos), 3-a (Crecimiento: clústeres en expansión y balanceo), 4-b (Madurez: Full Self-Healing).

Fuente 2: Resiliencia Física, Dominios de Fallo y Plano de Control (YARN vs JobTracker)
Instrucción: Disponga en el orden secuencial correcto las etapas del flujo de interacción entre una aplicación analítica, el ResourceManager de YARN y los NodeManagers de los trabajadores para la asignación y ejecución elástica de tareas:
Columna A
1. El ResourceManager asigna un contenedor inicial y ordena al NodeManager de un nodo trabajador arrancar el ApplicationMaster de la aplicación.
2. El cliente de la aplicación transmite la solicitud de ejecución de trabajo al ResourceManager especificando los requerimientos de memoria y CPU.
3. Los NodeManagers supervisan el consumo de recursos de los contenedores locales y transmiten señales de vida (heartbeats) al ResourceManager.
4. El ApplicationMaster evalúa la localidad de los datos en HDFS y negocia contenedores de ejecución adicionales directamente con el ResourceManager.
Columna B
1. 1ª posición
2. 2ª posición
3. 3ª posición
4. 4ª posición
Respuestas: 1-2, 2-1, 3-4, 4-3
Explicación: Secuencia: 2 -> 1 -> 4 -> 3. Solicitud al ResourceManager (2), asignación del ApplicationMaster en un contenedor inicial (1), negociación de contenedores adicionales (4) y supervisión periódica vía NodeManager heartbeats (3).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 9
Enunciado: Escriba el acrónimo técnico de 4 letras de la capa introducida en Hadoop 2.x que actúa como sistema centralizado de gestión de recursos y programación de tareas, desacoplando el cómputo del almacenamiento HDFS.
Respuesta Correcta: YARN / Yet Another Resource Negotiator
Explicación: YARN (Yet Another Resource Negotiator).

[TIPO: DESARROLLO]
Pregunta ID: 10
Enunciado: Un centro de datos aloja un clúster de Big Data compuesto por 30 servidores distribuidos equitativamente en 3 gabinetes físicos (racks R1, R2 y R3). Por un error de configuración en el archivo de topología de red, la propiedad de reconocimiento de rack (Rack Awareness) fue desactivada, por lo que el nodo maestro asumió una topología plana (todos los nodos pertenecen a un mismo rack virtual /default-rack). Un bloque de archivo crítico con factor de replicación 3 fue almacenado físicamente en los servidores N1, N2 y N3, los cuales residen coincidentemente en el mismo gabinete físico R1. Repentinamente, la unidad de distribución de energía (PDU) del rack R1 sufre un cortocircuito irrecoverable.

Requerimiento:
1. Analice conceptualmente la falla definiendo el término 'Dominio de Fallo'.
2. Explique las consecuencias inmediatas sobre la disponibilidad e integridad del bloque de datos almacenado.
3. Formule la política estándar de colocación de 3 réplicas que aplica HDFS cuando Rack Awareness está correctamente configurado.
Respuesta Correcta: 1. Dominio de Fallo: Conjunto de componentes físicos (línea de energía, PDU, switch ToR) que colapsan simultáneamente ante un único incidente.
2. Consecuencia: Al residir N1, N2 y N3 en el mismo gabinete R1, la pérdida de la PDU destruye las 3 réplicas a la vez, causando pérdida total e irreversible del bloque (Missing block / CORRUPT).
3. Política HDFS: Réplica 1 en el nodo local donde se escribe; Réplica 2 en un rack remoto diferente (R2); Réplica 3 en otro servidor dentro del mismo rack remoto (R2).
Explicación: 1. Dominio de Fallo: Conjunto de elementos físicos que comparten un único punto de interrupción.
2. Consecuencia: Pérdida permanente del bloque por almacenamiento simultáneo en el mismo dominio.
3. Política HDFS: R1 en nodo local, R2 en rack remoto, R3 en servidor distinto del mismo rack remoto.

# Módulo 3: Jerarquía de Memoria, Aislamiento Perimetral en DMZ y Topología de Red

[TIPO: OPCION MULTIPLE]
Pregunta ID: 11
Enunciado: Considere una topología jerárquica de red de un centro de datos donde los servidores se interconectan mediante conmutadores de extremo de gabinete (Top-of-Rack / ToR Switches) vinculados a un conmutador central (Core Switch). Si un proceso ejecutor de Apache Spark en el Nodo A (ubicado en el Rack 1) requiere consumir una partición de datos cuya única réplica reside en el Nodo B (ubicado en el Rack 2), ¿cuál es la distancia lógica cuantitativa (d, medida en saltos de conmutación de red) entre el cómputo y el dato según la métrica estándar de sistemas distribuidos?
Opciones: A) d = 0 B) d = 2 C) d = 4 D) d = 6 E) Ninguna de las anteriores.
Respuesta Correcta: C
Explicación: d = 4: Nodo A -> Switch ToR1 (salto 1) -> Core Switch (salto 2) -> Switch ToR2 (salto 3) -> Nodo B (salto 4).

Fuente 3: Jerarquía de Memoria, Aislamiento Perimetral en DMZ y Topología de Red
Instrucción: Asocie cada nivel de la jerarquía de hardware o modelo computacional (Columna A) con la métrica de latencia de acceso o característica de persistencia asociada (Columna B):
Columna A
1. Memoria RAM volátil del sistema
2. Disco de Estado Sólido (SSD / NVMe)
3. Disco Magnético Mecánico (HDD)
4. Modelo Apache Spark (RDDs)
Columna B
a. Tiempos de latencia física de búsqueda mecánica comprendidos entre 5 y 10 milisegundos (ms).
b. Tiempos de acceso ultrarrápidos comprendidos entre 10 y 100 nanosegundos (ns).
c. Mantiene datos intermedios en memoria RAM, reduciendo I/O en disco hasta 100 veces frente a MapReduce.
d. Tiempos de acceso a celdas de memoria semiconductora comprendidos entre 50 y 150 microsegundos (µs).
Respuestas: 1-b, 2-d, 3-a, 4-c
Explicación: 1-b (RAM: 10-100 ns), 2-d (SSD: 50-150 µs), 3-a (HDD: 5-10 ms), 4-c (Spark RDD: memoria RAM interactiva).

Fuente 3: Jerarquía de Memoria, Aislamiento Perimetral en DMZ y Topología de Red
Instrucción: Organice la secuencia paso a paso que sigue la información y los comandos desde la interfaz interactiva de un usuario hasta la ejecución paralela en la infraestructura privada:
Columna A
1. El Nodo Borde (Edge Node) compila el script analítico y envía la solicitud de recursos al plano de control del clúster (Nodo Maestro).
2. El usuario interactúa con la interfaz de comandos (CLI) o el notebook interactivo (Jupyter) alojado centralizadamente en el Nodo Borde.
3. El cortafuegos interno valida que las instrucciones provengan de la IP del Nodo Borde y autoriza el paso hacia la red del clúster privado.
4. Los Nodos Trabajadores (DataNodes / Workers) reciben los contenedores de ejecución y procesan los datos almacenados localmente.
Columna B
1. 1ª posición
2. 2ª posición
3. 3ª posición
4. 4ª posición
Respuestas: 1-2, 2-1, 3-3, 4-4
Explicación: Secuencia: 2 -> 1 -> 3 -> 4. Interacción en Nodo Borde (2), solicitud al Nodo Maestro (1), filtrado de firewall interno por IP autorizada (3) y procesamiento en trabajadores (4).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 14
Enunciado: ¿Qué término técnico representa la métrica matemática introducida para cuantificar el costo de comunicación en red (d) entre dos nodos del clúster en función del número acumulado de saltos por conmutadores?
Respuesta Correcta: Distancia Lógica / Métrica d / Distancia de red
Explicación: Distancia Lógica (o Métrica d en saltos de red).

[TIPO: DESARROLLO]
Pregunta ID: 15
Enunciado: Una empresa de tecnología sufrió una brecha de seguridad grave: un atacante externo logró acceder a la consola de administración Web UI del NameNode (puerto 9870) y emitió órdenes de formateo del sistema de archivos distribuido. El informe forense reveló que los servidores maestros y de trabajo poseían direcciones IP públicas accesibles directamente desde Internet para facilitar el trabajo remoto de los desarrolladores.

Requerimiento:
1. Redacte un diagnóstico de la falla arquitectónica basada en los principios de aislamiento perimetral.
2. Diseñe una arquitectura de red resiliente y segura incorporando un Nodo Borde (Gateway), una Zona Desmilitarizada (DMZ) y las reglas de filtrado de los cortafuegos externo e interno. Justifique la función de cada componente.
Respuesta Correcta: 1. Diagnóstico: La exposición directa de los puertos del plano de control (NameNode) a Internet viola el principio de aislamiento perimetral y mínima exposición.
2. Arquitectura: Disponer un Nodo Borde como único punto de entrada en una DMZ; un cortafuegos externo autoriza únicamente SSH/HTTPS autenticado a desarrolladores; un cortafuegos interno aísla el clúster privado, admitiendo tráfico solo desde la IP del Nodo Borde hacia los puertos RPC (9000/YARN).
Explicación: 1. Diagnóstico: Violación del principio de defensa en profundidad y aislamiento de planos de control.
2. Arquitectura: DMZ con Nodo Borde (Gateway) flanqueado por cortafuegos perimetral externo e interno.

# Módulo 4: Virtualización, Contenedores, Modelos Cloud y Alta Disponibilidad

[TIPO: OPCION MULTIPLE]
Pregunta ID: 16
Enunciado: Un equipo de infraestructura compara la arquitectura de virtualización tradicional mediante Máquinas Virtuales (VMs) gestionadas por un Hipervisor Tipo 1 (como VMware ESXi o KVM) frente al despliegue en Contenedores Docker sobre Linux. Desde la perspectiva de la abstracción del sistema operativo y el aislamiento de recursos del hardware anfitrión, ¿cuál de las siguientes afirmaciones describe con rigor la diferencia teórica entre ambos esquemas?
Opciones: A) Las máquinas virtuales comparten el mismo núcleo (Kernel) del sistema operativo anfitrión mediante namespaces y cgroups, reduciendo la memoria. B) Los contenedores virtualizan la pila completa de hardware, requiriendo que cada instancia ejecute un sistema operativo invitado (Guest OS) independiente. C) Las máquinas virtuales operan con una capa de archivos Copy-on-Write sobre UnionFS, lo que acelera el tiempo de arranque a milisegundos. D) Los contenedores comparten el Kernel anfitrión e imponen límites de memoria y CPU vía cgroups y aislamiento de visibilidad vía namespaces. E) Ninguna de las anteriores.
Respuesta Correcta: D
Explicación: Los contenedores comparten el Kernel anfitrión e implementan aislamiento de procesos y recursos mediante namespaces y cgroups sin requerir un Guest OS completo.

Fuente 4: Virtualización, Contenedores, Modelos Cloud y Alta Disponibilidad
Instrucción: Asocie cada modelo de servicio en la Nube / Alta Disponibilidad (Columna A) con la descripción técnica de su nivel de responsabilidad o métrica SLA (Columna B):
Columna A
1. Infraestructura como Servicio (IaaS)
2. Plataforma como Servicio (PaaS)
3. Disponibilidad 'Cinco Nueves' (99.999%)
4. Clasificación TIER IV (Uptime Institute)
Columna B
a. El proveedor administra hardware, SO y runtime; el cliente administra código y datos. Óptimo para desarrollo ágil.
b. Tolera máximo 5.26 minutos de inactividad acumulada al año; estándar de misión crítica en telecomunicaciones y banca.
c. Instalación con redundancia 2N+1, sistemas compartimentados activos con tolerancia a fallos y 26.3 minutos/año de indisponibilidad máxima.
d. El proveedor arrienda cómputo y redes virtuales; el usuario configura el SO, middleware, aplicaciones y datos.
Respuestas: 1-d, 2-a, 3-b, 4-c
Explicación: 1-d (IaaS: hardware y red), 2-a (PaaS: SO y runtime administrados), 3-b (Five Nines: 5.26 min/año), 4-c (Tier IV: 2N+1 y 26.3 min/año).

Fuente 4: Virtualización, Contenedores, Modelos Cloud y Alta Disponibilidad
Instrucción: Ordene los pasos mediante los cuales un sistema de archivos por capas (OverlayFS/UnionFS) en Docker permite el aprovisionamiento ligero e inmutable de contenedores trabajadores:
Columna A
1. El motor Docker inicializa el contenedor montando una capa delgada de lectura/escritura (Copy-on-Write) en la parte superior del apilamiento.
2. Las capas base e intermedias de la imagen Docker (con el sistema operativo y librerías de Hadoop) se cargan como volúmenes en modo solo lectura.
3. Al modificar un archivo existente, el contenedor copia el archivo desde la capa de solo lectura hacia su capa superior antes de escribir el cambio.
4. Las instancias múltiples de trabajadores que se ejecutan en el mismo servidor host comparten las mismas capas base en RAM sin duplicar gigabytes.
Columna B
1. 1ª posición
2. 2ª posición
3. 3ª posición
4. 4ª posición
Respuestas: 1-2, 2-1, 3-3, 4-4
Explicación: Secuencia: 2 -> 1 -> 3 -> 4. Montaje de capas base de solo lectura (2), creación de la capa Copy-on-Write superior (1), copia hacia la capa superior al modificar (3) y compartición de capas en memoria entre múltiples contenedores (4).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 19
Enunciado: Indique el acrónimo del pilar nativo del Kernel de Linux que se encarga de imponer cuotas de consumo de tiempo de CPU, límites de memoria RAM y ancho de banda de E/S a un grupo de procesos en un contenedor.
Respuesta Correcta: cgroups / Control Groups
Explicación: cgroups (Control Groups).

[TIPO: DESARROLLO]
Pregunta ID: 20
Enunciado: Un proveedor de servicios en la nube despliega un clúster de análisis de datos virtualizado en el cual un único servidor físico anfitrión (Host Bare Metal con 128 núcleos de CPU y 512 GB de RAM) ha sido particionado mediante un hipervisor para alojar 8 Máquinas Virtuales, cada una funcionando como un DataNode independiente de HDFS.

Requerimiento:
1. Analice críticamente esta práctica de diseño identificando los cuellos de botella latentes en el hardware subyacente.
2. Evalúe el impacto sistémico en caso de que la fuente de poder principal del servidor host sufra un colapso físico, relacionándolo con el concepto de Punto Único de Falla (SPOF) y la resiliencia del clúster distribuido.
Respuesta Correcta: 1. Cuellos de botella: Los 8 DataNodes compiten intensamente por los canales compartidos del bus PCIe, la controladora RAID/SATA y el conmutador de red físico (NIC), provocando saturación masiva de E/S.
2. Impacto sistémico: El servidor anfitrión constituye un Punto Único de Falla (SPOF). Si colapsa su fuente de poder, se pierden las 8 instancias de DataNode a la vez; si las 3 réplicas de un bloque residían en este grupo de VMs, se produce pérdida permanente de datos.
Explicación: 1. Cuellos de botella: Saturación de bus PCIe y controladora de almacenamiento compartida.
2. Impacto: SPOF a nivel de servidor físico que anula la redundancia lógica distribuida.

# Módulo 5: Ecuación de Diseño de Sistemas Distribuidos y Flujos I/O en HDFS

[TIPO: OPCION MULTIPLE]
Pregunta ID: 21
Enunciado: Durante la fase de lectura de un archivo de 1 TB en HDFS, una aplicación de analítica masiva invoca el método open() sobre el objeto DistributedFileSystem. Tras obtener del NameNode la lista ordenada topológicamente de ubicaciones de bloques, el cliente inicia la transferencia mediante FSDataInputStream. ¿Cómo gestiona el sistema el salto desde el último byte del Bloque 1 hacia el primer byte del Bloque 2 alojado en un DataNode físicamente distinto?
Opciones: A) El cliente interrumpe el socket TCP y emite una nueva solicitud remota getBlockLocations() al NameNode para resolver la IP del Bloque 2. B) El DataNode que custodia el Bloque 1 redirige internamente el tráfico mediante un proxy TCP hacia el DataNode que contiene el Bloque 2. C) El NameNode actúa como intermediario de flujo (streaming proxy), recibiendo los bytes del Bloque 2 y retransmitiéndolos al cliente. D) El stream FSDataInputStream cierra la conexión TCP con el primer DataNode y abre automáticamente un socket hacia el segundo DataNode de la lista sin consultar al NameNode. E) Ninguna de las anteriores.
Respuesta Correcta: D
Explicación: FSDataInputStream gestiona de forma transparente el salto: cierra el socket con el DataNode actual y abre uno nuevo hacia el siguiente DataNode según la lista de bloques precargada del NameNode.

Fuente 5: Ecuación de Diseño de Sistemas Distribuidos y Flujos I/O en HDFS
Instrucción: Asocie cada elemento de la Ecuación de Diseño de Sistemas Distribuidos (Columna A) con la manifestación técnica de su beneficio o costo operativo (Columna B):
Columna A
1. Beneficio: Escalabilidad Horizontal (Scale-Out)
2. Beneficio: Resiliencia por Replicación
3. Costo: Cuello de Botella en Red
4. Costo: Sobrecarga de Reconstrucción
Columna B
a. La regeneración de réplicas tras la caída de un nodo compite agresivamente por ancho de banda, CPU y accesos I/O en disco.
b. Capacidad de agregar hardware commodity al clúster para superar el techo de costo superlineal del escalamiento vertical.
c. Supervivencia del dato y disponibilidad ininterrumpida ante la avería impredecible de discos o nodos trabajadores.
d. Mover grandes volúmenes de datos brutos entre servidores satura rápidamente los conmutadores y multiplica las latencias.
Respuestas: 1-b, 2-c, 3-d, 4-a
Explicación: 1-b (Escalabilidad Horizontal: nodos commodity), 2-c (Resiliencia: supervivencia del dato), 3-d (Cuello de botella en red: contención de switches), 4-a (Sobrecarga de reconstrucción: competencia por recursos).

Fuente 5: Ecuación de Diseño de Sistemas Distribuidos y Flujos I/O en HDFS
Instrucción: Estructure cronológicamente los pasos que ejecuta el cliente de HDFS durante el flujo de escritura de un nuevo bloque de datos a través de la canalización de replicación (pipeline):
Columna A
1. El cliente solicita al NameNode la creación del archivo y la asignación de un identificador de bloque junto a una lista de 3 DataNodes.
2. El primer DataNode recibe el paquete de 64 KB, lo almacena en su memoria intermedia y lo retransmite al segundo DataNode, repitiéndose hacia el tercero.
3. El cliente establece un socket TCP con el primer DataNode de la lista e inicia la transmisión de datos divididos en paquetes de 64 KB.
4. Los acuses de recibo (ACKs) viajan en sentido inverso desde el tercer DataNode hacia el segundo, primero y finalmente al cliente.
Columna B
1. 1ª posición
2. 2ª posición
3. 3ª posición
4. 4ª posición
Respuestas: 1-1, 2-3, 3-2, 4-4
Explicación: Secuencia: 1 -> 3 -> 2 -> 4. Solicitud al NameNode (1), apertura de socket TCP con el primer DataNode (3), retransmisión encadenada en pipeline (2) y retorno inverso de confirmaciones ACK (4).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 24
Enunciado: ¿Cómo se denomina el identificador numérico de versión de bloque (sello de tiempo/secuencia) que el NameNode contrasta durante el Block Report de un DataNode reincorporado para identificar y purgar réplicas obsoletas (stale blocks)?
Respuesta Correcta: Generation Stamp / Sello de Generación / Sello de versión
Explicación: Generation Stamp (Sello de Generación de Bloque).

[TIPO: DESARROLLO]
Pregunta ID: 25
Enunciado: Un DataNode (DN-05) que alojaba 10,000 bloques de datos sufrió una desconexión accidental por la caída de su tarjeta de red. Transcurridos 15 minutos, el NameNode declaró muerto a DN-05 y concluyó exitosamente la clonación de emergencia de las réplicas perdidas en otros nodos del clúster. Dos horas más tarde, un técnico reemplaza la tarjeta de red y enciende nuevamente el servidor DN-05, reincorporándolo a la red.

Requerimiento:
1. Explique en detalle la secuencia de eventos que ocurren cuando DN-05 arranca y envía su Block Report al NameNode.
2. ¿Cómo clasifica el NameNode los bloques que conserva DN-05 en sus discos locales considerando que las réplicas ya fueron re-creadas en el clúster?
3. Describa el protocolo de purga e instrucciones que emite el NameNode para restablecer la consistencia estricta del espacio de nombres.
Respuesta Correcta: 1. Secuencia: DN-05 inicia, se registra ante el NameNode y remite su Block Report con la lista de bloques físicos y sus Generation Stamps.
2. Clasificación: El NameNode contrasta los Generation Stamps; los bloques intactos cuya replicación ya alcanzó RF=3 se marcan como sobre-replicados (over-replicated) y cualquier bloque modificado como obsoleto (stale).
3. Purga: En la siguiente respuesta de latido (heartbeat reply), el NameNode instruye a DN-05 a eliminar físicamente esos bloques locales para liberar disco y preservar consistencia.
Explicación: 1. Secuencia de inicio y envío de Block Report.
2. Detección de bloques over-replicated y stale.
3. Emisión de órdenes de borrado en la respuesta de heartbeat.

# Módulo 6: Pipeline de Replicación, Conciencia de Rack y Dimensionamiento Matemático

[TIPO: OPCION MULTIPLE]
Pregunta ID: 26
Enunciado: Una plataforma de procesamiento de datos bancarios ingiere diariamente un flujo continuo de datos de D_flujo = 1.5 TB de archivos planos sin comprimir. La arquitectura HDFS se configura con un tamaño de bloque de B = 128 MB, un factor de replicación RF = 3 y se establece un buffer de seguridad del b = 20% (0.20) utilizando el criterio de recargo directo sobre la capacidad bruta. ¿Cuál es el almacenamiento bruto diario requerido y la capacidad total provisionada con buffer para retener 30 días de operación?
Opciones: A) Almacenamiento bruto: 1.5 TB/día; Capacidad total (30 días): 45.0 TB. B) Almacenamiento bruto: 4.5 TB/día; Capacidad total (30 días): 162.0 TB. C) Almacenamiento bruto: 4.5 TB/día; Capacidad total (30 días): 135.0 TB. D) Almacenamiento bruto: 5.4 TB/día; Capacidad total (30 días): 168.75 TB. E) Ninguna de las anteriores.
Respuesta Correcta: B
Explicación: S_bruto = 1.5 TB * 3 = 4.5 TB/día. Con recargo de buffer (+20%): 4.5 * 1.20 = 5.4 TB/día. Capacidad para 30 días = 5.4 * 30 = 162.0 TB.

Fuente 6: Pipeline de Replicación, Conciencia de Rack y Dimensionamiento Matemático
Instrucción: Relacione el tipo de conmutador de red o réplica HDFS (Columna A) con su función topológica y nivel de conmutación de red (Columna B):
Columna A
1. Switch Top-of-Rack (ToR)
2. Switch Núcleo (Core Switch)
3. Primera Réplica (R1)
4. Segunda Réplica (R2)
Columna B
a. Ubicada en un rack remoto diferente al de la réplica local; atraviesa la red troncal para sobrevivir a la caída completa del rack 1.
b. Conmutador de alta velocidad que interconecta los switches ToR de todos los gabinetes; su ancho de banda es altamente propenso a contención.
c. Almacenada en el nodo local donde el cliente inicia la escritura; ofrece velocidad de persistencia con latencia cero de red.
d. Conmutador instalado en el gabinete que conecta los DataNodes locales; resuelve el tráfico intra-rack con latencia mínima.
Respuestas: 1-d, 2-b, 3-c, 4-a
Explicación: 1-d (ToR: intra-rack), 2-b (Core: troncal inter-rack), 3-c (R1: local con latencia cero), 4-a (R2: rack remoto para resiliencia).

Fuente 6: Pipeline de Replicación, Conciencia de Rack y Dimensionamiento Matemático
Instrucción: En el pipeline de replicación de HDFS durante la fase de escritura, organice la trayectoria del flujo físico de acuses de recibo (ACKs) de sockets TCP desde la perspectiva de la confirmación de consistencia en reversa:
Columna A
1. El DataNode 3 (nodo final de la cadena) escribe el paquete en su almacenamiento local y emite una señal ACK hacia el DataNode 2.
2. El DataNode 1 recibe la confirmación del DataNode 2, consolida la persistencia local de la cadena y entrega el ACK final al Cliente.
3. El DataNode 2 recibe el ACK del DataNode 3, valida la escritura en sus propios discos y transmite un ACK consolidado hacia el DataNode 1.
4. El Cliente HDFS recibe el ACK consolidado del DataNode 1, liberando el paquete de su cola de memoria temporal pendientes de confirmación.
Columna B
1. 1ª posición
2. 2ª posición
3. 3ª posición
4. 4ª posición
Respuestas: 1-1, 2-3, 3-2, 4-4
Explicación: Secuencia: 1 -> 3 -> 2 -> 4. ACK de DN3 a DN2 (1), ACK de DN2 a DN1 (3), ACK de DN1 a Cliente (2) y liberación en cola de cliente (4).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 29
Enunciado: ¿Cómo se denomina formalmente el conmutador de red instalado físicamente en la parte superior de un gabinete que conecta directamente a todos los servidores de ese rack?
Respuesta Correcta: Switch ToR / Top-of-Rack / Switch Top-of-Rack / ToR
Explicación: Switch ToR (Top-of-Rack).

[TIPO: DESARROLLO]
Pregunta ID: 30
Enunciado: Una empresa de telecomunicaciones opera un clúster HDFS con D_flujo = 2.0 TB/día, B = 128 MB, factor de replicación original RF = 3 y un buffer de ocupación máxima del 80% (b = 0.20 en la fórmula S_bruto / (1 - b)). Tras una auditoría gubernamental, la empresa es obligada a incrementar el factor de replicación a RF = 5.

Requerimiento:
1. Calcule matemáticamente el incremento exacto en Gigabytes o Terabytes de la capacidad diaria de almacenamiento con buffer requerida.
2. Analice el impacto en el tráfico de red de la dorsal central (Switch Núcleo) durante la fase de escritura al pasar de RF = 3 a RF = 5, fundamentando la respuesta en la topología de Conciencia de Rack.
Respuesta Correcta: 1. Cálculo: Para RF=3: S_bruto = 2.0 * 3 = 6.0 TB/día; Capacidad diaria con buffer = 6.0 / (1 - 0.20) = 7.5 TB/día. Para RF=5: S_bruto = 2.0 * 5 = 10.0 TB/día; Capacidad diaria con buffer = 10.0 / (1 - 0.20) = 12.5 TB/día. Incremento diario = 12.5 - 7.5 = 5.0 TB/día (5,000 GB/día).
2. Tráfico de Red: En RF=3 se requiere un único cruce troncal hacia el segundo rack (R2 y R3 están en el mismo gabinete remoto). En RF=5, las réplicas 4 y 5 deben distribuirse en racks adicionales para evitar superar la cuota máxima por rack, multiplicando los saltos por el Switch Núcleo e incrementando la contención troncal.
Explicación: 1. Incremento de 5.0 TB diarios al pasar de 7.5 TB a 12.5 TB/día.
2. Aumento de envíos inter-rack que saturan el conmutador central (Core Switch).

# Módulo 7: Particionamiento vs Replicación, Localidad de Datos e Integridad Silenciosa

[TIPO: OPCION MULTIPLE]
Pregunta ID: 31
Enunciado: En infraestructuras de Big Data como HDFS, la tolerancia a fallos distingue entre la salud de los bloques de datos y la disponibilidad de los nodos físicos. Para verificar que un bloque de datos no ha sufrido corrupción magnética silenciosa (degradación de bits / Bit Rot) en los platos del disco, el sistema calcula un Checksum mediante el algoritmo CRC32C sobre fragmentos de 512 bytes. ¿Cuál es el procedimiento exacto mediante el cual el cliente valida la integridad del bloque durante la lectura?
Opciones: A) El NameNode calcula el hash en tiempo real leyendo el disco del DataNode y lo compara contra la entrada fsimage. B) El DataNode lee el bloque, vuelve a calcular el hash esperado y si no coincide, formatea automáticamente el sector dañado. C) El cliente recibe los datos y el hash esperado guardado al escribir; calcula el hash actual y si difieren, rechaza el bloque y lee otra réplica. D) El hilo DataBlockScanner envía un latido al NameNode informando que la CPU del nodo ha sufrido una alteración de paridad. E) Ninguna de las anteriores.
Respuesta Correcta: C
Explicación: El cliente recibe tanto los datos como el checksum guardado al escribir. Al leer, recalcula el checksum sobre los datos recibidos y, si detecta discrepancia, descarta ese bloque y conmuta de forma transparente hacia otra réplica sana.

Fuente 7: Particionamiento vs Replicación, Localidad de Datos e Integridad Silenciosa
Instrucción: Relacione la prioridad de asignación del planificador de tareas (Data Locality) (Columna A) con la descripción de la ubicación física y métrica de distancia de red (Columna B):
Columna A
1. Prioridad 1: Mismo Nodo (Node-Local)
2. Prioridad 2: Mismo Rack (Rack-Local)
3. Prioridad 3: Otro Rack (Off-Rack)
4. Verificación DataBlockScanner
Columna B
a. La tarea se asigna a otro servidor dentro del mismo gabinete; el tráfico circula por el Switch ToR con distancia d = 2.
b. Auditoría en segundo plano que revisa periódicamente los checksums de bloques en los DataNodes sin esperar lecturas de clientes.
c. La tarea se ejecuta en el mismo servidor físico que custodia el bloque en disco; latencia cero y distancia d = 0.
d. La tarea se asigna a un servidor en un rack distinto; los datos deben cruzar el Switch Núcleo con distancia d = 4.
Respuestas: 1-c, 2-a, 3-d, 4-b
Explicación: 1-c (Node-Local: d=0), 2-a (Rack-Local: d=2), 3-d (Off-Rack: d=4), 4-b (DataBlockScanner: revisión preventiva en background).

Fuente 7: Particionamiento vs Replicación, Localidad de Datos e Integridad Silenciosa
Instrucción: Organice las 3 etapas continuas del protocolo de autorrecuperación automática de HDFS cuando un DataNode intermedio sufre un colapso físico a mitad de una operación de escritura en el pipeline:
Columna A
1. El NameNode detecta en segundo plano que el bloque ha quedado en condición de sub-replicación (2 de 3 copias) y ordena un clonaje silencioso a un nodo sano.
2. El sistema cierra la conexión con el servidor averiado, lo expulsa de la tubería y reconfigura el pipeline uniendo directamente al Nodo 1 con el Nodo 3.
3. El flujo de transmisión del pipeline se interrumpe repentinamente debido a que el Nodo 2 intermedio deja de emitir acuses de recibo de paquetes.
Columna B
1. 1ª posición
2. 2ª posición
3. 3ª posición
Respuestas: 1-3, 2-2, 3-1
Explicación: Secuencia: 3 -> 2 -> 1. Interrupción por falta de ACKs en Nodo 2 (3), exclusión de Nodo 2 y reanudación directa entre Nodo 1 y 3 (2), y regeneración en background de la réplica faltante (1).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 34
Enunciado: ¿Qué término técnico en inglés designa el fenómeno físico de degradación progresiva de sectores magnéticos donde un bit cambia de 0 a 1 sin generar un error mecánico en la controladora del disco?
Respuesta Correcta: Bit Rot / Degradación de bits / Silent data corruption
Explicación: Bit Rot (Degradación de Bits / Corrupción Silenciosa de Datos).

[TIPO: DESARROLLO]
Pregunta ID: 35
Enunciado: Un trabajo de analítica sobre un dataset de genómica falla repetidamente arrojando una excepción de inconsistencia de datos. Al ejecutar un análisis forense, se descubre que un bloque binario almacenado en el DataNode DN-12 sufrió una alteración silenciosa de 4 bits debido a fluctuaciones térmicas en el gabinete.

Requerimiento:
1. Explique detalladamente cómo el cliente HDFS detecta la corrupción al invocar la lectura.
2. Describa la secuencia de acciones transparentes que ejecuta el cliente para entregar los datos correctos a la aplicación sin interrumpir el proceso.
3. Detalle las órdenes que emite el NameNode tras recibir el reporte de corrupción para eliminar la copia dañada y restaurar el factor de replicación objetivo.
Respuesta Correcta: 1. Detección: El cliente computa el hash CRC32C sobre los fragmentos leídos de DN-12 y constata que difiere del checksum de control guardado en el archivo de metadatos (.meta).
2. Acción transparente: El cliente marca DN-12 como corrupto para ese bloque, interrumpe el socket y se reconecta de inmediato a DN-08 (poseedor de la réplica 2) entregando los datos intactos a la aplicación.
3. Restauración: El cliente envía un reporte de ChecksumException al NameNode. El NameNode programa la instrucción de borrado para DN-12 y comisiona a un nodo sano clonar el bloque en otro DataNode para restablecer RF=3.
Explicación: 1. Validación de hash CRC32C.
2. Conmutación transparente hacia réplica sana.
3. Purga de copia dañada y réplica de compensación orquestada por el NameNode.

# Módulo 8: Análisis Forense de Clúster HDFS Contenerizado y Medición de Tolerancia a Fallos

[TIPO: OPCION MULTIPLE]
Pregunta ID: 36
Enunciado: En el despliegue de un clúster HDFS sobre contenedores Docker para entornos de laboratorio y pruebas de resiliencia, se requiere ajustar el tiempo de detección de nodos caídos. En la configuración por defecto de producción, Hadoop utiliza un intervalo de latido (dfs.heartbeat.interval) de 3 segundos y un intervalo de rechequeo (dfs.namenode.heartbeat.recheck-interval) de 300,000 milisegundos (300 s), resultando en 630 segundos (10.5 minutos). Si en el laboratorio se redefine el recheck-interval a 15,000 milisegundos (15 s), ¿cuál es el tiempo exacto que transcurrirá desde que se detiene el contenedor de un DataNode hasta que el NameNode lo declara oficialmente en estado Dead datanodes?
Opciones: A) 18 segundos. B) 30 segundos. C) 45 segundos. D) 60 segundos. E) Ninguna de las anteriores.
Respuesta Correcta: D
Explicación: T_muerte = (2 * dfs.namenode.heartbeat.recheck-interval) + (10 * dfs.heartbeat.interval) = (2 * 15 s) + (10 * 3 s) = 30 s + 30 s = 60 segundos.

Fuente 8: Análisis Forense de Clúster HDFS Contenerizado y Medición de Tolerancia a Fallos
Instrucción: Asocie la herramienta o propiedad de configuración de HDFS CLI / Docker (Columna A) con su función técnica en el laboratorio (Columna B):
Columna A
1. hdfs dfsadmin -report
2. hdfs fsck / -files -blocks -locations
3. dfs.namenode.datanode.registration.ip-hostname-check
4. ENSURE_NAMENODE_DIR
Columna B
a. Variable de entorno de la imagen que verifica si la carpeta de metadatos existe; si no, ejecuta automáticamente hdfs namenode -format.
b. Genera un reporte integral del estado del clúster, detallando capacidad configurada, réplicas sub-replicadas y nodos vivos/muertos.
c. Inhabilita la verificación inversa de DNS entre la IP y el nombre de host, permitiendo el registro de DataNodes en redes bridge de Docker.
d. Audita la salud del sistema de archivos, retornando el Block Pool ID, identificador blk_..., número de réplicas vivas y IPs anfitrionas.
Respuestas: 1-b, 2-d, 3-c, 4-a
Explicación: 1-b (dfsadmin -report: telemetría global), 2-d (fsck: mapa de bloques y ubicaciones), 3-c (ip-hostname-check: redes bridge), 4-a (ENSURE_NAMENODE_DIR: bootstrap format).

Fuente 8: Análisis Forense de Clúster HDFS Contenerizado y Medición de Tolerancia a Fallos
Instrucción: Estructure el orden cronológico de ejecución de comandos en Windows PowerShell y Linux Bash para desplegar y verificar el clúster contenerizado HDFS:
Columna A
1. Ejecutar docker compose up -d en PowerShell para descargar las imágenes y levantar los contenedores en segundo plano.
2. Ingresar a la consola interactiva del contenedor maestro ejecutando docker exec -it namenode bash desde PowerShell.
3. Validar la sintaxis del manifiesto de servicios ejecutando docker compose config --quiet en la terminal de PowerShell.
4. Transferir un archivo local al sistema distribuido mediante el comando hdfs dfs -put /datos_local/dataset.csv /user/admin/.
Columna B
1. 1ª posición
2. 2ª posición
3. 3ª posición
4. 4ª posición
Respuestas: 1-2, 2-3, 3-1, 4-4
Explicación: Secuencia: 3 -> 1 -> 2 -> 4. Validación de sintaxis compose config (3), lanzamiento con up -d (1), acceso interactivo con exec bash (2) e ingestión HDFS con put (4).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 39
Enunciado: ¿Cuál es la palabra exacta que imprime la herramienta de auditoría hdfs fsck en el campo Status: cuando la totalidad de los bloques de un archivo poseen sus réplicas vivas completas y sin corrupción?
Respuesta Correcta: HEALTHY
Explicación: HEALTHY (Estado óptimo y sin corrupción del archivo en HDFS).

[TIPO: DESARROLLO]
Pregunta ID: 40
Enunciado: Durante una prueba de laboratorio de resiliencia en un clúster HDFS de 2 DataNodes (DN1 y DN2) con dfs.replication = 2, se ejecuta el comando docker stop datanode2 para simular la muerte instantánea de DN2.

Requerimiento:
1. Describa el comportamiento de la salida de hdfs dfsadmin -report durante los primeros 45 segundos posteriores a la detención del contenedor.
2. Explique las métricas que reporta hdfs fsck una vez transcurridos 65 segundos de la caída (desglose los campos Live_repl, Under-replicated blocks y Missing blocks).
3. Justifique formalmente por qué el comando hdfs dfs -cat continúa mostrando la totalidad de los datos del archivo sin errores a pesar de la falla.
Respuesta Correcta: 1. Primeros 45 s: dfsadmin -report aún lista Live datanodes (2), pues la ventana de 60 s no ha vencido; el contador Last contact de DN2 se incrementa continuamente.
2. A los 65 s: fsck reporta Live_repl = 1, Under-replicated blocks = 1 (100%), Missing blocks = 0. DN2 pasa a Dead datanodes.
3. Justificación de lectura: DN1 conserva una copia íntegra del bloque. HDFS garantiza lectura transparente mientras exista al menos una réplica viva disponible.
Explicación: 1. Estado de gracia hasta expirar la ventana de timeout.
2. Diagnóstico de sub-replicación sin pérdida de bloques.
3. Disponibilidad continua mediante la réplica restante en DN1.

# Módulo 9: Calibración Fina de Parámetros, Permisos y Despliegue de Producción HDFS

[TIPO: OPCION MULTIPLE]
Pregunta ID: 41
Enunciado: En un clúster HDFS contenerizado mediante Docker Compose sobre un sistema anfitrión Windows, se observa el siguiente error recurrente en los registros de inicio del NameNode: Permission denied: user hadoop (UID 1000) cannot write to /opt/hadoop/data/name. Al mismo tiempo, los DataNodes no logran registrarse reportando fallos de resolución DNS en la red virtual. ¿Qué combinación de directivas en el manifiesto docker-compose.yml resuelve de manera integral ambos fallos de infraestructura?
Opciones: A) Configurar user: root en todos los servicios y establecer HDFS-SITE.XML_dfs.namenode.datanode.registration.ip-hostname-check: 'false'. B) Eliminar la sección volumes e inyectar la variable de entorno HADOOP_DEFAULT_FS: hdfs://localhost:9000. C) Modificar el tiempo de recheck-interval a 300,000 ms y ejecutar el contenedor en modo interactivo sin depends_on. D) Cambiar la imagen base a Linux Alpine y asignar factor de replicación dfs.replication: '3' en un clúster de 2 nodos. E) Ninguna de las anteriores.
Respuesta Correcta: A
Explicación: user: root subsana las restricciones de permisos en bind mounts de Windows y ip-hostname-check: false permite que los DataNodes se registren en redes bridge de Docker sin DNS inverso.

Fuente 9: Calibración Fina de Parámetros, Permisos y Despliegue de Producción HDFS
Instrucción: Relacione el error u omisión de configuración en entornos HDFS (Columna A) con la causa técnica subyacente y solución de ingeniería (Columna B):
Columna A
1. Salida Live datanodes (0) en dfsadmin
2. NameNode is in safe mode al hacer put
3. Salida ls /datos_local muestra total 0
4. Error cmdlet no reconocido al correr hdfs
Columna B
a. Se intentó ejecutar un comando nativo de Linux/Hadoop en PowerShell en lugar de la consola interactiva del contenedor.
b. Mapeo incorrecto de bind mount en docker-compose.yml; la ruta anfitriona no coincide con la ubicación del archivo.
c. Los DataNodes iniciaron antes que el servicio RPC del maestro o falló la resolución de IP; requiere depends_on e ip-hostname-check: false.
d. El NameNode está en modo de solo lectura recolectando reportes de bloques al arrancar; requiere aguardar a que safemode se apague.
Respuestas: 1-c, 2-d, 3-b, 4-a
Explicación: 1-c (0 DataNodes: registro fallido por IP/DNS), 2-d (Safe mode: proceso de arranque de solo lectura), 3-b (ls vacío: error de bind mount), 4-a (cmdlet no reconocido: comando ejecutado en host en vez del contenedor).

Fuente 9: Calibración Fina de Parámetros, Permisos y Despliegue de Producción HDFS
Instrucción: Organice la secuencia de estados y validaciones que realiza el NameNode durante su proceso de arranque (bootstrapping) antes de habilitar operaciones de escritura:
Columna A
1. El NameNode abre el puerto RPC 9000 y el puerto HTTP 9870, e ingresa automáticamente en Modo Seguro (Safemode).
2. Los DataNodes se conectan al NameNode y transmiten sus informes de inventario de bloques locales (Block Reports).
3. El NameNode lee y carga en memoria RAM la imagen del sistema de archivos (fsimage) y aplica el registro de transacciones (edits).
4. El NameNode verifica que el 99.9% de los bloques alcancen el factor mínimo de replicación y desactiva Safemode (Safemode is off).
Columna B
1. 1ª posición
2. 2ª posición
3. 3ª posición
4. 4ª posición
Respuestas: 1-2, 2-3, 3-1, 4-4
Explicación: Secuencia: 3 -> 1 -> 2 -> 4. Carga en RAM de fsimage y edits (3), apertura de puertos e ingreso en Safemode (1), recepción de Block Reports (2) y desactivación de Safemode al superar el umbral de replicación (4).

[TIPO: RESPUESTA CORTA]
Pregunta ID: 44
Enunciado: Escriba el término técnico exacto (prefijo BP-...) que designa el identificador criptográfico del conjunto de bloques que aísla las estructuras de almacenamiento de un NameNode respecto a otros clústeres.
Respuesta Correcta: Block Pool ID / BP-... / ID de conjunto de bloques
Explicación: Block Pool ID (identificador del conjunto de bloques de HDFS).

[TIPO: DESARROLLO]
Pregunta ID: 45
Enunciado: Durante un mantenimiento programado en un centro de datos, se reinician simultáneamente todos los servidores de un clúster HDFS de producción. Al volver a iniciar el servicio NameNode, los administradores intentan ingestar de inmediato un archivo crítico mediante hdfs dfs -put, pero el sistema rechaza la operación devolviendo el mensaje de error: RemoteException: NameNode is in safe mode.

Requerimiento:
1. Explique la razón arquitectónica por la cual el NameNode entra automáticamente en Safemode durante el arranque y qué operaciones están permitidas y prohibidas durante este estado.
2. Describa las condiciones internas necesarias para que el NameNode abandone Safemode de forma autónoma.
3. Proporcione la instrucción CLI exacta para forzar la salida manual de Safemode en caso de una emergencia operativa respaldada por auditoría.
Respuesta Correcta: 1. Razón: Safemode previene inconsistencias permitiendo solo lectura mientras los DataNodes reportan sus bloques en memoria; prohíbe escrituras y modificaciones.
2. Salida autónoma: Requiere que al menos el 99.9% de los bloques reporten su factor mínimo de replicación configurado.
3. Comando CLI: hdfs dfsadmin -safemode leave.
Explicación: 1. Protección de metadatos durante la sincronización de inventario.
2. Umbral mínimo de replicación (99.9%).
3. Comando administrativo: hdfs dfsadmin -safemode leave.
