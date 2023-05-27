# Import libraries
######################
import numpy as np
import pandas as pd
import streamlit as st
import joblib
from PIL import Image
from rdkit import Chem
from rdkit.Chem import Descriptors
import requests
import io
import sys
import path
######################
# Custom function
######################
## Calculate molecular descriptors
def AromaticProportion(m):
  aromatic_atoms = [m.GetAtomWithIdx(i).GetIsAromatic() for i in range(m.GetNumAtoms())]
  aa_count = []
  for i in aromatic_atoms:
    if i==True:
      aa_count.append(1)
  AromaticAtom = sum(aa_count)
  HeavyAtom = Descriptors.HeavyAtomCount(m)
  AR = AromaticAtom/HeavyAtom
  return AR

def generate(smiles, verbose=False):

    moldata= []
    for elem in smiles:
        mol=Chem.MolFromSmiles(elem)
        moldata.append(mol)

    baseData= np.arange(1,1)
    i=0
    for mol in moldata:

        desc_MolLogP = Descriptors.MolLogP(mol)
        desc_MolWt = Descriptors.MolWt(mol)
        desc_NumRotatableBonds = Descriptors.NumRotatableBonds(mol)
        desc_AromaticProportion = AromaticProportion(mol)

        row = np.array([desc_MolLogP,
                        desc_MolWt,
                        desc_NumRotatableBonds,
                        desc_AromaticProportion])

        if(i==0):
            baseData=row
        else:
            baseData=np.vstack([baseData, row])
        i=i+1

    columnNames=["MolLogP","MolWt","NumRotatableBonds","AromaticProportion"]
    descriptors = pd.DataFrame(data=baseData,columns=columnNames)
    return descriptors

######################
# Page Title
######################


url_icon="https://github.com/dhiraj1008/Streamlit_apps-data_science-/blob/main/app7_molecular_solubility_regression/solubility-logo.jpg?raw=true"
response = requests.get(url_icon)
image = Image.open(io.BytesIO(response.content))
newimage=image.resize((500,200))
"""
st.image(newimage,use_column_width=True)
image = Image.open('solubility-logo.jpg')
"""
st.image(image, use_column_width=True)

st.write("""
# Molecular Solubility Prediction Web App
This app predicts the **Solubility (LogS)** values of molecules!
Data obtained from the John S. Delaney. [ESOL:  Estimating Aqueous Solubility Directly from Molecular Structure](https://pubs.acs.org/doi/10.1021/ci034243x). ***J. Chem. Inf. Comput. Sci.*** 2004, 44, 3, 1000-1005.
***
""")


######################
# Input molecules (Side Panel)
######################

st.sidebar.header('User Input Features')

## Read SMILES input
SMILES_input = "NCCCC\nCCC\nCN"

SMILES = st.sidebar.text_area("SMILES input", SMILES_input)
SMILES = "C\n" + SMILES #Adds C as a dummy, first item
SMILES = SMILES.split('\n')

st.header('Input SMILES')
SMILES[1:] # Skips the dummy first item

## Calculate molecular descriptors
st.header('Computed molecular descriptors')
X = generate(SMILES)
X[1:] # Skips the dummy first item

######################
# Pre-built model
######################


dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# load model
path_to_model = 'linearregressionmodel.joblib'


with open(path_to_model, 'rb') as file:
    model = joblib.load(file)
# Reads in saved model
#load_model = joblib.load("linearregressionmodel.joblib")

# Apply model to make predictions
prediction = load_model.predict(X)
#prediction_proba = load_model.predict_proba(X)

st.header('Predicted LogS values')
prediction[1:] # Skips the dummy first item
