import pandas as pd

def get_xls_data(xls_file):

    """ Convert a Excel file to an dict of Dataframes

    Args:
        xls_file (Excel file): A file

    Returns:
        [dict of DataFrames]: A dict of Dataframes that represents the excel files
    """
    
    sheet_name_array = [
        0,1,2,
        4,5,6
    ]
    var = pd.read_excel(xls_file,index_col=0, sheet_name=sheet_name_array) # Read the seven first sheet 
    return var
