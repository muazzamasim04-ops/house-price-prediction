import streamlit as st
import joblib
import numpy as np

# Model load karna
model = joblib.load('house_model.joblib')

st.title("🏡 House Price Prediction App")
st.write("Evolvix AI/ML Capstone Project")

# Simple text inputs taaki JavaScript ka error na aaye
med_inc = st.text_input('Median Income', '3.0')
house_age = st.text_input('House Age (Years)', '20.0')
ave_rooms = st.text_input('Average Rooms', '5.0')
ave_bedrms = st.text_input('Average Bedrooms', '1.0')
population = st.text_input('Population', '500.0')
households = st.text_input('Households', '200.0')
latitude = st.text_input('Latitude', '34.0')
longitude = st.text_input('Longitude', '-118.0')

if st.button('Predict House Price'):
    try:
        # Values ko float mein convert karna
        input_data = np.array([[
            float(longitude), float(latitude), float(house_age), 
            float(ave_rooms), float(ave_bedrms), float(population), 
            float(households), float(med_inc)
        ]])
        prediction = model.predict(input_data)
        st.success(f"Estimated House Price: ${prediction[0]*100000:,.2f}")
    except Exception as e:
        st.error(f"Please enter valid numbers! Error: {e}")
