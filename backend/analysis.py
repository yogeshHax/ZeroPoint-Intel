import re
from database import assets_collection

# 1. The "NLP" - Regex to find CVE IDs
def extract_cve_id(text):
    # Pattern: CVE followed by 4 digits, then 4-7 digits
    match = re.search(r'CVE-\d{4}-\d{4,7}', text)
    return match.group(0) if match else "N/A"

# 2. The "Correlation" - Match Threats to My Assets
def find_affected_assets(description):
    my_assets = list(assets_collection.find())
    affected = []
    
    for asset in my_assets:
        # Check if "Windows" matches "Microsoft Windows 10" in text
        if asset['name'].lower() in description.lower():
            affected.append(asset)
            
    return affected

# 3. Risk Scoring Algorithm
def calculate_risk(base_score, asset_criticality):
    # Algorithm: Base Severity + (Asset Criticality / 2)
    # Example: 9.0 (Critical Bug) + 5.0 (Critical Asset) = 14.0 (EXTREME)
    return round(float(base_score) + (asset_criticality / 2), 1)