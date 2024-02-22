# handel all the data stuff for our pets app
import json

# this function will load all the pets from the json file
def load_pets():
    with open("registered.json", "r") as my_file:
        pets = json.load(my_file)
    if not pets:
        pets = []
    return pets

# this function will add a new pet to the json file
def add_pet(pet_dict):
    # load pets from json
    pets = load_pets()
    # add to the list
    pets.append(pet_dict)
    # now update the json
    with open("registered.json", "w") as my_file:
        json.dump(pets, my_file, indent=2)






