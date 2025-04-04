import sqlite3
import os

# Always resolve path relative to this script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "database", "pocketlawyer.db")


def load_pii_keywords():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT keyword, pii_type FROM pii_keywords")
    keywords = cursor.fetchall()

    conn.close()
    return keywords

def scan_text_for_pii(document_id, text):
    keywords = load_pii_keywords()
    results = []

    for keyword, pii_type in keywords:
        if keyword.lower() in text.lower():
            start = text.lower().find(keyword.lower())
            snippet = text[max(0, start - 30):start + len(keyword) + 30]
            results.append((document_id, pii_type, snippet.strip()))
    return results

def save_pii_results(results):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for document_id, pii_type, snippet in results:
        cursor.execute("""
            INSERT INTO detected_pii (document_id, pii_type, context_snippet)
            VALUES (?, ?, ?)
        """, (document_id, pii_type, snippet))

    conn.commit()
    conn.close()

def test_scan_from_file(file_path, document_id=1):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tos_text = file.read()

        matches = scan_text_for_pii(document_id, tos_text)

        if matches:
            save_pii_results(matches)
            print("✅ PII found and logged:")
            for match in matches:
                print(f"- Type: {match[1]} | Snippet: {match[2]}")
        else:
            print("✅ No PII found in the document.")
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")

if __name__ == "__main__":
    test_scan_from_file("example_tos.txt", document_id=1)
