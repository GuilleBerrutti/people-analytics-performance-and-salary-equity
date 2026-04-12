# 📊 Análisis de Gestión de Talento y Equidad Salarial

---

## 🎯 Objetivo del Proyecto

Analizar indicadores clave de recursos humanos para mejorar la toma de decisiones en gestión de talento, con foco en **rotación, desempeño y equidad salarial**.

El proyecto permite monitorear KPIs en tiempo real, facilitando la detección temprana de desvíos y optimizando la respuesta organizacional.

---

## 🧠 Problema de Negocio

La organización no contaba con una visión integrada del desempeño del personal, lo que generaba:

- Dificultad para identificar áreas con alta rotación  
- Falta de visibilidad sobre cumplimiento de objetivos  
- Ineficiencia en la asignación de recursos humanos  

👉 Pregunta clave del análisis:

**¿Qué factores están afectando el desempeño y la retención del talento, y cómo se pueden optimizar?**

---

## 📊 Dashboard Interactivo

![Dashboard de People Analytics](preview_dashboard.png)

🔗 **Acceso al dashboard (Power BI):**  
👉 *[Acceder al dashboard (Power BI)](https://github.com/GuilleBerrutti/people-analytics-dashboard/blob/main/dashboard_gestion_talento.pbix)*




## 📊 Metodología

El análisis se desarrolló a partir de datos de empleados utilizando:

- **Extracción y limpieza de datos:** SQL y Excel  
- **Modelado de datos:** estructuración de métricas de RRHH  
- **Visualización:** Power BI para exploración interactiva  
- **Análisis estadístico:** distribución salarial y segmentación  

---

## 💡 Insights Clave

- **Rotación de personal:**  
  Se identificaron áreas con mayor tasa de rotación, permitiendo enfocar acciones de retención.

- **Desempeño organizacional:**  
  Diferencias significativas en el cumplimiento de objetivos entre equipos.

- **Equidad salarial:**  
  Variaciones en la distribución de salarios entre grupos, detectadas mediante análisis de densidad.

- **Clima y eficiencia:**  
  Relación entre desempeño y posibles necesidades de capacitación en ciertos sectores.

---

## 📈 Conclusión

El análisis demuestra que la gestión del talento puede optimizarse mediante monitoreo continuo y segmentación de datos.

👉 Recomendaciones:
- Implementar estrategias de retención en áreas críticas  
- Ajustar políticas salariales para mejorar equidad  
- Reforzar capacitación en equipos con bajo desempeño  

---

## 🛠️ Stack Tecnológico

- **Power BI** → Visualización y análisis interactivo  
- **SQL & Excel** → Extracción y limpieza de datos  
- **Python (Matplotlib & Seaborn)** → Análisis y visualización estadística  

---

## 🐍 Análisis de Distribución Salarial (Python)

Se utilizó Python para analizar la distribución salarial por género mediante un gráfico de densidad:

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))

sns.violinplot(x="Genero", y="Salario", data=dataset, inner="quartile")

plt.title("Distribución Salarial por Género")
plt.xlabel("Género")
plt.ylabel("Salario Mensual")

plt.show()
