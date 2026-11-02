# Qué hay que hacer para el Informe 2

Fecha de revisión: 26 de octubre de 2026.

## Objetivo de la nueva entrega

La segunda entrega exige implementar el modelo con el solver asignado, resolver las 15 instancias, acreditar la optimalidad de las soluciones y analizar los resultados mediante tablas, gráficos y experimentos con márgenes relativos. También exige presentar nuevamente el problema, el modelo y el generador. El enunciado original confirma que la sensibilidad térmica consiste en variar `U_max` y estudiar también la distribución de materiales seleccionados.

Para el **grupo 7 corresponde MiniZinc**, según `AsignacionSolver.pdf`. La identificación del grupo se toma de la carpeta `Informe_Grupo_7` y del nombre del PDF de la primera entrega; su portada aún conserva marcadores genéricos.

Este documento es una guía de trabajo basada en los archivos disponibles. No contiene resultados experimentales ni una implementación ya realizada. Las correcciones pendientes del generador se detallan en [CONTEXTO_INFORME_1.md](CONTEXTO_INFORME_1.md).

## Fuentes y límites de la información disponible

| Fuente | Contenido utilizado |
| --- | --- |
| [proyecto2026_2_enunciado (1).pdf](<proyecto2026_2_enunciado (1).pdf>) | Enunciado original de 2 páginas: modelo base (p. 1), dimensiones, relación U/costo, tamaños y sensibilidad térmica (p. 2). |
| [plantilla-informe-2.pdf](<plantilla-informe-2.pdf>) | Pauta de 2 páginas: secciones, requisitos y puntajes. |
| [plantilla-informe-2.tex](<plantilla-informe-2.tex>) | Fuente editable de la pauta; su contenido concuerda con el PDF. |
| [AsignacionSolver.pdf](<AsignacionSolver.pdf>) | Tabla de asignaciones: grupo 7, MiniZinc. |
| [retroalimentacion.txt](<retroalimentacion.txt>) | Observaciones al generador previo, con 40/50. |
| Material del Informe 1 | Modelo binario, generador y 15 instancias originales. |

La carpeta `informe 2` contiene sus cuatro archivos de referencia; no contiene aún un modelo MiniZinc, un ejecutor ni resultados. El enunciado original ahora está disponible en la raíz de `opti` y fue revisado completo. Los archivos disponibles no indican una fecha límite, instrucciones de empaquetado ni una selección de motor de resolución para MiniZinc.

## Qué aclara el enunciado y qué sigue pendiente

| Tema | Conclusión para el trabajo |
| --- | --- |
| Transmitancia y costo | **Menor U implica mayor costo por m²** dentro de cada categoría (p. 2). Queda resuelta la discrepancia con la frase de la retroalimentación. |
| Geometría | **Superficie habitable, altura y volumen interior son obligatorios**, junto con las áreas de elementos coherentes con la vivienda (p. 2). Una planta rectangular es una opción de implementación. |
| Instancias | **15 factibles: cinco pequeñas, cinco medianas y cinco grandes**, respetando los rangos del Cuadro 1 (p. 2). |
| Conteo de categorías | Se cuentan los tipos de componentes considerados en toda la vivienda, incluidos los fijos; no solo categorías con decisiones libres (p. 2). |
| Sensibilidad térmica | Variar **U_max** y evaluar factibilidad, espacio de búsqueda y **distribución de materiales seleccionados** (p. 2). |
| Formato de datos | El enunciado no exige un formato ni prohíbe JSON. Documentar el esquema y la conversión a MiniZinc. |
| Demanda energética | El modelo concreto del enunciado limita transmitancia promedio ponderada, no una demanda en kWh. Usar ese indicador térmico y explicitar la terminología de la plantilla. |
| Margen de costo | La plantilla pide analizarlo, pero el enunciado no define C_max, una referencia de costo o una fórmula de margen. Se debe explicitar la interpretación elegida o aclararla con el docente. |

Rangos obligatorios del Cuadro 1:

| Tamaño | Categorías totales | Alternativas por categoría | Elementos libres |
| --- | --- | --- | --- |
| Pequeña | 3-4 | 5-10 | 2-4 |
| Mediana | 5 | 11-25 | 5-8 |
| Grande | 5 | 26-50 | 9-15 |

El enunciado no fija cantidades de elementos fijos, rangos geométricos ni valores numéricos de áreas, transmitancias y costos. Deben definirse y justificarse; los 2-4 fijos del generador anterior son una decisión del equipo.

## Requisitos y ponderación

