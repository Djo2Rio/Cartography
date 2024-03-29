import re

def nameCorrection(name):
    
    """ Remove unwanted charcaters from a string Name

    Args:
        name (string): A name with some unwanted characters to remove (?, OK, .) ,
        or an email to transform into a real name

    Returns:
        [string]: A name composed by a fistname and a lastname separates by a space
    """

    str = re.sub("\(OK\)", "", name)
    str = re.sub("\(\?\)", "", str)
    str = re.sub("@isg.fr", "", str)
    str = re.sub("\.", " ", str)
    return str

def NormalCaseName(string):
    
    """ Format a string to looks likes Firstname LASTNAME

    Args:
        string (string): A name 

    Returns:
        [string]: A name
    """

    string = nameCorrection(string)
    string.lower()
    list = string.split()
    list[0][0].upper()
    list[1].upper()
    return list[0][0].upper() + list[0][1:] + " "+ list[1].upper()

def NormalCasePartenaire(string):
    
    """ Convert the first character of each word to uppercase,
        then call a function for standardization of all names

    Args:
        string (string): A name corresponding to a Partners

    Returns:
        [string]: A name corresponding to a Partners
    """

    string = string.lower()
    list = string.split()
    newstr = ""
    for e in list:
        newstr += e[0].upper() + e[1:] + " "
    return matchCorrectProjectName(newstr[:-1])

def matchCorrectProjectName(projectName):
    
    """ Match a Partners name to a stardarized name

    Args:
        projectName (string): A name corresponding to a Partners

    Returns:
        [type]: A standarized name corresponding to a Partners
    """

    result = re.match("Dumas", projectName) 
    if result or re.match("Artiste François Dumas", projectName):
        return "Artiste Dumas"
    result = re.match("Dumas", projectName) 
    if result or re.match("Artiste François Dumas", projectName):
        return "Artiste Dumas"
    result = re.match("Signés Toqué", projectName)
    if result or re.match("Signé Toqué", projectName) or re.match("Signé Tocqué", projectName):
        return "Signés Toqués"
    result = re.match("Esprit", projectName)
    if result:
        return "Esprit de Voyage"
    result = re.match("Mama", projectName)
    if result or re.match("Mam", projectName) or re.match("MAM", projectName):
        return "Mama Shelter"
    if re.match("Micro-stage", projectName) or re.match("Micro Stage Solidaire", projectName) :
        return "Micro Stage"
    result = re.match("Découverte Langues", projectName)
    if result or re.match("Découverte Des Langues", projectName):
        return "A La Découverte Des Langues"
    if re.match("Compétence", projectName) or re.match("Ref Compétences", projectName) or re.match("Ref Compétence", projectName):
        return "Référentiel Compétence"
    result = re.match("Arcs", projectName)
    if result:
        return "Les Arcs"
    result = re.match("Labrande", projectName)
    if result or re.match("Chateau La Brande", projectName):
        return "Château Labrande"
    result = re.match("Signés Toqués", projectName)
    if result:
        return "Signé Toqué"
    result = re.match("Oui Chef", projectName)
    if result:
        return "Oui Chef!"
    result = re.match("Musée", projectName)
    if result:
        return "Musée des Arts et Métiers"
    result = re.match("Grandes Tables Du Monde", projectName)
    if result:
        return "Les Grandes Tables Du Monde"
    if  re.match("Abbaye Pouilhes", projectName) or re.match("Prouilhe", projectName):
        return "Abbaye Prouilhe"
    if  re.match("Villages Pro Btp", projectName):
        return "Village Pro Btp"
    return projectName
    

def clearExcel(teams):

    """ Deletes unnecessary columns in a object representing a Excel file

    Args:
        teams (dict of DataFrames): An object

    Returns:
        [dict of DataFrames]: The same object with the unnecessary columns removed.
    """

    for frame in teams.values():
        try:
            del frame['promo']
            del frame['MISSION']
        except:
            print("Cannot delete Promo and Mission column")
        try:
            del frame['CLASSE']
        except:
            print("Cannot delete CLASSE column")
        try:
            del frame['Classe']
        except:
            print("Cannot delete Classe column")
        try:
            del frame['MISSION (Segment ou KPI)']
        except:
            print('Cannot delete Mission (Segment ou KPI) column')
        try:
            del frame['Mission 5 : Brand content & RS']
        except:
            print('Cannot delete Mission Brand content & RS column')
        frame.fillna(method='ffill', inplace=True)
    return teams