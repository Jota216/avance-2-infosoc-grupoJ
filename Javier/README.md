# Javier · Justificación Detallada del Presupuesto y Cotizaciones

**Rol:** Analista Financiero (Nivel de Complejidad: **Media**)  
**Sección asignada:** Justificación Detallada del Presupuesto, Cotizaciones y Transparencia de Costos (integrada en la Sección 4: *Presupuesto Detallado y Viabilidad Financiera*, 30\% de la calificación)  
**Módulos de trabajo:** `Javier/README.md` y `Javier/justificaciones.tex`  
**Colaboradores directos:** Joaquín (Líder Técnico · Presupuesto Maestro), Jose (Líder Técnico · Carta Gantt), Coni (Calidad y Edición), Mena (Gestor de Asociatividad) y Anais (Vinculación Institucional)

---

## 🎯 Alcance y Propósito del Rol

Como Analista Financiero del proyecto **Bio Planner** (sistema algorítmico de optimización matemática para el acondicionamiento térmico y eficiencia energética en viviendas vulnerables de Valparaíso), la responsabilidad central de Javier radica en fundamentar, con **máxima transparencia, austeridad y pertinencia socio-técnica**, cada uno de los montos y recursos solicitados en la propuesta.

Mientras Joaquín estructura la tabla maestra consolidada y evalúa la viabilidad económica macro, Javier provee el **respaldo cualitativo y cuantitativo detallado**:
1. Justificación exhaustiva ítem por ítem dentro de las 4 categorías presupuestarias reglamentarias (Recursos Humanos, Equipamiento, Operaciones y Difusión).
2. Levantamiento de **cotizaciones de mercado reales** en el contexto nacional chileno (proveedores verificables, aranceles de referencia y parámetros de mercado), respaldando la razonabilidad de los costos unitarios.
3. Demostración de criterios de **austeridad y priorización del gasto**, asegurando que cada peso invertido maximice el impacto social en las familias beneficiarias y optimice el desempeño del software.

---

## 🏆 Criterios de Evaluación: Nivel Destacado (91–100 pts)

De acuerdo con la [Rúbrica Oficial de Evaluación](../Pauta_segundo_avance.pdf) (*Prof. Horst von Brand / Ayudantes M. Guerra, C.M. Rosales*), la dimensión de Presupuesto y Viabilidad pondera el **30\% de la calificación final**. Para alcanzar el rango **Destacado**, la rúbrica exige:

> *"El presupuesto es altamente detallado, realista y transparente. La justificación de cada ítem es impecable, transparente y pertinente, demostrando una excelente gestión de recursos y viabilidad económica."*

Para asegurar este nivel de excelencia, el módulo `Javier/justificaciones.tex` satisface los siguientes estándares:
* **Pertinencia Técnica Directa:** Cada gasto en personal o equipamiento se justifica en función de una necesidad algorítmica, técnica o constructiva concreta (e.g. formulación en MiniZinc, calibración de transmitancias $U$ según norma chilena NCh853 y OGUC art. 4.1.10, monitoreo térmico con cámara termográfica y sensores datalogger).
* **Pertinencia Social y Territorial:** Los gastos operacionales y de difusión se fundamentan en la interacción real con los cerros y sectores vulnerables de Valparaíso, garantizando que el modelamiento beneficie directamente a la comunidad mediante talleres participativos y manuales didácticos.
* **Austeridad y Eficiencia de Recursos:** Se eligen soluciones de código abierto, arriendo u optimización de visitas a terreno, evitando sobredimensionamiento de infraestructura o gastos superfluos.
* **Trazabilidad y Respaldo de Cotizaciones:** Cada costo unitario cuenta con un parámetro de referencia contrastable en el mercado nacional (aranceles del Colegio de Ingenieros de Chile / Fondef para honorarios; cotizaciones de distribuidores oficiales de instrumentación como Flir / Testo; tarifas vigentes de servicios cloud AWS/DigitalOcean; e imprentas locales).

---

## 🔄 Coordinaciones Cruzadas Obligatorias

Para garantizar la coherencia global del informe (20\% de la rúbrica general):

1. **Coordinación Directa con Joaquín (Líder Técnico · Presupuesto Maestro):**
   * **Consistencia Numérica Absoluta (1:1):** Revisar ítem por ítem los 16 componentes de la tabla maestra de `Joaquin/presupuesto.tex`. Ningún valor de costo unitario, cantidad o subtotal en el desglose de Javier puede discrepar de los \$15.200.000 CLP totales ni de sus 4 categorías:
     - *Categoría A (Recursos Humanos):* \$9.300.000 (61,18\%)
     - *Categoría B (Equipamiento y Tecnología):* \$2.500.000 (16,45\%)
     - *Categoría C (Operaciones y Logística):* \$1.750.000 (11,51\%)
     - *Categoría D (Difusión y Vinculación):* \$1.650.000 (10,86\%)
   * Validar que la narrativa de viabilidad financiera general se complemente armónicamente con las justificaciones detalladas.

