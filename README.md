# Informe 2 · Optimización · Grupo 7

Debemos elegir los materiales de una vivienda con el menor costo posible, respetando su límite de transmitancia térmica. Usaremos **MiniZinc** y resolveremos **15 instancias: 5 pequeñas, 5 medianas y 5 grandes**.

## Reparto del trabajo

| Persona | Su carpeta | Qué debe hacer |
| --- | --- | --- |
| **Mena** | [Mena](Mena/README.md) | Redactar la introducción y las conclusiones a partir de los hallazgos del equipo. |
| **Jose** | [Jose](Jose/README.md) | Revisar el modelo, corregir el generador y desarrollar la sensibilidad térmica y de costo. |
| **Joaquin** | [Joaquin](Joaquin/README.md) | Implementar MiniZinc, ejecutar los experimentos, verificar soluciones y analizar el desempeño. |
| **Constanza** | [Constanza](Constanza/README.md) | Incorporar las tablas y figuras preparadas por el equipo, sus títulos y el formato de resultados. |

Cada persona trabaja en su carpeta. **`main.tex` reúne todo en el orden de la pauta.** Mena tiene la introducción y `conclusiones.tex`; Jose, el modelo, el generador y la sensibilidad; Joaquin, la implementación y los análisis de resultados y desempeño. `Constanza/parte.tex` organiza la presentación de resultados e incorpora esos análisis automáticamente.

## Cómo avanzar

1. Cada persona lee su README y trabaja principalmente en su carpeta.
2. Jose y Joaquin acuerdan los datos, escenarios y métricas. Jose prepara las instancias y el análisis de sensibilidad; Joaquin ejecuta el modelo y prepara los resultados y el análisis de desempeño.
3. Ambos entregan las tablas y figuras listas, con sus explicaciones. Constanza las incorpora al informe y revisa títulos, referencias y presentación.
4. Mena redacta las conclusiones con el resumen de hallazgos de Jose y Joaquin. Todos revisan el PDF final.

Para ver el informe, abrir **`main.tex`** en el editor LaTeX y compilar con **pdfLaTeX** dos veces. En Overleaf, subir esta carpeta y elegir `main.tex` como documento principal. Las secciones se incorporan con `\input`; no llevan su propio inicio o fin de documento. Las figuras deben referenciarse desde la raíz, por ejemplo `Constanza/figuras/tiempos.pdf`.

Antes de editar, traer los cambios del equipo; al terminar, subir los propios con un mensaje claro. Evitar editar la carpeta de otra persona sin coordinarse.

## PDF actualizado en GitHub

Al subir cambios en cualquier `.tex`, en las figuras o en el generador incluido en el informe, GitHub compila `main.tex` automáticamente.

Para descargar el PDF: abrir [Actions · Compilar informe](https://github.com/jastudilloi/opti-informe-2-grupo-7/actions/workflows/compilar-informe.yml), entrar a la ejecución más reciente de la rama que se está revisando y descargar **`informe-2.pdf`** en «Artifacts». Esperar a que termine con una marca verde. Si falla, revisar el paso de compilación o el archivo `compilacion-log`.

Cada PDF corresponde a los cambios de su ejecución y se conserva 14 días. También se puede generar de nuevo con «Run workflow». El acceso sigue siendo privado para quienes tienen acceso al repositorio. La compilación local indicada arriba sigue disponible.

## Puntos que no se nos pueden pasar

- **Menor transmitancia significa mayor costo por m².** El generador anterior no siempre lo cumple.
- Las áreas deben corresponder a una vivienda coherente, con **superficie habitable, altura y volumen** definidos.
- Hay que respetar los rangos de tamaños del enunciado y contar también las categorías de los elementos fijos.
- Una solución factible no basta: debemos acreditar que es **óptima**.
- Al variar `U_max`, comparar factibilidad, costo, desempeño y **qué materiales cambian**.
- La plantilla pide un margen de costo sin definirlo: acordar su interpretación y explicarla. El presupuesto no es una restricción explícita del modelo original.

## Checklist de entrega

- [ ] Completar paralelo, nombres y correos en la portada.
- [ ] Revisar el modelo y sus supuestos.
- [ ] Corregir costos y áreas del generador.
- [ ] Generar y validar las 15 instancias; obtener su tabla resumen desde los archivos.
- [ ] Resolverlas con MiniZinc y guardar evidencia de optimalidad.
- [ ] Comprobar selecciones, costo y balance térmico de cada solución.
- [ ] Comparar escenarios de `U_max` y definir el análisis del margen de costo.
- [ ] Incorporar tablas y gráficos de resultados, tiempos y cambios de materiales.
- [ ] Cerrar las conclusiones entre todos.
- [ ] Incluir el código del generador y de la implementación, con instrucciones para ejecutarlos.
- [ ] Quitar todos los avisos «Pendiente», compilar `main.tex` y revisar el PDF.
- [ ] Confirmar fecha y formato de entrega en el canal del curso.

## Material para empezar

La pauta, la asignación de solver, la retroalimentación y el enunciado están en esta carpeta. En [referencias/informe_1](referencias/informe_1) está la primera entrega, con sus datos originales. El modelo y el generador están en la carpeta de Jose para continuar desde ellos.

**Los datos originales son antecedentes: todavía necesitan las correcciones indicadas.** Para el detalle, consultar [el contexto de la primera entrega](CONTEXTO_INFORME_1.md) y [el plan de la segunda](PLAN_INFORME_2.md). Implementación y resultados suman **75 de los 100 puntos** de esta entrega.
