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

st.write("### **The Request: Generate overlapping histograms for the variable fgp for Player = Jordan versus Player = Lebron. Add an annotation for the average fgp for Player = Jordan versus average fgp for Player = Lebron.**")


import streamlit as st
import matplotlib.pyplot as plt

# Filter data for Players Jordan and Lebron
df_jordan = df_initial[df_initial['Player'] == 'Jordan']
df_lebron = df_initial[df_initial['Player'] == 'Lebron']

# Extract fgp values
fgp_jordan = df_jordan['fgp']
fgp_lebron = df_lebron['fgp']

# Calculate average fgp for annotation
avg_fgp_jordan = fgp_jordan.mean()
avg_fgp_lebron = fgp_lebron.mean()

# Create plot
fig1, ax1 = plt.subplots()

# Plot histograms
ax1.hist(fgp_jordan, bins=20, alpha=0.5, label='Jordan')
ax1.hist(fgp_lebron, bins=20, alpha=0.5, label='Lebron')

# Add annotations
ax1.axvline(avg_fgp_jordan, color='blue', linestyle='dashed', linewidth=1)
ax1.text(avg_fgp_jordan, max(ax1.get_ylim()) * 0.9, f'Avg Jordan: {avg_fgp_jordan:.2f}', color='blue')

ax1.axvline(avg_fgp_lebron, color='orange', linestyle='dashed', linewidth=1)
ax1.text(avg_fgp_lebron, max(ax1.get_ylim()) * 0.8, f'Avg Lebron: {avg_fgp_lebron:.2f}', color='orange')

# Add title and labels
ax1.set_title('FG% Histogram: Jordan vs Lebron')
ax1.set_xlabel('FG%')
ax1.set_ylabel('Frequency')
ax1.legend()

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


st.write("### **The Request: Generate a scatter plot with two series. Series 1: x= game_abs and y = pts for Player = Jordan and Series 2: x= game_abs and y = pts for Player = Lebron.  Use sklearn library to generate a regression line for both series. Annotate the regression lines with the Players.**")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Assuming df_initial is already populated
# Filter data for the two players
df_jordan = df_initial[df_initial['Player'] == 'Jordan']
df_lebron = df_initial[df_initial['Player'] == 'Lebron']

# Extract x and y for both players
x_jordan = df_jordan['game_abs'].values.reshape(-1, 1)
y_jordan = df_jordan['pts'].values
x_lebron = df_lebron['game_abs'].values.reshape(-1, 1)
y_lebron = df_lebron['pts'].values

# Create regression models
model_jordan = LinearRegression().fit(x_jordan, y_jordan)
model_lebron = LinearRegression().fit(x_lebron, y_lebron)

# Predict regression lines
x_range = np.linspace(df_initial['game_abs'].min(), df_initial['game_abs'].max(), 100).reshape(-1, 1)
y_pred_jordan = model_jordan.predict(x_range)
y_pred_lebron = model_lebron.predict(x_range)

# Plotting
fig1, ax1 = plt.subplots()
ax1.scatter(x_jordan, y_jordan, color='blue', label='Jordan')
ax1.scatter(x_lebron, y_lebron, color='red', label='Lebron')

# Plot regression lines
ax1.plot(x_range, y_pred_jordan, color='blue', linestyle='--')
ax1.plot(x_range, y_pred_lebron, color='red', linestyle='--')

# Annotate regression lines
ax1.annotate('Jordan', xy=(x_range[-1], y_pred_jordan[-1]), color='blue')
ax1.annotate('Lebron', xy=(x_range[-1], y_pred_lebron[-1]), color='red')

# Labels and legend
ax1.set_xlabel('Game Absolute')
ax1.set_ylabel('Points')
ax1.legend()

# Display the plot
st.pyplot(fig1)

# Clear the figure
fig1.clf()


st.write("### **The Request: Generate a scatter plot with two series. Series 1: x= game_abs and y = pts for Player = Jordan and Series 2: x= game_abs and y = pts for Player = Lebron.  Use sklearn library to generate a regression line for both series. Annotate the regression lines with the Players. for Series 1 use red points and a black regression line. For Series 2, use blue points and a yellow regression line.**")


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Assume df_initial is already populated
df_jordan = df_initial[df_initial['Player'] == 'Jordan']
df_lebron = df_initial[df_initial['Player'] == 'Lebron']

fig1, ax1 = plt.subplots()

# Scatter plot for Jordan
ax1.scatter(df_jordan['game_abs'], df_jordan['pts'], color='red', label='Jordan')

# Linear regression for Jordan
X_jordan = df_jordan['game_abs'].values.reshape(-1, 1)
y_jordan = df_jordan['pts'].values.reshape(-1, 1)
reg_jordan = LinearRegression().fit(X_jordan, y_jordan)
y_pred_jordan = reg_jordan.predict(X_jordan)
ax1.plot(df_jordan['game_abs'], y_pred_jordan, color='black')
ax1.annotate('Jordan', xy=(df_jordan['game_abs'].values[-1], y_pred_jordan[-1]), color='black')

# Scatter plot for Lebron
ax1.scatter(df_lebron['game_abs'], df_lebron['pts'], color='blue', label='Lebron')

# Linear regression for Lebron
X_lebron = df_lebron['game_abs'].values.reshape(-1, 1)
y_lebron = df_lebron['pts'].values.reshape(-1, 1)
reg_lebron = LinearRegression().fit(X_lebron, y_lebron)
y_pred_lebron = reg_lebron.predict(X_lebron)
ax1.plot(df_lebron['game_abs'], y_pred_lebron, color='yellow')
ax1.annotate('Lebron', xy=(df_lebron['game_abs'].values[-1], y_pred_lebron[-1]), color='yellow')

ax1.set_xlabel('Game Abs')
ax1.set_ylabel('Points')
ax1.legend()

st.pyplot(fig1)
fig1.clf()


st.write("### **The Request: Generate overlapping histograms for the variable \'pts\' for Player = Jordan versus Player = Lebron. Add an annotation for the average \'pts\' for Player = Jordan versus average \'pts\' for Player = Lebron.**")


import streamlit as st
import matplotlib.pyplot as plt

# Filter the data for the two players
df_jordan = df_initial[df_initial['Player'] == 'Jordan']
df_lebron = df_initial[df_initial['Player'] == 'Lebron']

# Calculate the average points for the two players
avg_pts_jordan = df_jordan['pts'].mean()
avg_pts_lebron = df_lebron['pts'].mean()

# Create the plot
fig1, ax1 = plt.subplots()

# Plot the histograms
ax1.hist(df_jordan['pts'], bins=20, alpha=0.5, label='Jordan')
ax1.hist(df_lebron['pts'], bins=20, alpha=0.5, label='Lebron')

# Add the annotations
ax1.axvline(avg_pts_jordan, color='blue', linestyle='dashed', linewidth=1)
ax1.text(avg_pts_jordan + 1, max(ax1.get_ylim()) * 0.9, f'Avg Jordan: {avg_pts_jordan:.2f}', color='blue')

ax1.axvline(avg_pts_lebron, color='orange', linestyle='dashed', linewidth=1)
ax1.text(avg_pts_lebron + 1, max(ax1.get_ylim()) * 0.85, f'Avg Lebron: {avg_pts_lebron:.2f}', color='orange')

# Add labels and legend
ax1.set_xlabel('Points')
ax1.set_ylabel('Frequency')
ax1.set_title('Points Distribution: Jordan vs Lebron')
ax1.legend()

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


