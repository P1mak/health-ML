import streamlit as st
import pickle
from PIL import Image
import joblib

st.set_page_config(
   page_title="Health Horizon",
   page_icon= "activity",
   layout="wide",
   initial_sidebar_state="expanded",
)

with open('C:/Users/Pawan/Downloads/diabetes.pkl', 'rb') as model_file:
    diabetes_model = pickle.load(model_file)

heart_disease_model = joblib.load(open('C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Models/heart.pkl','rb'))

Breast_Cancer_model = joblib.load(open('C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Models/breast_cancer.pkl', 'rb'))

kidney_model = joblib.load(open('C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Models/kidney.pkl', 'rb'))

liver_model = joblib.load(open('C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Models/liver .pkl', 'rb'))

parkinsons_model = joblib.load(open('C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Models/parkinsons_model.pkl', 'rb'))


def home_scr():
    col1, col2 = st.columns([3, 1])

    with col1:
        st.write('Multiple diseases prediction using machine learning involves the use of various algorithms and techniques to analyze medical data and identify patterns and relationships that can help predict the likelihood of a patient developing multiple diseases. These algorithms can be trained using various types of medical data, such as genetic data, clinical data, and imaging data, to build predictive models that can identify patients at risk of developing certain diseases.')
        st.write('The process of multiple diseases prediction using machine learning typically involves data pre-processing, feature extraction, model training, model evaluation, and prediction. In the pre-processing phase, the medical data is cleaned and prepared for analysis. In the feature extraction phase, relevant features are extracted from the data that can help in predicting the likelihood of a patient developing multiple diseases. In the model training phase, various machine learning algorithms are used to train predictive models using the extracted features. In the model evaluation phase, the performance of the trained models is assessed using various evaluation metrics. Finally, in the prediction phase, the trained models are used to predict the likelihood of a patient developing multiple diseases based on their medical data.')
        st.write('Multiple diseases prediction using machine learning has the potential to significantly improve the accuracy and efficiency of disease diagnosis and treatment. It can also help in identifying patients at risk of developing multiple diseases at an early stage, enabling early intervention and prevention.')
        
    with col2:
        image = Image.open('C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Img/Doctors-cuate.png')
        st.image(image)
        
    st.markdown("""---""")
    
    col1, col2 = st.columns([1, 3])

    with col1:
        image = Image.open("C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Img/Visual data-bro.png")
        st.image(image)
    with col2:
        
        st.subheader('Models with their Accuracy of Prediction')
        st.markdown('Diabetes Prediction = > 74.02%')
        st.markdown('Breast Cancer Prediction = > 96.49%')
        st.markdown('Heart Disease Prediction = > 86.89%')
        st.markdown('Parkinsons Prediction = > 87%')
        st.markdown('Kidney Disease Prediction = > 100%')
        st.markdown('Liver Disease Prediction = > 77.97%')
        
    st.markdown("""---""")
    
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("Diabetes")
        st.write("Diabetes mellitus refers to a group of diseases that affect how your body uses blood sugar (glucose). Glucose is vital to your health because it's an important source of energy for the cells that make up your muscles and tissues. It's also your brain's main source of fuel. The underlying cause of diabetes varies by type. But, no matter what type of diabetes you have, it can lead to excess sugar in your blood. Too much sugar in your blood can lead to serious health problems.")
        st.write()
        st.subheader("Symptoms")
        st.markdown('_= > Increased Thirst_')
        st.markdown('_= > Frequent Urination_')
        st.markdown('_= > Extreme Hunger_')
        
        
    with col2:
        image = Image.open("C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Img/Diabetes-cuate.png")
        st.image(image)
    
    st.markdown("""---""")
    
    col1, col2 = st.columns([1, 3])

    with col1:
        image = Image.open("C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Img/Cardiologist-rafiki.png")
        st.image(image)
    with col2:
        
        st.subheader("Heart Disease")
        st.write("Heart Disease refers to a group of diseases that affect the heart and blood vessels of your body. These diseases can affect one or many parts of your heart and /or blood vessels. A person may be symptomatic (physically experience the disease) or be asymptomatic (not feel anything at all).")
        st.write()
        st.subheader("Symptoms")
        st.markdown('_= > Pounding or racing heart (palpitations)_')
        st.markdown('_= > Chest pain_')
        st.markdown('_= > Sweating_')
        
    st.markdown("""---""")
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("Breast Cancer")
        st.write("Breast cancer is a type of cancer that starts in the breast. It can start in one or both breasts. After skin cancer, breast cancer is the most common cancer diagnosed in women in the United States. Breast cancer can occur in both men and women, but it's far more common in women.")
        st.write()
        st.subheader("Symptoms")
        st.markdown('_= > New lump in the breast or underarm (armpit)_')
        st.markdown('_= > Thickening or swelling of part of the breast_')
        st.markdown('_= > Irritation or dimpling of breast skin_')
        
        
    with col2:
        image = Image.open("C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Img/Breast cancer research-rafiki.png")
        st.image(image)
    
    st.markdown("""---""")
    
    col1, col2 = st.columns([1, 3])

    with col1:
        image = Image.open("C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Img/CT scan-amico.png")
        st.image(image)
    with col2:
        
        st.subheader("Parkinson's Disease")
        st.write("Parkinson's disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly. The first symptom may be a barely noticeable tremor in just one hand. Tremors are common, but the disorder may also cause stiffness or slowing of movement.")
        st.write()
        st.subheader("Symptoms")
        st.markdown('_= > Tremor while muscles are at rest_')
        st.markdown('_= > Blinking less often than usual_')
        st.markdown('_= > Cramped or small handwriting_')
        
    st.markdown("""---""")
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("Kidney Disease")
        st.write("Chronic kidney disease (CKD) means your kidneys are damaged and can’t filter blood the way they should. The disease is called “chronic” because the damage to your kidneys happens slowly over a long period of time. This damage can cause wastes to build up in your body. CKD can also cause other health problems.")
        st.write()
        st.subheader("Symptoms")
        st.markdown('_= > Nausea_')
        st.markdown('_= > Vomiting_')
        st.markdown('_= > Fatigue and weakness_')
        
        
    with col2:
        image = Image.open("C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Img/World Hepatitis Day-bro.png")
        st.image(image)
    
    st.markdown("""---""")
    
    col1, col2 = st.columns([1, 3])

    with col1:
        image = Image.open("C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/Img/liver.png")
        st.image(image)
    with col2:
        
        st.subheader("Liver Disease")
        st.write("The term “liver disease” refers to any of several conditions that can affect and damage your liver. Over time, liver disease can cause cirrhosis (scarring). As more scar tissue replaces healthy liver tissue, the liver can no longer function properly. Left untreated, liver disease can lead to liver failure and liver cancer.")
        st.write()
        st.subheader("Symptoms")
        st.markdown('_= > Abdominal (belly) pain (especially on the right side)_')
        st.markdown('_= > Bruising easily_')
        st.markdown('_= > Changes in the color of your urine or stool_')
        
    st.markdown("""---""")
     
