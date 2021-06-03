from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config, UniqueIdProperty, IntegerProperty
from neomodel.exceptions import DoesNotExist
from neomodel.relationship_manager import Relationship
from LeaderCsv import get_csv_data
from EffectifXlsx import get_xls_data
config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'


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
    partenaire = RelationshipTo('Partenaire', 'échange avec')
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
                partenaire = Partenaire.nodes.get(nom=row[0])
            except:
                partenaire = Partenaire(nom=row[0]).save()
            chef.partenaire.connect(partenaire)
            sousfifre.binome.connect(chef)
            partenaire.projet.connect(projet)
            #sousfifre.partenaire.connect(partenaire)

def addIsgTeams(teams):
    for index, row in teams.iterrows():
            #print(row)
            #print("nom: ", row[1] +" " + row[2], "equipe: ", row[4], "partenaire: ", row[5], "sherpa1", row[7], "sherpa2", row[8])
            try:
                teams = Teams.nodes.get(numéro=row[4])
            except DoesNotExist:
                 teams = Teams(numéro=row[4]).save()
            try:
                sherpa1 = Sherpa.nodes.get(nom=row[7])
            except:
                sherpa1 = Sherpa(nom=row[7]).save()
            try:
                sherpa2 = sherpa2.nodes.get(nom=row[8])
            except:    
                sherpa2 = Sherpa(nom=row[8]).save()
            sherpa1.sherpa2.connect(sherpa2)
            sherpa1.équipe.connect(teams)
            try:
                partenaire = Partenaire.nodes.get(nom=row[5])
            except:
                partenaire = Partenaire(nom=row[5]).save()
            teams.partenaire.connect(partenaire)
            try:
                eleves1 = Eleves.nodes.get(nom=row[1] + " " + row[2])
            except:
                eleves1 = Eleves(nom=row[1] + " " + row[2]).save()
            eleves1.teams.connect(teams)

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
    addIsgTeams(var)


if __name__ == "__main__":
    main()