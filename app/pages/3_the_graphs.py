

import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide"
)


# Assuming you have a pandas DataFrame named 'df_initial'
if 'graphs_made' not in st.session_state:
    st.write("Program error: Graph_made is notin the session state. Graphing will not work!")
else:
    df_initial = st.session_state['df_initial']

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

# new code below here

