import json # => will load the information and will translate it to a dictionary (key and value)
import os   # => Operation Systems
import sys  # => can find the path of the current folder

# "sys.path" will find all the path the work with this project.
# the first path in the array "sys.path[0]" is the current folder.

print(sys.path[0]) 


# "os" Gives me access to the contexts I'm in relative to the operating system.
# In the function below I request: In the current folder of the current file,
# find "persons.json" and merge them with me
# Mode - "r" - read only, "w" - write to the file (will erase and write new), "a" - append (add to the file)
# f - the name we give to the file
# when opening the file like this, the file will close in the end of the section "with",
# other wise we will have to close it "f.close()".
# "os.path" => create a path in the operation system. 
# "join(sys.path[0], "persons.json")" => that is build from the path of the current file and the file "persons.json".
# "data = json.load(f)" we load the information to data and we receive a dictionary (key and value)
# now we can use data in the python file.

with open(os.path.join(sys.path[0], "persons.json"), 'r') as f:
    data = json.load(f)
    
    print(data)

    persons = data["persons"]

    for person in persons:
        print(person["name"])