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

st.write("### **The Request: Generate overlapping histograms for the variable \'fgp\' for Player = Jordan versus Player = Lebron. Add an annotation for the average \'fgp\' for Player = Jordan versus average \'fgp\' for Player = Lebron.**")


import streamlit as st
import matplotlib.pyplot as plt

# Filter data for Jordan and Lebron
df_jordan = df_initial[df_initial['Player'] == 'Jordan']
df_lebron = df_initial[df_initial['Player'] == 'Lebron']

# Calculate average 'fgp' for both players
avg_fgp_jordan = df_jordan['fgp'].mean()
avg_fgp_lebron = df_lebron['fgp'].mean()

# Create the plot
fig1, ax1 = plt.subplots()

# Plot histograms
ax1.hist(df_jordan['fgp'], bins=20, alpha=0.5, label='Jordan')
ax1.hist(df_lebron['fgp'], bins=20, alpha=0.5, label='Lebron')

# Add annotations for the averages
ax1.axvline(avg_fgp_jordan, color='blue', linestyle='dashed', linewidth=1)
ax1.axvline(avg_fgp_lebron, color='orange', linestyle='dashed', linewidth=1)
ax1.text(avg_fgp_jordan, plt.ylim()[1]*0.9, f'Avg Jordan: {avg_fgp_jordan:.2f}', color='blue')
ax1.text(avg_fgp_lebron, plt.ylim()[1]*0.8, f'Avg Lebron: {avg_fgp_lebron:.2f}', color='orange')

# Labels and title
ax1.set_xlabel('Field Goal Percentage')
ax1.set_ylabel('Frequency')
ax1.set_title('Field Goal Percentage - Jordan vs Lebron')
ax1.legend()

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()


st.write("### **The Request: Type in your new request here, then hit control enter.**")


import streamlit as st
import matplotlib.pyplot as plt

# Sample data for df_initial
import pandas as pd
data = {
    'Player': ['Player1', 'Player2', 'Player3', 'Player4'],
    'pts': [20, 15, 25, 10],
    'ast': [7, 9, 5, 12]
}
df_initial = pd.DataFrame(data)

# Plotting
fig1, ax1 = plt.subplots()
ax1.bar(df_initial['Player'], df_initial['pts'], label='Points')
ax1.bar(df_initial['Player'], df_initial['ast'], bottom=df_initial['pts'], label='Assists')

ax1.set_xlabel('Player')
ax1.set_ylabel('Total')
ax1.set_title('Points and Assists by Player')
ax1.legend()

st.pyplot(fig1)
fig1.clf()


