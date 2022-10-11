# Write the syntax to do the following

# 1. Connect to database

# 2. Create a table in database

# 3. Insert record in table

# 4. Update a value in table

# 5. Delete a row from table 

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="assi"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
val = ("John", 21)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

sql = "UPDATE students SET age = %s WHERE name = %s"
val = (22, "John")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

sql = "DELETE FROM students WHERE name = %s"
val = ("John",)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