def about_us():
    st.title('About Us')
    st.write('We are a team of developers who are passionate about creating software that makes a difference. Our goal is to provide the best user experience possible and to make technology accessible to everyone.')
    st.write('We love to work with the latest technologies and are constantly looking for new ways to innovate. We believe in collaboration, creativity, and continuous learning.')
    st.write('If you have any questions or feedback, please feel free to reach out to us at pawankumar212003@gmail.com.')    


def contact_us():
    st.header(":mailbox: Get In Touch With Me!")
    contact_form = """<form action="https://formsubmit.co/codeinlastbench@gmail.com" method="POST"><input type="hidden" name="_captcha" value="false"><input type="text" name="Name" placeholder="Your name" required><input type="email" name="Email" placeholder="Your email" required><textarea name="Message" placeholder="Your message here"></textarea><button type="submit">Send</button></form>"""
    st.markdown(contact_form, unsafe_allow_html=True)

 # Use Local CSS File
def local_css(file_name):
     with open(file_name) as f:
         st.markdown(f"<style>{f.read()}<C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/style/style.css>", unsafe_allow_html=True)

local_css("C:/Users/Pawan/Downloads/Health-Horizons-main/Health-Horizons-main/style/style.css")
    

def footer():
    # Define the footer section
    st.write("")
    st.write("---")
    st.markdown('<p style="text-align:center">© 2023 MDPS: All rights reserved.</p>', unsafe_allow_html=True)
    
    

