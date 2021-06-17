from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config, UniqueIdProperty, IntegerProperty
from neomodel.exceptions import DoesNotExist
from neomodel.relationship_manager import Relationship
from LeaderCsv import get_csv_data
from EffectifXlsx import get_xls_data
from Normalise import *
import sys

if (len(sys.argv) > 1):
    address = sys.argv[1]
else:
    address = 'bolt://neo4j:password@localhost:7687'
config.DATABASE_URL = address
# Class 
class Partenaire(StructuredNode):
    nom = StringProperty(required = True, unique_index=True,)
    chefs = RelationshipFrom('Etudiant', 'échange avec')
    teams = RelationshipFrom('Teams', 'travaille pour')
    projet = Relationship('Projet', 'Est un sous projet de')

class Projet(StructuredNode):
    nom = StringProperty(required = True, unique_index=True,)

class Personne(StructuredNode):
    nom = StringProperty(required = True, unique_index=True)
    pole = Relationship('Pole', 'appartienne à')

class Etudiant(Personne):
    école = StringProperty()

class ChefDeProjet(Etudiant):
    partenaire = RelationshipTo('Partenaire', 'gère le projet')
    binome = Relationship('Etudiant', 'collabore avec')

class Leader(Personne):
    partenaire = RelationshipTo('Projet', 'définit les objectifs de')

class Leads(Personne):
    leader = Relationship("Leader", "échange des informations avec")
    partenaire = RelationshipTo('Projet', 'pilote et gère')
    binome = Relationship('Leads', 'collabore avec')
    Consultant = Relationship('Consultant', 'consulte')

class Consultant(Personne):
    pole = Relationship('Pole', 'aide')

class Pole():
    nom = StringProperty(required = True, unique_index=True)

class Eleves(Etudiant):
    # projet
    teams = Relationship('Teams', 'appatienne à')

class Teams(StructuredNode):
    numéro = StringProperty() # numéro de l'équipe
    partenaire = RelationshipTo('Partenaire', 'travaille pour')

class Sherpa(Personne):
    équipe = Relationship('Teams', 'pilote et note')
    # lien evrs sherpa
    sherpa2 = Relationship('Sherpa', 'travaille avec')


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
            #print(row)
            # if (row[0] == "MURET"):
            #     print(row)
            #print("nom: ", row[0] +" " + row[1], "equipe: ", row[3], "partenaire: ", NormalCasePartenaire(row[4]), "sherpa1", NormalCaseName(row[5]), "sherpa2", NormalCaseName(row[6]))
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

# Main Function
def main():
    projet = Projet(nom="Planète Solidaire").save()
    leader = Leader(nom="Caroline DePaoli").save()
    leader.partenaire.connect(projet)

    michel = Consultant(nom="Michel Sasson").save()

    mai= Leads(nom="Mai-Linh Lannes").save()
    maya = Leads(nom="Maya Hannachi").save()
    mai.partenaire.connect(projet)
    mai.binome.connect(maya)
    mai.Consultant.connect(michel)
    leads = get_csv_data("Listeleads.csv")
    var = get_xls_data("EFFECTIFS_CAMPUS.xlsx")
    addleadsAndPartenaire(leads, projet)
    var = clearExcel(var)
    addIsgTeams(var)


if __name__ == "__main__":
    main()
