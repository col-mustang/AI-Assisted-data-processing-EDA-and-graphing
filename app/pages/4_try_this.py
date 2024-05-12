import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import io

st.set_page_config(
    page_title="Hello",
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

                


import matplotlib.pyplot as plt
import streamlit as st

fig1, ax1 = plt.subplots()

scatter = ax1.scatter(df_initial['tenure'], df_initial['internet_charge_per_min'], c=df_initial['churn'])

# produce a legend with the unique colors from the scatter
legend1 = ax1.legend(*scatter.legend_elements(),
                    loc="upper right", title="Churn")
ax1.add_artist(legend1)

ax1.set_xlabel('Tenure')
ax1.set_ylabel('Internet Charge Per Min')

st.pyplot(fig1)




import matplotlib.pyplot as plt
import streamlit as st

# Assuming df_initial is your dataframe

fig1, ax1 = plt.subplots()

# Group by internet_service and plot avg_monthly_bill versus internet_monthly_charges
for name, group in df_initial.groupby("internet_services"):
    ax1.plot(group["internet_monthly_charges"], group["avg_monthly_bill"], marker='o', linestyle='', label=name, alpha=0.5)

ax1.set_xlabel("internet_monthly_charges")
ax1.set_ylabel("avg_monthly_bill")
ax1.legend(title="internet_service")

# Display the plot
st.pyplot(fig1)

# Clear the figure for reuse in the next iteration
fig1.clf()




import matplotlib.pyplot as plt
import streamlit as st

# Assume df_initial is your DataFrame
df_initial = df_initial[['payment_method', 'internet_charge_per_min']]

# Group by payment_method and create a list of values for each group
grouped_values = df_initial.groupby('payment_method')['internet_charge_per_min'].apply(list)

fig1, ax1 = plt.subplots()

# Create a boxplot
ax1.boxplot(grouped_values)

# Set x-tick labels
ax1.set_xticklabels(grouped_values.index)

# Show the plot
st.pyplot(fig1)

# Clear the figure for other plots
fig1.clf()


