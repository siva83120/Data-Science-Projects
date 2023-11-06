import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open(r"C:\Users\SIVASELVA\iraq students perfomance web.pkl","rb") as model_file:
    model = pickle.load(model_file)
    
# Load the dataset

data = pd.read_excel(r"C:\Users\SIVASELVA\Documents\Iraqi Student Performance Prediction.xlsx")
# Streamlit UI
st.title("Student Performance Prediction App")
st.sidebar.header("Student Information")

# Sidebar inputs for user
student_id = st.sidebar.number_input("Student ID", min_value=1, max_value=data["Student_ID"].max())
sex = st.sidebar.radio("Sex", data["Sex"].unique())
social_status = st.sidebar.radio("Social Status", data["Social Status"].unique())
age = st.sidebar.number_input("Age", min_value=data["Age"].min(), max_value=data["Age"].max())
governorate = st.sidebar.selectbox("Governorate", data["Governorate"].unique())
living = st.sidebar.selectbox("Living", data["Living"].unique())
mother_education = st.sidebar.selectbox("Mother's Education", data["Mother education"].unique())
father_education = st.sidebar.selectbox("Father's Education", data["Father education"].unique())
family_member_education = st.sidebar.radio("Family Member Education", data["Family member Education"].unique())
father_alive = st.sidebar.radio("Father Alive", data["Father Alive"].unique())

# You can add more input fields for other features as needed.

if st.sidebar.button("Predict"):
    # Filter the dataset based on user input
    selected_student = data[(data["Student_ID"] == student_id) & (data["Sex"] == sex) & (data["Social Status"] == social_status) & (data["Age"] == age) & (data["Governorate"] == governorate) & (data["Living"] == living) & (data["Mother education"] == mother_education) & (data["Father education"] == father_education) & (data["Family member Education"] == family_member_education) & (data["Father Alive"] == father_alive)]
    
    if not selected_student.empty:
        # Use the selected student's data to make a prediction
        features = selected_student.drop(["Student_ID"], axis=1)  # Remove the student ID
        prediction = rf_model.predict(features)
        st.write("Predicted Student Performance:", prediction[0])
    else:
        st.write("No matching student found in the dataset.")

 #You can add explanations and styling as needed.Make sure to replace "rf_model.pkl" and "Iraqi Student Performance Prediction.xlsx" with the correct paths to your trained model and dataset files. This code allows the user to input various student attributes and makes predictions based on the selected student's data.
#Please note that this code assumes you have the necessary data and a trained machine learning model for making predictions. You can further enhance the UI and functionality based on your specific use case and requirements.)


