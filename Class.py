class DataFrameFeatures:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def numeric_columns(self):
        numeric_columns = self.dataframe.select_dtypes(include=[np.number])
        return numeric_columns.groupby(self.dataframe['species']).agg(['mean', 'var']).reset_index()
    
    def string_columns(self):
        string_columns = self.dataframe.select_dtypes(exclude=[np.number])
        return string_columns.groupby(string_columns.columns.tolist()).size().reset_index(name='counts')