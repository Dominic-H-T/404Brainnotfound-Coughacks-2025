import sqlite3

# Set your full absolute path here, or adjust as needed
DB_PATH = r"C:\Users\Bryan Harris\PycharmProjects\404Brainnotfound-Coughacks-2025\Pocket-Lawyer\data_tracking\database\pocketlawyer.db"

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create pii_keywords table
cursor.execute("""
CREATE TABLE IF NOT EXISTS pii_keywords (
    id INTEGER PRIMARY KEY,
    keyword TEXT NOT NULL,
    pii_type TEXT NOT NULL,
    risk_level TEXT
);
""")

# Create detected_pii table
cursor.execute("""
CREATE TABLE IF NOT EXISTS detected_pii (
    id INTEGER PRIMARY KEY,
    document_id INTEGER NOT NULL,
    pii_type TEXT NOT NULL,
    context_snippet TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Create privacy_flags table (optional)
cursor.execute("""
CREATE TABLE IF NOT EXISTS privacy_flags (
    id INTEGER PRIMARY KEY,
    keyword TEXT NOT NULL,
    flag_level TEXT NOT NULL,
    description TEXT
);
""")

# Finalize
conn.commit()
conn.close()

print("✅ PII tracking database initialized successfully.")
