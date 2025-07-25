import streamlit as st
import matplotlib.pyplot as plt

# Título y descripción
st.title("Calculadora de Momento (Torque)")
st.markdown("""
Esta herramienta te permite calcular el momento (torque) generado por una fuerza respecto a un punto de giro.

**Fórmula:**
> Momento = Fuerza × Distancia
""")

# Inputs del usuario
fuerza = st.number_input("Fuerza (N)", min_value=0.0, step=0.1)
distancia = st.number_input("Distancia (m)", min_value=0.0, step=0.1)

# Cálculo
momento = fuerza * distancia
st.success(f"Momento = {momento:.2f} N·m")

# Visualización: palanca simple
fig, ax = plt.subplots(figsize=(6, 1))
ax.plot([0, distancia], [0, 0], color='black', linewidth=4)
ax.scatter([0], [0], color='red', label='Punto de giro (eje)')
ax.arrow(distancia, 0, 0, 0.2, head_width=0.1, head_length=0.1, fc='blue', ec='blue')
ax.text(distancia, 0.25, f'Fuerza = {fuerza} N', ha='center')

ax.set_xlim(-1, max(distancia + 1, 2))
ax.set_ylim(-0.5, 1)
ax.axis('off')
st.pyplot(fig)
