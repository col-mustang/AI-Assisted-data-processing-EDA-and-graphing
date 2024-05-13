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

fig1, ax1 = plt.subplots()

scatter = ax1.scatter(df_initial['tenure'], df_initial['internet_charge_per_min'], c=df_initial['churn'])
legend1 = ax1.legend(*scatter.legend_elements(),
                    loc="upper right", title="Churn")
ax1.add_artist(legend1)

st.pyplot(fig1)

fig1.clf()








fig1, ax1 = plt.subplots()

scatter = ax1.scatter(df_initial['avg_monthly_bill'], df_initial['internet_monthly_charges'], 
                      c=df_initial['internet_services'], alpha=0.5)

legend1 = ax1.legend(*scatter.legend_elements(), title="Internet Services")
ax1.add_artist(legend1) 

plt.xlabel('Average Monthly Bill')
plt.ylabel('Internet Monthly Charges')

st.pyplot(fig1)
fig1.clf()




fig1, ax1 = plt.subplots()
df_initial.boxplot(column='internet_charge_per_min', by='payment_method', ax=ax1)
ax1.set_xlabel('Payment Method')
ax1.set_ylabel('Internet Charge per Minute')
ax1.set_title('Box plot of Internet Charge per Minute by Payment Method')
plt.suptitle('') # Disabling the auto-generated title
st.pyplot(fig1)
fig1.clf()




fig1, ax1 = plt.subplots()
df_temp = df_initial[['tenure', 'churn']]
churn_grouped = df_temp.groupby('churn')
churn_grouped.boxplot(subplots=False, ax=ax1)
ax1.set_title('Boxplot of Tenure Grouped by Churn')
ax1.set_xlabel('Churn')
ax1.set_ylabel('Tenure')
st.pyplot(fig1)
fig1.clf()


