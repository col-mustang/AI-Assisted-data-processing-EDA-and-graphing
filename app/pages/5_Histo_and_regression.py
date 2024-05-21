import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import io

st.set_page_config(
    page_title="Hello",
    layout="wide"
)

st.write("""### Project 3 ASU AI Course: Graphing Page""")

# Assuming you have a pandas DataFrame named 'df_initial'
if 'graphs_made' not in st.session_state:
    st.write("Program error: Graph_made is not in the session state. Graphing will not work!")
else:
    df_initial = st.session_state['df_initial']

    # present pop up options for summary stats
    col1, col2 = st.columns(2)
    with col1:
        with st.popover("Summary stats: dataframe info"):
            st.write(f"Summary for dataframe: df_initial")
            buffer = io.StringIO() 
            df_initial.info(buf=buffer)
            s = buffer.getvalue()  
            st.text(f"#### {s}")
    with col2:
        with st.popover("Summary stats: shape and value_counts"):
            st.text("")
            st.write("The shape is: ")
            st.text(df_initial.shape)
            st.text(f"dataframe df_initial value_counts...")
            for the_col in df_initial.columns:
                st.write("dataframe df_initial value_counts are...")
                st.text(df_initial[the_col].value_counts())

# new code below here

st.write('### **The Request: Create the python code to create an interactive histogram chart in streamlit.  There should be a selectionbox where the column in df_initial can be selected. The histogram would then update to show a histogram of the selected column.**')


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df_initial is already defined and populated
# Example data (the actual data would be already in df_initial)


# Streamlit app
st.title('Interactive Histogram Chart')

# Column selection
column_to_plot = st.selectbox('Select column for histogram', df_initial.columns)

# Create and display histogram
fig1, ax1 = plt.subplots()
ax1.hist(df_initial[column_to_plot].dropna(), bins=30, edgecolor='k', alpha=0.7)
ax1.set_title(f'Histogram of {column_to_plot}')
ax1.set_xlabel(column_to_plot)
ax1.set_ylabel('Frequency')

st.pyplot(fig1)
fig1.clf()


st.write("### **The Request: Create the python code to create an interactive scatter chart with the linear regression line overlay in streamlit.  There should be two selectionbox's where the x and y columns from df_initial can be selected. The chart would then update to show a scatter plot and regression line for the selected x and y columns. use sklearn for the regression.**")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Assuming df_initial is already populated with the data
# df_initial = pd.read_csv('your_data.csv')  <- This line is to illustrate the df_initial should already be available

# Streamlit app
st.title('Interactive Scatter Plot with Regression Line')

# Select columns for x and y from the dataframe
x_col = st.selectbox('Select X-axis column', df_initial.columns)
y_col = st.selectbox('Select Y-axis column', df_initial.columns)

# Ensure both selected columns are numeric
if df_initial[x_col].dtype in [np.int64, np.float64] and df_initial[y_col].dtype in [np.int64, np.float64]:
    # Prepare the data
    X = df_initial[[x_col]].values
    y = df_initial[y_col].values

    # Create and fit the regression model
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Create the plot
    fig1, ax1 = plt.subplots()
    ax1.scatter(X, y, color='blue', label='Data points')
    ax1.plot(X, y_pred, color='red', label='Regression line')
    ax1.set_xlabel(x_col)
    ax1.set_ylabel(y_col)
    ax1.legend()

    # Display the plot in Streamlit
    st.pyplot(fig1)
    fig1.clf()
else:
    st.warning('Please select numeric columns for both X and Y axes.')


