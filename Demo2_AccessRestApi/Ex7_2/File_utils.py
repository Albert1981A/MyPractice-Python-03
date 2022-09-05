import os
import sys
import json
import requests

def get_user_data2(id):
    print('Received id', id)
    user_res = requests.get("https://jsonplaceholder.typicode.com/users/" + id)
    user = user_res.json()
    print("User Name: " + user["name"] + " User Email: " + user["email"])
    if user["name"].startswith("E"):
        todo_res = requests.get("https://jsonplaceholder.typicode.com/todos?userId=" + id)
        todo = todo_res.json()
        todo_titles = list(map(lambda x : x["title"] , todo))
        for title in todo_titles:
            print(title)
        obj = { "titles": todo_titles }
        with open(os.path.join(sys.path[0], "Titles.json"), "w") as file:
            json.dump(obj, file)