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


# Deteced pii table

cursor.execute("""
CREATE TABLE IF NOT EXSITS detected_pii (
    id INTEGER PRIMARY KEY,
    document_id INTEGER NOT NULL,
    pii_type TEXT NOT NULL,
    context_snippet TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (document_id) REFERENCES tos_documents(id)
);
""")