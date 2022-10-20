import functions
from telnetlib import X3PAD
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import plotly.graph_objects as go
import streamlit as st  # 🎈 data web app development
import csv

from pandas import *

# general styling and tab name
st.set_page_config(
    page_title="Sampling Studio",
    page_icon="✅",
    layout="wide",
)
 
# title
st.title("Sampling studio")
st.text("Change Your analog Signal into digital & See How the Sampling frequancy affect")
  
#initiating df(dataframe) and empty fig
TOADD_fig= px.density_heatmap(
         data_frame=[{}])
Samp_fig= px.density_heatmap(
         data_frame=[{}])
ADDED_fig= px.density_heatmap(
         data_frame=[{}])

#sidebar components
with st.sidebar:
    # st.title('Generate, reconstruct and sample your signal')
    tab0,tab1, tab2, tab3 = st.tabs(["Generate","Delete", "View" , "Sample"])
    with tab0:
        frq_value =st.number_input('signal frequancy', min_value= 0.0,value=1.0, step=1.0)
        amplitude_value =st.number_input('signal amplitude', min_value= 0.01,value=1.0, step=1.0)
        phase_value     =st.number_input('phase shift', min_value= 0,max_value=360,value=0, step=5)
        snr_value           =st.slider('SNR ratio')        
        # functions.ADD_NOISE(snr_value)
        if st.button('ADD signal'):
            ADDED_fig=functions.ADD_SIGNAL(amplitude_value,phase_value,frq_value)
    with tab1:
        todelete_list=st.multiselect("choose the signal you want to delete",options=["added signals"],key='disabled' ,default=None)
        if st.button(' DELETE signal'):
            ADDED_fig=functions.DELETE_SIGNAL()
    # with tab2:
        # a list of added signals
    with tab3: 
        st.title('max freq =')
        st.write('the sampling freq = sampling factor*max feq')
        samp_factor= st.slider('sampling factor', 0.0 , 20.0 , 2.0, 0.5)


TOADD_fig=functions.SHOW_SIN(amplitude_value,phase_value ,frq_value )
Res_fig=functions.SHOW_ADDED()

#add butthon
# with st.form(key='form1'):
#     freq_toadd=sampfrq_value 
#     amplitude_toadd=amplitude_value 
#     phase_toadd=phase_value 
#     st.form_submit_button(label='ADD signal')

#STREAMLIT COLUMNS AND ROWS 
fig_uploaded,fig_sampled= st.columns((2))
empty1, fig_toadd ,emplty2, empty3 = st.columns((4))
empty1, fig_res ,emplty2, empty3 = st.columns((4))
empty1, fig_sampled ,emplty2, empty3 = st.columns((4))
 
with fig_toadd:
    st.markdown("### Generating a signal")
    st.write(TOADD_fig)
 
with fig_res:
    st.markdown("### Resulted signal")
    st.write(Res_fig)    
 
with fig_sampled:
    st.markdown("### Sampled signal")
    st.write(Samp_fig)
