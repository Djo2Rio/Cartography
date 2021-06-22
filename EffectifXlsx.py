import pandas as pd

def get_xls_data(xls_file):
    var = pd.read_excel(xls_file,index_col=0, sheet_name = [0,1,2,4,5,6]) # Read the seven first sheet 
    return var