def diabetes():
    st.header("Diabetes Prediction")
    # page title
    #st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          st.success('The person is diabetic')
        else:
          st.error('The person is not diabetic')
        

def heart():
    st.header("Heart Disease Prediction")
    # page title
    #st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 3 = normal; 6 = fixed defect; 7 = reversable defect')
        
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          st.success('The person is having heart disease')
        else:
          st.error('The person does not have any heart disease')
        

def parkinsion():
    st.header("Parkinsons Prediction")
    # page title
    #st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          st.success("The person has Parkinson's disease")
        else:
          st.error("The person does not have Parkinson's disease")
        
    
def brest_cancer():
    st.header("Breast Cancer Prediction")
    # page title
    #st.title("Breast Cancer Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        rm = st.text_input('Radius Mean')
        
    with col2:
        tm = st.text_input('Texture Mean')
        
    with col3:
        pm = st.text_input('Perimeter Mean')
        
    with col4:
        am = st.text_input('Area Mean')
        
    with col5:
        smm = st.text_input('Smoothness Mean')
        
    with col1:
        compm = st.text_input('Compactness Mean')
        
    with col2:
        concm = st.text_input('Concavity Mean')
        
    with col3:
        cpm = st.text_input('Concave Points Mean')
        
    with col4:
        sym = st.text_input('Symetry Mean')
        
    with col5:
        rs = st.text_input('Radius Se')
        
    with col1:
        ps = st.text_input('Perimeter Se')
        
    with col2:
        ars = st.text_input('Area Se')
        
    with col3:
        comps = st.text_input('Compactness Se')
        
    with col4:
        concs = st.text_input('Concavity Se')
        
    with col5:
        cps = st.text_input('Concave Point Se')
        
    with col1:
        fds = st.text_input('Fractal Dimension Se')
        
    with col2:
        rw = st.text_input('Radius Worst')
        
    with col3:
        tw = st.text_input('Texture Worst')
        
    with col4:
        pw = st.text_input('Perimeter Worst')
        
    with col5:
        arw = st.text_input('Area Worst')
        
    with col1:
        smw = st.text_input('Smoothness Worst')
        
    with col2:
        compw = st.text_input('Compactness Worest')
        
    with col3:
        concw = st.text_input('Concavity Worest')
        
    with col4:
        cpw = st.text_input('Concave Points Worest')
        
    with col5:
        sw = st.text_input('Symmetry Worest')
        
    with col1:
        fdw = st.text_input('Fractal Dimension Worest')
        

    
    # creating a button for Prediction    
    if st.button("Breast Cancer's Test Result"):
        breast_cancer_prediction = Breast_Cancer_model.predict([[rm, tm, pm, am, smm, compm, concm, cpm, sym, rs, ps, ars, comps, concs, cps, fds, rw, tw, pw, arw, smw, compw, concw, cpw, sw, fdw]])                          
        
        if (breast_cancer_prediction[0] == 1):
          st.success("The person has Breast Cancer's disease")
        else:
          st.error("The person does not have Breast Cancer's disease")
        
    
    
