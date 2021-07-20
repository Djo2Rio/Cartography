from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config, UniqueIdProperty, IntegerProperty
from neomodel.relationship_manager import Relationship
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
    # lien vers sherpa
    sherpa2 = Relationship('Sherpa', 'travaille avec')