2. **Coordinación con Jose (Líder Técnico · Carta Gantt):**
   * Validar que cada recurso justificado dé soporte directo a las 11 actividades clave formuladas en `Jose/gantt.tex`.
   * Monitorear los dos hitos de liderazgo directo asignados a Javier en el cronograma:
     - **Actividad A-03 (Fase I, Semanas 2 a 4):** *Levantamiento de cotizaciones comerciales y base de costos unitarios.* Entregable: Repositorio de cotizaciones formales y matriz de costos unitarios.
     - **Actividad A-10 (Fase III, Semanas 12 a 14):** *Auditoría de costos incurridos, análisis de desvíos y balance financiero.* Entregable: Balance financiero de cierre y justificación detallada de ejecución.

3. **Coordinación con Coni (Calidad y Edición):**
   * Reportar formalmente las horas efectivas de trabajo para la tabla de dedicación de la portada (`Coni/portada.tex`) en los 4 rubros reglamentarios:
     - **Revisión:** 6 horas (análisis de bases, rúbrica, Avance 1 y referencias arancelarias).
     - **Desarrollo:** 14 horas (levantamiento de cotizaciones de mercado, redacción de justificaciones y estructuración de `justificaciones.tex`).
     - **Reuniones:** 6 horas (sincronización con Joaquín para cuadratura de cifras y con Jose para calce con Gantt).
     - **Informe:** 5 horas (revisión de estilo, pruebas de compilación y ajuste de extensión).
     - **Total Horas Javier:** 31 horas de dedicación efectiva.
   * Monitorear la extensión del texto en `Javier/justificaciones.tex` para evitar sobrepasar el límite de 5 a 7 páginas del documento final.

4. **Coordinación con Mena (Asociatividad) y Anais (Carta de Apoyo):**
   * Asegurar que los insumos de talleres (Categoría C y D) respondan a los requerimientos de trabajo con las juntas de vecinos mapeadas por Mena.
   * Respaldar que el equipamiento técnico adquirido complemente la infraestructura de la oficina de arquitectura técnica *Acua Plan*, entidad emisora de la carta de apoyo gestionada por Anais.

---

## 📋 Checklist Detallado de Tareas

### Fase 1: Levantamiento de Mercado y Cotizaciones (Semanas 1 a 4 · Actividad Gantt A-03)
- [x] Analizar la rúbrica de evaluación y los criterios de nivel Destacado para justificación presupuestaria.
- [x] Levantar cotizaciones de mercado en Chile para instrumental de medición térmica (cámaras termográficas compactas FLIR C5 / E4 y sensores datalogger Elitech / Testo).
- [x] Cotizar infraestructura cloud para ejecución de modelos de optimización (instancias computacionales AWS EC2 c6i / DigitalOcean Droplets CPU-optimized) por 8 meses.
- [x] Consultar valores de referencia de honorarios profesionales según aranceles vigentes del Colegio de Ingenieros de Chile y estándares de proyectos de innovación social ANID/CORFO.
- [x] Cotizar costos de traslados locales (Valparaíso), elementos de seguridad industrial (EPP clase constructiva) y kits didácticos de materiales aislantes.
- [x] Cotizar servicios de imprenta comunitaria (guías ciudadanas y pendones roller) y logística de talleres participativos (coffee break en sedes comunitarias).

### Fase 2: Redacción Estructural en LaTeX (`Javier/justificaciones.tex`) (Semanas 5 a 8)
- [x] Encabezar el archivo con `% !TEX root = ../main.tex`.
- [x] Redactar introducción metodológica con los criterios de **austeridad, pertinencia técnica/social y transparencia económica**.
- [x] Detallar exhaustivamente la **Categoría A (Recursos Humanos)**: perfil profesional de cada rol, cantidad de horas/meses y su contribución insustituible a los objetivos de Bio Planner.
- [x] Detallar exhaustivamente la **Categoría B (Equipamiento e Infraestructura)**: especificaciones del instrumental térmico, configuración del servidor cloud, licenciamiento y justificación de compra vs. arriendo.
- [x] Detallar exhaustivamente la **Categoría C (Operaciones y Logística)**: justificación de las 20 visitas a terreno, protección de la cuadrilla técnica y pertinencia didáctica de los muestrarios físicos.
- [x] Detallar exhaustivamente la **Categoría D (Difusión y Vinculación)**: impacto de las 300 guías ciudadanas impresas, valor social de los 3 talleres participativos y trascendencia de las cápsulas audiovisuales.
- [x] Incorporar subsección de respaldo de mercado con tabla sintética de cotizaciones y fuentes de verificación (proveedores chilenos, parámetros de referencia y condición impositiva).

### Fase 3: Auditoría Cruzada y Cierre (Semanas 11 a 14 · Actividad Gantt A-10)
- [x] Cuadrar ítem por ítem con la tabla maestra de `Joaquin/presupuesto.tex` (verificación de concordancia matemática al 100\%).
- [x] Verificar que cada ítem esté mapeado a tareas de la Carta Gantt (`Jose/gantt.tex`).
- [x] Reportar la matriz horaria final a Coni para la portada.
- [x] Revisar la sintaxis de LaTeX (escapes correctos de `\$`, `%`, tildes UTF-8 y referencias `\ref` cruzadas).
- [x] Validar que no existan desbordes horizontales ni conflictos de compilación en el pipeline de GitHub Actions.
