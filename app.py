# -------------------------------------
# ✅ Streamlit app.py with safe RESET using a callback
# -------------------------------------

import streamlit as st
import pandas as pd
import joblib

# === Load trained pipeline ===
model = joblib.load("final_xgb_pipeline.pkl")

# === Load dataset for dropdown options ===
data = pd.read_csv("mumbai_house_data.csv")

# === Options ===
bhk_list = sorted(data['bhk'].dropna().unique())
type_list = sorted(data['type'].dropna().unique())
locality_list = sorted(data['locality'].dropna().unique())
region_list = sorted(data['region'].dropna().unique())
status_list = sorted(data['status'].dropna().unique())

# === App title ===
st.title("🏠 Mumbai House Price Predictor")

# === --- Session State: Initialize default values --- ===
default_values = {
    "bhk": "Select number of BHK",
    "type_": "Select property type",
    "locality": "Select locality",
    "area": 127.0,
    "region": "Select region",
    "status": "Select status"
}

for key, val in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ✅ --- Define a Reset callback ---
def reset_fields():
    for key, val in default_values.items():
        st.session_state[key] = val
    # Note: no need to call st.rerun() here; it auto-runs after callbacks

# === --- Input fields using keys --- ===
bhk = st.selectbox(
    "Number of BHK",
    ["Select number of BHK"] + [str(int(x)) for x in bhk_list],
    key="bhk"
)

type_ = st.selectbox(
    "Property Type",
    ["Select property type"] + type_list,
    key="type_"
)

locality = st.selectbox(
    "Locality",
    ["Select locality"] + locality_list,
    key="locality"
)

area = st.number_input(
    "Area (in sqft)",
    min_value=127.0, max_value=1179.0, step=10.0,
    key="area"
)

region = st.selectbox(
    "Region",
    ["Select region"] + region_list,
    key="region"
)

status = st.selectbox(
    "Status",
    ["Select status"] + status_list,
    key="status"
)

# === --- Buttons: Predict & Reset --- ===
col1, col2 = st.columns(2)

with col1:
    if st.button("Predict Price"):
        if any(opt.startswith("Select") for opt in [bhk, type_, locality, region, status]):
            st.error("❌ Please select all fields properly.")
        else:
            try:
                # ✅ Input DataFrame
                input_df = pd.DataFrame([{
                    'bhk': int(bhk),
                    'type': type_,
                    'locality': locality,
                    'area': float(area),
                    'region': region,
                    'status': status
                }])

                # ✅ Predict
                predicted_price = model.predict(input_df)[0]

                st.success(f"💰 Predicted Price: {predicted_price:.2f} Lakhs")
                st.info("Price Unit: Lakhs")

            except Exception as e:
                st.error(f"❌ ERROR: {e}")

with col2:
    st.button("Reset", on_click=reset_fields)
