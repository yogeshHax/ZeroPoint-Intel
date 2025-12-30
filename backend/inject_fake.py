from pymongo import MongoClient

# Connect to the database
client = MongoClient("mongodb://localhost:27017/")
db = client['arctic_threat_db']
collection = db['threats']

# Create a Fake Threat
fake_card = {
    "cve_id": "CVE-2025-9999",
    "description": "TEST VIRUS: If you see this card, your Frontend is working perfectly!",
    "risk_score": 10.0,
    "affected_asset": "Windows Test",
    "source": "Manual Injection"
}

# Insert it
collection.insert_one(fake_card)
print("✅ INJECTED: 1 Fake Threat added to Database.")