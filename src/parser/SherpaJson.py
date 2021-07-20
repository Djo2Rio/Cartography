import json

def get_json_data(json_file):
    with open(json_file, "r") as file:
        json_dump = json.load(file)
    sherpas = json_dump["sherpas"]
    return sherpas

def main():
    var = get_json_data("sherpas.json")
    for n in var : 
        print(n)
main()