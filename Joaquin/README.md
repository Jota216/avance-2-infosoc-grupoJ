# Joaquin · MiniZinc, experimentos y desempeño

Explica la implementación en `parte.tex`, los resultados base en `resultados.tex` y el desempeño en `desempeno.tex`. Guarda aquí el modelo, los programas de ejecución y los datos de las corridas en `resultados/`.

- [ ] Acordar con Jose los datos de entrada, los escenarios de sensibilidad y las métricas a guardar.
- [ ] Crear `modelo.mzn`: una alternativa por libre, balance térmico con fijos y mínimo costo.
- [ ] Elegir y registrar el motor utilizado con MiniZinc y sus parámetros.
- [ ] Crear `ejecutar_experimentos.py` o una rutina equivalente para resolver las 15 instancias y los escenarios acordados.
- [ ] Comprobar selecciones, costo y transmitancia con los datos originales de cada instancia.
- [ ] Guardar estado, objetivo, tiempos, solución y evidencia de optimalidad; nodos y brecha si están disponibles.
- [ ] Ejecutar las 15 instancias y los escenarios acordados, distinguiendo óptimos, infactibles e interrupciones.
- [ ] Preparar la tabla de resultados base y los gráficos de desempeño, con el análisis de tiempos, tamaño, nodos y brecha disponibles.
- [ ] Entregar a Jose los resultados de sensibilidad y a Constanza las tablas y figuras listas con sus explicaciones.
- [ ] Explicar cómo busca el motor, cómo se construye el modelo y cómo se ejecuta en `parte.tex`.
- [ ] Añadir aquí los pasos y comandos para repetir las ejecuciones.
- [ ] Entregar a Mena un resumen de los hallazgos de implementación y desempeño.

No llamar «óptima» a una solución que solo sea factible. Si se omite el costo fijo dentro de la búsqueda, sumarlo al informar el costo total.
