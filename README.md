# 📊 People Analytics Dashboard: Gestión de Talento y Equidad Salarial

Este proyecto presenta un análisis integral de gestión de talento utilizando una arquitectura híbrida de datos. Combina la potencia de **Power BI** para la visualización de KPIs operativos y **Python** para análisis estadísticos avanzados de distribución.

---

## 🧠 Conclusiones y Valor de Negocio

El análisis de este dataset permite extraer las siguientes conclusiones clave para la toma de decisiones en Recursos Humanos:

* **Identificación de Brechas Salariales:** Mediante el uso de **gráficos de violín**, se identificó no solo el promedio, sino la *densidad* de los salarios. Esto permite detectar si existen "techos de cristal" o si la distribución de sueldos es equitativa en términos de dispersión por género.
* **Eficiencia en la Retención:** El reporte muestra un índice de **86% de personal activo**, permitiendo a la gerencia monitorear la salud de la rotación de manera visual y segmentada por departamento.
* **Optimización de Presupuesto por Área:** La comparativa de promedios salariales destaca a los departamentos de **IT y Finanzas** como los de mayor inversión, facilitando la planificación de futuras contrataciones según el presupuesto disponible.

---

## 🖼️ Evidencia del Análisis (Dashboard)

![Dashboard de People Analytics](https://github.com/GuilleBerrutti/people-analytics-dashboard/blob/main/tu_imagen.png?raw=true)

> *Nota: Sustituye el enlace de arriba por la ruta real de tu imagen una vez que la subas al repositorio.*

---

## 🚀 Características Técnicas

* **Análisis de Dotación:** Visualización del estado de los empleados (Activo vs. Inactivo).
* **Inversión en Nómina:** Desglose detallado del promedio salarial por departamentos.
* **Integración Avanzada con Python:** Uso de la librería `Seaborn` para superar las limitaciones de los gráficos nativos de Power BI, logrando una visualización de densidad salarial mucho más profunda.
* **Diseño UI/UX:** Interfaz optimizada en **Modo Oscuro** para mejorar la legibilidad y resaltar los puntos de datos clave.

---

## 🛠️ Stack Tecnológico

* **Excel:** Fuente de datos y preprocesamiento inicial.
* **Power BI:** Modelado de datos, medidas DAX y diseño de interfaz.
* **Python (Pandas, Matplotlib, Seaborn):** Utilizado para el análisis estadístico complejo y la generación de visuales personalizados.

### 🐍 Fragmento de Código Python Embebido
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración de estilo Dark Mode
plt.rcParams.update({"figure.facecolor": "#000000", "axes.facecolor": "#000000"})

# Generación del gráfico de distribución salarial
sns.violinplot(x="Genero", y="Salario", data=dataset, palette=["#00f5d4", "#ff006e"])
plt.show()
