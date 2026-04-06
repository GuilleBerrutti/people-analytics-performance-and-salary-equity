# 📊 People Analytics Dashboard: Gestión de Talento y Equidad Salarial

Este proyecto presenta un análisis integral de gestión de talento utilizando una arquitectura híbrida de datos. Combina la potencia de **Power BI** para la visualización de KPIs operativos y **Python** para análisis estadísticos avanzados de distribución.

---

## 🧠 Conclusiones del Análisis de Datos

Tras el procesamiento y visualización de la estructura organizacional, se determinan los siguientes hallazgos críticos:

1. **Brecha Salarial y Techos de Cristal:** El análisis de densidad mediante gráficos de violín revela que, aunque los promedios pueden parecer cercanos, el género masculino presenta una mayor concentración en los deciles salariales superiores. Esto sugiere la existencia de barreras invisibles para el acceso a cargos de alta jerarquía por parte del género femenino.
2. **Riesgo de Fuga de Talento (Churn):** Con un **14% de inactividad**, se identifica una oportunidad de mejora en las políticas de retención. Al cruzar estos datos con la antigüedad, se observa que la rotación se concentra en departamentos específicos como Ventas, lo que requiere una revisión de los incentivos locales.
3. **Desequilibrio en la Carga de Nómina:** El departamento de **IT** lidera el gasto salarial con $3.0M, superando en un 36% al área de Ventas. Esta disparidad indica una alta dependencia de perfiles técnicos especializados, sugiriendo la necesidad de planes de sucesión internos para mitigar el riesgo operativo.
4. **Segmentación de Fuerza Laboral:** El **86% de la plantilla activa** se distribuye de manera desigual, donde Marketing y Finanzas muestran una estructura más plana, permitiendo una comunicación más ágil en comparación con Recursos Humanos.

---

## 🖼️ Evidencia del Análisis (Dashboard)

![Dashboard de People Analytics](https://github.com/GuilleBerrutti/people-analytics-dashboard/blob/main/tu_imagen.png?raw=true)

---

## 🐍 Código Python: Visualización de Distribución Salarial

Para lograr la integración estética y estadística en Power BI, se utilizó el siguiente script de Python (Librerías `Seaborn` y `Matplotlib`):

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configuración de estilo para Modo Oscuro Puro (#000000)
plt.rcParams.update({
    "figure.facecolor": "#000000",
    "axes.facecolor": "#000000",
    "axes.edgecolor": "#444444",
    "axes.labelcolor": "#FFFFFF",
    "xtick.color": "#FFFFFF",
    "ytick.color": "#FFFFFF",
    "text.color": "#FFFFFF",
    "grid.color": "#222222"
})

# 2. Creación del lienzo
plt.figure(figsize=(10, 6))

# 3. Gráfico de Violín: Análisis de Densidad Salarial por Género
# Colores Neón: #00f5d4 (Cyan) y #ff006e (Magenta)
colores_neon = ["#00f5d4", "#ff006e"]
ax = sns.violinplot(x="Genero", y="Salario", data=dataset, 
                    palette=colores_neon, inner="quartile", linewidth=1.5)

# 4. Estilización de líneas de cuartiles
plt.setp(ax.collections, edgecolor="white")

# 5. Títulos y etiquetas profesionales
plt.title("Análisis de Distribución Salarial por Género", fontsize=16, fontweight='bold', pad=25)
plt.xlabel("Género", fontsize=13)
plt.ylabel("Salario Mensual", fontsize=13)

# 6. Limpieza de bordes (Spines)
sns.despine(left=True, bottom=False)

# 7. Renderizado final
plt.tight_layout()
plt.show()
