import json
import os
import sys

students = {}
students["id"] = 1
students["name"] = "Avi"
students["faculty"] = {}
students["faculty"]["profession"] = "Math"
students["faculty"]["grade"] = 90

# create new JSON file named "students-from-code.json" and enter the dictionary "students in it"

with open(os.path.join(sys.path[0], "students-from-code.json"), 'w') as f:
    json.dump(students, f)


# update JSON file

with open(os.path.join(sys.path[0], "students-from-code.json"), 'r') as f:
    data = json.load(f)
    data["faculty"]["grade"] = 100
    f.close()
    with open(os.path.join(sys.path[0], "students-from-code.json"), 'w') as f2:
        json.dump(data, f2)

# 38:20


