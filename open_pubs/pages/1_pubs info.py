import streamlit as st
import pandas as pd
import numpy as np
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "pubs.csv")

df = pd.read_csv(DATA_PATH)
df.drop(labels='Unnamed: 0',axis=1,inplace=True)

st.title(":red[:champagne: WELCOME TO THE  PUBS IN UK :beer:]")
st.header(":orange[Have some Drink and chillout:beers:]")
df = pd.read_csv(DATA_PATH)
df.drop(labels='Unnamed: 0',axis=1,inplace=True)

#st.dataframe(df)

unique=['Number of Pubs', 'Number of Local Authorities','Number of Postal Code']
option=st.selectbox(label="Select below options to see total count",
                options=unique,label_visibility="visible")

if option=='Number of Pubs':
    st.subheader(f":red[Total Pubs in UK:] :blue[{df['name'].nunique()}]")
elif option=='Number of Postal Code':
    st.subheader(f":red[Total Post Codes in UK:] :blue[{df['postcode'].nunique()}]")
else:
    st.subheader(f":red[Total Local Authorities in UK:] :blue[{df['local_authority'].nunique()}]")

def show_statistics():
   
    statistics = df.describe()
    st.write("Descriptive statistics:")
    st.dataframe(statistics)
if st.button("Describe data"):
    show_statistics()

page_bg_img = '''
<style>
.stApp {
background-image: url("https://c8.alamy.com/comp/W1F1K8/set-with-different-cocktails-on-a-bar-lights-background-W1F1K8.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)