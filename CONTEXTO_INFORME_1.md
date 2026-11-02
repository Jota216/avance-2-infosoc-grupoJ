# Contexto del Informe 1 y correcciones del generador

Fecha de revisión: 26 de octubre de 2026.

## Propósito y alcance

Este archivo conserva el contexto necesario para continuar el proyecto Bio Planner en la segunda entrega, especialmente las observaciones sobre el generador de instancias. La revisión abarcó el PDF, el código LaTeX, el generador Python, las 15 instancias JSON, la retroalimentación y el enunciado original incorporado posteriormente. Esta versión actualiza las conclusiones de la revisión inicial con los requisitos explícitos del enunciado.

Según lo indicado por el equipo, el generador fue la única sección con descuento. La evidencia local registra **40/50 en el generador**, equivalente a 10 puntos descontados en esa sección; no incluye una pauta con las notas de las demás secciones ni permite comprobar la nota total.

Esta revisión no modifica el generador, las instancias ni el informe original. Las correcciones descritas son trabajo pendiente.

## Fuentes locales

| Fuente | Ubicación y referencia |
| --- | --- |
| Enunciado original | [proyecto2026_2_enunciado (1).pdf](<proyecto2026_2_enunciado (1).pdf>), 2 páginas. Problema y balance térmico: p. 1; criterios del generador, sensibilidad y rangos: p. 2. |
| Informe 1 | [Proyecto entrega 1 grupo 7.pdf](<referencias/informe_1/Proyecto entrega 1 grupo 7.pdf>), 8 páginas. Modelo: pp. 1-4; generador: pp. 4-8; tabla de instancias: p. 6. |
| Fuente del informe | [main.tex](<referencias/informe_1/main.tex>). |
| Generador entregado | [generador.py](<referencias/informe_1/generador.py>), 108 líneas. |
| Datos entregados | Carpeta `referencias/informe_1/instancias/`, archivos `instancia_01.json` a `instancia_15.json`. |
| Retroalimentación | [retroalimentacion.txt](<retroalimentacion.txt>). Aunque está en la carpeta de la segunda entrega, su contenido evalúa el generador de la primera. |

## Requisitos confirmados por el enunciado

El enunciado resuelve las principales dudas de la revisión inicial:

- **Relación entre transmitancia y costo:** a menor transmitancia, mayor costo por metro cuadrado, dentro de cada categoría. La dirección utilizada en el informe es correcta (p. 2).
- **Dimensiones obligatorias:** se deben definir superficie habitable, altura y volumen interior, además de asignar áreas a los elementos. No basta con generar áreas independientes (p. 2).
- **Tamaños obligatorios:** 15 instancias factibles, cinco de cada tamaño, con los rangos de la tabla del enunciado; coinciden con las configuraciones del código actual (p. 2).
- **Categorías:** la columna cuenta el total de tipos de componentes considerados en la vivienda, no solamente los que tienen elementos libres. Los elementos fijos también deben encajar en esa clasificación (p. 2).
- **Sensibilidad obligatoria:** variar `U_max` y evaluar factibilidad, espacio de búsqueda y distribución de materiales seleccionados (p. 2).
- **Modelo base:** minimizar el costo de materiales, conservar los elementos fijos, elegir exactamente una alternativa por libre y limitar la transmitancia promedio ponderada por área (p. 1).

El enunciado no impone JSON ni otro formato de almacenamiento, no fija un número de elementos fijos y no da rangos numéricos para dimensiones, áreas, costos o transmitancias. Esas decisiones deben documentarse y ser técnicamente coherentes. Tampoco define una demanda en kWh ni un presupuesto máximo de costo; el margen de costo mencionado en la plantilla de la Entrega 2 sigue requiriendo una definición explícita.

## Problema y modelo que se deben conservar

Se elige exactamente una alternativa constructiva para cada elemento libre de una vivienda, desde el catálogo de su categoría. Cada alternativa tiene transmitancia térmica `U` y costo por metro cuadrado `C`. Se minimiza el costo total respetando una transmitancia promedio ponderada por área máxima `U_max`.

Notación:

- `I^O`: elementos optimizables; `I^F`: elementos fijos.
- `J_c`: alternativas de la categoría `c`; `g(i)`: categoría del elemento.
- `A_i`: área en m²; `U_ij` y `U_i^F`: transmitancias en W/(m²·K).
- `C_ij` y `C_i^F`: costos en unidades monetarias por m².
- `x_ij`: variable binaria que indica si se usa la alternativa `j` en el elemento `i`.

