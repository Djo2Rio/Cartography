from Normalise import *
from src.Class import *

# Utility Fonction
def addleadsAndPartenaire(leads, projet):
    for row in leads:
        if (row[0] != "Projet"):
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
            #sousfifre.partenaire.connect(partenaire)

def addIsgTeams(teams):
    equipe = ["Lille", "Bordeaux", "Lyon" ,"Paris","Strasbourg" ,"Toulouse"]
    i = 0
    for frame in teams.values():
        print(frame)
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