import requests


# Get all Users
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

for user in users:
    print(user["name"])

print("--------------------------------------------")

# Get one user
response2 = requests.get("https://jsonplaceholder.typicode.com/users/7")
user2 = response2.json()

print(user2["name"])

print("--------------------------------------------")

# Send new User
obj = {"name": "Avi", "email": "avi@gmail.com"}
response3 = requests.post("https://jsonplaceholder.typicode.com/users", json=obj)
user3 = response3.json()

print(user3)

print("--------------------------------------------")

# Update User
obj2 = {"name": "mosh", "email": "mosh@gmail.com", "id": 7}
response4 = requests.put("https://jsonplaceholder.typicode.com/users/7", json=obj2)
user4 = response4.json()

print(user4)

print("--------------------------------------------")

# Delete User
response5 = requests.delete("https://jsonplaceholder.typicode.com/users/7")
user5 = response5.json()

print(user5)

print("--------------------------------------------")

# => https://jsonplaceholder.typicode.com/todos?userId=2