```text
min Z = sum(i libre, j de su categoría) A_i C_ij x_ij
        + sum(i fijo) A_i C_i^F

sum(j de su categoría) x_ij = 1                  para cada i libre

sum(i libre, j) A_i U_ij x_ij + sum(i fijo) A_i U_i^F
    <= U_max * sum(i de todos los elementos) A_i

x_ij pertenece a {0, 1}
```

El costo fijo es constante y no cambia la selección óptima, pero debe incluirse al reportar el costo total. El área total del balance corresponde a las superficies constructivas consideradas, no a la superficie habitable de la vivienda.

## Retroalimentación recibida

El comentario califica el generador como muy bueno y señala tres asuntos:

1. Menciona detalles relacionados con el uso de JSON, sin precisar una falla de esquema, lectura o formato ni exigir expresamente reemplazarlo.
2. Indica casos donde no se cumple la relación esperada entre transmitancia y precio.
3. Cuestiona las áreas aleatorias porque no se vinculan con dimensiones físicas coherentes de una vivienda.

**Discrepancia resuelta mediante el enunciado:** la retroalimentación dice literalmente «una mayor transmitancia tengo un precio mayor», pero el enunciado establece explícitamente la relación inversa: **menor transmitancia implica mayor costo** (p. 2). Esa es la regla que se debe implementar y validar. La frase del comentario contradice el enunciado; no es necesario dejar pendiente el sentido de la relación ni invertir la fórmula por esa frase.

## Funcionamiento actual del generador

La función `generar_instancias()` fija `random.seed(42)` y crea cinco instancias de cada tamaño:

| Tamaño | Categorías | Alternativas por categoría | Elementos libres |
| --- | --- | --- | --- |
| Pequeña | 3-4 | 5-10 | 2-4 |
| Mediana | 5 | 11-25 | 5-8 |
| Grande | 5 | 26-50 | 9-15 |

En cada instancia se usa una misma cantidad de alternativas para todas sus categorías. Además:

- Se generan entre 2 y 4 elementos fijos.
- Todas las áreas, libres y fijas, se muestrean independientemente entre 5 y 40 m², con dos decimales.
- Las categorías son etiquetas genéricas `CAT-1`, `CAT-2`, etc.; cada elemento libre recibe una al azar.
- Para las alternativas, `U` está entre 0.3 y 3.5 y `C = round((15000/U)*(1+ruido), 0)`, con ruido independiente entre -10 % y +10 %.
- Para los elementos fijos, `U_fijo` está entre 0.8 y 3.0 y `C_fijo = round(15000/U_fijo, 0)`.
- El límite se calcula como `round(U_min_global * holgura, 2)`, con holgura entre 1.1 y 1.5.
- El único control explícito es `assert U_max >= U_min_global`.
- La salida contiene `metadata`, `catalogo` y `elementos`; los archivos se escriben en el directorio desde el cual se ejecuta el programa.

La semilla y las configuraciones están escritas dentro de la función; no se reciben mediante argumentos o línea de comandos, aunque el texto del informe habla de parámetros de entrada.

## Hallazgos comprobados

### 1. El ruido rompe la monotonía de los costos

Ubicación: `generador.py`, líneas 32-38.

Usar una fórmula inversa con ruido independiente no garantiza el orden entre alternativas próximas. Al comparar todos los pares con transmitancias distintas dentro de cada categoría, se encontraron **974 pares que incumplen `U_a < U_b => C_a > C_b`**, distribuidos en **13 de las 15 instancias**. Este conteo incluye todo el catálogo, incluso categorías sin elementos libres asignados, y no cuenta pares con igual `U`.

Ejemplo de `instancia_02.json`, categoría `CAT-1`:

| Alternativa | U | C por m² |
| --- | --- | --- |
| ALT-CAT-1-1 | 2.33 | 6264 |
| ALT-CAT-1-4 | 2.37 | 6467 |

La alternativa con menor `U` también cuesta menos, contrario a la regla declarada. Ordenar la lista por `U` no corrige este problema: hay que corregir la generación de los costos.

Corrección propuesta, pendiente: generar transmitancias distintas y asignar costos mediante una función inversa determinista por categoría, o construir explícitamente una secuencia de costos decreciente al ordenar `U` de menor a mayor. Si se conserva variación aleatoria, debe respetar ese orden después del redondeo. Validar todos los pares o los pares consecutivos de la secuencia ordenada y definir qué hacer con empates de `U` o costo.

