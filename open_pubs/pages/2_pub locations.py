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


st.title(" :red[Locations of all the Pubs in UK :beer:] ")

unique=['Post Code', 'Local Authority',"ALL"]

option=st.selectbox(label="Select Below Option to See the Available Pubs",
                options=unique)

if option=='Post Code':
    selected=st.selectbox(label='Select the PostCode',options=df['postcode'].unique())
    st.subheader(f"Total Pubs Found : {df[df['postcode']==selected].shape[0]}")
    st.map(data=df[df['postcode']==selected],  use_container_width=True)
elif option=='Local Authority':
    selected=st.selectbox(label='Select Local Authority',options=df['local_authority'].unique())
    st.subheader(f"Total Pubs Found : {df[df['local_authority']==selected].shape[0]}")
    st.map(data=df[df['local_authority']==selected],  use_container_width=True)
else:
    st.subheader(f"Total Pubs Found : {df.shape[0]}")
    st.map(data=df,  use_container_width=True)
page_bg_img = '''
<style>
.stApp {
background-image: url("https://c8.alamy.com/comp/W1F1K8/set-with-different-cocktails-on-a-bar-lights-background-W1F1K8.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)



