import os
import sys
import json

# the function needs to return
# person's name
# city 
# street number 
# all this if any
def get_person_data(street_name):
    print('The street name we entered:', street_name)
    with open(os.path.join(sys.path[0], "persons.json"), "r") as file:
        data = json.load(file)
        persons = data["persons"]
        res = list(filter(lambda x : x["address"]["street"]["name"] == street_name, persons))
        if (len(res) > 0):
            return res[0]
        else:
            return "No match"


