import streamlit as st
import joblib
import numpy as np

# Load saved model and scaler
model = joblib.load('car_price_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Car Price Prediction App")

# Input fields (keep them simple for now)
symboling = st.slider("Symboling", -3, 3, 0)
fueltype = st.selectbox("Fuel Type", ["gas", "diesel"])
aspiration = st.selectbox("Aspiration", ["std", "turbo"])
doornumber = st.selectbox("Number of Doors", ["two", "four"])
carbody = st.selectbox("Car Body", ["convertible", "sedan", "hatchback", "wagon", "hardtop"])
drivewheel = st.selectbox("Drive Wheel", ["fwd", "rwd", "4wd"])
enginelocation = st.selectbox("Engine Location", ["front", "rear"])
wheelbase = st.number_input("Wheelbase", value=88.6)
carlength = st.number_input("Car Length", value=168.8)
carwidth = st.number_input("Car Width", value=64.1)
carheight = st.number_input("Car Height", value=48.8)
curbweight = st.number_input("Curb Weight", value=2548)
enginetype = st.selectbox("Engine Type", ["dohc", "ohc", "ohcf", "rotor"])
cylindernumber = st.selectbox("Cylinder Number", ["four", "six", "five", "eight", "two", "three", "twelve"])
enginesize = st.number_input("Engine Size", value=130)
fuelsystem = st.selectbox("Fuel System", ["mpfi", "2bbl", "1bbl", "spdi"])
boreratio = st.number_input("Bore Ratio", value=3.47)
stroke = st.number_input("Stroke", value=2.68)
compressionratio = st.number_input("Compression Ratio", value=9.0)
horsepower = st.number_input("Horsepower", value=111)
peakrpm = st.number_input("Peak RPM", value=5000)
citympg = st.number_input("City MPG", value=21)
highwaympg = st.number_input("Highway MPG", value=27)
carCompany = st.selectbox("Car Brand", ["alfa-romeo", "audi", "bmw", "chevrolet", "toyota", "honda", "volkswagen"])

# Manual label encoding (must match training order!)
label_dicts = {
    "fueltype": {"gas": 1, "diesel": 0},
    "aspiration": {"std": 1, "turbo": 0},
    "doornumber": {"two": 1, "four": 0},
    "carbody": {"convertible": 0, "hardtop": 1, "hatchback": 2, "sedan": 3, "wagon": 4},
    "drivewheel": {"fwd": 1, "rwd": 2, "4wd": 0},
    "enginelocation": {"front": 1, "rear": 0},
    "enginetype": {"dohc": 0, "ohc": 1, "ohcf": 2, "rotor": 3},
    "cylindernumber": {"two": 0, "three": 1, "four": 2, "five": 3, "six": 4, "eight": 5, "twelve": 6},
    "fuelsystem": {"1bbl": 0, "2bbl": 1, "mpfi": 2, "spdi": 3},
    "carCompany": {"alfa-romeo": 0, "audi": 1, "bmw": 2, "chevrolet": 3, "honda": 4, "toyota": 5, "volkswagen": 6}
}

# Prepare input data
input_data = np.array([[
    symboling,
    label_dicts["fueltype"][fueltype],
    label_dicts["aspiration"][aspiration],
    label_dicts["doornumber"][doornumber],
    label_dicts["carbody"][carbody],
    label_dicts["drivewheel"][drivewheel],
    label_dicts["enginelocation"][enginelocation],
    wheelbase, carlength, carwidth, carheight, curbweight,
    label_dicts["enginetype"][enginetype],
    label_dicts["cylindernumber"][cylindernumber],
    enginesize,
    label_dicts["fuelsystem"][fuelsystem],
    boreratio, stroke, compressionratio, horsepower, peakrpm,
    citympg, highwaympg,
    label_dicts["carCompany"][carCompany]
]])

# Scale input
input_scaled = scaler.transform(input_data)

# Predict
if st.button("Predict Price"):
    try:
        # Model prediction
        prediction_usd = model.predict(input_scaled)[0]
        
        # Convert to INR and display result
        usd_to_inr = 83.0  # Use current USD to INR rate
        prediction_inr = prediction_usd * usd_to_inr
        st.success(f"Predicted Car Price: ₹{prediction_inr:,.0f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")


