import sqlite3

# Step 1: Connect to the database

conn = sqlite3.connect("students.db")
cursor = conn.cursor()



# Step 2: Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,name TEXT, age INTEGER)")



# Step 3: Data to insert (multiple students)

students = [(1, "murugan", 20),(2, "shanmukha", 22),(3, "subhramanya", 19),(4, "kartikeya", 21),(5, "skanda", 23)]

# Step 4: Bulk insert using executemany()
cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", students)

# Step 5: Commit and close
conn.commit()
conn.close()

print("Data inserted successfully!")
