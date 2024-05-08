import pandas as pd
import numpy as np

def get_data_definition(df):
    df_definition = pd.DataFrame(df.dtypes.values, index=df.dtypes.index, columns=["Data Type"]).reset_index()
    df_definition.columns = ["Feature", "Data Type"]
    return df_definition
