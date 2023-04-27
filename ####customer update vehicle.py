####customer update vehicle




from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_databse"
)

# Create cursor to execute SQL queries
mycursor = mydb.cursor()

# Define API endpoint to add a new vehicle to customer's profile
@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    # Get data from request body
    data = request.get_json()
    VIN = data['VIN']
    year_ = data['year_']
    V_type = data['V_type']
    Model = data['Model']
    Manufacturer = data['Manufacturer']
    color = data['color']
    customer_id = data['customer_id']
    
    # Insert data into vehicle table
    sql = "INSERT INTO vehicle (VIN, year_, V_type, Model, Manufacturer, color, customer_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (VIN, year_, V_type, Model, Manufacturer, color, customer_id)
    mycursor.execute(sql, val)
    mydb.commit()
    
    # Return success message
    return jsonify({'message': 'Vehicle added successfully!'})

if __name__ == '__main__':
    app.run()