| Sección | Puntos | Qué debe quedar listo |
| --- | ---: | --- |
| Introducción | 5 | Problema, motivación, contexto, objetivo y principales supuestos. |
| Modelamiento | 5 | Conjuntos, índices, parámetros con unidades/fuentes/rangos, variables y dominios, objetivo y todas las restricciones explicadas. |
| Generador de instancias | 5 | Procedimiento reproducible para 15 instancias factibles, configuración, estructura/almacenamiento, validación, tabla resumen y código completo. |
| Implementación | 30 | Solver asignado, búsqueda de optimalidad, construcción automática desde datos, ejecución por instancia, parámetros, criterios de optimalidad, formato de solución y verificaciones. Código en archivo independiente. |
| Resultados | 45 | Experimentos sobre las 15 instancias, tablas y gráficos de objetivos óptimos, factibilidad, tiempos y métricas; análisis de márgenes relativos y desempeño. Incorporar la distribución de materiales que exige la sensibilidad térmica del enunciado. |
| Conclusiones | 10 | Hallazgos del modelo, generador y solver; calidad/optimalidad, márgenes y relación entre tamaño y desempeño. |
| **Total** | **100** | **Implementación y resultados concentran 75 puntos.** |

La pauta solicita las métricas de nodos y brecha de optimalidad cuando estén disponibles. No corresponde inventarlas ni registrar cero cuando el motor no las informa.

## Orden de trabajo propuesto

### 1. Corregir y cerrar las instancias

- [x] Confirmar la regla con el enunciado: menor `U` implica mayor costo por m².
- [ ] Corregir el ruido que rompe la monotonía y validar el resultado después del redondeo.
- [ ] Definir y guardar superficie habitable, altura y volumen interior; derivar áreas de una geometría documentada y categorías físicas.
- [ ] Contar las categorías de todos los elementos, incluidos los fijos, dentro de los rangos. No añadir categorías fijas fuera de ese total para completar una vivienda pequeña.
- [ ] Documentar el esquema de datos y cómo alimentará a MiniZinc. El enunciado no impone un formato de almacenamiento.
- [ ] Generar cinco pequeñas, cinco medianas y cinco grandes con los rangos confirmados del enunciado.
- [ ] Generar 15 instancias base factibles, con semilla/configuración identificables y una solución testigo verificable.
- [ ] Obtener automáticamente la tabla resumen desde los archivos definitivos. La tabla original no coincide con sus JSON.

Conviene completar este paso antes de los experimentos: cambiar catálogos, áreas o umbrales invalida las comparaciones hechas sobre datos anteriores.

### 2. Implementar el modelo para MiniZinc

Trasladar el modelo del Informe 1:

- Variables binarias para pares válidos de elemento libre y alternativa de su categoría.
- Una igualdad de selección por elemento libre.
- Una restricción de transmitancia ponderada por área, incluyendo la contribución fija.
- Minimización de costo por área, con reporte del costo total incluyendo fijos.

El cargador o conversor debe leer cada instancia sin editar el modelo a mano. Debe conservar la correspondencia entre índices internos e identificadores originales, y rechazar datos inválidos con un mensaje claro. Usar un archivo `.dzn` generado u otro mecanismo de entrada compatible que se documente y verifique en el entorno elegido.

**MiniZinc es el sistema de modelado asignado; falta elegir y registrar el motor que ejecutará la búsqueda.** La explicación de cómo se obtiene el óptimo debe corresponder a ese motor y a la configuración realmente utilizados. Registrar versiones, parámetros, tolerancias, límites de tiempo y semillas del motor cuando correspondan.

Si se escalan costos o transmitancias para trabajar con enteros, explicar factores y unidades, y comprobar que no se altera el problema por truncamiento o redondeos adicionales.

### 3. Automatizar ejecución, validación y registro

Preparar una rutina que recorra las 15 instancias, invoque MiniZinc, guarde la salida y consolide resultados.

Para cada solución, un verificador independiente debe:

1. Comprobar exactamente una selección válida por elemento libre y su dominio binario.
2. Reconstruir costo libre, costo fijo y costo total desde los datos originales.
3. Reconstruir el numerador térmico, el área total y la transmitancia promedio.
4. Comprobar `U_promedio <= U_max` con una tolerancia explícita.
5. Validar cualquier restricción adicional del escenario, como un presupuesto.
6. Comparar los valores recalculados con los reportados por el motor.

La factibilidad y la optimalidad son verificaciones distintas. Una solución factible no basta para cumplir la exigencia de óptimo: debe conservarse la evidencia de terminación óptima del motor, o sus cotas y certificado aplicables. Una ejecución interrumpida con incumbente debe registrarse como tal. Si una instancia base no termina con optimalidad demostrada, esa parte de la exigencia sigue pendiente.

Como comprobación adicional propuesta, una instancia pequeña puede resolverse por enumeración exhaustiva y contrastarse con MiniZinc. Esto no reemplaza el solver asignado para los experimentos.

