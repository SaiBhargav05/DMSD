
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# define MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=Sai@12345",
    database="woody_database"
)

@app.route('/technicians', methods=['POST'])
def create_technician():
    # get input data from request body
    data = request.get_json()

    # extract values from input data
    tech_SSN = data['tech_SSN']
    hourly_rate = data['hourly_rate']

    # create new technician record in database
    cursor = db.cursor()
    sql = "INSERT INTO technician (tech_SSN, hourly_rate) VALUES (%s, %s)"
    val = (tech_SSN, hourly_rate)
    cursor.execute(sql, val)
    db.commit()

    # return success message
    return jsonify({"message": "New technician created successfully."}), 201