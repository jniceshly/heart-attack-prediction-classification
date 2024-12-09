import pickle
import streamlit as st
import numpy as np

with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

def make_predict(feature) :
    input_array = np.array(feature).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction

st.title("Heart Attack Prediction")

st.header("Patient Information")

age = st.number_input("Age (in years):", min_value=0, max_value=120, value=30, step=1)

sex = st.radio("Sex:", ["Male", "Female"], index=1)

cp = st.selectbox(
    "Chest Pain Type:",
    [
        "Typical Angina",
        "Atypical Angina",
        "Non-Anginal Pain",
        "Asymptomatic"
    ],
    index=0
)

trestbps = st.number_input("Resting Blood Pressure (mmHg):", min_value=50, max_value=250, value=120, step=1)

chol = st.number_input("Serum Cholesterol (mg/dL):", min_value=100, max_value=600, value=200, step=1)

fbs = st.radio("Fasting Blood Sugar > 120 mg/dL:", ["True", "False"], index=1)

restecg = st.selectbox(
    "Resting ECG Results:",
    [
        "Normal",
        "ST-T Wave Abnormality",
        "Left Ventricular Hypertrophy"
    ],
    index=0
)

thalach = st.number_input("Max Heart Rate Achieved (thalach):", min_value=50, max_value=250, value=150, step=1)

exang = st.radio("Exercise-Induced Angina:", ["Yes", "No"], index=1)

oldpeak = st.number_input("ST Depression (oldpeak):", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

slope = st.selectbox(
    "Slope of Peak Exercise ST Segment:",
    ["Upsloping", "Flat", "Downsloping"],
    index=0
)

ca = st.slider("Number of Major Vessels Colored by Fluoroscopy (ca):", min_value=0, max_value=3, value=0)

thal = st.selectbox(
    "Thalassemia (thal):",
    ["Normal", "Fixed Defect", "Reversible Defect"],
    index=0
)

if st.button("Make Prediction") :

    if sex == 'Male' :
        sex = 1
    else :
        sex = 0

    if cp == 'Typical Angina' :
        cp = 0
    elif cp == 'Atypical Angina' :
        cp = 1
    elif cp == 'Non-Anginal Pain' :
        cp = 2
    else :
        cp = 3
    
    if fbs == 'True': 
        fbs = 1
    else :
        fbs = 0

    if restecg == 'Normal' :
        restecg = 0
    elif restecg == 'ST-T Wave Abnormality' :
        restecg = 1
    else :
        restecg = 2

    if exang == 'Yes' :
        exang = 1
    else :
        exang = 0

    if slope == 'Upsloping' :
        slope = 0
    elif slope == 'Flat' :
        slope = 1
    else :
        slope = 2

    if thal == 'Normal' :
        thal = 0
    elif thal == 'Fixed Defect' :
        thal = 1
    else :
        thal = 2

    feature = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    prediction = make_predict(feature)

    information = "Heart disease detected" if prediction[0] == 1 else "No heart disease detected"
    st.success(f"Prediction made: {information}")