##ADDING service to appointment

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# define MySQL connection settings
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sai@12345",
    database="woody_database"
)

# define API endpoint for adding a service to an appointment
@app.route('/add_service_to_appointment', methods=['POST'])
def add_service_to_appointment():
    # retrieve data from POST request
    appointment_id = request.form.get('appointment_id')
    invoice_id = request.form.get('invoice_id')
    service_type = request.form.get('service_type')
    V_type = request.form.get('V_type')
    price = request.form.get('price')
    
    # define MySQL query to insert new record into appointment_service_invoice table
    sql = "INSERT INTO appointment_service_invoice (appointment_id, invoice_id, service_type, V_type, price) \
           VALUES (%s, %s, %s, %s, %s)"
    
    # execute MySQL query with data from POST request
    cursor = mydb.cursor()
    cursor.execute(sql, (appointment_id, invoice_id, service_type, V_type, price))
    mydb.commit()
    
    # return success message
    return jsonify({"message": "Service added to appointment successfully!"})
