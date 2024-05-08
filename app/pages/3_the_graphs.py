

import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide"
)


# Assuming you have a pandas DataFrame named 'df_initial'
if 'graphs_made' in st.session_state:
    df_initial = st.session_state['df_initial']

# new code below here



import matplotlib.pyplot as plt
import streamlit as st

fig1, ax1 = plt.subplots()
ax1.scatter(df_initial['tenure'], df_initial['internet_charge_per_min'], c=df_initial['churn'])
ax1.set_xlabel('Tenure')
ax1.set_ylabel('Internet Charge Per Min')
ax1.set_title('Scatter plot of Tenure vs Internet Charge Per Min')
st.pyplot(fig1)
fig1.clf()




import matplotlib.pyplot as plt
import seaborn as sns

# Create a figure and axis
fig1, ax1 = plt.subplots()

# Create boxplot
sns.boxplot(x='churn', y='tenure', data=df_initial, ax=ax1)

# Set labels
ax1.set_xlabel('Churn')
ax1.set_ylabel('Tenure')

# Show the plot
st.pyplot(fig1)


