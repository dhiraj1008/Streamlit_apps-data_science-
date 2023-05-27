import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
import joblib
import matplotlib.pyplot as plt
import seaborn as sb
import sys
import path
st.write("""
# Boston House Price Prediction App
This app predicts the **Boston House Price**!
""")
st.write('---')

# Loads the Boston House Price Dataset
boston = pd.read_csv("app9_Boston_HouseP_regression/Building_model/BostonHousing.csv")
X=boston.drop('medv',axis=1)
Y=boston['medv']
# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    crim = st.sidebar.slider('crim',float(X.crim.min()), float(X.crim.max()), float(X.crim.mean()))
    zn = st.sidebar.slider('zn', float(X.zn.min()), float(X.zn.max()), float(X.zn.mean()))
    indus = st.sidebar.slider('indus', float(X.indus.min()), float(X.indus.max()), float(X.indus.mean()))
    chas = st.sidebar.slider('chas', float(X.chas.min()), float(X.chas.max()), float(X.chas.mean()))
    nox = st.sidebar.slider('nox', float(X.nox.min()), float(X.nox.max()), float(X.nox.mean()))
    rm = st.sidebar.slider('rm', float(X.rm.min()), float(X.rm.max()), float(X.rm.mean()))
    age = st.sidebar.slider('age', float(X.age.min()), float(X.age.max()), float(X.age.mean()))
    dis = st.sidebar.slider('dis', float(X.dis.min()), float(X.dis.max()), float(X.dis.mean()))
    rad = st.sidebar.slider('rad', float(X.rad.min()), float(X.rad.max()), float(X.rad.mean()))
    tax = st.sidebar.slider('tax', float(X.tax.min()), float(X.tax.max()), float(X.tax.mean()))
    ptratio = st.sidebar.slider('ptratio', float(X.ptratio.min()), float(X.ptratio.max()), float(X.ptratio.mean()))
    b = st.sidebar.slider('b', float(X.b.min()), float(X.b.max()), float(X.b.mean()))
    lstat = st.sidebar.slider('lstat', float(X.lstat.min()), float(X.lstat.max()), float(X.lstat.mean()))
    # converted to float due to streamlit complains about the min() and max() returning int64 instead of int and we get this when we apply function on object of wrong type..!
    data = {'crim': crim,
            'zn': zn,
            'indus': indus,
            'chas': chas,
            'nox': nox,
            'rm': rm,
            'age': age,
            'dis': dis,
            'rad': rad,
            'tax': tax,
            'ptratio': ptratio,
            'b': b,
            'lstat': lstat}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')


# Reads in saved classification model
dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# load model
path_to_model = "app9_Boston_HouseP_regression/Building_model/modelBoston.joblib"


with open(path_to_model, 'rb') as file:
    load_clf = joblib.load(file)
# Reloading Regression model
#model = joblib.load("Building_model\\modelBoston.joblib")
# Apply Model to Make Prediction
prediction = model.predict(df)

st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')

# How these features plus MEDV distributions look like 
st.header("Gaphs:")
fig,axs=plt.subplots(ncols=7,nrows=2,figsize=(20,10))
axs=axs.flatten()
index=0
for k,v in boston.items():
    sb.distplot(v,ax=axs[index])
    index+=1

    #st.pyplot(plt.show())

    
plt.tight_layout(pad=0.9,w_pad=1,h_pad=3)
st.pyplot(fig)