### 4. Ejecutar el experimento base

- [ ] Resolver las 15 instancias corregidas bajo una configuración común documentada.
- [ ] Guardar soluciones, estados y registros originales de ejecución.
- [ ] Separar el tiempo de resolución del tiempo total de lectura, conversión y ejecución.
- [ ] Registrar equipo, sistema operativo, versiones y condiciones del experimento.
- [ ] Si se hacen repeticiones, definir cuántas y cómo se resumirán tiempos y variabilidad.

Dimensionalidad del modelo base escrito de forma directa:

```text
N_binarias = sum(i libre) |J_g(i)|
N_restricciones_algebraicas = |I^O| + 1
```

Ese conteo excluye dominios y corresponde al modelo matemático. El motor puede transformar el modelo; reportar por separado sus estadísticas internas cuando existan. Si se utiliza otra representación de variables, describirla y no confundir su conteo con el de binarias de la formulación original. Con presupuesto explícito se añade una desigualdad al modelo directo.

En los archivos originales hay entre 16 y 637 binarias. Esos valores son una referencia de la revisión, no resultados definitivos de las instancias corregidas.

### 5. Diseñar la sensibilidad térmica y el análisis de márgenes

**Requisitos combinados:** el enunciado pide variar `U_max` y estudiar factibilidad, espacio de búsqueda y distribución de materiales. La plantilla añade el análisis del valor objetivo y de los márgenes relativos térmicos y de costo. No se debe omitir ninguno de esos resultados.

**Serie térmica obligatoria:** mantener geometría, áreas, catálogo y elementos fijos de cada instancia, y variar únicamente el umbral térmico. Una parametrización propuesta es:

```text
U_max(r_U) = U_ref * (1 + r_U)
U_ref = U_max del escenario base de esa instancia
```

Una grilla inicial posible es `r_U ∈ {-20 %, -10 %, 0 %, +10 %, +20 %}`; los porcentajes y la fórmula relativa son decisiones experimentales que hay que documentar, no valores impuestos por el enunciado. Este sí confirma que el parámetro a variar es `U_max`. La expresión «demanda energética» de la plantilla debe contextualizarse mediante este indicador de transmitancia, conservando W/(m²·K); no se deben reportar kWh sin un modelo energético adicional.

En cada escenario se debe registrar factibilidad, costo óptimo, transmitancia obtenida, selección por elemento y composición de materiales por categoría y por área. Elegir un rango de umbrales que permita observar cambios; si la grilla inicial no los muestra, ampliarla justificadamente.

Comprobaciones analíticas útiles para interpretar la serie térmica:

- Si `U_max < U_min_global`, la instancia es infactible bajo el modelo base.
- Si `U_max` aumenta, el conjunto factible se amplía o permanece igual; el costo óptimo de minimización no puede aumentar si los demás datos permanecen fijos.
- Si el umbral admite una selección de mínimo costo independiente por elemento, ese costo ya es óptimo para el modelo base. No es necesario que todas las combinaciones sean factibles para llegar a esa meseta.
- El tiempo y los nodos del motor no tienen por qué variar de forma monótona con el umbral, aunque exista inclusión entre conjuntos factibles.

Las 15 instancias base deben ser factibles; escenarios térmicos deliberadamente más exigentes pueden ser infactibles y ese resultado forma parte del análisis.

**Margen de costo pendiente de definición:** ni el enunciado ni la plantilla definen un presupuesto `C_max`, una referencia o una fórmula de margen de costo. La p. 1 menciona restricciones configurables del usuario de forma general, lo que no impone por sí solo una restricción numérica de presupuesto. No agregarla al modelo base como si fuera un requisito explícito del caso.

Para cubrir el análisis pedido por la plantilla se propone una segunda serie experimental, identificada como extensión: agregar `Z_total <= C_max`, con `C_max(r_C) = C_ref * (1 + r_C)`, tomar `C_ref` como el costo óptimo total del escenario térmico base y conservarlo al cruzar los márgenes. Una grilla inicial posible es `r_C ∈ {-10 %, 0 %, +10 %, +25 %}`. Explicar y justificar esta interpretación, o sustituirla si el docente precisa otra definición. Esta cuestión no impide avanzar con el generador, el modelo base y la sensibilidad a `U_max` ya definidos.

Para un umbral térmico fijo, un presupuesto igual o superior al costo óptimo deja disponible ese mismo óptimo; un presupuesto inferior vuelve infactible el problema. La comparación conjunta con el margen térmico permite estudiar una frontera de factibilidad. No prometer que variar solo el presupuesto cambiará el valor óptimo cuando se sigue minimizando ese mismo costo.

