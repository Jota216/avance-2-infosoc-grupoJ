# Joaquin · Presupuesto Detallado Maestro y Viabilidad Financiera

**Rol:** Líder Técnico (Complejidad Alta)  
**Sección asignada:** Presupuesto Detallado Maestro y Viabilidad Financiera (30\% de la calificación)  
**Módulos de trabajo:** `Joaquin/README.md` y `Joaquin/presupuesto.tex`  
**Colaboradores directos:** Javier (Analista Financiero), Jose (Líder Técnico / Carta Gantt), Coni (Calidad y Edición)

---

## 🎯 Alcance y Propósito del Rol

Como Líder Técnico a cargo de la dimensión económica y estructural de la Fase 3, el objetivo primordial de Joaquín es formular la **matriz presupuestaria maestra y el análisis de viabilidad financiera** del proyecto *Bio Planner* (software de optimización algorítmica para eficiencia energética residencial y acondicionamiento térmico comunitario).

La propuesta debe reflejar una planificación financiera profesional, rigurosa y transparente, respaldada en una asignación balanceada de recursos que calce milimétricamente con el cronograma de actividades de la Carta Gantt y con las cotizaciones de mercado detalladas por Javier.

---

## 🏆 Criterios de Evaluación: Nivel Destacado (91–100 pts)

De acuerdo con la [Rúbrica Oficial de Evaluación](../Pauta_segundo_avance.pdf), el criterio **Presupuesto Detallado (Viabilidad Financiera)** pondera un **30\% de la nota final**. Para alcanzar el puntaje máximo, se exige:

1. **Transparencia y Detalle Extremo:** Presentar cada ítem con su denominación clara, unidad de medida, cantidad requerida, costo unitario en \$ CLP y costo total proyectado.
2. **Tabla Profesional Estructurada:** Uso impecable de entornos y paquetes formales de LaTeX (`booktabs`, `tabularx`, `array`), evitando tablas desbordadas o de difícil lectura.
3. **Columnas Obligatorias:**
   - *Ítem / Denominación del Gasto*
   - *Categoría Presupuestaria*
   - *Cantidad*
   - *Unidad de Medida*
   - *Costo Unitario ($ CLP)*
   - *Costo Total ($ CLP)*
   - *Justificación Sintética*
4. **Agrupación Obligatoria en 4 Categorías Lógicas:**
   - **Categoría A: Recursos Humanos / Personal Técnico:** Remuneración y honorarios profesionales acorde a los perfiles de ingeniería de software, arquitectura bioclimática y articulación social.
   - **Categoría B: Equipamiento e Infraestructura Tecnológica:** Adquisición o arriendo de instrumental de medición térmica de terreno, servidores en la nube para procesamiento computacional y licencias.
   - **Categoría C: Operaciones, Terreno y Logística:** Movilización técnica a sectores vulnerables (ej. cerros de Valparaíso), elementos de seguridad y muestreo físico de materiales aislantes.
   - **Categoría D: Materiales de Difusión y Vinculación Comunitaria:** Producción de manuales ciudadanos impresos, material de divulgación y soporte de talleres participativos comunitarios.
5. **Viabilidad y Sostenibilidad Económica:** Demostración explícita de congruencia con la línea de financiamiento postulada (Fondo Concursable de Innovación Social / Corfo / Vinculación con el Medio UTFSM / MINVU), fundamentando la eficiencia en el uso de los fondos y la viabilidad operativa posterior a la ejecución del fondo.

---

## 🔄 Coordinación Cruzada Directa

Para garantizar la coherencia global del informe (20\% de la rúbrica):

* **Coordinación con Javier (Analista Financiero):**
  - Joaquín define la matriz maestra de costos y valores numéricos en `Joaquin/presupuesto.tex`.
  - Javier redacta en `Javier/justificaciones.tex` el desglose exhaustivo de las justificaciones técnicas/sociales y las cotizaciones de mercado reales (proveedores, enlaces, parámetros de referencia).
  - **Regla:** Ningún valor numérico en el desglose de Javier puede discrepar de la tabla de Joaquín.

* **Coordinación con Jose (Líder Técnico - Plan de Actividades):**
  - Cada gasto presupuestado debe vincularse a una o más actividades de la Carta Gantt en `Jose/gantt.tex` (ej. viáticos asociados a visitas de diagnóstico, horas de desarrollo asociadas a la fase de programación del solver, talleres vinculados a la fase comunitaria).
  - Las fechas y duraciones de contratación de personal deben coincidir con los períodos de las tareas en la Gantt.

* **Coordinación con Coni (Calidad y Edición):**
  - Reportar periódicamente el desglose de horas invertidas en el avance: `Revisión`, `Desarrollo`, `Reuniones` e `Informe`.
  - Supervisar que la tabla presupuestaria y su análisis sintético no sobrepasen el espacio presupuestado para mantener el informe total estrictamente entre **5 y 7 páginas**.

---

## 📋 Checklist de Tareas Detallado

### Fase 1: Planificación y Diseño Estructural
- [ ] Analizar los requerimientos de la pauta y rúbrica para el ítem Presupuesto (30%).
- [ ] Definir el monto total del proyecto (monto equilibrado en \$15.200.000 CLP) acorde a bases de fondos de innovación social y tecnológica.
- [ ] Distribuir los montos porcentuales de forma realista entre las 4 categorías obligatorias (aprox. 61% RRHH, 16% Equipamiento, 12% Operaciones, 11% Difusión).

### Fase 2: Construcción de la Plantilla LaTeX (`Joaquin/presupuesto.tex`)
- [ ] Incluir encabezado identificador `% !TEX root = ../main.tex`.
- [ ] Redactar introducción contextualizando la línea de financiamiento y la viabilidad del proyecto.
- [ ] Implementar tabla maestra con `tabularx`, `booktabs` y formato monetario chileno (\$ CLP con separadores de miles legibles).
- [ ] Registrar los 16 ítems clave distribuidos en las Categorías A, B, C y D.
- [ ] Incorporar subtotales calculados por categoría y el Total General del Proyecto (\$15.200.000 CLP).
- [ ] Redactar síntesis de viabilidad financiera, sostenibilidad económica post-proyecto y congruencia con los objetivos del modelo de optimización.

### Fase 3: Sincronización y Validación Técnica
- [ ] Validar con Javier los ítems y montos para que inicie la redacción de justificaciones detalladas y cotizaciones en `Javier/justificaciones.tex`.
- [ ] Contrastar con Jose que cada gasto guarde correspondencia con una tarea del cronograma Gantt (`Jose/gantt.tex`).
- [ ] Notificar a Coni las horas dedicadas para la tabla de la portada reglamentaria.
- [ ] Verificar la ausencia de errores de sintaxis en LaTeX (`\$` escapados, `\%` en textos, entornos cerrados correctamente).
- [ ] Validar que la compilación no genere desbordes horizontales (*overfull hbox*) en el documento final.
