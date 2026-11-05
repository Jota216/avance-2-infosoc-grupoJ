# Jose · Plan de Actividades y Carta Gantt

**Rol:** Líder Técnico (Nivel de Complejidad: **Alta**)  
**Sección asignada:** Sección 3: Plan de Actividades y Carta Gantt (**30% de la calificación final**)  
**Módulos de trabajo:** [`Jose/README.md`](README.md) y [`Jose/gantt.tex`](gantt.tex)  
**Colaboradores directos:** Joaquín Barrios (Presupuesto Maestro), Javier Bravo (Cotizaciones), José Mena (Asociatividad), Anais Quinchao (Carta de Apoyo), Constanza Ríos (Calidad y Portada)  
**Proyecto:** *Campus Zero: Control Automatizado de Iluminación y Climatización de Salas* (Grupo J: SmartGrid — UTFSM Casa Central, INF276)

---

## 🎯 Alcance y Responsabilidad del Rol

* **Integrante:** Jose Astudillo
* **Objetivo General:** Traducir la estrategia y los cuatro Objetivos Específicos (OE1 a OE4) formulados en el Avance 1 ([`GrupoJ_Fase1.pdf`](../GrupoJ_Fase1.pdf)) en una hoja de ruta operacional de **15 semanas** para intervenir las **5 salas de estudio piloto** en Casa Central USM (reducción del consumo fantasma de $0{,}26\text{ kW/sala}$ en luminarias LED y extractores de aire mediante corte autónomo tras 10 minutos de inactividad, sin intervenir computadores).

---

## 🏆 Criterios de la Rúbrica Cubiertos para Nivel Destacado (91–100 pts)

De acuerdo con la [Rúbrica Oficial de Evaluación](../Pauta_segundo_avance.pdf) (*Prof. Horst von Brand / Ayudantes M. Guerra, C.M. Rosales*), el criterio **Plan de Actividades (Carta Gantt)** pondera el **30%** y exige:

> **Nivel Destacado (91–100 pts):** *"La Carta Gantt presenta una planificación estratégica y realista, con las tareas perfectamente definidas, optimizando el tiempo y la asignación de recursos."*

La implementación en [`Jose/gantt.tex`](gantt.tex) cumple íntegramente estos requisitos:
1. **Rango Reglamentario y Especificidad Técnica:** Se definen **11 actividades clave (`A-01` a `A-11`)** dentro del rango de 8 a 15 tareas exigido por pauta, 100% contextualizadas a *Campus Zero*.
2. **Alineación Exacta con los Plazos de los 4 Objetivos Específicos (Fase 1):**
   * **Fase I: Diseño Electrónico, Adquisiciones y Línea Base (Semanas 1 a 5 — OE1 y base OE3):** Cumple el plazo máximo de 5 semanas desde la adjudicación para diseñar el control, activar el convenio con *MCI Electronics* (15% descuento y soporte técnico), adquirir los componentes y armar los 6 nodos (5 salas + 1 respaldo), midiendo en paralelo el consumo eléctrico *ex-ante*.
   * **Fase II: Montaje Eléctrico, Calibración en Terreno y Señalética (Semanas 6 a 9 — OE2 y avance OE4):** Cumple el plazo máximo de 4 semanas tras recibir materiales para montar los gabinetes IP65 y canalizaciones bajo norma SEC RIC N.º 04/05 y calibrar los sensores duales (PIR + radar mmWave 24 GHz) con corte a los 10 minutos sin presencia humana, instalando en paralelo la señalética acrílica.
   * **Fase III: Medición Comparativa, Auditoría y Transferencia Replicable (Semanas 10 a 15 — OE3 y OE4):** Cumple las 4 semanas de medición *ex-post* (Semanas 10 a 13) para certificar una reducción $\ge 50\%$ del desperdicio energético en desocupación, y ejecuta entre las Semanas 11 y 15 la auditoría operativa, rendición financiera, inventario USM e impresión de la *Guía Técnica de Replicación*.
