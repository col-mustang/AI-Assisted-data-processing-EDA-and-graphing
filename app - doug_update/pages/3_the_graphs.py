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

st.write("### **The Request: Create a plot of x=tenure, y=internet_charge_per_min and color it by churn.  Create x and y labels. Add a legend for churn color.**")


import streamlit as st
import matplotlib.pyplot as plt

# Assuming df_initial is already available and populated

fig1, ax1 = plt.subplots()

# Scatter plot
scatter = ax1.scatter(df_initial['tenure'], df_initial['internet_charge_per_min'], c=df_initial['churn'], cmap='viridis', label=df_initial['churn'])

# Labels
ax1.set_xlabel('Tenure')
ax1.set_ylabel('Internet Charge Per Min')

# Legend
legend1 = ax1.legend(*scatter.legend_elements(), title="Churn")
ax1.add_artist(legend1)

# Display plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


st.write("### **The Request: Create overlapping histograms for number_customer_service_calls for churn=0 versus churn=1. Since the are many more data rows where churn=0, convert the data to relative frequency**")


import streamlit as st
import matplotlib.pyplot as plt

# Filter the data for churn=0 and churn=1
df_churn_0 = df_initial[df_initial['churn'] == 0]
df_churn_1 = df_initial[df_initial['churn'] == 1]

# Create the histograms
fig1, ax1 = plt.subplots()

# Plot the histograms
ax1.hist(df_churn_0['number_customer_service_calls'], bins=10, alpha=0.5, label='Churn=0', density=True)
ax1.hist(df_churn_1['number_customer_service_calls'], bins=10, alpha=0.5, label='Churn=1', density=True)

# Add titles and labels
ax1.set_title('Number of Customer Service Calls by Churn Status')
ax1.set_xlabel('Number of Customer Service Calls')
ax1.set_ylabel('Relative Frequency')
ax1.legend(loc='upper right')

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


st.write("### **The Request: Create the python code to create an interactive histogram chart in streamlit.  There should be a selectionbox where the column in df_initial can be selected. The histogram would then update to show a histogram of the selected column.**")


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df_initial is already populated
# df_initial = pd.read_csv('your_data.csv')  # Example of loading the dataframe

# List of columns to choose from
columns = df_initial.columns.tolist()

# Streamlit selection box
selected_column = st.selectbox('Select column for histogram', columns)

# Plot the histogram
fig1, ax1 = plt.subplots()
ax1.hist(df_initial[selected_column].dropna(), bins=30, edgecolor='k')
ax1.set_title(f'Histogram of {selected_column}')
ax1.set_xlabel(selected_column)
ax1.set_ylabel('Frequency')

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


st.write("### **The Request: Create the python code to create an interactive scatter chart with the linear regression line overlay in streamlit.  There should be two selectionbox\'s where the x and y columns from df_initial can be selected. The chart would then update to show a scatter plot and regression line for the selected x and y columns.**")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Assuming df_initial is already populated
# Uncomment the following line if you need to read the data
# df_initial = pd.read_csv('your_data.csv')

st.title('Scatter Plot with Regression Line')

# Selection boxes for x and y axis
x_col = st.selectbox('Select the X-axis column', df_initial.columns)
y_col = st.selectbox('Select the Y-axis column', df_initial.columns)

if x_col and y_col:
    # Creating the plot
    fig1, ax1 = plt.subplots()
    
    # Scatter plot
    sns.scatterplot(data=df_initial, x=x_col, y=y_col, ax=ax1)
    
    # Linear Regression
    X = df_initial[[x_col]].values
    y = df_initial[y_col].values
    reg = LinearRegression().fit(X, y)
    y_pred = reg.predict(X)
    
    # Plotting the regression line
    ax1.plot(df_initial[x_col], y_pred, color='red', linewidth=2)
    ax1.set_title(f'Scatter plot of {x_col} vs {y_col} with Regression Line')
    ax1.set_xlabel(x_col)
    ax1.set_ylabel(y_col)

    # Display the plot in Streamlit
    st.pyplot(fig1)
    
    # Clear the figure after displaying
    fig1.clf()


