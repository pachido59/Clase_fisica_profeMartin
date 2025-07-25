import streamlit as st

st.title("Calculadora de Momento (Torque)")
st.markdown("""
Esta herramienta permite calcular el **momento total** generado por múltiples fuerzas aplicadas a diferentes distancias desde un punto de giro.

Puedes ingresar fuerzas positivas (hacia arriba) o negativas (hacia abajo).

**Fórmula general:**
> Momento total = Σ (Fuerza × Distancia)
""")

# Número de fuerzas
num_fuerzas = st.slider("¿Cuántas fuerzas quieres ingresar?", min_value=1, max_value=5, value=2)

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

# Pie de página
st.markdown("""
---
App desarrollada para fines educativos.  
**Hecho por Rodrigo Tovilla Rangel**
""")
