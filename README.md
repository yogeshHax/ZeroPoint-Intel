🔐 Zeropoint Intel
Autonomous Security Threat Intelligence Aggregator
📌 Project Description

Zeropoint Intel is an autonomous, asset-aware threat intelligence platform designed to help cybersecurity teams identify, correlate, and prioritize security threats effectively.

The platform aggregates threat intelligence from multiple public sources such as CVE databases and security advisories, normalizes fragmented data, extracts key security entities, and correlates related threats. By combining technical severity scores with user-defined asset criticality, Zeropoint Intel generates risk-scored alerts that help organizations focus on the most impactful vulnerabilities first.

This approach reduces manual monitoring, minimizes alert fatigue, and enables faster, more informed security decision-making.

⚙️ Tech Stack

Frontend

HTML

CSS

JavaScript

Backend

Python (REST APIs)

Node.js

Database

MongoDB

External Data Sources

NVD (CVE Database)

GitHub Security Advisories

RSS Feeds

🛠️ Setup Instructions
1️⃣ Clone the Repository
git clone <repository-url>
cd zeropoint-intel

2️⃣ Backend Setup
cd backend
pip install -r requirements.txt
python main.py

3️⃣ Frontend Setup
cd frontend
npm install
npm start

4️⃣ Database Setup

Install MongoDB locally or use MongoDB Atlas

Ensure MongoDB is running before starting the backend

🔐 Environment Variables

Create a .env file inside the backend folder and add:

MONGO_URI=your_mongodb_connection_string
NVD_API_KEY=your_nvd_api_key
PORT=5000


⚠️ Do not commit .env files to GitHub

📁 Project Structure Template
zeropoint-intel/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   └── requirements.txt
│
├── database/
│
├── README.md
└── .gitignore

👥 Team Members

Team Name: GeniusMinds

Name	Branch	Year
Nitesh Barnwal	CSE	Second Year
Sunny Kumar	CSE	Second Year
Raj Singh	CSE	Second Year
Yogesh Prasad	CSE	First Year
🚀 Project Highlights

Multi-source threat intelligence aggregation

Automated threat correlation

Asset-aware risk scoring

Prioritized alerts for critical assets

Interactive dashboards and search

📜 License

This project was developed as part of the CODE@FROST Hackathon and is intended for educational and evaluation purposes.
