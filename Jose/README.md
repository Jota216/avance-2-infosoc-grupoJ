# Jose · Modelo, instancias y sensibilidad

Revisa el modelo en `modelo.tex`, explica el generador en `parte.tex` y desarrolla el análisis de márgenes en `sensibilidad.tex`. Trabaja sobre `generador.py`, copiado de la primera entrega. **Todavía tiene las fallas observadas; hay que corregirlo antes de usar sus datos finales.**

- [ ] Acordar con Joaquin el formato de entrada y las unidades.
- [ ] Revisar la formulación matemática, sus supuestos y su correspondencia con el código de MiniZinc.
- [ ] Garantizar que menor transmitancia implique mayor costo dentro de cada categoría, incluso después de redondear.
- [ ] Definir superficie habitable, altura y volumen, y obtener áreas coherentes sin doble conteo.
- [ ] Identificar las categorías de libres y fijos y respetar los rangos del enunciado.
- [ ] Generar 15 instancias factibles, cinco de cada tamaño, con semilla reproducible.
- [ ] Guardar las instancias definitivas en `instancias/`, dentro de esta carpeta.
- [ ] Validar los datos y una selección que demuestre factibilidad.
- [ ] Producir la tabla resumen desde los archivos, sin rellenarla a mano.
- [ ] Explicar rangos, algoritmo, almacenamiento y validación en `parte.tex`.
- [ ] Dejar aquí el comando de generación y revisar el código que se incluye al final del informe.
- [ ] Diseñar con Joaquin los escenarios de U_max y definir la interpretación del margen de costo.
- [ ] Analizar factibilidad, costo y cambios de materiales a partir de las ejecuciones de Joaquin.
- [ ] Preparar las tablas y figuras de sensibilidad y entregar a Constanza los archivos listos y sus explicaciones.
- [ ] Entregar a Mena un resumen de los hallazgos del modelo, instancias y sensibilidad.

Los JSON anteriores están en `../referencias/informe_1/instancias/` solo como referencia. No mezclar esos archivos con los corregidos. Coordinar cualquier cambio de formato antes de que Joaquin ejecute los experimentos.
