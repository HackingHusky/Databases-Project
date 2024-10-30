Restaurant Database
This repository contains a simple SQLite database for storing restaurant information. The database includes details such as the name, cuisine type, rating, and price range of each restaurant.

Project Objectives
Store data in a database

Create a schema for the database using SQLite

Populate the database with sample data

Query the database to retrieve and display data

Installation
Clone the repository:

sh

Copy
git clone https://github.com/yourusername/restaurant-database.git
Navigate to the project directory:

sh

Copy
cd restaurant-database
Usage
Run the main.py script:

sh

Copy
python main.py
The script will create a SQLite database (example.db) and populate it with sample data. It will then query the database and print the results to the console.

Code
python

Copy
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
Contributing
Feel free to fork this repository, submit issues, and make pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.