### 2. Las áreas no provienen de una geometría

Ubicación: líneas 51-59 y 67-77.

No se generan largo, ancho, altura, superficie habitable ni volumen. Tampoco se identifican fachadas, vanos, techumbre o piso mediante categorías físicas. Por ello no puede comprobarse que las áreas formen una vivienda coherente. La ausencia de superficie habitable, altura y volumen **incumple un requisito explícito del enunciado**, además de diferir del texto del informe, que afirma que esas dimensiones forman parte de la caracterización de cada instancia. Largo y ancho son una forma propuesta de construir una geometría consistente; el enunciado no exige específicamente esos dos parámetros.

Corrección propuesta, pendiente:

1. Definir una geometría simplificada y documentada, por ejemplo una vivienda rectangular de una planta con largo `L`, ancho `W` y altura `h`.
2. Derivar superficie habitable `L*W`, volumen `L*W*h`, muros brutos `2*(L+W)*h` y áreas de piso y techo según el supuesto adoptado.
3. Ubicar ventanas y puertas en fachadas concretas; descontar sus áreas del muro opaco correspondiente para evitar doble conteo.
4. Particionar superficies físicas para alcanzar la cantidad de elementos libres, en vez de aumentar arbitrariamente el área de la vivienda al aumentar el número de decisiones.
5. Asignar el estado libre/fijo a esas superficies o particiones, conservando el total de cada superficie. Contar las categorías de todos los elementos, incluidos los fijos, dentro del límite de 3-4 o 5 tipos de la instancia. No añadir tipos fijos fuera de ese conteo para completar una vivienda pequeña; utilizar una representación simplificada y documentar qué superficies se consideran en su balance.
6. Guardar dimensiones, categorías físicas y relaciones de pertenencia para que otro programa pueda comprobar la geometría.

Definir las dimensiones es obligatorio; la geometría rectangular, las fórmulas de fachadas y la partición de superficies son propuestas para cumplir ese requisito y la coherencia técnica. Los rangos geométricos y los supuestos constructivos se deben justificar. Esta propuesta no constituye una certificación de cumplimiento normativo.

### 3. JSON necesita un contrato de datos claro

No se observó un error de lectura: los 15 archivos pudieron cargarse correctamente. Ni el comentario ni el enunciado prohíben expresamente JSON; el enunciado no fija un formato de almacenamiento.

Sí hay mejoras concretas: `metadata` no guarda semilla ni versión del generador, los fijos no tienen categoría, y no hay dimensiones físicas ni unidades explícitas. La categoría de los fijos no es necesaria para evaluar sus constantes en el modelo actual, pero sí ayuda a mantener coherencia con la definición de `g(i)` para todos los elementos y con la geometría.

Recomendación: conservar JSON como formato de intercambio y documentar su esquema; agregar identificación y versión, semilla/configuración, unidades, las dimensiones obligatorias, geometría y categorías de libres y fijos. Para la Entrega 2 se debe preparar la conversión al formato de entrada utilizado con MiniZinc. Cambiar el formato por sí solo no soluciona los costos ni las áreas.

### 4. La tabla del informe no representa los JSON entregados

La tabla de la p. 6 del PDF también aparece en `main.tex`. Sus filas presentan diferencias respecto de los datos reales. Por ejemplo, `INST-01` aparece con 7 alternativas por categoría, 3 elementos libres y `U_max=1.45`, pero el archivo contiene 5 alternativas, 4 libres y `U_max=1.25`.

Resumen calculado directamente desde los archivos actuales:

| ID | Tamaño | Categorías | Alternativas por categoría | Libres | Fijos | U_max | Binarias del modelo |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| INST-01 | Pequeña | 3 | 5 | 4 | 3 | 1.25 | 20 |
| INST-02 | Pequeña | 3 | 8 | 3 | 3 | 1.47 | 24 |
| INST-03 | Pequeña | 3 | 8 | 2 | 4 | 1.83 | 16 |
| INST-04 | Pequeña | 4 | 6 | 3 | 3 | 1.20 | 18 |
| INST-05 | Pequeña | 3 | 9 | 4 | 2 | 1.69 | 36 |
| INST-06 | Mediana | 5 | 11 | 7 | 3 | 1.15 | 77 |
| INST-07 | Mediana | 5 | 21 | 7 | 3 | 1.11 | 147 |
| INST-08 | Mediana | 5 | 20 | 5 | 2 | 1.84 | 100 |
| INST-09 | Mediana | 5 | 24 | 7 | 2 | 1.09 | 168 |
| INST-10 | Mediana | 5 | 15 | 8 | 4 | 1.08 | 120 |
| INST-11 | Grande | 5 | 30 | 10 | 2 | 1.29 | 300 |
| INST-12 | Grande | 5 | 32 | 15 | 2 | 0.70 | 480 |
| INST-13 | Grande | 5 | 43 | 12 | 2 | 0.77 | 516 |
| INST-14 | Grande | 5 | 49 | 13 | 4 | 0.85 | 637 |
| INST-15 | Grande | 5 | 44 | 14 | 4 | 1.07 | 616 |

