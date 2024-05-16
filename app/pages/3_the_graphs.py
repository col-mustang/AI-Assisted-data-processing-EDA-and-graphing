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


st.write('Create a plot of x=tenure, y=internet_charge_per_min and color it by churn.  Create x and y labels. Add a legend for churn color.')


fig1, ax1 = plt.subplots()

# Scatter plot of tenure vs internet_charge_per_min colored by churn
scatter = ax1.scatter(df_initial['tenure'], df_initial['internet_charge_per_min'], c=df_initial['churn'], cmap='viridis')

# Labels
ax1.set_xlabel('Tenure')
ax1.set_ylabel('Internet Charge Per Minute')

# Legend
legend1 = ax1.legend(*scatter.legend_elements(), title="Churn")
ax1.add_artist(legend1)

# Display the plot in Streamlit
st.pyplot(fig1)

# Clear the figure
fig1.clf()



st.write('generate a graph of the counts of payment_method as a bar chart. Counts of payment_method are similar to value counts across the dataframe for the payment_method ')


fig1, ax1 = plt.subplots()
payment_method_counts = df_initial['payment_method'].value_counts()
payment_method_counts.plot(kind='bar', ax=ax1)
ax1.set_title('Counts of Payment Methods')
ax1.set_xlabel('Payment Method')
ax1.set_ylabel('Count')
st.pyplot(fig1)
fig1.clf()



st.write('create a box plot of internet_charge_per_min with payment_method on the x-axis')


fig1, ax1 = plt.subplots()

df_filtered = df_initial[['payment_method', 'internet_charge_per_min']]

df_filtered.boxplot(column='internet_charge_per_min', by='payment_method', ax=ax1)

ax1.set_title('Box Plot of Internet Charge Per Minute by Payment Method')
ax1.set_xlabel('Payment Method')
ax1.set_ylabel('Internet Charge Per Minute')
plt.suptitle('')

st.pyplot(fig1)
fig1.clf()


