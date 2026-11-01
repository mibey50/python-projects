import sqlite3

connection = sqlite3.connect("water.db")
cursor = connection.cursor()


cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meter_no TEXT,
    name TEXT,
    previous INTEGER,
    current INTEGER,
    status TEXT
)
""")

rows = [
    ("M001", "Wanjiku Kamau", 120, 135, "Unpaid"),
    ("M002", "Otieno Ochieng", 300, 308, "Paid"),
    ("M003", "Chebet Rono", 50, 72, "Unpaid"),
    ("M004", "Mwangi Njoroge", 410, 430, "Unpaid"),
]
cursor.executemany(
    "INSERT INTO customers (meter_no, name, previous, current, status) VALUES (?, ?, ?, ?, ?)",
    rows,
)
connection.commit()


for row in cursor.execute("SELECT * FROM customers"):
    print(row)

connection.close()
