import json

def get_json_data(json_file):

    """ Convert a Json file to a Pyhton Json Object

    Args:
        json_file (Json file): A file 

    Returns:
        [Json Object]: An object
    """
    
    with open(json_file, "r") as file:
        json_dump = json.load(file)
    sherpas = json_dump["sherpas"]
    return sherpas