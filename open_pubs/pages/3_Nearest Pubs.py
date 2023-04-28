import streamlit as st
import pandas as pd
import numpy as np
import os


FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


DATA_PATH = os.path.join(dir_of_interest, "data", "pubs.csv")

df = pd.read_csv(DATA_PATH)
df.drop(labels='Unnamed: 0',axis=1,inplace=True)
st.title(":red[Find The Nearest Pub Location]")
 
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** ( 1 / 2)
 
# Function to calculate K closest points
def kClosest(points, target, K):
    pts = []
    n = len(points)
    d = []
 
    for i in range(n):
        d.append({
            "first": distance(points[i][0], points[i][1], target[0], target[1]),
            "second": i
        })
    

    d = sorted(d, key=lambda l:l["first"])
    
    for i in range(K):
        pt = []
        pt.append(points[d[i]["second"]][0])
        pt.append(points[d[i]["second"]][1])
        pts.append(pt)
   
# Calling DataFrame constructor on list
    df_nearest_loc = pd.DataFrame(pts,columns=['latitude','longitude'])
    st.map(df_nearest_loc)
    
# Driver code
df_geoloc=df[['latitude','longitude']]
points = df_geoloc.values.tolist()

lat = st.number_input(':blue[Enter Latitude] ', min_value=49.892485, max_value=60.764969)
log = st.number_input(':blue[Enter Longitude]',min_value=-7.384525, max_value=1.757763)


target = [lat,log]
K = 5

kClosest(points, target, K)

page_bg_img = '''
<style>
.stApp {
background-image: url("https://c8.alamy.com/comp/W1F1K8/set-with-different-cocktails-on-a-bar-lights-background-W1F1K8.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