3. **Secuencia Lógica y Ruta Crítica Explícita:** Se formalizan las predecesoras de cada tarea y se identifica la ruta crítica ($\text{A-01} \rightarrow \text{A-04} \rightarrow \text{A-05} \rightarrow \text{A-06} \rightarrow \text{A-08} \rightarrow \text{A-11}$).
4. **Optimización Temporal (De 32 semanas-actividad / 17 semanas lineales a 15 semanas efectivas):** Se documentan tres ejes de paralelización (medición *ex-ante* concurrente con compras y laboratorio en Sem. 1–5; señalética paralela a calibración en Sem. 8–10; auditoría y cierre documental solapados al monitoreo en Sem. 11–15).
5. **Trazabilidad 1:1 con el Presupuesto Maestro (`Joaquin/presupuesto.tex`):** Cada actividad especifica las categorías presupuestarias ejecutadas (Cat. 1 a Cat. 5, totalizando $\$1.199.300\text{ CLP}$ + $\$50.700\text{ CLP}$ de reserva = $\$1.250.000\text{ CLP}$).
6. **Balance Equitativo de Responsabilidades:** Distribución simétrica del liderazgo de las 11 actividades entre los 6 integrantes del equipo.

---

## ⏱️ Reporte de Dedicación Horaria (Para `Coni/portada.tex`)

Horas efectivas de trabajo de **Jose Astudillo** para la tabla reglamentaria de la portada:

| Integrante | Revisión | Desarrollo | Reuniones | Informe | Total |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Jose Astudillo** | 2,0 h | 4,0 h | 1,5 h | 2,5 h | **10,0 h** |

---

## 📋 Checklist Detallado de Trabajo

### Fase de Diagnóstico y Alineación Técnica
- [x] Revisar el documento del Avance 1 (`GrupoJ_Fase1.pdf`) y los 4 Objetivos Específicos (OE1–OE4) para mantener continuidad conceptual y de plazos.
- [x] Analizar la pauta oficial (`Segundo_avance.pdf`) y la rúbrica de evaluación (`Pauta_segundo_avance.pdf`).
- [x] Desglosar el proyecto *Campus Zero* en 11 actividades clave estratégicas (dentro del rango reglamentario de 8 a 15).

### Fase de Modelamiento y Optimización de la Carta Gantt
- [x] Agrupar las 11 actividades en 3 fases cronológicas vinculadas explícitamente a OE1, OE2, OE3 y OE4.
- [x] Establecer las relaciones de precedencia directa para cada actividad.
- [x] Identificar las tareas que conforman la ruta crítica y las tres rutas de paralelización concurrente.
- [x] Definir duraciones realistas en semanas dentro del horizonte semestral (Semanas 1 a 15).
- [x] Asignar responsabilidades principales distribuidas de forma equitativa entre los 6 miembros: Joaquín, Jose, Javier, Mena, Anais y Coni.
- [x] Formular hitos verificables y vincular las 5 categorías presupuestarias para cada actividad.

### Fase de Implementación en LaTeX (`Jose/gantt.tex`)
- [x] Incluir la cabecera obligatoria de enlace: `% !TEX root = ../main.tex`.
- [x] Redactar la introducción metodológica alineada con el alcance de *Campus Zero* y los 4 OE.
- [x] Programar la tabla profesional en LaTeX utilizando `booktabs`, `tabularx` y formato compacto para respetar el límite global de 5 a 7 páginas.
- [x] Redactar el análisis de ruta crítica y optimización temporal por paralelización.
- [x] Redactar la justificación de la distribución balanceada de responsabilidades y categorías de recursos.

### Fase de Sincronización y Cierre
- [x] Cruzar referencias con `Joaquin/presupuesto.tex` y `Anais/carta_apoyo.tex` (MCI Electronics) para asegurar coherencia total.
- [x] Dejar registrado el desglose de horas dedicadas (`Revisión`, `Desarrollo`, `Reuniones`, `Informe`).
