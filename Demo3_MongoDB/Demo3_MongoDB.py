from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(port=27017)

db = client["personsdb"]

persons_collection = db["persons"]


print("---------------Get all persons------------------")
# Get all persons
persons = persons_collection.find({})  # This is like => "select * from collection" of mysql
for person in persons:
    print(person)

print("---------------Get person by Id------------------")
# Get person by Id
person2 = persons_collection.find_one({ "_id": ObjectId("630cfe3404b1429b19f5844f") })
print(person2)

print("---------------Create new person------------------")
# Create new person 
obj = {'name': 'Inbal', 'age': 32, 'city': 'Rehovot'}
resp = persons_collection.insert_one(obj)
print( "The Id received is:", resp.inserted_id)
# Create new person 
obj0 = {'name': 'Dov', 'age': 16, 'city': 'Holon'}
resp0 = persons_collection.insert_one(obj0)
print( "The Id received is:", resp0.inserted_id)
# Get all persons
persons3 = persons_collection.find({})
for person3 in persons3:
    print(person3)

print("----------------Update one person by his id-----------------")
# Update one person by his id
obj2 = {'name': 'Inbal2', 'age': 33, 'city': 'Haifa2'}
resp2 = persons_collection.update_one({"_id" : ObjectId(resp.inserted_id)} , {"$set" : obj2})
print( "Update response:", resp2.raw_result)
# Get all persons
persons4 = persons_collection.find({})
for person4 in persons4:
    print(person4)

print("----------------Update all persons that lives in \"Holon\" to \"Omer\"-----------------")
# Update all persons that lives in "Holon" to "Omer"
obj3 = {"city": "Omer"}
res = persons_collection.update_many({"city": "Holon"}, {"$set" : obj3})
print( "Update response:", res.raw_result)
# Get all persons
persons5 = persons_collection.find({})
for person5 in persons5:
    print(person5)

print("----------------Delete person-----------------")
# Delete person
resp3 = persons_collection.delete_one({"_id" : ObjectId(resp.inserted_id)})
print( "Delete response:", resp.acknowledged)
# Get all persons
persons6 = persons_collection.find({})
for person6 in persons6:
    print(person6)

print("---------------------------------")

# 3:55:30