Las binarias se cuentan como `sum(i libre) |J_g(i)|`, sin crear variables para categorías que no corresponden al elemento. Esta tabla describe la entrega original; deberá regenerarse al corregir las instancias.

### 5. Hay una base correcta de reproducibilidad y factibilidad

Se ejecutó la rutina con captura de salida en memoria, sin escribir ni reemplazar instancias. Los **15 objetos generados con semilla 42 coincidieron con los 15 JSON entregados**.

Para cada instancia se recalculó:

```text
U_min_global = [sum(i libre) A_i * min(j) U_ij
                + sum(i fijo) A_i U_i^F] / sum(i) A_i
```

Las 15 cumplen `U_min_global <= U_max`. Elegir una alternativa de mínima transmitancia para cada libre constituye una solución testigo factible del modelo actual, ya que no hay restricciones de acoplamiento adicionales. Esto acredita existencia de una solución; **no calcula ni demuestra el costo óptimo**.

La selección de menor costo por elemento incumple el límite térmico en las 15 instancias actuales. Hay, por tanto, un conflicto entre el objetivo y la restricción térmica que merece resolverse mediante optimización.

La garantía basada únicamente en `U_min_global` deberá revisarse si se agregan presupuesto u otras restricciones. Asimismo, el control debe hacerse con los valores finales serializados y su precisión numérica.

### 6. Otras diferencias de documentación

- El informe atribuye el rango 0.3-3.5 tanto a libres como a fijos; el código usa 0.8-3.0 para los fijos.
- Algunas categorías del catálogo no se asignan a ningún elemento libre. No es automáticamente un error, pero deben distinguirse categorías disponibles y categorías efectivamente utilizadas.
- El PDF y el `.tex` conservan marcadores de título/autores y texto instructivo en introducción y conclusiones. Es una observación sobre la copia local, no evidencia de descuentos adicionales.

### 7. Falta el análisis de sensibilidad exigido en el enunciado

La p. 2 pide variar el máximo de transmitancia permitido y analizar factibilidad, espacio de búsqueda y distribución de materiales seleccionados. El generador actual asigna un único `U_max` a cada instancia, y el informe local no presenta una comparación de escenarios ni resultados de selección de materiales.

Para la segunda entrega, conservar geometría y catálogos al variar `U_max`, resolver cada escenario y registrar qué alternativa se selecciona en cada elemento. Comparar también la composición de materiales por categoría y por área, porque las áreas pueden diferir. Este requisito se suma al análisis de desempeño y márgenes de la plantilla; no se satisface únicamente graficando tiempos o costos.

## Lista de cierre para corregir el generador

- [x] Confirmar con el enunciado la regla: menor transmitancia implica mayor costo.
- [ ] Garantizar y validar monotonía después del redondeo.
- [ ] Definir superficie habitable, altura y volumen, y generar áreas coherentes con esas dimensiones, sin doble conteo.
- [ ] Cumplir cinco instancias por tamaño y los rangos del enunciado, contando categorías de libres y fijos.
- [ ] Documentar y validar el esquema de datos y la conversión hacia MiniZinc.
- [ ] Parametrizar semilla, configuración y directorio de salida.
- [ ] Validar identificadores, referencias de categoría, dominios, unidades y existencia de alternativas.
- [ ] Guardar una selección testigo y verificar su factibilidad con los datos serializados.
- [ ] Regenerar las 15 instancias y producir la tabla del informe desde esos mismos archivos.
- [ ] Actualizar la explicación para que coincida con el código final.
- [ ] Evaluar sensibilidad a `U_max`, incluyendo factibilidad, espacio de búsqueda y distribución de materiales seleccionados.

Continuación: [plan de trabajo de la Entrega 2](PLAN_INFORME_2.md).
