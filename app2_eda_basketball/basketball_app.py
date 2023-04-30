import streamlit as st
import pandas as pd 
import matplotlib.pylab as plt 
import numpy as np
import seaborn as sb
import base64 # pip install pybase64
# Fundamentally, Base64 is used to encode binary data as printable text. This allows you to transport binary over protocols or mediums that cannot handle binary data formats and require simple text.

st.title("NBA Player Stats Explorer")


st.markdown("""
This app performs simple webscraping of NBA player stats data !
* **Python libraries :** base64,pandas ,streamlit
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com)
""")

st.sidebar.header("User Input Features")
selected_year=st.sidebar.selectbox('Year',list(reversed(range(1950,2023))))

#websraping of nba player stats
# here data is loaded on the fly or on demand not stored on any local server
st.cache(suppress_st_warning=True)
def load_data(year):
    url="https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html=pd.read_html(url,header=0)
    df=html[0]
    filt = df['Age']=='Age'
    player_stats=df.drop(df[filt].index) #remove the redundant data
    player_stats.fillna(0,inplace=True)
    player_stats.drop(['Rk'],axis=1,inplace=True)
    return player_stats

player_stats=load_data(selected_year)
#sidebar -Team selection

teams = sorted(player_stats.Tm.unique())
select_teams = st.sidebar.multiselect("Team",teams,teams)

#slidebar - Position selection
pos=['C','PF',"SF",'PG','SG']
select_position=st.sidebar.multiselect("Position",pos,pos)

# filtering data
df_selected_team = player_stats[(player_stats.Tm.isin(select_teams)) & (player_stats.Pos.isin(select_position))]

st.header("DIsplay Player Stats of Selected Team(s)")
st.write("Data Dimension: "+str(df_selected_team.shape[0])+" rows and "+str(df_selected_team.shape[1]))
st.dataframe(df_selected_team)

#downolad NBA player stats data

def filedownload(df):
    csv = df.to_csv(index=False)
    b64=base64.b64encode(csv.encode()).decode() # string <-> bytes conversion
    href = f"<a href='data:file/csv;base64,{b64}'  download='playerstats.csv'>Download CSV File</a>"
    return href


st.markdown(filedownload(df_selected_team),unsafe_allow_html=True)

# Creating Heatmap
if st.button("Intercorrelation Heatmap"):
    st.header("Intercorrelation Matrix Heatmap")
    df_selected_team.to_csv('output.csv',index=False)
    df=pd.read_csv('output.csv')
    corr=df.corr() #Compute pairwise correlation of columns, excluding NA/null values.
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)]=True
    with sb.axes_style("white"):
        f,ax=plt.subplots(figsize=(7,5))
        ax=sb.heatmap(corr,mask=mask,vmax=1,square=True)
    st.pyplot(f)






