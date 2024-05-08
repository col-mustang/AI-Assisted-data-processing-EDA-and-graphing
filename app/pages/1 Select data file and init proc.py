# Description: This is the second page of the app. It allows the user to upload a csv file to begin the process of creating graphs and performing exploratory data analysis. 
# The user can then proceed to the next page create graphs and explore the data.


import streamlit as st
import pandas as pd
import numpy as np
import os
import io
import pdb
import time




st.set_page_config(
    layout="wide",
    page_title="👋 Initial Processing Screen 👋",
    page_icon="👋"
)

st.write("""### Project 3 ASU AI Course: Automated Graphing and Exploratory Data Analysis
### Page: **Select Data File and Init Proc**

Select csv file. It will upload to a dataframe, df_initial, Then go to "2 Build and Display Graphs"
""")

# initialize variables
if 'file_name' in st.session_state:
    file_name = st.session_state['file_name']

container_1 = st.empty()
with container_1:
    uploaded_file = st.file_uploader("Choose a file")

def get_data_definition(df):
    df_definition = pd.DataFrame(df.dtypes.values, index=df.dtypes.index, columns=["Data Type"]).reset_index()
    df_definition.columns = ["Feature", "Data Type"]
    return df_definition

if uploaded_file is not None:  
    file_name = uploaded_file.name
    st.session_state['file_name'] = file_name
    df_initial = pd.read_csv(uploaded_file, index_col=False)
    st.session_state['new_file'] = True
    st.session_state['df_initial'] = df_initial
    st.session_state['df_initial_loaded'] = True
    st.write(f"#### Working with file :blue[{file_name}]")
    # write out entire dataframe w RAW_ suffix
    dir_and_raw_file_name = "data/" + "RAW_" + file_name
    df_initial.to_csv(dir_and_raw_file_name, index=False)

  
  
if 'df_initial_loaded' in st.session_state and st.session_state['df_initial_loaded']:
    df_definition = get_data_definition(df_initial)
    st.write(f"#### Data Definition for {file_name}")
    st.write("Here is the data definition")
    st.dataframe(df_definition)
    st.write("the data...")
    st.dataframe(df_initial)
    st.session_state['df_definition_loaded'] = True  
    st.session_state['df_definition'] = df_definition
    the_request = st.text_area("Enter your graphing request here")
    st.write("your requested: ", the_request)

    # df.info() does not return anything to python, so need to pipe it
    with st.popover("Summary stats for loaded dataframe"):
        st.write(f"Summary for file {file_name} (dataframe: df_initial)")
        buffer = io.StringIO() 
        df_initial.info(buf=buffer)
        s = buffer.getvalue()  
        st.text(f"#### {s}")
        st.text("\n")
        st.write(f"The shape is: \n{df_initial.shape}")
        st.text(f"dataframe df_initial value_counts...")
        for the_col in df_initial.columns:
            st.text(f"dataframe df_initial value_counts are...\n{df_initial[the_col].value_counts()}")
    
    # container_2 = st.empty()
    # with container_2:
   
    if st.button(":blue[READY: Proceed to 'Preprocessing?] Click to proceed"):
        if len(the_request) > 0:
            st.session_state['the_request'] = the_request
            st.session_state['new_request'] = True
            st.switch_page(("pages/2 create_graphs.py"))
        else:
            st.write("## Please enter a graphing request before proceeding")
   
