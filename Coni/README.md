# Coni · Portada Reglamentaria, Integración Avance 1 y Control de Formato

Bienvenida a la guía interna de trabajo para el módulo de **Portada Reglamentaria, Integración del Avance 1 (Fase 2), Referencias Bibliográficas y Control de Calidad/Formato**, correspondiente a la **Fase 3: Segundo Avance (Plan de Acción y Viabilidad Financiera)** de la asignatura *Ingeniería, Informática y Sociedad* (INF-234, UTFSM Casa Central).

---

## 🎯 Alcance y Responsabilidad del Rol

* **Integrante:** Coni (Constanza Silva P.)
* **Rol:** Calidad, Formato, Integración y Control de Extensión (Nivel de Complejidad: **Media**)
* **Ponderación de la Sección:** **20% de la calificación final** (Criterio 4: *Coherencia y Presentación del Documento / Formato*).
* **Archivos Fuente Asignados:**
  * [`Coni/README.md`](README.md): Esta guía interna y orquestador metodológico.
  * [`Coni/portada.tex`](portada.tex): Portada reglamentaria oficial y Tabla Obligatoria de Dedicación Horaria de los 6 integrantes.
  * [`Coni/avance1_resumen.tex`](avance1_resumen.tex): Síntesis ejecutiva densa, rigurosa y articulada del Primer Avance (Fase 2).
  * [`Coni/referencias.tex`](referencias.tex): Fuentes bibliográficas, normativas chilenas, bases de postulación y cotizaciones formales.
* **Misión Principal:** Garantizar que el documento maestro consolidado cumpla de manera estricta e intransable con el rango reglamentario de **5 a 7 páginas totales**, articulando los módulos de los 6 integrantes en un todo coherente, elegante, con ortografía intachable y formato profesional `IEEEtran`.

---

## 🏆 Criterios de la Rúbrica para Nivel Destacado (91–100 pts)

De acuerdo con la pauta y rúbrica oficial de evaluación del curso (*Profesor Horst von Brand / Ayudantes M. Guerra, C.M. Rosales*), el criterio **Coherencia y Presentación del Documento (Formato)** pondera el **20%** de la nota total. La rúbrica establece textualmente:

> **Nivel Destacado (91–100 pts):** *"El documento es impecable en forma, fondo y redacción. La información es presentada de manera concisa y clara, superando la extensión y formato mínimo requerido."*

Para alcanzar la calificación máxima, el trabajo bajo responsabilidad de Coni debe verificar los siguientes estándares de oro:

1. **Control Estricto de Extensión (5 a 7 páginas totales):**
   - El documento final generado por `main.tex` debe tener un mínimo de 5 páginas completas y un máximo de 7 páginas.
   - **No se toleran desbordes:** Tener 7 páginas y una línea en la página 8 equivale a una penalización directa a rango *En Desarrollo* o *Inicial* en formato.
   - Coni audita la densidad tipográfica de cada sección para asegurar que las tablas (`gantt.tex` de Jose y `presupuesto.tex` de Joaquín) no empujen el documento fuera del rango.

2. **Portada Reglamentaria Completa:**
   - Debe contener la totalidad de los datos institucionales exigidos:
     * Institución: *Universidad Técnica Federico Santa María*
     * Unidad Académica: *Departamento de Informática*
     * Asignatura: *Ingeniería, Informática y Sociedad (INF-234)*
     * Semestre: *2026-2*
     * Título formal del proyecto y entrega: *"Fase 3: Segundo Avance -- Plan de Acción y Viabilidad Financiera"*, con subtítulo descriptivo del proyecto *Bio Planner*.
     * Equipo Docente: *Profesor Horst von Brand*, *Ayudantes: M. Guerra, C.M. Rosales*.
     * Nómina completa de los 6 integrantes con sus roles funcionales específicos y correos institucionales `@sansano.usm.cl`.

