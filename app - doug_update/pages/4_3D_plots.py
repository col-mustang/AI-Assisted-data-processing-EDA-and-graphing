import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os as os
import io
import pdb


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide"
)


st.write("""# 👋 Plotly 👋
## 3D graphing page""")

def get_unique_tripples(the_columns):
    '''
        Given a list of columns (greater than or equal to 3 columns), this function returns all permeatations / or combinations of those columns, ignoring order, of those columns
        It is intended for use in 3D plotting.  
        Arguments: the_columns is a list of text strings, intended to be column names (but would not have to be...)
        Returns: all unique combinations of those columns where
        1) no column name is duplicated and
        2) irrespective of ordering, all unique combinations are returned. 
        Note: Returned value is a list within a list. Innner list are the tripplets of columns.
    '''
    the_len = len(the_columns)
    list_of_numeric_tripples = []
    list_of_column_tripples = []
    if the_len < 3:
        return False
    # we'll work with numbers instead of the columns and then use them to generate the column lists at the end.

    # for now, working with indices (numbers) should be more efficient
    number_list = np.arange(0,the_len)
    for x in number_list:
        for y in number_list[1:]:
            for z in number_list[2:]:
                if x != y and x != z and y != z:
                    a_tripple = sorted([x,y,z])
                    #print(f" canidate tripple is: {a_tripple}")
                    if a_tripple not in list_of_numeric_tripples:
                        list_of_numeric_tripples.append(a_tripple)
                        list_of_column_tripples.append([the_columns[i] for i in a_tripple])
    return list_of_column_tripples

def generate_graphing_spec_list(num_graphs):
    num_list = np.arange(0,num_graphs)
    spec_list = []
    for i in num_list:
        spec_list.append([{'type': 'scatter3d'}])
    return spec_list
    

def generate_3D_scatter_plots(df_to_plot, the_columns, colorby):
    # check inputs (right now, just number of columns)
    if len(the_columns) < 3:
        print("Must have at least 3 columns to graph. Exiting")
        return False
    # get all combinations of columns to plot
    # unique column tripples are a list within a list. Inner list are x, y and z column names.
    # if 3 columns are fed to this function, only one tripple will results
    # if 4 columns are fed in, there would be 3 sets of tripples would result. 
    # the three correspond to these positions (one based for illustration, not zero) [1,2,3], [1,2,4], [2,3,4]
    unique_column_tripples = get_unique_tripples(the_columns)
    # print("unique_column_tripples are...")
    # print(unique_column_tripples)
    num_graphs = len(unique_column_tripples)
    spec_list = generate_graphing_spec_list(num_graphs)
    # print("the spec_list is...")
    # print(spec_list)

    num_items_list = np.arange(0,num_graphs) 
    # print(f"num_items_list is {num_items_list}")
    
    fig = make_subplots(rows=num_graphs, cols=1,
                    specs= spec_list,
                    vertical_spacing=0.02)
    
    if color_by is "blue":
        color_it_by = "blue"
    if color_by == "red":
        color_it_by = "red"
    else:
        color_it_by = df_to_plot[color_by]
    
    for i, three_columns_2_plot in enumerate(unique_column_tripples):
        fig.add_trace(go.Scatter3d(x=df_to_plot[three_columns_2_plot[0]], y=df_to_plot[three_columns_2_plot[1]], z=df_to_plot[three_columns_2_plot[2]], mode='markers',
                           marker=dict(size=4, color=color_it_by, colorscale='Viridis', opacity=0.8)), row= i + 1, col=1)
    
    # next loop is one based NOT zero
    for i in range(1,num_graphs + 1):
        fig.update_layout(**{
            f'scene{i}': {
                'xaxis_title': unique_column_tripples[i-1][0],
                'yaxis_title': unique_column_tripples[i-1][1],
                'zaxis_title': unique_column_tripples[i-1][2]
            }
        })
    
    # Update layout
    fig.update_layout(height=850 * num_graphs, width=1800, title_text="3D Scatter Plots")
    # print("ready for fig.show")
    # Show figure
    fig.show()
    # print("fig.show was executed")
                
    return True


if ('df_initial_loaded' in st.session_state) and st.session_state['df_initial_loaded'] and ('df_definition' in  st.session_state):
    data_definition = st.session_state['df_definition']
    df_initial = st.session_state['df_initial']

    # present pop up options for summary stats for dataframe
    col1, col2 = st.columns(2)
    with col1:
        with st.popover("Summary stats: dataframe info"):
            st.write(f"Summary for dataframe, df_initial)")
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

    graph_columns = st.multiselect("Select at least three columns to plot", data_definition["Feature"].values)
    color_by_list = data_definition["Feature"].values.tolist()
    color_by_list.insert(0, "all blue - no color by column")
    color_by_list.insert(0, "all red- no color by column")
    color_by = st.selectbox("Select a column to color by", color_by_list)
    if color_by == "all blue - no color by column":
        color_by = "blue"
    elif color_by == "all red- no color by column":
        color_by = "red"
    if (len(graph_columns) > 2) and (len(color_by) > 0):
        if st.button("Have your request... :blue[Click to produce graph]"):
            result = generate_3D_scatter_plots(df_initial,graph_columns,color_by)
else:
    st.write("No data loaded yet. Go back to 'Select Data...' page")

