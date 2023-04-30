import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

penguin_data = pd.read_csv("penguinclassificstion\\modelbuild\\penguins_cleaned.csv")


target = 'species'
encode=['sex','island']
df=penguin_data.copy()

for col in encode:
    #Convert categorical variable into dummy/indicator variables.
    dummy=pd.get_dummies(penguin_data[col],prefix=col)
    df=pd.concat([df,dummy],axis=1)
    del df[col]

target_mapper = {'Adelie':0,'Chinstrap':1,'Gentoo':2}
def target_encode(val):
    return target_mapper[val]


df['species']=df['species'].apply(target_encode)
#print(df)

x=df.drop('species',axis=1)
y=df['species']

model=RandomForestClassifier()
model.fit(x,y)

joblib.dump(model,"penguinclassificstion\\modelbuild\\modelpenguinclass.joblib") 
print(x.columns)
print(y)

