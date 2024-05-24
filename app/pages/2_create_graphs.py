from typing import TypedDict, List
import colorama
import os
from dotenv import load_dotenv, find_dotenv


from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

from langgraph.graph import StateGraph, END
from langgraph.pregel import GraphRecursionError

from langchain_openai import ChatOpenAI

import streamlit as st
import pandas as pd
import numpy as np
import io
import pdb
from shutil import copyfile
import json
from streamlit_mic_recorder import speech_to_text

st.set_page_config(
    layout="wide",
    page_title="👋 graph creation screen 👋",
    page_icon="👋"
)

st.write("""### Project 3 ASU AI Course: Automated Graphing and Exploratory Data Analysis
### Page: **Create graph for the request**
""")

# st.write(f"the dir is: {os.getcwd()}")

# global variables -> had to resort to global variables because of st.session_state limitations within the LangGraph framework
# global g_data_definition  # set right after these commments
# global g_the_request  # have to check to see if there is a request_from_select_data_bool before setting the request. Currently set on line 59
# global g_the_code
# global g_message
# global g_graph_file_w_path
g_graphs_made = False  # Check to see if this works. It is set to True in write_graphs_code


if 'df_definition' in  st.session_state:
    # pdb.set_trace()
    g_data_definition = st.session_state['df_definition']

    col1, col2 = st.columns(2)
    with col1:
        st.write("the data definition is:")
        st.dataframe(g_data_definition)
        if 'graph_file_name_w_path' in st.session_state:
            if st.button("click to view the page with the graphs"):
                st.switch_page(st.session_state['graph_file_name_w_path'])
    with col2:
        if ('request_from_select_data_bool' in st.session_state) and st.session_state['request_from_select_data_bool'] and ('the_request_from_select_data' in st.session_state):
            st.session_state['the_request'] = st.session_state['the_request_from_select_data']
            st.session_state['new_request'] = True
            g_the_request = st.session_state['the_request']
            st.write(f"the request from 'Select data...' page is: {st.session_state['the_request_from_select_data']}")
            # remove the request from the 'select data...' page. It is underway now.
            del st.session_state['the_request_from_select_data']
            del st.session_state['request_from_select_data_bool']
            if st.button("Click to generate another graph"):
                # no need to do anything here. The button click will cause the page to rerun and that is all that is needed.
                st.write("Reinitiaing page")
        else:
            # Get user input for new request
            st.write("Enter your next graphing request here or click below to provide a voice prompt.")

            with st.form(key='voice_form'):
                if st.form_submit_button("Click to open. Click again to submit recording."):
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

            g_new_request = st.text_area("")

            if 'text_received' in st.session_state and st.session_state['text_received']:
                text = st.session_state['text_received'][-1]
                if isinstance(text, str) and len(text) > 0:
                    st.session_state['voice_request'] = text
                    st.write(f"Recorded Request: {text}")
                    g_new_request = text  # Use the voice input as the request
            if len(g_new_request) > 0:
                st.session_state['new_request'] = True
                st.session_state['the_request'] = g_new_request
            # on this branch, we give the user a chance to drop the last code block in the graph file
            
            if ("have_graph_file_backup" in st.session_state) and ("graph_file_name" in st.session_state):
                if st.button("click to undo last graph file change?"):
                    copyfile("templates/graph_file_backup.py", "pages/" + st.session_state['graph_file_name'])
else:
    st.write("No data definition found. Go back to 'Select Data...' page")


    
