from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config, UniqueIdProperty, IntegerProperty
from neomodel.relationship_manager import Relationship
from LeaderCsv import get_csv_data
from EffectifXlsx import get_xls_data
config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'


# Class 
class Partenaire(StructuredNode):
    nom = StringProperty(required = True)
    chefs = RelationshipFrom('Etudiant', 'échange avec')
    teams = RelationshipFrom('Teams', 'travaille pour')

class Personne(StructuredNode):
    nom = StringProperty(required = True)

class Etudiant(Personne):
    école = StringProperty()

class ChefDeProjet(Etudiant):
    partenaire = RelationshipTo('Partenaire', 'échange avec')
    binome = Relationship('Etudiant', 'collabore avec')

class Eleves(Etudiant):
    # projet
    teams = Relationship('Teams', 'appatienne à')

class Teams(StructuredNode):
    numéro = IntegerProperty() # numéro de l'équipe
    # missions vers partenaire
    # lien vers chef d projets et binome
    # lien vers sherpa
    partenaire = RelationshipTo('Partenaire', 'travaille pour')

class Sherpa(Personne):
    équipe = Relationship('Teams', 'pilote et note')
    # lien evrs sherpa
    sherpa2 = Relationship('Sherpa', 'travaille avec')

# Utility Fonction
def addleadsAndPartenaire(leads):
    for row in leads:
        if (row[0] != "Projet"):
            chef = ChefDeProjet(nom=row[1], école="Epita").save()
            sousfifre = ChefDeProjet(nom=row[2], école="Epita").save()
            partenaire = Partenaire(nom=row[0]).save()
            chef.partenaire.connect(partenaire)
            sousfifre.binome.connect(chef)
            #sousfifre.partenaire.connect(partenaire)

def addIsgTeams(teams):
    for index, row in teams.iterrows():
        print(row[1], row[2])
        #print("______________________________________________________________")
    #print(teams)
    teams = Teams(numéro=5).save()
    sherpa1 = Sherpa(nom="ilaa").save()
    sherpa2 = Sherpa(nom="paoaoa").save()
    sherpa1.sherpa2.connect(sherpa2)
    partenaire = Partenaire(nom='villages').save()
    teams.partenaire.connect(partenaire)
    eleves1 = Eleves(nom="a").save()
    eleves2 = Eleves(nom="b").save()
    eleves3 = Eleves(nom="c").save()
    eleves4 = Eleves(nom="d").save()
    eleves5 = Eleves(nom="e").save()
    eleves1.teams.connect(teams)
    eleves2.teams.connect(teams)
    eleves3.teams.connect(teams)
    eleves4.teams.connect(teams)
    eleves5.teams.connect(teams)


# Main Function
def main():
    leads = get_csv_data("Listeleads.csv")
    var = get_xls_data("EFFECTIFS_CAMPUS.xlsx")
    addleadsAndPartenaire(leads)
    addIsgTeams(var)


if __name__ == "__main__":
    main()