import json

def get_json_data(json_file):
    with open(json_file, "r") as file:
        json_dump = json.load(file)
    sherpas = json_dump["sherpas"]
    return sherpas