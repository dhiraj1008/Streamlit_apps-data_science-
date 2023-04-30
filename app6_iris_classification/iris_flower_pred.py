#here we are gone include machine learning capabilities inti the web application
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App

This app predicts the iris flower type !
""")

st.sidebar.header("User Input Parameters")

def user_input_features():
    sepal_length = st.sidebar.slider("smpal_length",4.3,7.9,5.4)
    sepal_width = st.sidebar.slider("sepal_width",2.8,4.4,3.4)
    petal_length= st.sidebar.slider("petal_length",1.0,2.5,0.2)
    petal_width=st.sidebar.slider("petal_width",0.1,2.5,0.2)    
    data = pd.DataFrame( {
        'sepal_length':sepal_length,
        'sepal_width':sepal_width,
        'petal_length':petal_length,
        'petal_width':petal_width
    ,},index=[0]
    )
    return data 

df = user_input_features()

st.subheader("User Input parameters")
st.write(df)

iris=datasets.load_iris()
x=iris.data
y=iris.target
x
y
clf = RandomForestClassifier()
clf.fit(x,y)

prediction = clf.predict(df)

prediction_probs = clf.predict_proba(df)

st.subheader("Class labels and their corresponding index number")
st.write(iris.target_names)


st.subheader("Prediction")
st.write(iris.target_names[prediction])

st.subheader("Prediction Probability")
st.write(prediction_probs)

