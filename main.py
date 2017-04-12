import sqlite3

# Connect to database
def connectToDatabase():
    conn = sqlite3.connect('company.db')
    print 'Opened database successfully!'

    try:
        conn.execute('''CREATE TABLE COMPANY
                (ID INT PRIMARY KEY     NOT NULL,
                NAME            TEXT    NOT NULL,
                AGE             INT     NOT NULL,
                ADDRESS         CHAR(50),
                SALARY          REAL);''')
    except sqlite3.OperationalError:
        None

    print 'Table created successfully!'
    conn.close()

# Insert employee into database
def insertEmployeeToDatabase(emp_id, name, age, address, salary):
    conn = sqlite3.connect('company.db')
    print 'Opened database successfully'

    conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
            VALUES (?, ?, ?, ?, ?)", (emp_id, name, age, address, salary));
    conn.commit()
    print 'Inserted into database'
    conn.close()

# Displays all current records in the database
def displayAllRecords():
    conn = sqlite3.connect('company.db')
    print 'Opened database successfully'

    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]
        print "ADDRESS = ", row[2]
        print "SALARY = ", row[3], "\n"

    print "Operation done successfully";
    conn.close()


# Main method
if __name__ == "__main__":
    connectToDatabase()
    emp_id = int(raw_input('Enter id: '))
    name = raw_input("Enter name: ")
    age = int(raw_input("Enter age: "))
    address = raw_input("Enter address: ")
    salary = float(raw_input("Enter salary: "))
    insertEmployeeToDatabase(emp_id, name, age, address, salary)
    displayAllRecords()
