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

st.write("### **The Request: Create a histogram with game ABS on the x-axis and field goal percentage on the y-axis separated by player**")


import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Assuming df_initial is already defined and populated
fig1, ax1 = plt.subplots()

# Create a histogram with game_abs on the x-axis and field goal percentage on the y-axis, separated by player
players = df_initial['Player'].unique()

for player in players:
    player_data = df_initial[df_initial['Player'] == player]
    ax1.hist(player_data['game_abs'], weights=player_data['fgp'], alpha=0.5, label=player)

ax1.set_xlabel('Game ABS')
ax1.set_ylabel('Field Goal Percentage')
ax1.legend(title='Player')
ax1.set_title('Field Goal Percentage by Game ABS for Each Player')

st.pyplot(fig1)
fig1.clf()


st.write("### **The Request: Create a histogram with game ABS on the x-axis and field goal percentage on the y-axis separated by player**")


import streamlit as st
import matplotlib.pyplot as plt

# Create a new dataframe from df_initial to filter out the required columns
df_filtered = df_initial[['Player', 'game_abs', 'fgp']]

# Create the plot
fig1, ax1 = plt.subplots()

# Loop through each player and plot their data
players = df_filtered['Player'].unique()
for player in players:
    player_data = df_filtered[df_filtered['Player'] == player]
    ax1.plot(player_data['game_abs'], player_data['fgp'], label=player)

# Adding labels and title
ax1.set_xlabel('Game ABS')
ax1.set_ylabel('Field Goal Percentage')
ax1.set_title('Field Goal Percentage by Game ABS for Each Player')
ax1.legend()

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


st.write("### **The Request: Create a histogram with game ABS on the x-axis and field goal percentage on the y-axis separated by player**")


import streamlit as st
import matplotlib.pyplot as plt

# Create a unique list of players
players = df_initial['Player'].unique()

# Create subplots for each player
fig1, ax1 = plt.subplots(len(players), 1, figsize=(10, 6 * len(players)), sharex=True)

# If there's only one player, ax1 won't be an array
if len(players) == 1:
    ax1 = [ax1]

# Plot histogram for each player
for i, player in enumerate(players):
    player_data = df_initial[df_initial['Player'] == player]
    ax1[i].hist(player_data['game_abs'], weights=player_data['fgp'], bins=20, alpha=0.7)
    ax1[i].set_title(f"{player}'s Field Goal Percentage by Game ABS")
    ax1[i].set_xlabel('Game ABS')
    ax1[i].set_ylabel('Field Goal Percentage')

# Display the plot using Streamlit
st.pyplot(fig1)

# Clear the figure after display
fig1.clf()


st.write("### **The Request: Create a histogram with game ABS on the x-axis and 3p on the y-axis separated by player**")


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Assuming df_initial is already populated and available
df_initial = pd.read_csv('path_to_your_csv_file.csv')  # Replace with the actual path to your data

# Filter the necessary columns
df_filtered = df_initial[['Player', 'game_abs', 'three']]

# Create the plot
fig1, ax1 = plt.subplots()

# Plotting the histogram for each player
players = df_filtered['Player'].unique()
for player in players:
    player_data = df_filtered[df_filtered['Player'] == player]
    ax1.hist(player_data['game_abs'], weights=player_data['three'], alpha=0.5, label=player)

ax1.set_xlabel('Game ABS')
ax1.set_ylabel('3P')
ax1.legend(title='Player')
ax1.set_title('Histogram of 3P by Game ABS for each Player')

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


