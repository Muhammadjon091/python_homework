import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("star_trek.db")
cursor = conn.cursor()

# Create the Roster table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

conn.commit()



# Insert the given values
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", roster_data)
conn.commit()




cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
conn.commit()




cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
bajorans = cursor.fetchall()

print("Bajorans in the roster:")
for name, age in bajorans:
    print(f"Name: {name}, Age: {age}")

# Close the connection
conn.close()




