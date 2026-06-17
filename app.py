import streamlit as st

# Configuración de la página estilo Dark Mode "aesthetic"
st.set_page_config(page_title="Mis Metas", page_icon="✨", layout="centered")

# Título Principal
st.title("✨ Mis metas")

# Crear pestañas para organizar la app
tab1, tab2, tab3 = st.tabs(["🎯 Metas de Ahorro", "📊 Calificaciones", "📝 Apuntes"])

# --- PESTAÑA 1: METAS DE AHORRO ---
with tab1:
    st.subheader("Buscar metas")
    search = st.text_input("🔍 Buscar metas", label_visibility="collapsed")
    
    # Formulario para agregar nueva meta
    with st.expander("➕ Nueva meta"):
        nombre_meta = st.text_input("Ingresa el nombre de la meta")
        monto_objetivo = st.number_input("Monto objetivo ($)", min_value=0.0, step=100.0)
        monto_ahorrado = st.number_input("Monto ahorrado ($)", min_value=0.0, step=100.0)
        
        if st.button("Guardar meta"):
            st.success(f"¡Meta '{nombre_meta}' guardada con éxito!")

# --- PESTAÑA 2: CALCULADORA DE CALIFICACIONES ---
with tab2:
    st.subheader("🧮 ¿Cuánto necesito para pasar?")
    st.write("Ingresa tus calificaciones de los dos primeros parciales para saber cuánto necesitas en el tercero.")
    
    parcial1 = st.number_input("Calificación Parcial 1", min_value=0.0, max_value=10.0, step=0.5)
    parcial2 = st.number_input("Calificación Parcial 2", min_value=0.0, max_value=10.0, step=0.5)
    
    if st.button("Calcular"):
        # Suponiendo que se pasa con 6 de promedio final mínimo
        # (P1 + P2 + P3) / 3 = 6  =>  P1 + P2 + P3 = 18  =>  P3 = 18 - P1 - P2
        necesario = 18.0 - (parcial1 + parcial2)
        if necesario <= 0:
            st.balloons()
            st.success("¡Ya aprobaste la materia! Felicidades 🎉")
        elif necesario > 10:
            st.error(f"Necesitas un {necesario:.1f}. ¡Está muy difícil pasar en este parcial! 😰")
        else:
            st.warning(f"Necesitas sacar al menos **{necesario:.1f}** en el tercer parcial para aprobar con 6.0.")

# --- PESTAÑA 3: APUNTES Y NOTAS ---
with tab3:
    st.subheader("📝 Mis Apuntes")
    nota_nueva = st.text_area("Escribe una nueva nota aquí...")
    if st.button("Guardar Nota"):
        st.info("Nota guardada (simulación).")
