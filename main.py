import streamlit as st
import pickle

model = pickle.load(open("diabetes.sav",'rb'))

st.title('Diabetes Prediction')

col1,col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('No of Pregnancies')

with col2:
    Glucose = st.text_input('Glucose Level')

with col1:
        BloodPressure = st.text_input('Blood Pressure value')
    
with col2:
    SkinThickness = st.text_input('Skin Thickness value')
    
with col1:
    Insulin = st.text_input('Insulin Level')
    
with col2:
    BMI = st.text_input('BMI value')
    
with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
with col2:
    Age = st.text_input('Age of the Person')
    
# Prediction

diab_dignosis = '' # empty string to save the end result

# creating a button
if st.button('Submit'):
    diag_pred = model.predict([[Pregnancies,Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if (diag_pred[0] == 1):
        diab_dignosis = 'The Person is Diabetic'
    else:
        diab_dignosis = 'The Person is Non Diabetic'

st.success(diab_dignosis) 