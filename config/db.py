from pymongo import MongoClient
MONGO_URI = "mongodb://localhost:27017/"

# connect to MongoDB
conn = MongoClient(MONGO_URI)