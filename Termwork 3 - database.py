'''Create a table to store the population and land area of the Karnataka state (Assume data) 
⦁ Create a new database called census.db. 
⦁ Make a database table called Density that will hold the name of the district (TEXT), the population (INTEGER), and the land area (REAL). 
⦁ Insert data into the table. 
⦁ Display the contents of the table. 
⦁ Display the populations. 
⦁ Display the districts that have populations of less than 1 million.
⦁ Display the districts that have populations less than 1 million or greater than 5 million.
⦁ Display the districts that do not have populations less than 1 million or greater than 5 million.
⦁ Display the populations of districts that have a land area greater than 200,000 square kilometers.
⦁ Display the districts along with their population densities (population divided by land area).'''
import sqlite3

# Create a new database and table
con = sqlite3.connect('census.db')
cur = con.cursor()

# Create table with auto-incremented id
cur.execute('''CREATE TABLE IF NOT EXISTS density1(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    province_name TEXT NOT NULL,
                    population INTEGER NOT NULL,
                    land_area REAL NOT NULL)''')

# Insert sample data
data = [
    ('Belagavi', 1000000, 200000),
    ('Karwar', 2000000, 300000),
    ('Gulbarga', 6000000, 10000),
    ('Bagalkot', 400000, 10000),
    ('Vijayapur', 400000, 10000)
]
cur.executemany('''INSERT INTO density1(province_name, population, land_area)
                   VALUES (?, ?, ?)''', data)

con.commit()

# Display all data in the table
cur.execute('''SELECT * FROM density1''')
rows = cur.fetchall()
print("\n===============================")
print("CONTENTS OF THE TABLE")
print("{:<5} {:<20} {:<15} {:<10}".format("ID", "District NAME", "POPULATION", "LAND AREA"))
for row in rows:
    print("{:<5} {:<20} {:<15} {:<10}".format(row[0], row[1], row[2], row[3]))
print("===============================\n")

# Display populations
cur.execute('''SELECT province_name, population FROM density1''')
rows = cur.fetchall()
print("\n===============================")
print("POPULATION DETAILS")
print("{:<20} {:<15}".format("District NAME", "POPULATION"))
for row in rows:
    print("{:<20} {:<15}".format(row[0], row[1]))
print("===============================\n")

# Display districts with population less than 1 million
cur.execute('''SELECT province_name, population FROM density1 WHERE population < 1000000''')
rows = cur.fetchall()
print("\n===============================")
print("DISTRICTS WITH POPULATION LESS THAN 1 MILLION")
print("{:<20} {:<15}".format("District NAME", "POPULATION"))
for row in rows:
    print("{:<20} {:<15}".format(row[0], row[1]))
print("===============================\n")

# Display districts with population less than 1 million or greater than 5 million
cur.execute('''SELECT province_name, population FROM density1 WHERE population < 1000000 OR population > 5000000''')
rows = cur.fetchall()
print("\n===============================")
print("DISTRICTS WITH POPULATION LESS THAN 1 MILLION OR GREATER THAN 5 MILLION")
print("{:<20} {:<15}".format("District NAME", "POPULATION"))
for row in rows:
    print("{:<20} {:<15}".format(row[0], row[1]))
print("===============================\n")

# Display districts with population between 1 million and 5 million
cur.execute('''SELECT province_name, population FROM density1 WHERE population > 1000000 AND population < 5000000''')
rows = cur.fetchall()
print("\n===============================")
print("DISTRICTS WITH POPULATION BETWEEN 1 MILLION AND 5 MILLION")
print("{:<20} {:<15}".format("District NAME", "POPULATION"))
for row in rows:
    print("{:<20} {:<15}".format(row[0], row[1]))
print("===============================\n")

# Display population density (population / land_area)
cur.execute('''SELECT province_name, population / land_area AS density FROM density1''')
rows = cur.fetchall()
print("\n===============================")
print("POPULATION DENSITY")
print("{:<20} {:<20}".format("District NAME", "POPULATION DENSITY"))
for row in rows:
    print("{:<20} {:<20.2f}".format(row[0], row[1]))
print("===============================\n")

# Display districts with land area greater than 200,000 square kilometers
cur.execute('''SELECT province_name, population, land_area FROM density1 WHERE land_area > 200000''')
rows = cur.fetchall()
print("\n===============================")
print("DISTRICTS WITH LAND AREA GREATER THAN 200,000 SQUARE KILOMETERS")
print("{:<20} {:<15} {:<15}".format("District NAME", "POPULATION", "LAND AREA"))
for row in rows:
    print("{:<20} {:<15} {:<15}".format(row[0], row[1], row[2]))
print("===============================\n")

# Insert a new record into the table
province_name = input("Enter District Name (text): ")
population = input("Enter Population (integer): ")
land_area = input("Enter Land Area (real): ")

cur.execute('''INSERT INTO density1(province_name, population, land_area)
               VALUES (?, ?, ?)''', (province_name, population, land_area))
con.commit()
print("\nNew record added successfully!")

# Close the connection
con.close()
