import mysql.connector
connector = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1309",
    database = "student_management"
)
cursor = connector.cursor()

print("Database connection successful!")

id = int(input("Enter your ID: "))

Name = input("Enter your name: ")

email_id = input("Enter your email ID: ")

contact_no = (input("Enter your contact number: "))

address = input("Enter your address: ")

course = input("Enter your course: ")

adhar_no = (input("enter the your adhar_number"))

sql = "INSERT INTO Students (id, Name, email_id, contact_no, address, course, adhar_no) VALUES (%s, %s, %s, %s, %s, %s, %s)"

val = (id, Name, email_id, contact_no, address, course, adhar_no)

try:
    cursor.execute(sql, val)
    connector.commit()
    print("student details added successfully")

except mysql.connector.Error as err:
    print("error")    
    
cursor.close()
connector.close()
