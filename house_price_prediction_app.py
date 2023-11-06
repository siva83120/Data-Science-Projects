import streamlit as st
import pickle
import numpy as np

# Load the pre-trained machine learning model
with open(r"C:\Users\SIVASELVA\house prediction web.pkl","rb") as model_file:
    model = pickle.load(model_file)

st.title("House Price Prediction")

# Input features
st.subheader("Input Features")

# You can create input fields for various features like number of bedrooms, square footage, etc.
bedroom_count = st.number_input("Number of Bedrooms", value=3)
center_distance = st.number_input("Number of center_distance", value=2)
net_sqm = st.number_input("Square Footage of Living Area", value=1500)
metro_distance = st.number_input("km of metro_distance", value=2)
floor	 = st.number_input("Number of floor	", value=2)
age = st.number_input("Number of age", value=2)

# Button to trigger prediction
if st.button("Predict Price"):
    # Prepare input data as a NumPy array
    input_data = np.array([bedroom_count,center_distance,net_sqm,metro_distance,floor,age]).reshape(-1,1)

    # Make a prediction
    prediction = model.predict(input_data)

    st.subheader("Prediction")
    st.write(f"The estimated house price is ${prediction[0]:.2f}")

st.sidebar.markdown("Built with ❤️ by Your Name")