3. **Tabla Obligatoria de Dedicación Horaria:**
   - Tabla profesional (`booktabs`) que registre una fila individual por cada uno de los 6 miembros del equipo: Joaquín, Jose, Javier, Mena, Anais y Coni.
   - Columnas reglamentarias exactas: `Integrante`, `Revisión`, `Desarrollo`, `Reuniones`, `Informe`, `Total (h)`.
   - Inclusión obligatoria y textual del párrafo aclaratorio que define los 4 conceptos según la pauta:
     > *"Revisión: lectura de apuntes, búsquedas bibliográficas y referencias. Desarrollo: tiempo invertido en la elaboración técnica y metodológica de la solución. Reuniones: coordinación sincrónica y trabajo colaborativo grupal. Informe: tiempo requerido para la redacción y maquetación de los entregables."*
   - Cifras balanceadas y verosímiles que reflejen el compromiso real y la complejidad del trabajo de ingeniería.

4. **Integración Densa y Concisa del Primer Avance (Fase 2):**
   - Resumir de forma fiel y depurada el diagnóstico del problema socio-técnico (pobreza energética en sectores vulnerables de Valparaíso), la propuesta tecnológica (*Bio Planner* como motor de optimización matemática lineal entera binaria para acondicionamiento térmico según norma CEV/OGUC), los beneficiarios directos/indirectos, el objetivo general y los objetivos específicos, y la línea de financiamiento seleccionada (Fondo de Innovación Social de CORFO / Vinculación con el Medio UTFSM).
   - Servir de puente directo y orgánico hacia la Fase 3, explicando por qué las actividades (Jose) y los gastos (Joaquín/Javier) nacen de esta estrategia.

5. **Aparato Crítico y Referencias Bibliográficas Rigurosas:**
   - Construcción de un listado bibliográfico ordenado y formal con fuentes primarias: normativas oficiales del MINVU (OGUC art. 4.1.10, CEV, NCh853), bases concursables públicas (CORFO, VCM UTFSM), estudios de pobreza energética (RedPE, INE, CASEN) y cotizaciones comerciales formales.

---

## 🔄 Coordinación Cruzada Directa con los 5 Integrantes

Para asegurar la coherencia integral del informe consolidado, Coni lidera las siguientes acciones de coordinación:

1. **Recopilación y Validación de Horas Dedicadas (Todos los integrantes):**
   - Coordinar con Joaquín, Jose, Javier, Mena y Anais para recopilar sus horas dedicadas exactas en las 4 dimensiones (`Revisión`, `Desarrollo`, `Reuniones`, `Informe`) y mantener actualizada la tabla de la portada en [`Coni/portada.tex`](portada.tex).

2. **Coordinación con Joaquín y Jose (Líderes Técnicos):**
   - Auditar que la Carta Gantt ([`Jose/gantt.tex`](../Jose/gantt.tex)) y el Presupuesto Maestro ([`Joaquin/presupuesto.tex`](../Joaquin/presupuesto.tex)) encajen en el espacio de página asignado sin provocar saltos de página huérfanos ni tablas partidas antiestéticas.
   - Contrastar que los objetivos específicos planteados en [`Coni/avance1_resumen.tex`](avance1_resumen.tex) sean exactamente las fases y metas operacionales que Jose desglosa en sus 11 actividades y que Joaquín costea en sus 16 ítems.

3. **Coordinación con Javier (Analista Financiero):**
   - Asegurar que todas las fuentes de cotización citadas en [`Javier/justificaciones.tex`](../Javier/justificaciones.tex) (catálogos de materiales, cotizaciones de instrumental termográfico, proveedores cloud) cuenten con su entrada bibliográfica formal en [`Coni/referencias.tex`](referencias.tex).

4. **Coordinación con Mena (Gestor de Asociatividad):**
   - Verificar la coherencia territorial: validar que las juntas de vecinos de Valparaíso, comités de vivienda social y la oficina de arquitectura Acua Plan descritos en [`Mena/asociatividad.tex`](../Mena/asociatividad.tex) coincidan plenamente con los beneficiarios y aliados caracterizados en el resumen del Avance 1.

