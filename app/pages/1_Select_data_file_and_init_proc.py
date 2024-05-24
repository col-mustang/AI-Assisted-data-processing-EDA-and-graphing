# Description: This is the second page of the app. It allows the user to upload a csv file to begin the process of creating graphs and performing exploratory data analysis. 
# The user can then proceed to the next page create graphs and explore the data.


import streamlit as st
import pandas as pd
import numpy as np
import os
import io
import pdb
import time
from shutil import copyfile
from streamlit_mic_recorder import speech_to_text

st.set_page_config(
    layout="wide",
    page_title="👋 Initial Processing Screen 👋",
    page_icon="👋"
)

st.write("""### Project 3 ASU AI Course: Automated Graphing and Exploratory Data Analysis
### Page: **Select Data File and Init Proc**

Select csv file. It will upload to a dataframe, df_initial, Then go to "2 Build and Display Graphs"
""")


def get_data_definition(df):
    df_definition = pd.DataFrame(df.dtypes.values, index=df.dtypes.index, columns=["Data Type"]).reset_index()
    df_definition.columns = ["Feature", "Data Type"]
    return df_definition

def init_default_graph_file_w_path():
    # copy the 'pages/template/graph_file_template.py' to pages/graph_file_template.py
    copyfile("templates/graph_file_template.py", "pages/3_the_graphs.py")
    st.session_state['graph_file_name_w_path'] = "pages/3_the_graphs.py"
    return "pages/3_the_graphs.py"

def init_new_graph_file_w_path(new_graph_file_name):
    global graph_file_name_w_path
    graph_file_name_w_path = "pages/" + new_graph_file_name
    st.session_state['graph_file_name_w_path'] =  graph_file_name_w_path
    # pdb.set_trace()
    copyfile("templates/graph_file_template.py", graph_file_name_w_path)
    return True, graph_file_name_w_path


def clean_up_graph_f_name(f_name_to_clean):
    # pdb.set_trace()
    if len(f_name_to_clean) == 0:
        st.write("### Using default graph page or last specified. No graph file specified")
        return(False,"")
    first_char = f_name_to_clean[0]
    second_char = f_name_to_clean[1]
    if first_char.isdigit() and second_char == "_":
        if ".py" == f_name_to_clean[(len(f_name_to_clean)-3):].lower():
            return(True, f_name_to_clean)
        else:
            if "." not in f_name_to_clean:
                cleaned_f_name = f_name_to_clean + ".py"
                # could have better error checking here
                return(True, cleaned_f_name)
            else:   # not a good file name
                st.write(f"## Invalid file name: {f_name_to_clean}. Has a '.', but not '.py'. Could not initialize new graph file")
                return(False,"")
    else:
        st.write(f"## Invalid file name: {f_name_to_clean}. Must start with a digit and underscore. Could not initialize new graph file")
        return(False,"")

def speech_recognition(): 
    text = speech_to_text(language='en', use_container_width=True, just_once=False, key='STT')    
    if 'text_received' not in st.session_state:    
        st.session_state['text_received'] = []      
    # text = speech_to_text(language='en', use_container_width=True, just_once=False, key='STT')   
    print(st.session_state)
    if text:    
        st.session_state['text_received'].append(text)  
        for text in st.session_state['text_received']:      
            st.text(text)    
    else:  
        st.write("No text transcribed.") 
## ---- Main Flow -----------

# initialize variables
if 'file_name' in st.session_state:
    file_name = st.session_state['file_name']

container_1 = st.empty()
with container_1:
    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:  
    # zzz should add a conditional. If df_initial_loaded, then why reload. Just get it from the session state.
    st.write(" in select data page; if uploaded_file is not None")
    file_name = uploaded_file.name
    st.session_state['file_name'] = file_name
    df_initial = pd.read_csv(uploaded_file, index_col=False)
    st.session_state['new_file'] = True
    st.session_state['df_initial'] = df_initial
    st.session_state['df_initial_loaded'] = True
    st.write(f"#### Working with file :blue[{file_name}]")
   

  