def kidney():
    st.header("Kidney Disease Predictor")
    # page title
    #st.title("Kidney Disease Predictor using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        kage = st.text_input('Age of Patient')
        
    with col2:
        bp = st.text_input('Blood Presure')
        
    with col3:
        al = st.text_input('Albumin')
        
    with col4:
        su = st.text_input('Sugar')
        
    with col5:
        rbc = st.text_input('Red Blood Cells')
        
    with col1:
        pc = st.text_input('Pus Cells')
        
    with col2:
        pcc = st.text_input('Pus Cell Clumps')
        
    with col3:
        ba = st.text_input('Bacteria')
        
    with col4:
        bgr = st.text_input('Blood Glucose Random')
        
    with col5:
        bu = st.text_input('Blood Urea')
        
    with col1:
        sc = st.text_input('Serum Creatinine')
        
    with col2:
        pot = st.text_input('Potassium ')
        
    with col3:
        wc = st.text_input('White Blood Cell Count')
        
    with col4:
        htn = st.text_input('Hypertension')
        
    with col5:
        dm = st.text_input('Diabetes Mellitus')
        
    with col1:
        cad = st.text_input('Coronary Artery Disease')
        
    with col2:
        pe = st.text_input('Pedal Edema')
        
    with col3:
        ane = st.text_input('Anemia')
           
    
 
    
    # creating a button for Prediction    
    if st.button("Kidney's Test Result"):
        kidney_prediction = kidney_model.predict([[kage, bp, al, su, rbc, pc, pcc, ba, bgr, bu, sc, pot, wc, htn, dm, cad, pe, ane]])                          
        
        if (kidney_prediction[0] == 1):
          st.success("The person has Kidney's disease")
        else:
          st.error("The person does not have Kidney's disease")
        
    
def liver():
    st.header("Liver Disease Prediction")
    # page title
    #st.title('Liver Disease Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age Of Person')
        
    with col2:
        t_bili = st.text_input('Total Bilirubin')
    
    with col3:
        d_bili = st.text_input('Direct Bilirubin')
    
    with col1:
        alk_phos = st.text_input('Alkaline Phosphotase')
    
    with col2:
        sgpt = st.text_input('Alamine Aminotransferase')
    
    with col3:
        sgot = st.text_input('Aspartate Aminotransferase')
    
    with col1:
        tot_pro = st.text_input('Total Protiens')
    
    with col2:
        albu = st.text_input('Albumin Of Patients')
        
    with col3:
        ag_ratio = st.text_input('Albumin and Globulin Ratio')
    
    with col1:
        g = st.text_input('Gender')
    
    
    
    # creating a button for Prediction
    
    if st.button('Liver Test Result'):
        liver_prediction = liver_model.predict([[age, t_bili, d_bili, alk_phos, sgpt, sgot, tot_pro, albu, ag_ratio, g]])
        
        if (liver_prediction[0] == 1):
          st.success("The person have Kidney's disease")
        else:
          st.error("The person does not have Kidney's disease")


tab1, tab2, tab3, tab4 = st.tabs(["Home","Health Screen", "About Us", "Contact Us"])

with tab1:
    home_scr()
    

with tab2:
    st.markdown('<p style="text-align:center">Which Disease do you want to Test?</p>', unsafe_allow_html=True)
    option = st.selectbox('',("None","Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction", "Breast Cancer Prediction", "Kidney Disease Prediction", "Liver Disease Prediction")
    )

    if option == "None":
        st.empty()
        
    elif option == "Diabetes Prediction":
        diabetes()
        
    elif option == "Heart Disease Prediction":
        heart()
        
    elif option == "Parkinsons Prediction":
        parkinsion()

    elif option == "Breast Cancer Prediction":
        brest_cancer()

    elif option == "Kidney Disease Prediction":
        kidney()
        
    else:
        liver()
        
with tab3: 
   about_us()
   
   
with tab4:
     contact_us()
     
footer()
