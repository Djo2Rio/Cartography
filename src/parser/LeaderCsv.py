import csv

def get_csv_data(csv_file):

    """ Convert a csv file to a list

    Args:
        csv_file ([type]): A CSV file with the format :
                            Colonnes: 
                                Projet, Binôme, Contact Leader,
                                Contact Binôme, Téléphone Leader, Téléphone Binôme

    Returns:
        [List]: A list
    """
    
    data = []
    with open(csv_file, "r") as file:
        for row in file:
            data.append(row.encode("latin-1").decode("utf-8").strip("\ufeff")[:-1].split(";"))
    return data