# see if we are ready to create a graph
if ('the_request' in st.session_state) and ('df_definition' in st.session_state) and \
    ('new_request' in st.session_state) and st.session_state['new_request'] and ('graph_file_name_w_path' in st.session_state):
    # pdb.set_trace()
    g_the_request = st.session_state['the_request']
    st.write(f"the request is: {g_the_request}")
    
    g_graph_file_w_path = st.session_state['graph_file_name_w_path']
    # debug only
    st.write(f"The graph file is {g_graph_file_w_path}")
    
    # load the key
    load_dotenv(find_dotenv())

    # together_api_key = os.environ.get("TOGETHER_API_KEY")
    # print(together_api_key)
    Open_AI_API_KEY = os.environ.get("Open_AI_API_KEY")
    
    llm = ChatOpenAI(api_key=Open_AI_API_KEY, model="gpt-4o")

    # llm = ChatOpenAI(base_url="https://api.together.xyz/v1",
    # api_key=together_api_key,
    # model="deepseek-ai/deepseek-coder-33b-instruct")

    class AgentState(TypedDict):
        data_definition: pd.DataFrame
        the_request: List[str]
        graph_source: str
        graph_file: str
        llm_message: str

    # Create the graph.
    workflow = StateGraph(AgentState)
    user_prompt_template = """ {the_request}"""

    system_prompt_template = """You will be writing code in python to create a plot in Streamlit using matplotlib.pyplot.  
    In the code, display the final figure using the Streamlit command st.pyplot(fig1).  Note that st.pyplot() with no
    arguments is depreciated. Start you plot definition with ```fig1, ax1 = plt.subplots()```. After showing the plot with 
    ```st.pyplot(fig1)```, end your code with  ```fig1.clf()```. The data to use is in the dataframe df_initial, which is already populated. Do not recreate df_initial. If you need to 
    filter data or subset it, etc. then you can make another dataframe from df_initial. Do not alter df_initial. 
    Here is the data definition {data_definition}, you will be working with. In the code you generate, use only ASCII characters. Do not used non-ASCII characters.

    Any request must use one or more of these columns from the data definition. Reply with the source code only. 
    """



    def extract_code_from_message(message):
        # pdb.set_trace()
        lines = message.split("\n")
        code = ""
        in_code = False
        for line in lines:
            if "```" in line:
                in_code = not in_code
            elif in_code:
                code += line + "\n"
        st.write(f"### The extracted code is: {code}") 
        return code


    def generate_graph_code(state: AgentState):
        global g_data_definition
        global g_the_request
        global g_the_code
        global g_message
        global g_graph_file_w_path
        # pdb.set_trace()
        st.write("debug: in generate_graph_code")
        # state["graph_file"] = graph_file
        # st.write(f"the graph file is: {state['graph_file']}")
        state["graph_source"] = ""
        state["data_definition"] = g_data_definition
        state["the_request"] = g_the_request
        
        user_prompt = user_prompt_template.format(the_request=g_the_request)

        system_prompt = system_prompt_template.format(data_definition=g_data_definition)
        # Get the test source code.
        system_message = SystemMessage(system_prompt)
        human_message = HumanMessage(user_prompt)

        g_message = llm.invoke([system_message, human_message]).content
        
        state["llm_message"] = g_message
        # pdb.set_trace()
        code = extract_code_from_message(g_message)
        g_the_code = code
        state["graph_source"] = "\n\n" + code + "\n\n"
        st.write(f"### The message from the LLM is: \n{g_message}")
        return state

    def write_graph_code(state: AgentState):
        global g_graphs_made
        global g_graph_file_w_path
        'zzz'
        the_request = state["the_request"]
        # escape the quotes both double and single
        the_request_escaped = the_request.replace("'", "\\'")
        the_request_escaped = the_request_escaped.replace('"', '\\"')
        # make sure the first letter is capitalized
        the_request_escaped = the_request_escaped[0].upper() + the_request_escaped[1:]
        # the_file_name = state["graph_file"]
        # back up the graph file and set up session state
        copyfile(g_graph_file_w_path,"templates/graph_file_backup.py")
        
         # append the code to the file along with the request
        with open(g_graph_file_w_path, "a") as f:
            f.write(f"""st.write("### **The Request: {the_request_escaped}**")\n""")
            f.write(state["graph_source"])
            f.close()
        # zzz
        g_graphs_made = True
        return state

    # Add a node to for discovery.
    workflow.add_node(
        "generate_graph_code",
        generate_graph_code
    )

    workflow.add_node(
        "write_graph_code",
        write_graph_code
    )

    # Define the entry point. This is where the flow will start.
    workflow.set_entry_point("generate_graph_code")

    # try with no conditional note
    workflow.add_edge("generate_graph_code", "write_graph_code")

    # Find out if we are done. For Version 1.0, we are always done after writing the graph code.
    def should_continue(state: AgentState):
        return "end"
    
    # Not for version 1.0, but could add conditional edge here to check the code
    # workflow.add_conditional_edges(
    #     "generate_graph_code",
    #     should_continue,
    #     {
    #         "continue": "generate_graph_code",
    #         "end": "write_graph_code"
    #     }
    # )

    # Always go from write the graph file to end.
    workflow.add_edge("write_graph_code", END)
    # Create the app and run it
    app = workflow.compile()
    inputs = {}
    config = RunnableConfig(recursion_limit=100)
    # pdb.set_trace()
    try:
        result = app.invoke(inputs, config)
        print(result)
        st.session_state['graphs_made'] = True
        st.session_state['new_request'] = False
    except GraphRecursionError:
        st.write("### *Graph recursion limit reached*")

    if st.button("Do you want to back up the graph file?"):
        copyfile(g_graph_file_w_path,"templates/graph_file_backup.py")