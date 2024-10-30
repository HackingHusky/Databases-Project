import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create the restaurants table
cursor.execute('''
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    cuisine TEXT NOT NULL,
    rating REAL,
    price TEXT
)
''')

# Insert sample data into the table
cursor.execute('''
INSERT INTO restaurants (name, cuisine, rating, price)
VALUES ('Sushi Place', 'Japanese', 4.5, '$$')
''')

cursor.execute('''
INSERT INTO restaurants (name, cuisine, rating, price)
VALUES ('Pizza Palace', 'Italian', 4.0, '$')
''')

cursor.execute('''
INSERT INTO restaurants (name, cuisine, rating, price)
VALUES ('Burger Joint', 'American', 4.2, '$')
''')

cursor.execute('''
INSERT INTO restaurants (name, cuisine, rating, price)
VALUES ('Taco Town', 'Mexican', 4.8, '$$')
''')

cursor.execute('''
INSERT INTO restaurants (name, cuisine, rating, price)
VALUES ('Pasta House', 'Italian', 4.1, '$$')
''')

# Commit the changes
conn.commit()

# Query the data
cursor.execute('SELECT * FROM restaurants')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()
