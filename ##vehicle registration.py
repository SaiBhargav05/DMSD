##vehicle registration 


from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Set up MySQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_database"
)

@app.route('/vehicle', methods=['POST'])
def create_vehicle():
    # Get request data
    data = request.get_json()
    VIN = data['VIN']
    year_ = data['year']
    V_type = data['V_type']
    Model = data['Model']
    Manufacturer = data['Manufacturer']
    color = data['color']
    customer_id = data['customer_id']

    # Create cursor
    mycursor = mydb.cursor()

    # SQL query to insert new vehicle
    sql = "INSERT INTO vehicle (VIN, year_, V_type, Model, Manufacturer, color, customer_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (VIN, year_, V_type, Model, Manufacturer, color, customer_id)
    mycursor.execute(sql, val)

    # Commit changes to database
    mydb.commit()

    # Return success message
    return {'message': 'New vehicle created successfully.'}, 201

if __name__ == '__main__':
    app.run(debug=True)
