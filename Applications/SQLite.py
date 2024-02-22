import sqlite3

# Connect to an SQLite database named 'example.db' (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands and interact with the database
cur = conn.cursor()

# Create a table named 'users' if it doesn't already exist, with columns for id, name, and age
cur.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,
                                                name TEXT,
                                                age INTEGER)''')

# Insert initial data into the 'users' table
cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cur.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
cur.execute("INSERT INTO users (name, age) VALUES ('Charlie', 22)")

# Update the age of the user named 'Alice' to 31
cur.execute("UPDATE users SET age = ? WHERE name = ?", (31, 'Alice'))
conn.commit()  # Commit the changes to the database

# Display the updated data from the 'users' table
print("Updated data:")
rows = cur.execute("SELECT * FROM users")
for row in rows:
    print(row)

# Delete the user named 'Bob' from the 'users' table
cur.execute("DELETE FROM users WHERE name = ?", ('Bob',))
conn.commit()  # Commit the changes to the database

# Display the updated data after deletion
print("Updated data:")
rows = cur.execute("SELECT * FROM users")

# Commit any pending changes to the disk
conn.commit()

# Query all data from the 'users' table and print it
rows = cur.execute("SELECT * FROM users") # Select all from users
for row in rows:
    print(row)

# Close the connection to the database
conn.close()
