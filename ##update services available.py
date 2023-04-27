##update services available


from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_database"
)

# define the API endpoint for updating available services
@app.route('/services/update', methods=['POST'])
def update_services():
    # get the new service price and parts cost from the request body
    new_service_price = request.json['service_price']
    new_parts_cost = request.json['parts_cost']
    
    # get the service type and vehicle type from the request parameters
    service_type = request.args.get('service_type')
    vehicle_type = request.args.get('vehicle_type')
    
    # create a cursor object to execute MySQL queries
    mycursor = mydb.cursor()
    
    # execute the MySQL query to update the available services based on the service and vehicle types
    sql = "UPDATE service SET service_price = %s, parts_cost = %s WHERE service_type = %s AND V_type = %s"
    val = (new_service_price, new_parts_cost, service_type, vehicle_type)
    mycursor.execute(sql, val)
    
    # commit the changes to the database
    mydb.commit()
    
    # return a success message
    return 'Services updated successfully'
