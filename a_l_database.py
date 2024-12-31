import sqlite3
con = sqlite3.connect("culture_lib.db")

cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Languages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT
)WITHOUT ROWID;""")

cur.execute("""CREATE TABLE IF NOT EXISTS Countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT
)WITHOUT ROWID;""")

cur.execute("""CREATE TABLE IF NOT EXISTS Cultures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT
)WITHOUT ROWID;""")

cur.execute("""CREATE TABLE IF NOT EXISTS Meanings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT
)WITHOUT ROWID; """)
    
cur.execute("""CREATE TABLE IF NOT EXISTS Expressions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type TEXT,
    language_id INT,
    country_id INT,
    culture_id INT,
    description TEXT,
    meaning_id INT,
    FOREIGN KEY(language_id) REFERENCES Languages(id),
    FOREIGN KEY(country_id) REFERENCES Countries(id),
    FOREIGN KEY(culture_id) REFERENCES Cultures(id),
    FOREIGN KEY(meaning_id) REFERENCES Meanings(id)
)WITHOUT ROWID; """) 

# An example
cur.execute("""INSERT INTO Languages
            VALUES(1, 'English'); """)

cur.execute("""INSERT INTO Countries
            VALUES(1, 'United Kingdom'); """)

cur.execute("""INSERT INTO Cultures
            VALUES(1, 'English'); """)

cur.execute("""INSERT INTO Meanings
            VALUES(1, ' engagement and confidence'); """)

cur.execute("""INSERT INTO Expressions
            VALUES(1, 'Gesture', 1, 1, 1, 'direct eye contact', 1); """)

con.commit()
