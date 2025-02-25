import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_pdf_viewer import pdf_viewer
import base64

#Streamlit code

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: red;'>AIRBNB DATA ANALYSIS</h1>", unsafe_allow_html=True)
st.write("")

with st.sidebar:
    select =option_menu("Main menu",["Home","Data Exploration","About"])

if select == "Home":
    img=Image.open(r"C:\Users\HP\Music\images.jpg")
    img=img.resize((800,300))
    st.image(img)
    st.header("About Airbnb")
    st.write("")
    st.markdown('''- Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays.''')
    st.markdown('''- Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.''')
    st.markdown('''- Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.''')
    st.markdown('''- The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.markdown('''- Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.''')

if select == "Data Exploration":
    pdf_path = r"C:\Users\HP\Downloads\Power Bi.pdf"

    # Convert PDF to base64 encoding
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    # Embed PDF using an HTML iframe with PDF.js
    pdf_display = f"""
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" 
        height="800px"
        style="border: none;">
    </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)

if select == "About":
    st.header("ABOUT THIS PROJECT")

    st.subheader(":orange[1. Data Collection:]")

    st.write('''***Gather data from Airbnb's public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.***''')
    
    st.subheader(":orange[2. Data Cleaning and Preprocessing:]")

    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.***''')
    
    st.subheader(":orange[3. Exploratory Data Analysis (EDA):]")

    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.***''')
    
    st.subheader(":orange[4. Visualization:]")

    st.write('''***Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')
    
    st.subheader(":orange[5. Geospatial Analysis:]")

    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')