5. **Coordinación con Anais (Vinculación Institucional):**
   - Revisar que la Carta de Apoyo Simulada ([`Anais/carta_apoyo.tex`](../Anais/carta_apoyo.tex)) esté correctamente configurada como anexo formal obligatorio, respetando los márgenes y sin empujar el informe fuera de la página 7.

---

## 📋 Checklist Detallado de Tareas

### Módulo de Portada y Dedicación Horaria (`Coni/portada.tex`)
- [ ] Incorporar el encabezado institucional completo de la UTFSM y Departamento de Informática.
- [ ] Redactar el título formal de la entrega: "Fase 3: Segundo Avance -- Plan de Acción y Viabilidad Financiera" con referencia explícita al proyecto *Bio Planner*.
- [ ] Especificar los nombres de los docentes: Profesor Horst von Brand, Ayudantes: M. Guerra, C.M. Rosales.
- [ ] Incluir la lista formal de los 6 integrantes con sus roles específicos asignados y correos institucionales `@sansano.usm.cl`.
- [ ] Maquetar la Tabla Obligatoria de Dedicación Horaria en LaTeX con paquetes profesionales (`booktabs`, `tabularx`).
- [ ] Incorporar una fila individual con desglose de horas para Joaquín, Jose, Javier, Mena, Anais y Coni, con sus totales individuales y la suma grupal.
- [ ] Colocar textualmente el párrafo explicativo oficial que define los conceptos de Revisión, Desarrollo, Reuniones e Informe.

### Módulo de Síntesis del Primer Avance (`Coni/avance1_resumen.tex`)
- [ ] Redactar la Sección I: "Antecedentes e Integración del Primer Avance".
- [ ] Exponer el diagnóstico social y territorial de la pobreza energética y deficiencia térmica habitacional en los cerros de Valparaíso.
- [ ] Describir la propuesta de software *Bio Planner*, motor de optimización matemática binaria y cumplimiento de estándares $U_{\max}$ (normas CEV y OGUC art. 4.1.10).
- [ ] Definir los grupos de beneficiarios directos (comités habitacionales vulnerables) e indirectos (SERVIU, municipios, profesionales técnicos).
- [ ] Detallar el Objetivo General y los 4 Objetivos Específicos claros, técnicos y medibles.
- [ ] Identificar la línea de financiamiento seleccionada (Fondo de Innovación Social de CORFO) y articularla orgánicamente con el Plan de Acción y Presupuesto de la Fase 3.
- [ ] Cuidar la concisión y densidad del texto para garantizar que la sección ocupe el espacio óptimo de 1 a 1,5 páginas.

### Módulo de Referencias Bibliográficas (`Coni/referencias.tex`)
- [ ] Crear el entorno bibliográfico en LaTeX compatible con la compilación directa de `main.tex`.
- [ ] Incorporar normativas técnicas oficiales chilenas (OGUC art. 4.1.10, Manual CEV, norma NCh853).
- [ ] Citar diagnósticos sociodemográficos y de habitabilidad (INE Censo 2017, Encuesta CASEN 2022, RedPE 2020).
- [ ] Incluir las bases concursables públicas (CORFO Fondo de Innovación Social, Fondo VCM UTFSM).
- [ ] Incorporar fuentes técnicas del solver de optimización (MiniZinc) y referencias de la FESW 2025 (*Bio Planner*).
- [ ] Registrar fuentes de cotización comercial e instrumental (ChileCompra, Sodimac/Imperial, Flir Systems, proveedores cloud).

### Control Global de Calidad, Formato y Extensión
- [ ] Comprobar que todos los módulos comiencen con la directiva `% !TEX root = ../main.tex`.
- [ ] Verificar la ausencia total de advertencias críticas de desborde horizontal (`Overfull \hbox`).
- [ ] Monitorear que el documento consolidado resultante de `main.tex` tenga **estrictamente entre 5 y 7 páginas**.
- [ ] Revisar la redacción, ortografía en español, puntuación y estilo académico formal en todo el informe.
- [ ] Validar la compilación exitosa en el flujo automatizado de GitHub Actions ([`compilar-informe.yml`](../.github/workflows/compilar-informe.yml)).
