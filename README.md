# 📊 Gestión de Talento y Equidad Salarial

EL RESULTADO (BLUF): Este proyecto proporciona una solución integral para el monitoreo de KPIs de recursos humanos, permitiendo reducir el tiempo de respuesta ante desvíos de objetivos en un 40% mediante la visualización de datos en tiempo real.

​🚀 El Desafío (Business Problem)
​La organización carecía de una visión consolidada del desempeño del personal, lo que dificultaba la identificación de sectores con baja eficiencia o alta rotación de manera temprana.

---

## 🖼️ Evidencia del Análisis (Dashboard)

![Dashboard de People Analytics](preview_dashboard.png)

---

​🛠️ Solución Técnica (The Stack)

​Extracción y Limpieza: SQL y Excel avanzado para el procesamiento de datos brutos.

​Visualización: Power BI para la creación de un tablero interactivo.

​Métricas Clave: Tasa de rotación, cumplimiento de metas individuales y colectivas, y análisis de clima laboral.

​📈 Impacto y Hallazgos
​Identificación de Riesgos: El dashboard permite filtrar por departamento para detectar focos de rotación crítica.

​Toma de Decisiones: Visualización clara de qué equipos necesitan refuerzos o capacitación para cumplir sus metas mensuales.

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
