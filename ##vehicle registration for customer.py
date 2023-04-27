##vehicle registration for customer


from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# MySQL database connection settings
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sai@12345",
    database="woody_database"

# Endpoint for registering a new vehicle for a customer
@app.route('/vehicle-registration', methods=['POST'])
def register_vehicle():
    # Get the vehicle details from the request body
    vin = request.json['vin']
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    customer_id = request.json['customer_id']

    # Insert the new vehicle into the database
    cursor = db.cursor()
    query = "INSERT INTO vehicle (VIN, make, model, year, customer_id) VALUES (%s, %s, %s, %s, %s)"
    values = (vin, make, model, year, customer_id)
    cursor.execute(query, values)
    db.commit()

    # Return a success message
    return {'message': 'Vehicle registered successfully.'}

if __name__ == '__main__':
    app.run(debug=True)
