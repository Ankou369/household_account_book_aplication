import sqlite3

conn = sqlite3.connect("kakeibo.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY,
        date TEXT,
        item TEXT,
        price INTEGER
    )
""")

conn.commit()
conn.close()

print("テーブル作成成功")