if 'df_initial_loaded' in st.session_state and st.session_state['df_initial_loaded']:
    # Get and write out the data definition
    df_initial = st.session_state['df_initial']
    df_definition = get_data_definition(df_initial)
    
    st.write("The data from the csv...")
    st.dataframe(df_initial)
    # update session statewith df_definition info
    st.session_state['df_definition_loaded'] = True  
    st.session_state['df_definition'] = df_definition

    # present pop up options for summary stats
    col1, col2 = st.columns(2)
    with col1:
        with st.popover("Summary stats: dataframe info"):
            st.write(f"Summary for file {file_name} (dataframe: df_initial)")
            buffer = io.StringIO() 
            df_initial.info(buf=buffer)
            s = buffer.getvalue()  
            st.text(f"#### {s}")
    with col2:
        with st.popover("Summary stats: shape and value_counts"):
            st.text("\n")
            st.write(f"The shape is: \n{df_initial.shape}")
            st.text(f"dataframe df_initial value_counts...")
            for the_col in df_initial.columns:
                st.text(f"dataframe df_initial value_counts are...\n{df_initial[the_col].value_counts()}")
    
    
    # if not defined, set up the graph file
    if 'graph_file_name_w_path' not in st.session_state:
        graph_file_name_w_path = init_default_graph_file_w_path() 
        # next line is redundant. It is set in the function call
        st.session_state['graph_file_name_w_path'] = graph_file_name_w_path
        graph_file_bool = True
    else:
        graph_file_name_w_path = st.session_state['graph_file_name_w_path']
        graph_file_bool = True

    # provide opportunity to change the graph file name
    new_graph_file_name = ""   # initialize to empty string
    new_graph_file_name = st.text_input("If you need a new graph file, enter the new file name (start with a digit and underscore like 3_the_graphs.py)")
    new_graph_file_bool, new_graph_file_name = clean_up_graph_f_name(new_graph_file_name)
    if new_graph_file_bool and (len(new_graph_file_name) > 0) and (graph_file_name_w_path != "pages/" + new_graph_file_name):
        # pdb.set_trace()
        new_graph_file_name_w_path = "pages/" + new_graph_file_name
        st.write(f"The new graph file is: {new_graph_file_name}")
        new_graph_file_bool2, new_graph_file_name_w_path = init_new_graph_file_w_path(new_graph_file_name)
        if new_graph_file_bool2:
            graph_file_name_w_path = new_graph_file_name_w_path   
            st.session_state['graph_file_name_w_path'] = graph_file_name_w_path
            graph_file_bool = True
        else:
            st.write(f"### Could not initialize new graph file! {new_graph_file_name} is invalid. No change made")
            graph_file_name_w_path = st.session_state['graph_file_name_w_path'] 
            graph_file_bool = True

    if graph_file_bool:
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"#### Data Definition for {file_name}")
            st.dataframe(df_definition)
        # Get the graphing request
        the_request = ""  # initialize first to empty string
        with col2:
            st.write("Enter your graphing request here")
            
            the_request = st.text_area("")
            st.write("### Or use voice input")
            
            with st.form(key='my_form'):
                if st.form_submit_button("Click to open. Click again to submit recording."):
                    speech_recognition()
            
            if 'text_received' in st.session_state and st.session_state['text_received']:
                text = st.session_state['text_received'][-1]
                if isinstance(text, str) and len(text) > 0:
                    st.session_state['voice_request'] = text
                    st.write(f"Recorded Request: {text}")
                    the_request = text  # Use the voice input as the request
            
            if len(the_request) > 0:
                st.session_state['the_request_from_select_data'] = the_request
                st.session_state['request_from_select_data_bool'] = True
                if st.button("Request received... :blue[Click to produce graph(s)]"):
                    st.session_state['new_request'] = True
                    st.switch_page("pages/2_create_graphs.py")
    else:
        st.write("### Could not initialize new graph file!")
       
   
