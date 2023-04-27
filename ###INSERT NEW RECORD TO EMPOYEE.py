###INSERT NEW RECORD TO EMPOYEE

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# establish connection to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_database"
)

# create cursor
cursor = mydb.cursor()

@app.route('/employee', methods=['POST'])
def add_employee():
    ssn = request.json['ssn']
    emp_name = request.json['emp_name']
    hire_date = request.json['hire_date']
    loc_id = request.json['loc_id']
    
    # insert new record into employee table
    sql = "INSERT INTO employee (SSN, emp_name, Hire_date, loc_id) VALUES (%s, %s, %s, %s)"
    val = (ssn, emp_name, hire_date, loc_id)
    cursor.execute(sql, val)
    mydb.commit()
    
    return jsonify({'message': 'New employee added.'})

if __name__ == '__main__':
    app.run(debug=True)
