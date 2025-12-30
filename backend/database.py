from pymongo import MongoClient
import sys

# CONNECT TO MONGODB
MONGO_URI = "mongodb://localhost:27017/"

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info() # Trigger check
    print("✅ SUCCESS: Connected to MongoDB!")
except Exception as e:
    print("❌ ERROR: Could not connect to MongoDB. Is the Service running?")
    sys.exit(1)

# --- HERE IS THE LINE YOU ASKED ABOUT ---
# We changed the name to 'v2' so you get a fresh, empty start.
db = client['arctic_threat_db_v2'] 
# ----------------------------------------

threats_collection = db['threats']
assets_collection = db['assets']

# Seed default assets IF the list is empty
if assets_collection.count_documents({}) == 0:
    # We leave this empty now so YOU can add your own assets (like Tesla, Django)
    print("New Database Created. Waiting for user input...")