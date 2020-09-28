import streamlit as st
from streamlit_folium import folium_static

import folium
import pandas

from folium import plugins

import streamlit as st

import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('robi_t.png')

#st.set_option('deprecation.showfileUploaderEncoding', False)

#file = st.file_uploader("Upload CSV",type=["csv"])

st.title("DSR route plan")
st.subheader("Analyzing GIS data to optimize DSR route plan and thus recommend DSR allocation")
data = pandas.read_csv("retailer.csv")
st.title("Demo Dataset")
st.dataframe(data)



from folium.plugins import MeasureControl

map_robi = folium.Map(location=[23.737054, 90.369061], zoom_start=100)
st.title("Map")
folium_static(map_robi)
i=1
for (index, row) in data.iterrows():
    folium.CircleMarker(location=[row.loc['lat'], row.loc['long']], 
                  popup='Retailer shop:'+str(row.loc['sr']) ,color='black',
                  tooltip='click').add_to(map_robi)
  
map_robi.add_child(MeasureControl())
st.title("Retailer Shops")
st.subheader("Click on the following buttons for visualizing the retailer shops")
if st.button("Click"):
    folium_static(map_robi)
st.title("Routes")
st.subheader("By continously clicking on the following button route between one retailer shop to another retailer shop will be visible.[Note:First the first time click on the reset button]")
st.subheader("Red marker is the starting point and green is the last point")
if st.button("Add line"):
    file1 = open("tusher.txt","r")
    count = file1.read()
    c = int(count)
    c += 1
    file1.close()
    df=pandas.read_csv('location.csv')
    if c > 0:
    	
        file2 = open("tusher.txt","w")
        s = str(c)
        file2.write(s)
        
        lst=[] 
        for i in range(0,c):
          lat = df['lat'].values[i]
          lng = df['long'].values[i]
          val=[lat,lng]
          
          
          lst.append(val)
          
        p1 = df['timestamp'].values[c-1]
        p2 = df['p2p'].values[c-1]
        p3 = df['elapsed_time'].values[c-1]
        p4 = df['elapsed_distance'].values[c-1]
        st.sidebar.title("DSR-1")
        st.sidebar.subheader("Timestamp:")
        st.sidebar.write(p1)
        st.sidebar.subheader("Point to point Distance:")
        st.sidebar.write(p2)
        st.sidebar.subheader("Elapsed Time:")
        st.sidebar.write(p3)
        st.sidebar.subheader("Elapsed Distance:")
        st.sidebar.write(p4)

        map_robi = folium.Map(location=val, zoom_start=100)
        folium.Marker(
        location=[23.737054, 90.369061],
        popup='Start from Here',
        icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(map_robi)
        
        for (index, row) in data.iterrows():
            folium.Marker(location=[row.loc['lat'], row.loc['long']], 
            popup='shop:'+str(row.loc['sr']) , 
            tooltip='click').add_to(map_robi)
        

        # route_lats_longs = [[23.6515, 90.6573], [23.7595, 90.7595]]
        folium.PolyLine(lst).add_to(map_robi)
        plugins.AntPath(lst).add_to(map_robi)
        folium_static(map_robi)
        file2.close()


st.subheader("To do reset click on the reset button")
if st.button("Reset"):
    file3 = open("tusher.txt","w")
    st.write("Now you can add lines again")
    file3.write("0")
    file3.close()


####
df=pandas.read_csv('location.csv')
L2=[]
folium.Map(location=[23.741256, 90.370660], zoom_start=80)
st.subheader("To show the total route click on the following button:")
if st.button("Show total route"):
    st.subheader("Overall Time Served in the Field by DSR: 258.0")
    st.subheader("First to Last Point On Air Distance: 0.419")
    st.subheader("Overall Distance: 2.387")
    st.subheader("Average Time Required to Reach Each Shop by DSR: 11.727")
    st.subheader("Average Distance Between the Shops: 0.108")
    for (index, row) in df.iterrows():
        L2.append([row.loc['lat'], row.loc['long']])
    folium.PolyLine(L2).add_to(map_robi)
    plugins.AntPath(L2).add_to(map_robi)
    folium.Marker(
        location=[23.737054, 90.369061],
        popup='Start from Here',
        icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(map_robi)
    folium_static(map_robi)
    st.sidebar.title("DSR-1")
    st.sidebar.subheader("Distance vs Time")
    from PIL import Image
    img=Image.open("p1.png")
    st.sidebar.image(img,width=300,height=500,caption="Distance vs Time")
    
    st.sidebar.subheader("BoxPlot")
    img1=Image.open("p2.png")
    st.sidebar.image(img1,width=300,height=500,caption="Distance vs Time")
st.subheader("Click on the following buttons for showing Graphs")   
from PIL import Image
if st.button("View Graph"):
        st.subheader("Distance vs Time")
        I1=Image.open("p1.png")
        st.image(I1,width=900,caption="Distance vs Time")
if st.button("View BoxPlot"):
        st.subheader("BoxPlot")
        I2=Image.open("p2.png")
        st.image(I2,caption="BoxPlot")




#import matplotlib.pyplot as plt

#import numpy as np

#arr = np.random.normal(1, 1, size=100)

#plt.hist(arr, bins=20)

#st.sidebar.pyplot()