#update service price


from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Define MySQL database connection details
mysql_config = {
    'user': 'root',
    'password': 'Sai@12345',
    'host': 'localhost',
    'database': 'woody_databse'
}

# Define Flask API endpoint for updating service price
@app.route('/update-service-price', methods=['PUT'])
def update_service_price():
    # Connect to MySQL database
    db = mysql.connector.connect(**mysql_config)
    cursor = db.cursor()

    # Extract service type and vehicle type from request body
    service_type = request.json['service_type']
    vehicle_type = request.json['vehicle_type']

    # Extract new service price and parts cost from request body
    service_price = request.json['service_price']
    parts_cost = request.json['parts_cost']

    # Execute SQL query to update service price in the database
    query = f"""UPDATE service
                SET service_price = {service_price}, parts_cost = {parts_cost}
                WHERE service_type = '{service_type}' AND V_type = '{vehicle_type}'"""
    cursor.execute(query)

    # Commit changes to the database and close the connection
    db.commit()
    db.close()

    # Return success response
    return {'message': f'Service price for {service_type} on {vehicle_type} updated successfully.'}

if __name__ == '__main__':
    app.run()
