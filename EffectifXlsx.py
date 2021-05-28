import pandas as pd

def get_xls_data(xls_file):
    var = pd.read_excel(xls_file,index_col=0) 
    return var

def main():
    var = get_xls_data("EFFECTIFS_CAMPUS.xlsx")
    print(var)
    
main()