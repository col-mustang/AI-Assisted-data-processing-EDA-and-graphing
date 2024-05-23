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

st.write("""### **The Request: Generate a scatter plot with two series. Series 1: x= game_abs and y = pts for Player = Jordan and Series 2: x= game_abs and y = pts for Player = Lebron.  Use sklearn library to generate a regression line for both series. Annotate the regression lines with the Players.**""")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Filter data for Jordan and Lebron
jordan_data = df_initial[df_initial['Player'] == 'Jordan']
lebron_data = df_initial[df_initial['Player'] == 'Lebron']

# Create the plot
fig1, ax1 = plt.subplots()

# Jordan scatter plot
ax1.scatter(jordan_data['game_abs'], jordan_data['pts'], label='Jordan', color='blue')

# Lebron scatter plot
ax1.scatter(lebron_data['game_abs'], lebron_data['pts'], label='Lebron', color='red')

# Regression for Jordan
X_jordan = jordan_data['game_abs'].values.reshape(-1, 1)
y_jordan = jordan_data['pts'].values.reshape(-1, 1)
regressor_jordan = LinearRegression()
regressor_jordan.fit(X_jordan, y_jordan)
y_pred_jordan = regressor_jordan.predict(X_jordan)
ax1.plot(jordan_data['game_abs'], y_pred_jordan, color='blue')
ax1.annotate('Jordan', xy=(jordan_data['game_abs'].iloc[-1], y_pred_jordan[-1]), color='blue')

# Regression for Lebron
X_lebron = lebron_data['game_abs'].values.reshape(-1, 1)
y_lebron = lebron_data['pts'].values.reshape(-1, 1)
regressor_lebron = LinearRegression()
regressor_lebron.fit(X_lebron, y_lebron)
y_pred_lebron = regressor_lebron.predict(X_lebron)
ax1.plot(lebron_data['game_abs'], y_pred_lebron, color='red')
ax1.annotate('Lebron', xy=(lebron_data['game_abs'].iloc[-1], y_pred_lebron[-1]), color='red')

# Add legend and labels
ax1.legend()
ax1.set_xlabel('Game Absolute')
ax1.set_ylabel('Points')
ax1.set_title('Points by Game Absolute for Jordan and Lebron')

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure to free memory
fig1.clf()


