import sqlite3

# Connect to or create the data base file
conn = sqlite3.connect('pocketlawyer.db')
cursor = conn.cursor()


# pii keywords table
cursor.execute("""
CREATE TABLE IF NOT EXISTS pii_keywords (
    id INTGER PRIMARY KEY,
    keyword TEXT NOT NULL,
    pii_type TEXT NOT NULL,
    risk_level TEXT
);
""")


# Detected pii table

cursor.execute("""
CREATE TABLE IF NOT EXISTS detected_pii (
    id INTEGER PRIMARY KEY,
    document_id INTEGER NOT NULL,
    pii_type TEXT NOT NULL,
    context_snippet TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (document_id) REFERENCES tos_documents(id)
);
""")

# Create privacy_flags

cursor.execute("""
CREATE TABLE IF NOT EXISTS privacy_flags (
    id INTEGER PRIMARY KEY,
    keyword TEXT NOT NULL,
    flag_level TEXT NOT NULL,
    description TEXT
);
""")

# Save changes and close the connection
conn.commit()
conn.close()

print("PII tracking database initialized.")
