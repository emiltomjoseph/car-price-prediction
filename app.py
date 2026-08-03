import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

# -------------------------------------------------------
# Load Model
# -------------------------------------------------------

model = joblib.load("car_price_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.title("🚗 Used Car Price Prediction")

st.markdown(
    """
Predict the **selling price of a used car** using a Machine Learning model
trained on the **CarDekho Used Car Dataset**.
"""
)

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

st.sidebar.header("📌 Project Information")

st.sidebar.markdown("""
### μLearn Epochs '26

**Assignment:** Day 9

**Model**
- Random Forest Regressor

**Dataset**
- CarDekho Used Car Dataset

**Developer**
- Emil Tom Joseph
""")

# -------------------------------------------------------
# Input Layout
# -------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    vehicle_age = st.number_input(
        "Vehicle Age (Years)",
        min_value=0,
        max_value=30,
        value=5
    )

    km_driven = st.number_input(
        "Kilometers Driven",
        min_value=0,
        value=50000
    )

    mileage = st.number_input(
        "Mileage (km/l)",
        min_value=0.0,
        value=18.0
    )

    engine = st.number_input(
        "Engine (CC)",
        min_value=500,
        max_value=5000,
        value=1200
    )

with col2:

    max_power = st.number_input(
        "Max Power",
        min_value=10.0,
        value=80.0
    )

    seats = st.number_input(
        "Seats",
        min_value=2,
        max_value=10,
        value=5
    )

    brand = st.selectbox(
        "Brand",
        [
            "Maruti",
            "Hyundai",
            "Honda",
            "Mahindra",
            "Toyota",
            "Tata",
            "Ford",
            "Volkswagen",
            "Renault",
            "Kia"
        ]
    )

    seller_type = st.selectbox(
        "Seller Type",
        [
            "Dealer",
            "Individual",
            "Trustmark Dealer"
        ]
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        [
            "Petrol",
            "Diesel",
            "CNG",
            "LPG",
            "Electric"
        ]
    )

    transmission_type = st.selectbox(
        "Transmission",
        [
            "Manual",
            "Automatic"
        ]
    )

# -------------------------------------------------------
# Prediction Button
# -------------------------------------------------------

predict = st.button(
    "🚗 Predict Selling Price",
    use_container_width=True
)

# -------------------------------------------------------
# Prediction
# -------------------------------------------------------

if predict:

    km_per_year = km_driven / (vehicle_age + 1)

    data = {}

    # Numerical Features
    data["vehicle_age"] = vehicle_age
    data["km_driven"] = km_driven
    data["mileage"] = mileage
    data["engine"] = engine
    data["max_power"] = max_power
    data["seats"] = seats
    data["km_per_year"] = km_per_year

    # Initialize all remaining columns with 0
    for col in feature_columns:
        if col not in data:
            data[col] = 0

    # One-Hot Encoding
    brand_col = f"brand_{brand}"
    seller_col = f"seller_type_{seller_type}"
    fuel_col = f"fuel_type_{fuel_type}"
    transmission_col = f"transmission_type_{transmission_type}"

    if brand_col in data:
        data[brand_col] = 1

    if seller_col in data:
        data[seller_col] = 1

    if fuel_col in data:
        data[fuel_col] = 1

    if transmission_col in data:
        data[transmission_col] = 1

    input_df = pd.DataFrame([data])

    input_df = input_df[feature_columns]

    numeric_columns = [
        "vehicle_age",
        "km_driven",
        "mileage",
        "engine",
        "max_power",
        "seats",
        "km_per_year"
    ]

    input_df[numeric_columns] = scaler.transform(
        input_df[numeric_columns]
    )

    prediction = model.predict(input_df)[0]

    st.success("Prediction Generated Successfully!")

    st.metric(
        label="💰 Estimated Selling Price",
        value=f"₹ {prediction:,.2f}"
    )

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit, Scikit-learn, Pandas and Python | μLearn Epochs '26'"
)