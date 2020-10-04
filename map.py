import streamlit as st
from streamlit_folium import folium_static

import folium
import pandas

from folium import plugins

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
st.title("DSR route plan")
st.subheader("Analyzing GIS data to optimize DSR route plan and thus recommend DSR allocation")

status = st.radio("Select day:",("day1","day2","day3","day4","day5","day6","day7"))

if status == "day1" :
    data = pandas.read_csv("retailer.csv")
    st.title("Demo Dataset")
    st.dataframe(data)


    from folium.plugins import MeasureControl

    map_robi = folium.Map(location=[23.737054, 90.369061], zoom_start=100)
    st.title("Map")
    folium_static(map_robi)
    i=1
    for (index, row) in data.iterrows():
        folium.Marker(location=[row.loc['lat'], row.loc['long']], 
                      popup='Retailer shop:'+str(row.loc['sr']) ,color='black',
                      tooltip='click').add_to(map_robi)
      
    map_robi.add_child(MeasureControl())
    st.title("Retailer Shops")
    st.subheader("Click on the following buttons for visualizing the retailer shops")
    if st.button("Click"):
        folium.Marker(
                location=[23.741276,90.370660],
                popup='Tower',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            
        folium.Marker(
                location=[23.739567,90.364373],
                popup='Tower',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
        folium.Marker(
                location=[23.736483,90.373235],
                popup='Tower',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
        folium.Marker(
                location=[23.742474,90.376840],
                popup='Tower',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
        folium.Marker(
                location=[23.745931,90.368729],
                popup='Tower',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
        folium.Marker(
                location=[23.737054, 90.369061],
                popup='Start from Here',
                icon=folium.Icon(color='red', icon='info-sign')
                ).add_to(map_robi)
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
        df=pandas.read_csv('location2.csv')
        if c > 0:
            
            file2 = open("tusher.txt","w")
            s = str(c)
            file2.write(s)
            
            lst=[]
            lst2=[] 
            for i in range(0,c):
              lat = df['lat'].values[i]
              lng = df['long'].values[i]
              val=[lat,lng]
              lat1 = df['lat1'].values[i]
              lng1 = df['long1'].values[i]
              if(str(lat1)!="nan"):
                val1=[lat1,lng1]
                lst2.append(val1)    
              
              
              
              lst.append(val)
              
            p1 = df['timestamp'].values[c-1]
            p2 = df['p2p'].values[c-1]
            p3 = df['elapsed_time'].values[c-1]
            p4 = df['elapsed_distance'].values[c-1]


            t1= df['retailer'].values[c-1]
            t2= df['amount'].values[c-1]
            t3= df['distance'].values[c-1]
            t4= df['lat1'].values[c-1]
            t5= df['long1'].values[c-1]

            st.sidebar.title("DSR-1")
            st.sidebar.subheader("Timestamp:")
            st.sidebar.write(p1)
            st.sidebar.subheader("Point to point Distance:")
            st.sidebar.write(p2)
            st.sidebar.subheader("Elapsed Time:")
            st.sidebar.write(p3)
            st.sidebar.subheader("Elapsed Distance:")
            st.sidebar.write(p4)








            if len(str(t1)) > 0 and str(t1) != "nan":
                s = "Send "+str(t2)+"taka to the retailer "+str(t1)+" from distance"+str(t3)+"km, which is located at "+str(t4)+","+ str(t5)
                st.sidebar.write(s) 
            if str(t1) == "nan":
                st.sidebar.write("No transaction")

            map_robi = folium.Map(location=val, zoom_start=100)
            folium.Marker(
            location=[23.737054, 90.369061],
            popup='Start from Here',
            icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(map_robi)

            map_robi = folium.Map(location=val, zoom_start=100)
            folium.Marker(
            location=[23.737839, 90.367806],
            popup='Bank',
            icon=folium.Icon(color='green', icon='info-sign')
            ).add_to(map_robi)


            #map_robi = folium.Map(location=val, zoom_start=100)
            folium.Marker(
            location=[23.741276,90.370660],
            popup='Tower',
            icon=folium.Icon(color='black', icon='info-sign')
            ).add_to(map_robi)


            #some red shops 
            folium.CircleMarker(
                location=[23.737618,90.370107],
                popup='Tower',color='red',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            folium.CircleMarker(
                location=[23.737996,90.371818],
                popup='Tower',color='red',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            folium.CircleMarker(
                location=[23.738792,90.374552],
                popup='Tower',color='red',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            folium.CircleMarker(
                location=[23.74181,90.374214],
                popup='Tower',color='red',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            folium.CircleMarker(
                location=[23.743825,90.369464],
                popup='Tower',color='red',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            folium.CircleMarker(
                location=[23.741125,90.366709],
                popup='Tower',color='red',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            folium.CircleMarker(
                location=[23.739529,90.375468],
                popup='Tower',color='red',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)

            folium.CircleMarker(
                location=[23.74127,90.374472],
                popup='Tower',color='black',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)




            for i in lst2:
              folium.CircleMarker(location=i, 
                      popup='Retailer shop:'+str(row.loc['sr']) ,color='green',
                      tooltip='click').add_to(map_robi)



            folium.Marker(
                location=[23.741276,90.370660],
                popup='Tower',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            
            folium.Marker(
                location=[23.739567,90.364373],
                popup='Tower',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            folium.Marker(
                location=[23.736483,90.373235],
                popup='Tower',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            folium.Marker(
                location=[23.742474,90.376840],
                popup='Tower',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
            folium.Marker(
                location=[23.745931,90.368729],
                popup='Tower',
                icon=folium.Icon(color='black', icon='info-sign')
                ).add_to(map_robi)
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
    df2=pandas.read_csv('location2.csv')
    L2=[]
    folium.Map(location=[23.741256, 90.370660], zoom_start=80)
    st.subheader("To show the total route click on the following button:")
    if st.button("Show total route"):
        st.subheader("Overall Time Served in the Field by DSR: 698.0 minutes")
        st.subheader("First to Last Point On Air Distance: 0.0 km")
        st.subheader("Overall Distance: 4 km")
        st.subheader("Average Time Required to Reach Each Shop by DSR: 32 minutes")
        st.subheader("Average Distance Between the Shops: 0.182 km")
        for (index, row) in df2.iterrows():
            L2.append([row.loc['lat'], row.loc['long']])
        folium.PolyLine(L2).add_to(map_robi)
        plugins.AntPath(L2).add_to(map_robi)

        for (index, row) in df.iterrows():
            L2.append([row.loc['lat'], row.loc['long']])
        folium.PolyLine(L2).add_to(map_robi)
        #plugins.AntPath(L2).add_to(map_robi)

        
       
        folium.Marker(
            location=[23.737839, 90.367806],
            popup='Bank',
            icon=folium.Icon(color='green', icon='info-sign')
            ).add_to(map_robi)
        #tower
        folium.Marker(
            location=[23.741276,90.370660],
            popup='Tower',
            icon=folium.Icon(color='black', icon='info-sign')
            ).add_to(map_robi)
        folium.Marker(
            location=[23.739567,90.364373],
            popup='Tower',
            icon=folium.Icon(color='black', icon='info-sign')
            ).add_to(map_robi)
        folium.Marker(
            location=[23.736483,90.373235],
            popup='Tower',
            icon=folium.Icon(color='black', icon='info-sign')
            ).add_to(map_robi)
        folium.Marker(
            location=[23.742474,90.376840],
            popup='Tower',
            icon=folium.Icon(color='black', icon='info-sign')
            ).add_to(map_robi)
        folium.Marker(
            location=[23.745931,90.368729],
            popup='Tower',
            icon=folium.Icon(color='black', icon='info-sign')
            ).add_to(map_robi)
        folium.Marker(
            location=[23.737054, 90.369061],
            popup='Start from Here',
            icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(map_robi)


        for (index, row) in data.iterrows():
                folium.CircleMarker(location=[row.loc['lat'], row.loc['long']], 
                popup='shop:'+str(row.loc['sr']) ,color='green', 
                tooltip='click').add_to(map_robi)

        folium.CircleMarker(
                location=[23.74127,90.374472],
                popup='Shop:11',color='black',
                icon=folium.Icon(color='yellow', icon='info-sign')
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
if status == "day2" :

    data = pandas.read_csv("retailer.csv")
    st.title("Demo Dataset")
    st.dataframe(data)


    from folium.plugins import MeasureControl

    map_robi = folium.Map(location=[23.737054, 90.369061], zoom_start=100)
    st.title("Map")
    folium_static(map_robi)
    i=1
    for (index, row) in data.iterrows():
        folium.Marker(location=[row.loc['lat'], row.loc['long']], 
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


if status == "day3" :
    st.success("day3")
if status == "day4" :
    st.success("day4")
if status == "day5" :
    st.success("day5")
if status == "day6" :
    st.success("day6")
if status == "day7" :
    st.success("day7")    
