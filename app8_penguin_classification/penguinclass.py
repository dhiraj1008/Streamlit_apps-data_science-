import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib
import path
import sys
st.write("""
# Penguin Prediction App

his app predicts the **Palmer Penguin** species!
Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
"""
)

st.sidebar.header("User Input Features")
st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# Collects the user input features into dataframe 

uploaded_file = st.sidebar.file_uploader("Upload your input csv file",type=["csv"])
if uploaded_file!=None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
        sex = st.sidebar.selectbox('Sex',('male','female'))
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
        body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
        data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
        features=pd.DataFrame(data,index=[0])
        return features
    
    input_df=user_input_features()
    
#Combine User input features with entire penguins dataset
# This will be usefull for the encoding phase
penguin_raw=pd.read_csv('penguins_cleaned.csv')
penguin=penguin_raw.drop(columns=['species'])
df = pd.concat([input_df,penguin],axis=0)
st.dataframe(df)

# Encoding of ordinal features

encode=['sex','island']

for col in encode:
    #Convert categorical variable into dummy/indicator variables.
    dummy=pd.get_dummies(df[col],prefix=col)
    df=pd.concat([df,dummy],axis=1)
    del df[col]

df=df[:1]#selects only the first row(the user input)


# Displays the user input features
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)

# Reads in saved classification model
dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# load model
path_to_model = "app7_molecular_solubility_regression/linearregressionmodel.joblib"


with open(path_to_model, 'rb') as file:
    load_clf = joblib.load(file)
#load_clf = joblib.load("app8_penguin_classification/modelpenguinclass.joblib")
# Apply model to make predictions
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)
st.subheader('Prediction')
penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.write(penguins_species[prediction])


st.subheader('Prediction Probability')
st.write(prediction_proba)
