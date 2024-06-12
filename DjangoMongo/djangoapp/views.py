from django.http import HttpResponse
import pymongo


def index(request):
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")


client = pymongo.MongoClient('mongodb+srv://mongo_db:mango_db_password@cluster0.veqwiqm.mongodb.net/?retryWrites=true'
                             '&w=majority&appName=Cluster0')

dbname = client['mongo_database']

collection = dbname['users']

user_1 = {

    "name": "Vlad",
    "age": 3,
    "role": "developer"
}

collection.insert_one(user_1)

users_details = collection.find_one({})

for users in users_details:
    print(users)
