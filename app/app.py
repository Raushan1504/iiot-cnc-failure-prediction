import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Configuracion global de la interfaz
st.set_page_config(page_title="Mantenimiento Predictivo CNC", layout="centered")

# ==========================================
# 1. CARGA Y CACHÉ DE ARTEFACTOS
# ==========================================
@st.cache_resource
def load_artifacts():
    # Resolucion absoluta de rutas para garantizar portabilidad en entornos Linux/Windows
    base_dir = Path(__file__).resolve().parent.parent
    scaler_path = base_dir / "models" / "scaler.joblib"
    model_path = base_dir / "models" / "rf_model.joblib"
    
    # Deserializacion de artefactos matematicos
    scaler_obj = joblib.load(scaler_path)
    model_obj = joblib.load(model_path)
    
    return scaler_obj, model_obj

scaler, model = load_artifacts()

# ==========================================
# 2. CAPTURA DE TELEMETRÍA (UI)
# ==========================================
st.title("Sistema de Mantenimiento Predictivo Industrial")
st.write("Ingrese los parámetros de telemetría de la fresadora CNC para predecir anomalías.")

st.header("Entrada de Variables de Proceso")

air_temp = st.number_input(
    label="Air temperature [K]",
    min_value=200.0,
    max_value=400.0,
    value=300.0,
    step=0.1,
    help="Temperatura del aire ambiente en Kelvin."
)

process_temp = st.number_input(
    label="Process temperature [K]",
    min_value=200.0,
    max_value=400.0,
    value=310.0,
    step=0.1,
    help="Temperatura del proceso de manufactura en Kelvin."
)

rotational_speed = st.number_input(
    label="Rotational speed [rpm]",
    min_value=0,
    max_value=5000,
    value=1500,
    step=10,
    help="Velocidad de rotación del husillo en RPM."
)

torque = st.number_input(
    label="Torque [Nm]",
    min_value=0.0,
    max_value=200.0,
    value=40.0,
    step=0.5,
    help="Fuerza de torsión aplicada (Newton-metro)."
)

tool_wear = st.number_input(
    label="Tool wear [min]",
    min_value=0,
    max_value=500,
    value=0,
    step=1,
    help="Desgaste acumulado de la herramienta de corte en minutos."
)

# ==========================================
# 3. MOTOR DE INFERENCIA Y RESULTADOS
# ==========================================
if st.button("Ejecutar Diagnóstico"):
    
    # Construccion de la matriz de caracteristicas (Feature Matrix) respetando el esquema original
    input_data = pd.DataFrame([{
        "Air temperature [K]": air_temp,
        "Process temperature [K]": process_temp,
        "Rotational speed [rpm]": rotational_speed,
        "Torque [Nm]": torque,
        "Tool wear [min]": tool_wear
    }])
    
    # Estandarizacion de la varianza en tiempo real
    input_scaled = scaler.transform(input_data)
    
    # Inferencia algoritmica
    prediction = model.predict(input_scaled)
    
    # Extraccion del umbral de probabilidad para la clase positiva (falla = 1)
    probability = model.predict_proba(input_scaled)[0, 1]
    
    # Renderizado de resultados de negocio
    st.subheader("Resultado del Diagnóstico")
    
    st.metric(label="Probabilidad de Falla Computada", value=f"{probability * 100:.2f}%")
    
    # Logica de enrutamiento visual de alertas
    if prediction[0] == 1:
        st.error("Alerta Crítica: Se detecta riesgo inminente de falla. Requerido protocolo de paro y mantenimiento preventivo.")
    else:
        st.success("Operación Estable: La telemetría se encuentra dentro de los límites de tolerancia algorítmica.")