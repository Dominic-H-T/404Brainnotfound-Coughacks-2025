import sqlite3

# Connect to the existing database
conn = sqlite3.connect("pocketlawyer.db")
cursor = conn.cursor()

# List of keyword to insert
keywords = [
    ("email address", "email", "high"),
    ("phone number", "contact", "high"),
    ("IP address", "network", "medium"),
    ("home address", "location", "high"),
    ("credit card", "payment", "high"),
    ("social security number", "identity", "high"),
    ("date of birth", "identity", "medium"),
    ("geolocation", "location", "medium"),
    ("user ID", "account", "low"),
    ("device ID", "device", "medium"),
    ("contacts", "social", "medium"),
    ("browsing history", "behavior", "medium"),
    ("biometric data", "biometric", "high")
]

# Insert each Keyword (if not already there)
for keyword, pii_type, risk in keywords:
    cursor.execute("""
        INSERT OR IGNORE INTO pii_keywords (keyword, pii_type, risk_level)
        VALUES (?, ?, ?)
    """, (keyword, pii_type, risk))

# Commit and close
conn.commit()
conn.close()

print("PII keywords seeded successfully.")