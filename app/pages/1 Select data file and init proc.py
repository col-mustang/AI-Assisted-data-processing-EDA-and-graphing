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

def init_default_graph_file():
    # copy the 'pages/template/graph_file_template.py' to pages/graph_file_template.py
    copyfile("templates/graph_file_template.py", "pages/3_the_graphs.py")
    return "3_the_graphs.py"

def init_new_graph_file(new_graph_file_name):
    # zzz pick it up here!!!
    st.session_state['graph_file_name'] = new_graph_file_name
    # pdb.set_trace()
    junk_result_for_now = add_starter_text_to_new_graph_file(new_graph_file_name)
    return True

def add_starter_text_to_new_graph_file(graph_file_name):
    # write out the graphing file
    # pdb.set_trace()
    copyfile("templates/graph_file_template.py", "pages/" + graph_file_name)
    st.session_state['graph_file_name'] = graph_file_name
    return True


def clean_up_graph_f_name(f_name_to_clean):
    if ".py" in f_name_to_clean.lower():
        return(f_name_to_clean)
    else:
        if "." not in f_name_to_clean:
            cleaned_f_name = f_name_to_clean + ".py"
            return(cleaned_f_name)
        else:   # not a good file name
            st.write(f"## Invalid file name {f_name_to_clean}. Could not initialize new graph file")
            return(init_default_graph_file())

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
    st.write(f"#### Data Definition for {file_name}")
    st.write("Here is the data definition")
    st.dataframe(df_definition)
    st.write("the data...")
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
    if 'graph_file_name' not in st.session_state:
        graph_file_name = init_default_graph_file() 
        st.session_state['graph_file_name'] = graph_file_name
        graph_file_bool = True
    else:
        graph_file_name = st.session_state['graph_file_name']
        graph_file_bool = True

    # provide opportunity to change the graph file name
    new_graph_file_name = ""   # initialize to empty string
    new_graph_file_name = st.text_input("If you need a new graph file, enter the new file name", value="3_the_graphs.py")
    new_graph_file_name = clean_up_graph_f_name(new_graph_file_name)
    # NOTE: if file name doesn't pass basic check (very basic check), then new_file_name will just be the default file name
    # that's what clean_up_graph_f_name will return if there is an issue
    
    if (len(new_graph_file_name) > 0) and (new_graph_file_name != graph_file_name):
        # received new graph file name
        # check if .py is in the name
        # pdb.set_trace()
        st.write(f"a new graph file -> {new_graph_file_name}")
        graph_file_bool = init_new_graph_file(new_graph_file_name)
        graph_file_name = new_graph_file_name   # important they are the same so repeatof this section of code does not happen

    if graph_file_bool:
        # Git the graphing request
        the_request = ""  # initialize first to empty string
        the_request = st.text_area("Enter your graphing request here")
        if len(the_request) > 0:
            st.session_state['the_request'] = the_request
            if st.button("Have your request... :blue[Click to produce graph]"):
                st.session_state['new_request'] = True
                st.switch_page(("pages/2 create_graphs.py"))
    else:
        st.write("### Could not initialize new graph file")
       
   
