##update vehicle




from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_database"
)

# API endpoint for updating a vehicle record
@app.route('/vehicle/update', methods=['PUT'])
def update_vehicle():
    # Parse the JSON request body
    data = request.get_json()

    # Extract the values from the request body
    vin = data['VIN']
    year = data['year']
    v_type = data['V_type']
    model = data['Model']
    manufacturer = data['Manufacturer']
    color = data['color']
    customer_id = data['customer_id']

    # Create a MySQL cursor object
    mycursor = mydb.cursor()

    # Execute the SQL query to update the vehicle record
    sql = "UPDATE vehicle SET year_ = %s, V_type = %s, Model = %s, Manufacturer = %s, color = %s, customer_id = %s WHERE VIN = %s"
    val = (year, v_type, model, manufacturer, color, customer_id, vin)
    mycursor.execute(sql, val)

    # Commit the changes to the database
    mydb.commit()

    # Return a success message
    return jsonify({'message': 'Vehicle record updated successfully.'})

if __name__ == '__main__':
    app.run(debug=True)
