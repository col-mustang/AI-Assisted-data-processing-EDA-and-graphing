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

st.write("### **The Request: Create a line graph with game ABS on the x-axis and fgp on the y-axis separated by player**")


import streamlit as st
import matplotlib.pyplot as plt

# Assuming df_initial is already defined and populated

# Create a figure and an axis
fig1, ax1 = plt.subplots()

# Loop through each player and plot their data
for player in df_initial['Player'].unique():
    player_data = df_initial[df_initial['Player'] == player]
    ax1.plot(player_data['game_abs'], player_data['fgp'], label=player)

# Add labels and title
ax1.set_xlabel('Game ABS')
ax1.set_ylabel('FGP')
ax1.set_title('Field Goal Percentage Over Games by Player')
ax1.legend()

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure after displaying
fig1.clf()


st.write("### **The Request: Create a line graph with game ABS on the x-axis and fgp on the y-axis separated by player**")


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df_initial is already populated and available
df = df_initial.copy()

# Create a figure and axis
fig1, ax1 = plt.subplots()

# Loop through each player and plot their data
players = df['Player'].unique()
for player in players:
    player_data = df[df['Player'] == player]
    ax1.plot(player_data['game_abs'], player_data['fgp'], label=player)

# Set the labels and title
ax1.set_xlabel('Game ABS')
ax1.set_ylabel('FGP')
ax1.set_title('FGP over Game ABS by Player')
ax1.legend()

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


st.write("### **The Request: Create a line graph with game ABS on the x-axis and fgp on the y-axis separated by player**")


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df_initial is already populated and available.

# Create the plot
fig1, ax1 = plt.subplots()

# Plot each player's data
for player in df_initial['Player'].unique():
    player_data = df_initial[df_initial['Player'] == player]
    ax1.plot(player_data['game_abs'], player_data['fgp'], label=player)

# Set plot title and labels
ax1.set_title('Field Goal Percentage (FG%) Over Games')
ax1.set_xlabel('Game ABS')
ax1.set_ylabel('FG%')

# Add legend
ax1.legend(title='Player')

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure after displaying
fig1.clf()


st.write("### **The Request: Create a line graph with game ABS on the x-axis and 3p on the y-axis separated by player**")


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df_initial is already populated
# Example of how df_initial might look like:
# df_initial = pd.DataFrame({
#     'Player': ['A', 'A', 'B', 'B'],
#     'game_abs': [1, 2, 1, 2],
#     'threep': [0.3, 0.4, 0.5, 0.6]
# })

# Create the plot
fig1, ax1 = plt.subplots()

# Filtering the data and plotting
players = df_initial['Player'].unique()
for player in players:
    player_data = df_initial[df_initial['Player'] == player]
    ax1.plot(player_data['game_abs'], player_data['threep'], label=player)

# Adding labels and title
ax1.set_xlabel('Game ABS')
ax1.set_ylabel('3P')
ax1.set_title('3P Percentage by Game ABS for Each Player')
ax1.legend()

# Display the plot using Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


st.write("### **The Request: Create a line graph with game ABS on the x-axis and 3p on the y-axis separated by player**")


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df_initial is already loaded
# Create a new dataframe with the necessary columns
df = df_initial[['Player', 'game_abs', 'threep']]

# Create the plot
fig1, ax1 = plt.subplots()

# Plot each player's 3-point percentage over the game_abs
for player in df['Player'].unique():
    player_data = df[df['Player'] == player]
    ax1.plot(player_data['game_abs'], player_data['threep'], label=player)

# Add labels and title
ax1.set_xlabel('Game ABS')
ax1.set_ylabel('3P%')
ax1.set_title('3-Point Percentage Over Time by Player')
ax1.legend()

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


