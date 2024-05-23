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


st.write("### **The Request: Generate overlapping histograms for the variable fgp for Player = Jordan versus Player = Lebron. Add an annotation for the average fgp for Player = Jordan versus average fgp for Player = Lebron.**")


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df_initial is already populated
df_jordan = df_initial[df_initial['Player'] == 'Jordan']
df_lebron = df_initial[df_initial['Player'] == 'Lebron']

fig1, ax1 = plt.subplots()

# Plot histograms
ax1.hist(df_jordan['fgp'], bins=15, alpha=0.5, label='Jordan')
ax1.hist(df_lebron['fgp'], bins=15, alpha=0.5, label='Lebron')

# Calculate and annotate average fgp
avg_jordan = df_jordan['fgp'].mean()
avg_lebron = df_lebron['fgp'].mean()

ax1.axvline(avg_jordan, color='blue', linestyle='dashed', linewidth=1)
ax1.axvline(avg_lebron, color='orange', linestyle='dashed', linewidth=1)
ax1.text(avg_jordan, max(ax1.get_ylim())*0.9, f'Avg Jordan: {avg_jordan:.2f}', color='blue')
ax1.text(avg_lebron, max(ax1.get_ylim())*0.8, f'Avg Lebron: {avg_lebron:.2f}', color='orange')

ax1.set_xlabel('Field Goal Percentage (fgp)')
ax1.set_ylabel('Frequency')
ax1.set_title('Histogram of Field Goal Percentage for Jordan vs Lebron')
ax1.legend()

# Display plot in Streamlit
st.pyplot(fig1)

# Clear the figure after displaying
fig1.clf()


