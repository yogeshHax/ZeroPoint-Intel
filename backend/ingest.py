import requests
import feedparser

# --- 1. NVD SCANNER (Dynamic) ---
def fetch_nvd(keyword):
    # If the user didn't type anything, skip it
    if not keyword or keyword == "Windows": 
        # Optional: Skip default if you ONLY want user input
        pass 

    print(f"   🔎 SEARCHING NVD DATABASE FOR: '{keyword}'...")
    
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}&resultsPerPage=3"
    headers = {"User-Agent": "ArcticThreatProject_v1.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            items = response.json().get('vulnerabilities', [])
            print(f"      ✅ Found {len(items)} hits for {keyword}")
            
            clean_list = []
            for item in items:
                cve = item['cve']
                clean_list.append({
                    "cve_id": cve['id'],
                    "description": cve['descriptions'][0]['value'],
                    "base_score": cve.get('metrics', {}).get('cvssMetricV31', [{}])[0].get('cvssData', {}).get('baseScore', 5.0),
                    "source": f"NVD ({keyword})"
                })
            return clean_list
    except Exception as e:
        print(f"      ⚠️ Error scanning for {keyword}: {e}")
    return []

# --- 2. GOOGLE OSV SCANNER (Dynamic) ---
def fetch_google_osv(keyword):
    print(f"   🔎 SEARCHING GOOGLE OSV FOR: '{keyword}'...")
    
    url = "https://api.osv.dev/v1/query"
    # OSV requires lowercase package names
    payload = {"package": {"name": keyword.lower(), "ecosystem": "PyPI"}}
    
    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            items = response.json().get('vulns', [])[:3]
            print(f"      ✅ Found {len(items)} hits for {keyword}")
            
            clean_list = []
            for item in items:
                clean_list.append({
                    "cve_id": item.get('id'),
                    "description": item.get('details', "No details provided."),
                    "base_score": 7.5,
                    "source": f"OSV ({keyword})"
                })
            return clean_list
    except:
        pass
    return []

# --- 3. NEWS FEED (General) ---
def fetch_rss():
    # RSS is general news, so it doesn't search by keyword, it just grabs headlines
    try:
        feed = feedparser.parse("https://feeds.feedburner.com/TheHackersNews")
        clean_list = []
        for entry in feed.entries[:3]:
            clean_list.append({
                "cve_id": "NEWS",
                "description": f"{entry.title}",
                "base_score": 5.0,
                "source": "HackerNews"
            })
        return clean_list
    except:
        return []

# --- THE MAIN LOOP ---
def run_autonomous_scan(user_assets):
    all_findings = []
    
    # 1. First, get general news
    print("\n--- STEP 1: Fetching General News ---")
    all_findings.extend(fetch_rss())

    # 2. Then, loop through YOUR assets
    print(f"\n--- STEP 2: Scanning for {len(user_assets)} User Assets ---")
    
    for asset in user_assets:
        target_name = asset['name']
        
        # Scan NVD for this specific name
        all_findings.extend(fetch_nvd(target_name))
        
        # Scan OSV for this specific name
        all_findings.extend(fetch_google_osv(target_name))
        
    return all_findings