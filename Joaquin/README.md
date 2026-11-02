# Joaquin · Presupuesto Detallado Maestro y Viabilidad Financiera

**Rol:** Líder Técnico (Complejidad Alta)  
**Sección asignada:** Sección 4: Presupuesto Detallado y Viabilidad Financiera (30% de la calificación)  
**Módulos de trabajo:** `Joaquin/README.md` y `Joaquin/presupuesto.tex`  
**Colaboradores directos:** Javier (Analista Financiero), Jose (Líder Técnico / Carta Gantt), Coni (Calidad y Edición)  
**Proyecto:** *Campus Zero: Control Automatizado de Iluminación y Climatización de Salas de Estudio* (Grupo J: Smart Grid - UTFSM Casa Central, ramo INF276)

---

## 🎯 Alcance y Propósito del Rol

Como Líder Técnico a cargo de la dimensión económica y estructural de la Fase 3, el objetivo primordial de Joaquín es formular la **matriz presupuestaria maestra y el análisis de viabilidad financiera** del proyecto *Campus Zero* (control inteligente de iluminación y extracción de aire mediante microcontroladores ESP32, sensores duales PIR y mmWave radar 24 GHz, y metrología no invasiva PZEM-004T).

La propuesta refleja una planificación financiera profesional, rigurosa y transparente, respaldada en una asignación balanceada de recursos que calza milimétricamente con el cronograma de actividades de la Carta Gantt (`Jose/gantt.tex`) y con las cotizaciones de mercado detalladas por Javier (`Javier/justificaciones.tex`).

---

## 🏆 Criterios de Evaluación: Nivel Destacado (91–100 pts)

De acuerdo con la [Rúbrica Oficial de Evaluación](../Pauta_segundo_avance.pdf) del Prof. Horst von Brand, el criterio **Presupuesto Detallado (Viabilidad Financiera)** pondera un **30% de la nota final**. Para alcanzar el puntaje máximo, se exige:

1. **Cumplimiento del Tope Presupuestario Institucional:**
   - Monto tope postulado a Fondos Concursables USM (Línea de Sustentabilidad y Medio Ambiente): **\$1.250.000 CLP**.
   - Monto ejecutado en BOM: **\$1.199.300 CLP** (**95,94%** de ejecución presupuestaria).
   - Fondo de reserva operacional y contingencias: **\$50.700 CLP** (**4,06%** de reserva técnica).

2. **Agrupación en 5 Categorías Estratégicas y 19 Ítems:**
   - **Categoría 1: Equipos y Componentes Electrónicos de Control (OE1, OE2):** \$279.840 CLP (23,33%).
   - **Categoría 2: Instrumentación y Medición Energética (OE3):** \$300.580 CLP (25,06%).
   - **Categoría 3: Materiales de Instalación Eléctrica, Montaje y Seguridad (OE2):** \$293.760 CLP (24,49%).
   - **Categoría 4: Difusión, Señalética y Documentación Técnica Replicable (OE4):** \$180.620 CLP (15,06%).
   - **Categoría 5: Herramientas de Calibración, Banco de Pruebas y Contingencia (OE1, OE2):** \$144.500 CLP (12,05%).

3. **Columnas Obligatorias en Tabla Maestra:**
   - *ID del Ítem*
   - *Componente / Denominación Técnica*
   - *Cantidad*
   - *Unidad de Medida*
   - *Costo Unitario ($ CLP)*
   - *Costo Total ($ CLP)*
   - *Justificación Sintética y Proveedor Chileno Referencial*

4. **Análisis Riguroso de Retorno de la Inversión (ROI) y Sostenibilidad:**
   - **Potencia instalada:** 0,26 kW por sala (4 paneles LED 0,16 kW + 2 extractores 0,10 kW a 220VAC).
   - **Desperdicio fantasma:** 3 h/día por sala desocupada = 0,78 kWh/día/sala = 17,16 kWh/mes/sala (22 días hábiles) = 85,8 kWh/mes en 5 salas piloto = 772,2 kWh/año académico (9 meses lectivos).
   - **Ahorro económico directo:** Con tarifa institucional de \$195 CLP/kWh, ahorro de \$150.579 CLP/año en las 5 salas piloto.
   - **Escalabilidad campus (50 salas):** Ahorro de 7.722 kWh/año y \$1.505.790 CLP/año, con un payback simple de ~2,5 a 3 años para la infraestructura completa.
   - **Descarbonización (SEN):** Factor de emisión de 0,35 kg CO2e/kWh. Reducción directa de 270,3 kg CO2e/año en el piloto, escalable a 2,7 t CO2e/año en el campus.
   - **Preservación de vida útil:** +660 horas operativas de vida útil ahorradas anualmente por componente (+660 h/año).

---

## 🔄 Coordinación Cruzada Directa

* **Con Javier (Analista Financiero):**
  - Joaquín define la matriz maestra de costos y valores numéricos en `Joaquin/presupuesto.tex`.
  - Javier redacta en `Javier/justificaciones.tex` el desglose exhaustivo de las justificaciones técnicas/sociales y las cotizaciones de mercado reales (MCI, AFEL, MechatronicStore, Dartel, Gobantes, Sodimac, Imprenta USM, PubliAcrílicos).
  - **Regla:** Cero discrepancia numérica entre Joaquín y Javier.

* **Con Jose (Líder Técnico - Plan de Actividades):**
  - Cada gasto presupuestado se vincula directamente a los Objetivos Específicos (OE1, OE2, OE3, OE4) y a las 11 actividades de la Carta Gantt en `Jose/gantt.tex`.

* **Con Coni (Calidad y Edición):**
  - Reporte de dedicación horaria: Revisión, Desarrollo, Reuniones e Informe.
  - Asegurar que la tabla y análisis ocupen el espacio exacto para mantener el informe general en el rango de 5 a 7 páginas.
