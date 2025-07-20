import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import time

# === Load model & dataset ===
model = joblib.load("final_xgb_pipeline.pkl")
data = pd.read_csv("mumbai_house_data.csv")

bhk_list = sorted(data['bhk'].dropna().unique())
type_list = sorted(data['type'].dropna().unique())
locality_list = sorted(data['locality'].dropna().unique())
region_list = sorted(data['region'].dropna().unique())
status_list = sorted(data['status'].dropna().unique())

# === Page Config ===
st.set_page_config(page_title="Mumbai House Price Predictor", page_icon="🏠", layout="wide")

# === Price Formatter (Lakhs/Crores) ===
def format_price_in_indian_units(price):
    try:
        price = float(price)
    except:
        return "Invalid"
    if price >= 1e7:
        return f"{price/1e7:.2f} Crore"
    else:
        return f"{price/1e5:.2f} Lakh"

# === CSS (Dark Theme, Clean Layout) ===
st.markdown("""
    <style>
    .main {
        background-color: #121212;
        color: #f1f1f1;
    }
    h1 {
        text-align: center;
        color: #4CAF50;
    }
    .price-box {
        background: #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 20px auto;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.3);
    }
    .price-box h1, .price-box h3, .price-box p {
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# === Title ===
st.title("Mumbai House Price Predictor")

# === Sidebar Data Summary ===
st.sidebar.markdown(
    f"""
    <div style="
        background-color:#e0e0e0;
        border-radius:10px;
        padding:15px;
        color:#000000;
        font-size:16px;
        line-height:1.6;
        box-shadow:0px 4px 8px rgba(0,0,0,0.3);
        ">
        <h3 style="margin-top:0; margin-bottom:10px; font-size:18px; color:#000000;">📊 Data Summary</h3>
        <hr style="border:0; border-top:1px solid #555; margin:5px 0;">
        <p><b>Total Records:</b> {len(data):,}</p>
        <p><b>Regions:</b> {len(region_list):,}</p>
        <p><b>Price Range:</b><br> ₹449,000 – ₹600,000,000</p>
    </div>
    """,
    unsafe_allow_html=True
)

# === Session State for fields and price ===
if "final_price" not in st.session_state:
    st.session_state.final_price = None
if "reset_trigger" not in st.session_state:
    st.session_state.reset_trigger = False

# Function to reset all fields
def reset_fields():
    st.session_state.bhk = "Select BHK"
    st.session_state.type_ = "Select type"
    st.session_state.locality = "Select locality"
    st.session_state.area = 127.0
    st.session_state.region = "Select region"
    st.session_state.status = "Select status"
    st.session_state.final_price = None
    st.session_state.reset_trigger = True

# === Tabs ===
tab1, tab2, tab3 = st.tabs(["🏠 Predict Price", "📊 Insights", "ℹ️ About"])

# === Tab 1: Prediction ===
with tab1:
    st.header("Enter Property Details")
    col1, col2, col3 = st.columns(3)

    # Use session state for all inputs
    bhk = st.selectbox("Number of BHK", ["Select BHK"] + [str(int(x)) for x in bhk_list],
                       key="bhk")
    type_ = st.selectbox("Property Type", ["Select type"] + type_list, key="type_")
    locality = st.selectbox("Locality", ["Select locality"] + locality_list, key="locality")
    area = st.number_input("Area (sqft)", min_value=127.0, max_value=1179.0, step=10.0, key="area")
    region = st.selectbox("Region", ["Select region"] + region_list, key="region")
    status = st.selectbox("Status", ["Select status"] + status_list, key="status")

    col4, col5 = st.columns(2)
    with col4:
        if st.button("🔮 Predict Price", use_container_width=True):
            if any(x.startswith("Select") for x in [bhk, type_, locality, region, status]):
                st.error("❌ Please select all fields before predicting.")
            else:
                # Prepare input data
                input_df = pd.DataFrame([{
                    'bhk': int(bhk),
                    'type': type_,
                    'locality': locality,
                    'area': float(area),
                    'region': region,
                    'status': status
                }])
                with st.spinner("Analyzing market trends..."):
                    time.sleep(1.5)
                    price = model.predict(input_df)[0]
                    if price < 1e6:  # Scale if needed
                        price *= 1e5
                st.session_state.final_price = price

    # Display the final price (if available)
    if st.session_state.final_price is not None:
        st.markdown(f"""
            <div class="price-box">
                <h3>Final Predicted Price</h3>
                <h1>₹ {format_price_in_indian_units(st.session_state.final_price)}</h1>
                <p>Prediction complete.</p>
            </div>
        """, unsafe_allow_html=True)

    with col5:
        st.button("🔄 Reset", on_click=reset_fields, use_container_width=True)

# === Tab 2: Insights ===
with tab2:
    st.header("Market Insights")
    st.write("Explore price trends across regions and property sizes.")
    fig1 = px.box(data, x="region", y="price", color="region", title="Price Distribution by Region")
    st.plotly_chart(fig1, use_container_width=True)
    fig2 = px.scatter(data, x="area", y="price", color="bhk", title="Price vs Area by BHK")
    st.plotly_chart(fig2, use_container_width=True)

# === Tab 3: About ===
with tab3:
    st.header("About This App")
    st.image("https://cdn-icons-png.flaticon.com/512/25/25694.png", width=80)
    st.write("""
    **Mumbai House Price Predictor** uses a trained XGBoost model 
    to estimate prices based on BHK, area, property type, and region.

    **Features:**
    - User-friendly interface
    - Interactive visualizations
    - Predict price instantly in Lakhs or Crores
    - Market insights with box plots and scatter charts
    - Responsive design for all devices
    """)
    st.markdown("---")
    st.markdown("Made with ❤️ by [Sivaprasad T R](www.linkedin.com/in/sivaprasad-t-r) | Github : [Sivaprasad-creator](https://github.com/Sivaprasad-creator)")
    st.markdown("Data Source: [Mumbai House Data](https://www.kaggle.com/datasets/ashishpatel26/mumbai-house-data)")