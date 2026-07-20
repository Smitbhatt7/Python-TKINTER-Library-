import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="smit2007",   # Replace with your MySQL password
    database="CollegeDB"
)

# Create cursor
cur = con.cursor()

#id=n
#str=f"SELECT * FROM Student where id={id}"

# Execute query
cur.execute("SELECT * FROM Student")

# Fetch all records
records = cur.fetchall()

# Display records
print("Roll_No\tName\tAge\tGender\tCourse\tCity\tMarks")
print("-" * 70)

for row in records:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}")

# Close connection
cur.close()
con.close()
