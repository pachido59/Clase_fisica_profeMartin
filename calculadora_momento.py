import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Calculadora de Momento", layout="centered")

st.title("Calculadora de Momento (Torque)")
st.markdown("""
Esta herramienta permite calcular el **momento total** generado por múltiples fuerzas aplicadas a diferentes distancias desde un punto de giro.

Puedes ingresar fuerzas positivas (hacia arriba) o negativas (hacia abajo).

**Fórmula general:**
> Momento total = Σ (Fuerza × Distancia)
""")

# Número de fuerzas
num_fuerzas = st.slider("¿Cuántas fuerzas quieres ingresar?", min_value=1, max_value=5, value=3)

fuerzas = []
distancias = []

# Inputs múltiples
st.markdown("### Datos de fuerzas:")
for i in range(num_fuerzas):
    col1, col2 = st.columns(2)
    with col1:
        f = st.number_input(f"Fuerza #{i+1} (N)", value=0.0, key=f"f{i}")
    with col2:
        d = st.number_input(f"Distancia #{i+1} (m)", value=0.0, key=f"d{i}")
    fuerzas.append(f)
    distancias.append(d)

# Cálculo de momento total
momentos = [f*d for f, d in zip(fuerzas, distancias)]
momento_total = sum(momentos)

# Resultados
st.markdown("### Resultados:")
for i in range(num_fuerzas):
    st.write(f"F{i+1} × d{i+1} = {fuerzas[i]} × {distancias[i]} = {momentos[i]:.2f} N·m")
st.success(f"Momento total = {momento_total:.2f} N·m")

# === DIAGRAMA DE CUERPO LIBRE ===
st.markdown("### Diagrama de Cuerpo Libre:")

fig1, ax1 = plt.subplots(figsize=(7, 2))
barra_long = max(distancias) + 0.5
ax1.plot([0, barra_long], [0, 0], color='black', linewidth=5)  # barra
ax1.scatter([0], [0], color='red', zorder=5)
ax1.text(0, -0.3, "Punto de giro", ha='center', fontsize=9)

for i in range(num_fuerzas):
    color = 'blue' if fuerzas[i] > 0 else 'orange'
    dy = 0.3 if fuerzas[i] > 0 else -0.3

    # Flecha de fuerza
    ax1.arrow(distancias[i], 0, 0, dy, head_width=0.1, head_length=0.1, fc=color, ec=color, linewidth=2)

    # Texto de fuerza y distancia
    ax1.text(distancias[i], dy + (0.12 if fuerzas[i] > 0 else -0.15),
             f'F{i+1} = {fuerzas[i]} N\n d{i+1} = {distancias[i]} m',
             ha='center', fontsize=9)

ax1.set_xlim(-0.5, barra_long + 0.5)
ax1.set_ylim(-1, 1)
ax1.axis('off')
st.pyplot(fig1)

# === DIAGRAMA SIMPLIFICADO ===
st.markdown("### Diagrama del Resultado Final:")

fig2, ax2 = plt.subplots(figsize=(5, 2))
ax2.plot([0, 2], [0, 0], color='black', linewidth=5)
ax2.scatter([0], [0], color='red', zorder=5)
ax2.text(0, -0.3, "Punto de giro", ha='center', fontsize=9)

# Mostrar flecha del momento resultante
if abs(momento_total) > 0:
    sentido = "Horario" if momento_total < 0 else "Antihorario"
    color = "orange" if momento_total < 0 else "blue"
    ax2.arrow(1, 0, 0, 0.4 if momento_total > 0 else -0.4,
              head_width=0.1, head_length=0.1, fc=color, ec=color, linewidth=2)
    ax2.text(1, 0.6 if momento_total > 0 else -0.7,
             f"Momento Total\n{momento_total:.2f} N·m\n({sentido})",
             ha='center', fontsize=10, color=color)

ax2.set_xlim(-0.5, 2.5)
ax2.set_ylim(-1, 1)
ax2.axis('off')
st.pyplot(fig2)

# Pie de página
st.markdown("""
---
App desarrollada para fines educativos.  
**Hecho por Rodrigo Tovilla Rangel**
""")
