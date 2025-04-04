# 🧠 Pocket Lawyer

**“Understand what you’re agreeing to — before your data is used against you.”**

Pocket Lawyer is a browser-integrated tool that simplifies Terms of Service (TOS) and Privacy Policies into plain English — specifically targeting a 6th-grade reading level. It highlights how websites collect, use, and sell your personal information (PII), including your hobbies, interests, and online behavior.

---

## 🚀 What It Does

- ✅ Automatically detects and fetches TOS/Privacy Policy from visited websites
- ✅ Rewrites complex legal language into simple, readable summaries
- ✅ Flags risky or invasive data practices
- ✅ Tracks what PII (personal identifiable information) a site collects or shares
- ✅ Stores original and simplified versions in a local database
- ✅ Provides users with clarity on how their **interests and hobbies** are tracked online

---

## 🎯 Why It Matters

Every day, users blindly accept legal agreements they don’t understand — often giving companies permission to:

- Collect and store personal data
- Track hobbies, interests, and behaviors
- Share or sell data to third parties

**Pocket Lawyer puts that information back into users’ hands.**

---

## 🛠 How It Works

### 🧩 Tech Stack

| Layer      | Tech                      |
|------------|---------------------------|
| Frontend   | HTML/CSS/JS (Browser Extension UI) |
| Backend    | C++ or Python             |
| DB         | SQLite                    |
| Integration | Chrome Extension (Manifest V3) |
| Source Control | GitHub for transparency ✅ |

### 🗃️ Database Schema

- `tos_documents`: original & simplified TOS content
- `pii_keywords`: tracked terms (email, phone, IP, etc.)
- `detected_pii`: matched PII in each TOS
- `privacy_flags`: risky phrases with severity levels

---

## 🔐 Key Features

- ✍️ **TOS Rewriting**: Plain-English summaries of complex legal jargon
- 🔎 **PII Detection**: Find out what data is being collected/sold
- 🧠 **Privacy Risk Flagging**: Highlight high-risk phrases like “sell”, “third-party”, “retain indefinitely”
- 🌐 **Auto Detection**: Automatically runs when a user visits a known site
- 💬 **Hobby Data Awareness**: Understand how your interests (music, shows, games) are tracked and monetized

---

## 🧪 Demo Flow

1. Visit a website (e.g., amazon.com)
2. The extension automatically fetches its Privacy Policy or TOS
3. Backend rewrites and simplifies the document
4. UI displays:
   - Side-by-side TOS comparison
   - Highlighted risky phrases
   - Summary of PII being collected
5. (Optional future feature) Suggests data opt-out or deletion actions

---

## ⚡ Themes & Impact

- 🔐 **Theme: Privacy & Online Presence**
- 🎮 **Theme: Hobbies and Interests**  
Pocket Lawyer reveals how companies track and monetize personal interests — often without informed consent.

---

## 🔭 Future Features

- 🧹 Auto-scrubbing: Pre-filled opt-out request forms
- 📊 Analytics: See which companies collect which types of PII
- 🔁 Crowd-sourced TOS summaries

---

## 📂 Project Structure

pocket-lawyer/
├── backend/
│   └── simplify.py / simplify.cpp
├── extension/
│   ├── popup.html
│   ├── content.js
│   └── manifest.json
├── database/
│   ├── init_db.py
│   ├── schema.sql
├── README.md
└── .gitignore

---

## 🧑‍💻 Team & Contributions

| Role               | Name (fill in yours!)      |
|--------------------|----------------------------|
| Database Architect | Bryan (You!)               |
| Backend Developer  | [Name]                     |
| Frontend Developer | Morgan                     |
| Chrome Extension   | [Name]                     |
| Pitch & Docs       | [Name]                     |

---

## 📣 Hackathon: CougHacks 2025  
> Created in 24 hours to make the web more understandable, one TOS at a time.

---

## 📄 License
MIT — free to modify, fork, and improve.
