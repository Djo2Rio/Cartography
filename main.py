from src.parser.LeaderCsv import get_csv_data
from src.parser.EffectifXlsx import get_xls_data
from src.Normalise import *
import sys
from src.Class import *
from src.CommitData import *

if (len(sys.argv) > 1):
    address = sys.argv[1]
else:
    address = 'bolt://neo4j:password@localhost:7687'
config.DATABASE_URL = address

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
    leads = get_csv_data("Ressources/Listeleads.csv")
    var = get_xls_data("Ressources/EFFECTIFS_CAMPUS.xlsx")
    addleadsAndPartenaire(leads, projet)
    var = clearExcel(var)
    addIsgTeams(var)

if __name__ == "__main__":
    main()