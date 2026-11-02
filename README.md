# Segundo Avance · Ingeniería, Informática y Sociedad · UTFSM

Repositorio de trabajo colaborativo para la **Fase 3: Segundo Avance (Plan de Acción y Viabilidad Financiera)** del curso **Ingeniería, Informática y Sociedad** (UTFSM Casa Central).

El objetivo central de esta entrega es traducir la estrategia formulada en la fase previa en un **plan de acción concreto, viable y financiable**, cumpliendo con la extensión reglamentaria estricta de **5 a 7 páginas** y apuntando al nivel **Destacado (91-100 pts)** en todos los criterios de la rúbrica de evaluación.

---

## 👥 Reparto del Trabajo y Roles del Equipo (6 Integrantes)

| Integrante | Rol y Nivel de Complejidad | Carpeta de Trabajo | Responsabilidad Principal |
| :--- | :--- | :--- | :--- |
| **Joaquín** | Líder Técnico (Complejidad Alta) | [`Joaquin/`](Joaquin/README.md) | **Presupuesto Detallado Maestro (30%):** Estructura de tabla maestra, categorización de costos, cálculo unitario/total, análisis de viabilidad financiera y coherencia con la línea de financiamiento + Configuración e integración maestra del documento. |
| **Jose** | Líder Técnico (Complejidad Alta) | [`Jose/`](Jose/README.md) | **Plan de Actividades / Carta Gantt (30%):** Definición de 8 a 15 actividades clave agrupadas por fases/objetivos, secuencia lógica, optimización de tiempos, asignación de responsables y recursos + Coherencia técnica con objetivos del Avance 1. |
| **Javier** | Analista Financiero (Complejidad Media) | [`Javier/`](Javier/README.md) | **Justificación Detallada del Presupuesto:** Redacción exhaustiva y pertinente de la justificación por ítem y categoría (criterio Destacado: transparencia absoluta), fuentes de cotización y desglose en coordinación con Joaquín. |
| **Mena** | Gestor de Asociatividad (Complejidad Media) | [`Mena/`](Mena/README.md) | **Colaboración y Asociatividad (20%):** Identificación de red de apoyo sólida (actores internos USM y externos territoriales/sectoriales), análisis estratégico de su rol, integración comunitaria y aportes recíprocos. |
| **Anais** | Vinculación Institucional (Complejidad Media) | [`Anais/`](Anais/README.md) | **Carta de Apoyo Simulada (Anexo Obligatorio):** Redacción formal, institucional y convincente del borrador de carta de apoyo, alineado con los actores de Mena + Verificación de conexión narrativa con la Fase 2. |
| **Coni** | Calidad y Edición (Complejidad Media) | [`Coni/`](Coni/README.md) | **Portada Reglamentaria, Tabla de Horas y Síntesis Avance 1:** Portada oficial completa, tabla horaria por integrante (`Revisión \| Desarrollo \| Reuniones \| Informe`), integración concisa del Avance 1 (control estricto de 5 a 7 páginas) y referencias. |

---

## 🏗️ Arquitectura Modular del Repositorio

El archivo raíz [`main.tex`](main.tex) ensambla todo el documento mediante llamadas modulares `\input`:

```
avance2/
├── .github/workflows/compilar-informe.yml  # Compilación automática en CI/CD
├── main.tex                               # Documento raíz LaTeX
├── README.md                              # Este orquestador general
├── Pauta_segundo_avance.pdf               # Rúbrica oficial (Horst von Brand / Ayudantes)
├── Segundo_avance.pdf                     # Pauta de entrega Fase 3
│
├── Joaquin/                               # Presupuesto maestro y viabilidad financiera
│   ├── README.md                          # Instrucciones específicas de Joaquín
│   └── presupuesto.tex                    # Tabla presupuestaria maestra y análisis financiero
│
├── Jose/                                  # Plan de actividades y Carta Gantt
│   ├── README.md                          # Instrucciones específicas de Jose
│   └── gantt.tex                          # Tabla de 8-15 actividades y optimización temporal
│
├── Javier/                                # Justificaciones y cotizaciones del presupuesto
│   ├── README.md                          # Instrucciones específicas de Javier
│   └── justificaciones.tex                # Justificaciones técnicas y sociales por ítem
│
├── Mena/                                  # Red de colaboradores y asociatividad
│   ├── README.md                          # Instrucciones específicas de Mena
│   └── asociatividad.tex                  # Párrafo y análisis estratégico de actores
│
├── Anais/                                 # Borrador formal de carta de apoyo
│   ├── README.md                          # Instrucciones específicas de Anais
│   └── carta_apoyo.tex                    # Carta de apoyo simulada (anexo formal)
│
├── Coni/                                  # Portada, tabla de horas, Avance 1 y referencias
│   ├── README.md                          # Instrucciones específicas de Coni
│   ├── portada.tex                        # Portada con datos completos y tabla horaria
│   ├── avance1_resumen.tex                # Síntesis concisa del Avance 1 / Fase 2
│   └── referencias.tex                    # Fuentes, normativas y cotizaciones
│
└── referencias/                           # Material de apoyo y archivos archivados
    └── legacy_optimizacion/               # Archivos legados del repositorio base original
```

