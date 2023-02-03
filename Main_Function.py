def main():
    data_frame = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    data_frame= data_frame[['petal_length','species']]
    
    df_features = DataFrameFeatures(data_frame)
    print("\nString Columns:")
    print(df_features.string_columns())
    print("Numeric Columns:")
    print(df_features.numeric_columns())