# Jose · Plan de Actividades y Carta Gantt

Bienvenido a la guía interna de trabajo para el módulo de **Plan de Actividades y Carta Gantt** correspondiente a la **Fase 3: Segundo Avance (Plan de Acción y Viabilidad Financiera)** de la asignatura *Ingeniería, Informática y Sociedad* (UTFSM Casa Central).

---

## 🎯 Alcance y Responsabilidad del Rol

* **Integrante:** Jose
* **Rol:** Líder Técnico (Nivel de Complejidad: **Alta**)
* **Ponderación de la Sección:** **30% de la calificación final** de la entrega.
* **Archivo Fuente Principal:** [`Jose/gantt.tex`](gantt.tex)
* **Objetivo General:** Traducir los compromisos estratégicos y técnicos formulados en el Avance 1 (Fase 2) en una hoja de ruta operacional concreta, temporalizada y viable, estructurada mediante una Carta Gantt profesional con optimización de tiempos, paralelización de procesos y balance equitativo de responsabilidades entre los 6 integrantes del equipo.

---

## 🏆 Criterios de la Rúbrica para Nivel Destacado (91–100 pts)

De acuerdo con la pauta oficial de evaluación docente (*Prof. Horst von Brand / Ayudantes M. Guerra, C.M. Rosales*), el criterio **Plan de Actividades (Carta Gantt)** pondera el **30%** y exige lo siguiente para alcanzar el puntaje máximo:

> **Nivel Destacado (91–100 pts):** *"La Carta Gantt presenta una planificación estratégica y realista, con las tareas perfectamente definidas, optimizando el tiempo y la asignación de recursos."*

Para asegurar este estándar, la planificación implementada en [`Jose/gantt.tex`](gantt.tex) debe satisfacer:
1. **Rango Reglamentario de Actividades:** Definir estrictamente entre **8 y 15 actividades clave** (el modelo incluye 11 actividades), perfectamente formuladas y sin ambigüedades.
2. **Estructura Fásica Coherente:** Agrupar las actividades en tres fases cronológicas y funcionales:
   * **Fase I:** Planificación y Validación Inicial.
   * **Fase II:** Desarrollo y Ejecución Técnico-Social.
   * **Fase III:** Pruebas, Evaluación y Cierre.
3. **Secuencia Lógica y Predecesoras:** Cada actividad debe especificar de forma explícita sus dependencias lógicas, permitiendo trazar con claridad la ruta crítica.
4. **Optimización Temporal y Paralelización:** Demostrar cómo se comprimen los plazos de ejecución mediante la superposición de rutas de trabajo concurrentes (desarrollo técnico, gestión comunitaria y auditoría financiera) para evitar cuellos de botella.
5. **Asignación Equitativa de Responsables:** Asignar un responsable principal a cada tarea, equilibrando la carga de trabajo entre los 6 integrantes del grupo de acuerdo a sus roles.
6. **Entregables e Hitos Medibles:** Cada actividad debe asociarse a un hito concreto o producto verificable.

---

## 🔄 Coordinaciones Cruzadas Obligatorias

Para garantizar la coherencia global del informe requerida por la pauta docente:

1. **Coordinación Directa con Joaquín (Líder Técnico · Presupuesto Maestro):**
   * Toda actividad de la Carta Gantt que demande erogación de recursos (e.g., desarrollo en infraestructura cloud, talleres comunitarios, adquisición de licencias, materiales de difusión) debe contar con su correspondiente reflejo financiero en `Joaquin/presupuesto.tex`.
   * Verificar que los plazos de desembolso y el cronograma de flujo de fondos coincidan exactamente con la duración de las actividades planificadas.

2. **Coordinación Directa con Coni (Calidad, Edición y Portada):**
   * Reportar de forma oportuna y precisa las horas efectivas de dedicación personal en las cuatro categorías reglamentarias para su incorporación en la portada oficial (`Coni/portada.tex`):
     * **Revisión:** Lectura de pautas, bases de licitación, análisis del Avance 1 y referencias técnicas.
     * **Desarrollo:** Diseño de la Carta Gantt, definición de actividades, cálculo de ruta crítica y redacción en LaTeX.
     * **Reuniones:** Asistencia y participación en reuniones de avance interno y sesiones de sincronización de equipo.
     * **Informe:** Confección, corrección estilística y pruebas de compilación del módulo `gantt.tex`.

3. **Coordinación con Javier, Mena y Anais:**
   * Validar con **Javier** que los hitos de cotizaciones de mercado y balance final de costos tengan suficiente holgura en el cronograma.
   * Alinear con **Mena** las semanas destinadas a talleres de validación comunitaria y vinculación con actores territoriales (Fase I y II).
   * Confirmar con **Anais** las fechas de gestión y formalización de cartas de apoyo institucional simuladas para que precedan a la ejecución en terreno.

---

## 📋 Checklist Detallado de Trabajo

### Fase de Diagnóstico y Alineación Técnica
- [ ] Revisar el documento del Avance 1 y los objetivos específicos planteados en la Fase 2 para mantener continuidad conceptual.
- [ ] Analizar la pauta oficial (`Segundo_avance.pdf`) y la rúbrica de evaluación (`Pauta_segundo_avance.pdf`).
- [ ] Desglosar el proyecto en exactamente 11 actividades clave estratégicas (dentro del rango reglamentario de 8 a 15).

### Fase de Modelamiento y Optimización de la Carta Gantt
- [ ] Agrupar las 11 actividades en las 3 fases obligatorias: Planificación, Desarrollo/Ejecución y Pruebas/Cierre.
- [ ] Establecer las relaciones de precedencia directa para cada actividad.
- [ ] Identificar las tareas que conforman la ruta crítica y aquellas pasibles de paralelización concurrente.
- [ ] Definir duraciones realistas en semanas dentro de un horizonte semestral (Semanas 1 a 15).
- [ ] Asignar responsabilidades principales distribuidas de forma equitativa entre los 6 miembros: Joaquín, Jose, Javier, Mena, Anais y Coni.
- [ ] Formular hitos y productos tangibles para cada una de las 11 actividades.

### Fase de Implementación en LaTeX (`Jose/gantt.tex`)
- [ ] Incluir la cabecera obligatoria de enlace: `% !TEX root = ../main.tex`.
- [ ] Redactar una introducción metodológica concisa explicando el marco de planificación temporal y secuencia lógica.
- [ ] Programar la tabla profesional en LaTeX utilizando `booktabs`, `tabularx` y columnas con justificación adecuada (`array`).
- [ ] Redactar el párrafo de análisis de optimización de la ruta de trabajo, detallando la reducción de tiempos por paralelización y mitigación de cuellos de botella.
- [ ] Redactar el párrafo de justificación de la distribución balanceada de responsabilidades y cargas de trabajo.
- [ ] Verificar que la tabla y el texto se ajusten a los márgenes definidos en `main.tex` sin generar advertencias de desborde (`Overfull \hbox`).

### Fase de Sincronización y Cierre
- [ ] Cruzar referencias con `Joaquin/presupuesto.tex` para verificar correlación 1:1 entre actividades financiadas y partidas presupuestarias.
- [ ] Enviar a Coni el desglose de horas dedicadas (`Revisión`, `Desarrollo`, `Reuniones`, `Informe`).
- [ ] Compilar el documento maestro `main.tex` localmente o en el pipeline de CI/CD para certificar cero errores de compilación.
