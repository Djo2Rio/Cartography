from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'

class Book(StructuredNode):
    title = StringProperty(unique_index=True)
    author = RelationshipTo('Author', 'AUTHOR')

class Author(StructuredNode):
    name = StringProperty(unique_index=True)
    books = RelationshipFrom('Book', 'AUTHOR')

harry_potter = Book(title='Harry potter and the..').save()
rowling =  Author(name='J. K. Rowling').save()
harry_potter.author.connect(rowling)



# def get_csv_data(csv_file):
#     # Colonnes: Projet, Binôme, Contact Leader, Contact Binôme, Téléphone Leader, Téléphone Binôme
#     data = []
#     with open(csv_file, "r") as file:
#         for row in file:
#             data.append(row[:-1].split(";"))
#     return data