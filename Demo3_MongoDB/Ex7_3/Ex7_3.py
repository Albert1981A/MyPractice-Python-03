from pymongo import MongoClient
from bson import ObjectId
import requests

client = MongoClient(port=27017)

resp = requests.get("https://api.tvmaze.com/shows")
shows = resp.json()

# To get the first 10 shows:
shows = shows[0:10]

# create new collection with only name, genres and average_rating
new_shows = list(map( lambda x : { "name" : x["name"] , "genres" : x["genres"] , "average_rating" : x["rating"]["average"]}  ,shows))

db = client["moviesdb"]
movies_collection = db["movies"]

resp = movies_collection.insert_many(new_shows)
print( "The Id received is:", resp.inserted_ids)

def replace_name(new_name, current_name):
    print("New name:", new_name)
    print("Current name:", current_name)
    obj = {"name": new_name}
    res = movies_collection.update_one({"name": current_name}, {"$set" : obj})
    print( "Update response:", res.raw_result)