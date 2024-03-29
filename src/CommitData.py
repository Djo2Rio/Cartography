from src.Normalise import *
from src.Class import *
from neomodel.exceptions import DoesNotExist

# Utility Fonction
def addleadsAndPartenaire(leads, projet):
    
    """ Create nodes: Chef de Projet and Partenaire in Neo4j,
        Add relashionships between the nodes

    Args:
        leads (list): A list of row with the following data for each row :
                                    Projet, Binôme, Contact Leader, Contact Binôme,
                                    Téléphone Leader, Téléphone Binôme
        projet (Projet node): A Neo4j representing the Projet node 
    """

    for row in leads:
        if row[0] != "Projet":
            try:
                chef = ChefDeProjet.nodes.get(nom=row[1])
            except DoesNotExist:
                chef = ChefDeProjet(nom=row[1], école="Epita").save()
            try:
                sousfifre = ChefDeProjet.nodes.get(nom=row[2])
            except DoesNotExist:
               sousfifre = ChefDeProjet(nom=row[2], école="Epita").save()
            try:
                partenaire = Partenaire.nodes.get(nom=NormalCasePartenaire(row[0]))
            except:
                partenaire = Partenaire(nom=NormalCasePartenaire(row[0])).save()
            chef.partenaire.connect(partenaire)
            sousfifre.binome.connect(chef)
            partenaire.projet.connect(projet)

def addIsgTeams(teams):
    
    """ Create nodes : teams, sherpa and Partenaire in Neo4j,
        and the relashionships between them

    Args:
        teams (dict of DataFrames): A dict of Dataframes that represents an excel files
    """

    equipe = [
        "Lille", "Bordeaux", "Lyon",
        "Paris","Strasbourg" ,"Toulouse"
    ]
    i = 0
    for frame in teams.values():
        for index, row in frame.iterrows():
            try:
                teams = Teams.nodes.get(numéro= "[" + equipe[i]+ "] "  + "Equipe " + str(row[3]))
            except DoesNotExist:
                 teams = Teams(numéro="[" + equipe[i]+ "] "  + "Equipe " + str(row[3])).save()
            try:
                sherpa1 = Sherpa.nodes.get(nom=NormalCaseName(row[5]))
            except:
                sherpa1 = Sherpa(nom= NormalCaseName(row[5])).save()
            try:
                sherpa2 = sherpa2.nodes.get(nom= NormalCaseName(row[6]))
            except:    
                sherpa2 = Sherpa(nom= NormalCaseName(row[6])).save()
            sherpa1.sherpa2.connect(sherpa2)
            sherpa1.équipe.connect(teams)
            try:
                partenaire = Partenaire.nodes.get(nom=NormalCasePartenaire(row[4]))
            except:
                partenaire = Partenaire(nom=NormalCasePartenaire(row[4])).save()
            teams.partenaire.connect(partenaire)
        i += 1