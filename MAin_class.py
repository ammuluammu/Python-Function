import pandas as pd
import numpy as np


class dataframe:
    def __init__(self, df):
        self.df = df
df= pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv') 

def mean_varience(input_df, valuecol, categeroycol):
    
    temp_df= input_df.groupby([categeroycol]).agg(mean_col=(valuecol,'mean'), var_col=(valuecol,'var'))
    
    return print(temp_df)