"""
Run this script ONCE after setting up your database to insert demo users with correct password hashes.

Usage:
  python seed.py
"""

from werkzeug.security import generate_password_hash
import MySQLdb

conn = MySQLdb.connect(
    host='localhost',       # change to 'db' if running inside Docker
    user='devlog_user',
    password='devlog_pass',
    db='devlog_db',
)
cur = conn.cursor()

users = [
    ('keerti', 'demo123', 'KT'),
    ('arjun',  'demo123', 'AR'),
    ('meera',  'demo123', 'MS'),
]

print("Inserting demo users...")
for username, password, initials in users:
    pw_hash = generate_password_hash(password)
    try:
        cur.execute(
            "INSERT IGNORE INTO users (username, password_hash, avatar_initials) VALUES (%s, %s, %s)",
            (username, pw_hash, initials)
        )
        print(f"  ✓ {username}")
    except Exception as e:
        print(f"  ✗ {username}: {e}")

conn.commit()
cur.close()
conn.close()
print("\nDone! Login with username=keerti password=demo123")