No confundir los márgenes del problema con el `MIP gap` o una tolerancia de terminación del motor. Relajar el criterio de optimalidad no sustituye el análisis de márgenes solicitado.

### 6. Preparar tablas y gráficos

Tabla mínima de resultados por instancia base:

| Grupo de datos | Campos propuestos |
| --- | --- |
| Identificación | ID, tamaño, semilla y versión del generador. |
| Dimensión | Categorías, alternativas, libres, fijos, binarias y restricciones. |
| Límites y solución | U_max, transmitancia promedio obtenida, costo libre, fijo y total, selección de alternativas. |
| Composición de materiales | Alternativa por elemento, categoría y área cubierta; comparar distribución entre escenarios. |
| Estado | Factible/infactible, óptimo demostrado, interrupción o error. |
| Desempeño | Tiempo del motor y total, nodos, cota y gap si están disponibles. |
| Verificación | Resultado del verificador independiente y referencia al registro de ejecución. |

Para escenarios, agregar identificación de escenario, referencias, márgenes y límites efectivos. Si la salida no informa una métrica, registrar `no disponible` y explicar por qué.

Gráficos propuestos para cubrir la pauta:

- Tiempo de resolución frente a cantidad de binarias, distinguiendo tamaños.
- Nodos frente a tamaño, cuando el motor los informe.
- Costo óptimo y transmitancia promedio frente al margen de U_max.
- Distribución de materiales seleccionados por categoría y área frente a U_max; acompañar con una tabla de cambios de alternativa por elemento.
- Mapa de factibilidad al cruzar margen energético y de costo, si se implementa presupuesto.

Analizar tendencias y excepciones con datos. Más variables no garantizan mayor tiempo en cada caso; no concluir dificultad únicamente desde las etiquetas pequeña/mediana/grande. Los nodos explorados describen el esfuerzo del motor, no equivalen al número total de soluciones factibles.

### 7. Redactar el informe y preparar la entrega

- [ ] Completar portada con paralelo, grupo, nombres y correos reales.
- [ ] Escribir introducción y conclusiones propias; la copia local del Informe 1 conserva instrucciones de plantilla en ambas secciones.
- [ ] Reutilizar el modelo consistente y explicar cualquier extensión realizada.
- [ ] Actualizar generador, parámetros, rangos, esquema y tabla para reflejar los archivos finales.
- [ ] Explicar la implementación y la búsqueda de optimalidad del motor utilizado con MiniZinc.
- [ ] Incorporar tablas, gráficos y análisis de las 15 instancias y de los márgenes, incluyendo cambios de materiales al variar U_max.
- [ ] Explicar la interpretación del margen de costo y distinguir cualquier extensión de presupuesto del modelo base del enunciado.
- [ ] Diferenciar óptimos demostrados, soluciones factibles sin prueba e infactibilidad.
- [ ] Redactar conclusiones basadas en los resultados obtenidos, incluyendo casos extremos y limitaciones.
- [ ] Compilar y revisar visualmente el PDF final.
- [ ] Comprobar las instrucciones de entrega y fecha en el canal oficial del curso, ausentes de los documentos revisados.

## Archivos a producir

Los nombres siguientes son una organización propuesta; la pauta no impone estos nombres:

| Archivo o carpeta | Finalidad |
| --- | --- |
| `informe_2.tex` y PDF compilado | Informe completo según la plantilla y sus puntajes. |
| `generador.py` | Generador corregido; incluir también su código completo en la documentación según la pauta. |
| `instancias/` | Las 15 instancias base definitivas. |
| `modelo.mzn` | Modelo parametrizado para MiniZinc. |
| `ejecutar_experimentos.py` | Conversión de datos, invocación, verificación y ejecución de escenarios. |
| `datos_minizinc/` | Entradas generadas para el modelo, si se utiliza este mecanismo. |
| `resultados/` | Tablas consolidadas, soluciones y registros del motor. |
| `figuras/` | Gráficos derivados de las tablas consolidadas. |
| `README.md` | Dependencias, versiones y comandos para reproducir generación y experimentos. |

La pauta exige expresamente código de implementación en archivo independiente. Guardar registros y un README es una recomendación de reproducibilidad que facilita sustentar las verificaciones.

## Criterio de término

La entrega estará lista cuando las 15 instancias base corregidas cumplan las dimensiones, categorías y rangos del enunciado, se puedan generar y resolver automáticamente con MiniZinc, las soluciones pasen la verificación independiente y la optimalidad esté acreditada. El informe debe analizar factibilidad, costo, espacio de búsqueda y distribución de materiales al variar U_max; además debe explicitar el tratamiento del margen de costo pedido por la plantilla. Deben coincidir modelo, código, datos, tablas, gráficos y conclusiones, con evidencia reproducible.
