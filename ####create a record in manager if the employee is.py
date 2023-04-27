####create a record in manager if the employee is manager


from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# create MySQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_database"
)

# create MySQL cursor
mycursor = mydb.cursor()

# create manager record for employee
@app.route('/manager/create', methods=['POST'])
def create_manager():
    manager_ssn = request.form['manager_ssn']
    salary = request.form['salary']
    
    # check if employee is a manager
    mycursor.execute("SELECT SSN FROM employee WHERE SSN = %s AND job_title = 'manager'", (manager_ssn,))
    result = mycursor.fetchone()
    
    if result is None:
        return "Employee is not a manager"
    else:
        # create manager record
        sql = "INSERT INTO manager (manager_SSN, salary) VALUES (%s, %s)"
        val = (manager_ssn, salary)
        mycursor.execute(sql, val)
        mydb.commit()
        return "Manager record created successfully"

if __name__ == '__main__':
    app.run(debug=True)
