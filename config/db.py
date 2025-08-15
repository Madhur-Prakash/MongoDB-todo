from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017/"

# connect to MongoDB
conn = AsyncIOMotorClient(MONGO_URI)