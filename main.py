import pickle
import numpy as np
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler
#loading the saved models
diabetes_model= pickle.load(open('trained_model (1).sav','rb'))
heart_disease_model= pickle.load(open('heart_model.sav','rb'))
parkinsons_model= pickle.load(open('parkinsons_model.sav','rb'))

#sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                            icons=['activity','heart','person'],
                           default_index=0) #default index is the page appears when you first open 
    
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using ML')

      #getting the input data from the user
      #columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
       Pregnancies = st.text_input('Number of Pregnancies')
       SkinThickness = st.text_input('Skin Thickness value')
       DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2: 
       Glucose = st.text_input('Glucose Level')
       Insulin = st.text_input('Insulin Level')
       Age = st.text_input('Age of the Person')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        BMI = st.text_input('BMI value')
    
    diab_diagnosis = '' #a null string
    #creating a button for Prediction
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
          
    st.success(diab_diagnosis)

if (selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting Electrocardiographic results')
        oldpeak = st.text_input('ST depression induced by exercise')
        thal=st.text_input('Thalassemia')
    
    with col2:
       sex=st.text_input('Sex')
       col = st.text_input('cholesterol')
       thalach = st.text_input('Maximum Heart Rate achieved')
       slope = st.text_input('Slope of the peak exercise ST segment')

    
    
    with col3:
       cp=st.text_input('Chest Pain types')
       fbs = st.text_input('Fasting Blood Sugar')
       exang = st.text_input('Exercise Induced Angina')
       ca= st.text_input('Number of major vessels colored by fluoroscopy')
        
    heart_diagnosis = '' #a null string
    #creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, col, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person has heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
    
    st.success(heart_diagnosis)

if (selected == 'Parkinsons Prediction'):
    #page title
    st.title('Parkinsons Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
  

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        PPQ = st.text_input('MDVP:PPQ')
        Shimmer_DB = st.text_input('MDVP:Shimmer(dB)')
        MDVP_APQ = st.text_input('MDVP:APQ')
        HNR = st.text_input('HNR')
        spread1 = st.text_input('spread1')
        PPE= st.text_input('PPE')

    
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        Jitter_DDP =st.text_input('Jitter:DDP')
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
        Shimmer_DDA = st.text_input('Shimmer:DDA')
        RPDE = st.text_input('RPDE')
        spread2 = st.text_input('spread2')


    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        RAP = st.text_input('MDVP:RAP')
        Shimmer = st.text_input('MDVP:Shimmer')
        Shimmer_APQ5= st.text_input('Shimmer:APQ5')
        NHR = st.text_input('NHR')
        DFA = st.text_input('DFA')
        D2 = st.text_input('D2')
         
    parkinsons_diagnosis = '' #a null string
    #creating a button for Prediction
    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, Jitter_DDP,
                      Shimmer, Shimmer_DB, Shimmer_APQ3, Shimmer_APQ5,MDVP_APQ, Shimmer_DDA,
                      NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        
        
        parkinsons_prediction = parkinsons_model.predict([user_input])
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"      
         
    st.success(parkinsons_diagnosis)