import sqlite3

db_path = 'app/data/marks.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print('Tables in database:')
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for t in tables:
    print(t[0])
conn.close()