---

## 🎯 Criterios para Nivel Destacado (91-100 pts)

Según la [Rúbrica de Evaluación](Pauta_segundo_avance.pdf):

1. **Plan de Actividades / Carta Gantt (30%):**
   - Presentar entre **8 a 15 actividades clave**, perfectamente definidas.
   - Agrupación coherente por fases (Planificación, Ejecución, Cierre) u objetivos específicos.
   - Secuencia lógica demostrable, optimizando el tiempo (tareas paralelas) y asignando recursos y responsables de forma realista.
2. **Presupuesto Detallado / Viabilidad Financiera (30%):**
   - Altamente detallado, transparente y profesional.
   - Columnas obligatorias: Ítem, Categoría, Cantidad, Costo Unitario, Costo Total y Justificación clara.
   - Agrupación obligatoria por categorías lógicas (Recursos Humanos, Equipamiento, Operaciones, Difusión).
   - Justificación impecable de cada gasto, demostrando excelente gestión de recursos y viabilidad económica.
3. **Colaboración y Asociatividad (20%):**
   - Identificación clara de una **red de apoyo sólida** (actores internos USM y externos comunitarios/institucionales).
   - Explicación que demuestre integración estratégica en la comunidad y beneficio recíproco.
   - Anexo obligatorio: **Borrador de carta de apoyo simulada** con tono formal, institucional y convincente.
4. **Coherencia y Presentación (Formato) (20%):**
   - Extensión estricta: **entre 5 y 7 páginas totales** (incluyendo la integración del Avance 1).
   - Portada con datos completos: Proyecto, Ramo, Semestre, Nombres y Roles.
   - **Tabla obligatoria de dedicación horaria** con columnas: `Integrante | Revisión | Desarrollo | Reuniones | Informe`.
   - Redacción impecable, uso elegante de tablas LaTeX (`booktabs`) y superación de los estándares mínimos requeridos.

---

## 🔄 Flujo de Trabajo y Sincronización

1. **Lectura de Instrucciones:** Cada integrante revisa el `README.md` dentro de su carpeta personal.
2. **Trabajo en Módulos Propios:** Cada persona edita exclusivamente los archivos `.tex` de su carpeta para evitar conflictos en Git.
3. **Coordinación Cruzada Clave:**
   - **Joaquín y Javier:** Coordinan la estructura del presupuesto y las justificaciones por ítem para que calcen número a número.
   - **Jose y Joaquín:** Alinean las actividades de la Gantt con los recursos y gastos presupuestados (cada actividad clave con costo debe reflejarse en el presupuesto).
   - **Mena y Anais:** Validan que la entidad emisora de la Carta de Apoyo coincida exactamente con uno de los actores estratégicos priorizados por Mena.
   - **Todos con Coni:** Cada integrante reporta sus horas dedicadas (`Revisión`, `Desarrollo`, `Reuniones`, `Informe`) a Coni para completar la tabla obligatoria de la portada.
4. **Compilación del Documento:**
   - **Vía GitHub Actions:** Al hacer `push` a la rama principal, el flujo [Compilar informe](.github/workflows/compilar-informe.yml) genera el PDF listo para descarga en los Artifacts (`informe-pdf`).
   - **Vía Overleaf:** Importar la carpeta completa del repositorio y seleccionar `main.tex` como archivo raíz de compilación.

---

## 📋 Checklist de Entrega

- [ ] Portada reglamentaria con todos los datos y tabla horaria de 6 integrantes completa.
- [ ] Integración concisa del Avance 1 sin desbordar el límite de páginas.
- [ ] Plan de Actividades con 8 a 15 tareas, fases, plazos, responsables y optimización temporal.
- [ ] Presupuesto detallado en tabla profesional agrupado por categorías lógicas.
- [ ] Justificación exhaustiva y cálculo transparente de cada ítem de gasto.
- [ ] Sección de Colaboración y Asociatividad con análisis estratégico de actores.
- [ ] Anexo con Borrador de Carta de Apoyo simulada en formato institucional formal.
- [ ] Conteo total de páginas verificado: **estrictamente entre 5 y 7 páginas**.
- [ ] Nombre del archivo para entrega según pauta: `Grupo[letra]_Fase3.pdf` (o formato oficial de Aula).
