import csv

def get_csv_data(csv_file):
    # Colonnes: Projet, Binôme, Contact Leader, Contact Binôme, Téléphone Leader, Téléphone Binôme
    data = []
    with open(csv_file, "r") as file:
        for row in file:
            data.append(row.encode("latin-1").decode("utf-8").strip("\ufeff")[:-1].split(";"))
    return data