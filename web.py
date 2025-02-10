import os
import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreak',
                   page_icon='👨🏻‍⚕️',
                   layout='wide')

diabetes_model_path = r'Save_model\diabetes_model.sav'
heart_model_path = r'Save_model\heart-disease-mode.sav'
parkinsons_model_path = r"Save_model\parkinson's_model.sav"
with open(diabetes_model_path, 'rb') as file:
    diabetes_model = pickle.load(file)
with open(heart_model_path, 'rb') as file:
    heart_model = pickle.load(file)
with open(parkinsons_model_path, 'rb') as file:
    parkinsons_model = pickle.load(file)

with st.sidebar:
    selected = option_menu(
        menu_title="Prediction of Disease Outbreak",
      options=["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
        icons=["house", "activity", "list-task"],
        menu_icon="cast",
        default_index=0,
    )

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', key="Pregnancies")  # Add keys!
    with col2:
        Glucose = st.text_input('Glucose level', key="Glucose")
    with col3:
        BloodPressure = st.text_input('Blood Pressure', key="BloodPressure")
    with col1:
        SkinThickness = st.text_input('Skin Thickness value', key="SkinThickness")
    with col2:
        Insulin = st.text_input('Insulin level', key="Insulin")
    with col3:
        BMI = st.text_input('BMI value', key="BMI")
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', key="DiabetesPedigreeFunction")
    with col2:
        Age = st.text_input('Age of the person', key="Age")

    if st.button("Predict Diabetes"):
        try:
            Pregnancies = float(Pregnancies) if Pregnancies else 0.0
            Glucose = float(Glucose) if Glucose else 0.0
            BloodPressure = float(BloodPressure) if BloodPressure else 0.0
            SkinThickness = float(SkinThickness) if SkinThickness else 0.0
            Insulin = float(Insulin) if Insulin else 0.0
            BMI = float(BMI) if BMI else 0.0
            DiabetesPedigreeFunction = float(DiabetesPedigreeFunction) if DiabetesPedigreeFunction else 0.0
            Age = int(Age) if Age else 0

            input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            prediction = diabetes_model.predict(input_data)[0]

            
            if prediction == 1:
                st.write("The person is likely to have diabetes.")
            else:
                st.write("The person is not likely to have diabetes.")

        except ValueError:
            st.error("Invalid input. Please enter numerical values.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', key="age")  # Add keys!
    with col2:
        sex = st.text_input('Sex', key="sex")
    with col3:
         cp = st.text_input('Chest Pain Type', key="cp")
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', key="trestbps")
    with col2:
        chol = st.text_input('Cholesterol', key="chol")
    with col3:
        fbs = st.text_input('Fasting Blood Sugar', key="fbs")
    with col1:
        restecg = st.text_input('Resting ECG', key="restecg")
    with col2:
        thalach = st.text_input('Max Heart Rate', key="thalach")
    with col3:
         exang = st.text_input('Exercise Induced Angina', key="exang")
    with col1:
        oldpeak = st.text_input('ST Depression', key="oldpeak")
    with col2: 
        slope = st.text_input('Slope of the peak excercise ST segment', key="slope")
    with col3:
        ca = st.text_input('Number of major vessels colored by fluoroscopy', key="ca")
    with col1:
        thal = st.text_input('Thalassemia', key="thal")
    if st.button("Predict Heart Disease"):
        try:
            age = float(age) if age else 0.0
            sex = float(sex) if sex else 0.0
            cp = float(cp) if cp else 0.0
            trestbps = float(trestbps) if trestbps else 0.0
            chol = float(chol) if chol else 0.0
            fbs = float(fbs) if fbs else 0.0
            restecg = float(restecg) if restecg else 0.0
            thalach = float(thalach) if thalach else 0.0
            exang = float(exang) if exang else 0.0
            oldpeak = float(oldpeak) if oldpeak else 0.0
            slope = float(slope) if slope else 0.0
            ca = float(ca) if ca else 0.0
            thal = float(thal) if thal else 0.0
            
            input_data = np.array([['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']])

            prediction = heart_model.predict(input_data)[0]
        except ValueError:
            st.error("Invalid input. Please enter numerical values.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)', key="MDVP_Fo_Hz")  # Add keys!
    with col2:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)', key="MDVP_Fhi_Hz")
    with col3:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)', key="MDVP_Flo_Hz")
    with col1:
        MDVP_Jitter_Percent = st.text_input('MDVP:Jitter(%)', key="MDVP_Jitter_Percent")
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', key="MDVP_Jitter_Abs")
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP', key="MDVP_RAP")
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ', key="MDVP_PPQ")
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP', key="Jitter_DDP")
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer', key="MDVP_Shimmer")
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', key="MDVP_Shimmer_dB")
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3', key="Shimmer_APQ3")
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5', key="Shimmer_APQ5")
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ', key="MDVP_APQ")
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA', key="Shimmer_DDA")
    with col3:
        NHR = st.text_input('NHR', key="NHR")
    with col1:
        HNR = st.text_input 
    if st.button("Predict Parkinsons"):
        try:
            MDVP_Fo_Hz = float(MDVP_Fo_Hz) if MDVP_Fo_Hz else 0.0
            MDVP_Fhi_Hz = float(MDVP_Fhi_Hz) if MDVP_Fhi_Hz else 0.0
            MDVP_Flo_Hz = float(MDVP_Flo_Hz) if MDVP_Flo_Hz else 0.0
            MDVP_Jitter_Percent = float(MDVP_Jitter_Percent) if MDVP_Jitter_Percent else 0.0
            MDVP_Jitter_Abs = float(MDVP_Jitter_Abs) if MDVP_Jitter_Abs else 0.0
            MDVP_RAP = float(MDVP_RAP) if MDVP_RAP else 0.0
            MDVP_PPQ = float(MDVP_PPQ) if MDVP_PPQ else 0.0
            Jitter_DDP = float(Jitter_DDP) if Jitter_DDP else 0.0
            MDVP_Shimmer = float(MDVP_Shimmer) if MDVP_Shimmer else 0.0
            MDVP_Shimmer_dB = float(MDVP_Shimmer_dB) if MDVP_Shimmer_dB else 0.0
            Shimmer_APQ3 = float(Shimmer_APQ3) if Shimmer_APQ3 else 0.0
            Shimmer_APQ5 = float(Shimmer_APQ5) if Shimmer_APQ5 else 0.0
            MDVP_APQ = float(MDVP_APQ) if MDVP_APQ else 0.0
            Shimmer_DDA = float(Shimmer_DDA) if Shimmer_DDA else 0.0
            NHR = float(NHR) if NHR else 0.0
            HNR = float(HNR) if HNR else 0.0
            
            input_data = np.array([['MDVP_Fo_Hz','MDVP_Fhi_Hz','MDVP_Flo_Hz','MDVP_Jitter_Percent','MDVP_Jitter_Abs','MDVP_RAP','MDVP_PPQ','Jitter_DDP','MDVP_Shimmer','MDVP_Shimmer_dB','Shimmer_APQ3','Shimmer_APQ5','MDVP_APQ','Shimmer_DDA','NHR','HNR']])

            prediction = parkinsons_model.predict(input_data)[0]
        except ValueError:
            st.error("Invalid input. Please enter numerical values.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")