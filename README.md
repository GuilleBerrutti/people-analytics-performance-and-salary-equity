# 👥 People Analytics & Workforce Intelligence

Análisis estratégico de talento orientado a identificar patrones de rotación, desempeño y distribución salarial para optimizar decisiones de Recursos Humanos mediante analítica avanzada y visualización ejecutiva.

---

# 🎯 Objetivo del Proyecto

Desarrollar un sistema de análisis de talento que permita detectar riesgos organizacionales vinculados a:

- Rotación de personal
- Desempeño operativo
- Equidad salarial
- Eficiencia organizacional

El proyecto busca transformar datos de RRHH en insights accionables para mejorar retención, productividad y asignación de recursos humanos.

---

# 🧠 Problema de Negocio

La organización no contaba con visibilidad centralizada sobre indicadores críticos de talento, generando:

- Alta dificultad para detectar áreas con rotación crítica
- Falta de seguimiento del desempeño organizacional
- Escasa transparencia en distribución salarial
- Baja capacidad de anticipación sobre riesgos de talento

👉 Pregunta central del análisis:

**¿Qué patrones organizacionales están impactando la retención y el desempeño del talento, y cómo pueden mitigarse mediante decisiones basadas en datos?**

---

# 📊 Dashboard Ejecutivo

![Dashboard de People Analytics](preview_dashboard.png)

🔗 **Acceso al dashboard interactivo:**  
👉 [People Analytics Dashboard](https://github.com/GuilleBerrutti/people-analytics-dashboard/blob/main/dashboard_gestion_talento.pbix)

---

# 🚀 Resultados Clave del Negocio

| KPI Estratégico | Resultado |
|---|---|
| Concentración de rotación | 68% de la rotación concentrada en el 24% de las áreas |
| Brecha de desempeño | Equipos de bajo rendimiento con hasta 32% menos cumplimiento de objetivos |
| Riesgo de fuga de talento | 57% de las desvinculaciones asociadas a empleados con baja satisfacción |
| Equidad salarial | Diferencias salariales promedio de hasta 18% entre segmentos comparables |
| Optimización organizacional | Potencial mejora del 22% en eficiencia mediante estrategias focalizadas de retención y capacitación |

---

# 📦 KPIs Estratégicos Analizados

- Tasa de rotación de empleados
- Distribución salarial por segmento
- Nivel de cumplimiento de objetivos
- Performance por departamento
- Headcount organizacional
- Comparativa salarial por género
- Distribución de desempeño
- Riesgo de fuga de talento

---


# 🛠️ Metodología Analítica

El proyecto fue desarrollado mediante un flujo completo de análisis de datos:

### 📥 Extracción y Transformación
- Limpieza y preparación de datos con SQL y Excel
- Normalización de métricas de RRHH
- Validación y estructuración del dataset

### 📊 Modelado y Visualización
- Construcción de dashboard ejecutivo en Power BI
- Diseño de KPIs estratégicos
- Segmentación organizacional

### 🐍 Análisis Estadístico
- Distribución salarial
- Análisis de densidad
- Comparativas entre segmentos
- Detección de patrones de comportamiento

---

# 🐍 Análisis de Distribución Salarial en Python

Se utilizó Python para analizar patrones de distribución salarial y detectar variaciones entre segmentos organizacionales.

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))

sns.violinplot(
    x="Genero",
    y="Salario",
    data=dataset,
    inner="quartile"
)

plt.title("Distribución Salarial por Género")
plt.xlabel("Género")
plt.ylabel("Salario Mensual")

plt.show()
