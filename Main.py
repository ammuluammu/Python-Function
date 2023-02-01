import pandas as pd
import numpy as np
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
iris.head()
df_columns[['petal_length','species']
group= df_columns.groupby(df_columns.species)

group.count()

group.agg(mean_col=('petal_length','mean'), var_col=('petal_length','var'))

def mean_varience(input_df, valuecol, categeroycol):
    
    temp_df= input_df.groupby([categeroycol]).agg(mean_col=(valuecol,'mean'), var_col=(valuecol,'var'))
    
    return print(temp_df)

mean_varience(df_columns, 'petal_length', 'species')