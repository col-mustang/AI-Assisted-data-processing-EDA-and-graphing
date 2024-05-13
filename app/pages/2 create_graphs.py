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


st.set_page_config(
    layout="wide",
    page_title="👋 graph creation screen 👋",
    page_icon="👋"
)

st.write("""### Project 3 ASU AI Course: Automated Graphing and Exploratory Data Analysis
### Page: **Create graph for the request**
""")

st.write(f"the dir is: {os.getcwd()}")

def extract_code_from_message(message):
    lines = message.split("\n")
    code = ""
    in_code = False
    for line in lines:
        if "```" in line:
            in_code = not in_code
        elif in_code:
            code += line + "\n"
    return code

if 'df_definition' in  st.session_state:
    # pdb.set_trace()
    data_definition = st.session_state['df_definition']
    col1, col2 = st.columns(2)
    with col1:
        st.write("the data definition is:")
        st.dataframe(data_definition)
    with col2:
        new_request = st.text_area("Enter your next graphing request here")
        if ('new_request' in st.session_state) and (st.session_state['new_request']==False) and \
           (len(new_request) > 0):
            st.session_state['new_request'] = True
            st.session_state['the_request'] = new_request
else:
    st.write("No data definition found. Go back to 'Select Data...' page")
    
# see if we are ready to create a graph
if ('the_request' in st.session_state) and ('df_definition' in st.session_state) and \
    ('new_request' in st.session_state) and st.session_state['new_request'] and ('graph_file_name' in st.session_state):
    # pdb.set_trace()
    the_request = st.session_state['the_request']
    st.write(f"the request is: {the_request}")
    
    # Define the paths.
    # search_path = os.path.join(os.getcwd(), "pages")
    
    graph_file = "pages/" + st.session_state['graph_file_name']
    print(f"the graph file is {graph_file}")
    
    # load the key
    load_dotenv(find_dotenv())

    # together_api_key = os.environ.get("TOGETHER_API_KEY")
    # print(together_api_key)
    Open_AI_API_KEY = os.environ.get("Open_AI_API_KEY")

    llm = ChatOpenAI(api_key=Open_AI_API_KEY, model="gpt-4")

    # llm = ChatOpenAI(base_url="https://api.together.xyz/v1",
    # api_key=together_api_key,
    # model="deepseek-ai/deepseek-coder-33b-instruct")

    class AgentState(TypedDict):
        data_definition: pd.DataFrame
        the_request: List[str]
        graph_source: str
        graph_file: str

    # Create the graph.
    workflow = StateGraph(AgentState)

    user_prompt_template = """ {the_request}"""

    system_prompt_template = """You will be writing code in python to create a plot in Streamlit using matplotlib.pyplot.  
    In the code, display the final figure using the Streamlit command st.pyplot(fig1).  Note that st.pyplot() with no
    arguments is deprecistaed. Start you plot definition with ```fig1, ax1 = plt.subplots()```. After showing the plot with 
    ```st.pyplot(fig1)```, end your code with  ```fig1.clf()```. The data to use is in the dataframe df_initial. If you need to 
    filter data or subset it, etc. then you can make another dataframe from df_initial. Do not alter df_initial. 
    Here is the data definition {data_definition}, you will be working with. 

    Any request must use one or more of these columns from the data definition. Reply with the source code only. 
    Do not include the ```import``` statements in your response. I will add the import statements myself.
    
    """

    def generate_graph_code(state: AgentState):
        # pdb.set_trace()
        state["graph_file"] = graph_file
        st.write(f"the graph file is: {state['graph_file']}")
        state["graph_source"] = ""
        state["data_definition"] = data_definition
        state["the_request"] = the_request

        user_prompt = user_prompt_template.format(the_request=the_request)

        system_prompt = system_prompt_template.format(data_definition=data_definition)
        # Get the test source code.
        system_message = SystemMessage(system_prompt)
        human_message = HumanMessage(user_prompt)


        message = llm.invoke([system_message, human_message]).content
        st.write(f"the message is: {message}")
        code = extract_code_from_message(message)
        state["graph_source"] = "\n\n" + code + "\n\n"
        return state

    def write_graph_code(state: AgentState):
        # pdb.set_trace()
        the_file_name = state["graph_file"]
        with open(the_file_name, "a") as f:
            f.write(state["graph_source"])
            f.close()
        st.session_state["graphs_made"] = True
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

    # Find out if we are done.
    def should_continue(state: AgentState):
        return "end"
    
    # Add the conditional edge.
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
        # pdb.set_trace()
        st.write("Just before rerun")
       
    except GraphRecursionError:
        print("Graph recursion limit reached.")