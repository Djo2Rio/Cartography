import re

def nameCorrection(name):
    str = re.sub("\(OK\)", "", name)
    str = re.sub("\(\?\)", "", str)
    str = re.sub("@isg.fr", "", str)
    str = re.sub("\.", " ", str)
    return str

def NormalCaseName(string):
    string = nameCorrection(string)
    string.lower()
    list = string.split()
    list[0][0].upper()
    list[1].upper()
    return list[0][0].upper() + list[0][1:] + " "+ list[1].upper()

def NormalCasePartenaire(string):
    string = string.lower()
    list = string.split()
    newstr = ""
    for e in list:
        newstr += e[0].upper() + e[1:] + " "
    return matchCorrectProjectName(newstr[:-1])

def matchCorrectProjectName(projectName):

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
    for frame in teams.values():
        #print(frame)
        try:
            del frame['promo']
            del frame['MISSION']
        except:
            print("a")
        try:
            del frame['CLASSE']
        except:
            print("b")
        try:
            del frame['Classe']
        except:
            print("c")
        try:
            del frame['MISSION (Segment ou KPI)']
        except:
            print('d')
        try:
            del frame['Mission 5 : Brand content & RS']
        except:
            print('e')
        frame.fillna(method='ffill', inplace=True)
    return teams
