import sqlite3
from datetime import datetime

def load_pii_keywords():
    conn = sqlite3.connect("pocketlawyer.db")
    cursor = conn.cursor()

    cursor.execute("SELECT keyword,")
    keywords = cursor.fetchall()

    conn.close()
    return keywords # List of tuples (keywords, pii_type)