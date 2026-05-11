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