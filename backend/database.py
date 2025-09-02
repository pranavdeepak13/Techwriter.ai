import sqlite3
import json
from pathlib import Path

DB_PATH = Path("output/blog_writer.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        outline TEXT,
        draft TEXT,
        citations TEXT,
        evaluation TEXT,
        feedback_history TEXT,
        status TEXT DEFAULT 'in_progress'
    )
    """)
    conn.commit()
    conn.close()

def save_session(topic, outline, draft, citations, evaluation, feedback_history, status="in_progress"):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO sessions (topic, outline, draft, citations, evaluation, feedback_history, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        topic,
        outline,
        draft,
        json.dumps(citations),
        json.dumps(evaluation),
        json.dumps(feedback_history),
        status
    ))
    conn.commit()
    session_id = cur.lastrowid
    conn.close()
    return session_id

def update_session(session_id, draft, evaluation, feedback_history, status="in_progress"):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    UPDATE sessions
    SET draft = ?, evaluation = ?, feedback_history = ?, status = ?
    WHERE id = ?
    """, (
        draft,
        json.dumps(evaluation),
        json.dumps(feedback_history),
        status,
        session_id
    ))
    conn.commit()
    conn.close()

def get_session(session_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM sessions WHERE id=?", (session_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "topic": row[1],
            "outline": row[2],
            "draft": row[3],
            "citations": json.loads(row[4]),
            "evaluation": json.loads(row[5]),
            "feedback_history": json.loads(row[6]),
            "status": row[7]
        }
    return None
