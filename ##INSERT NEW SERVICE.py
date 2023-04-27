##INSERT NEW SERVICE


from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# create a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_database"
)

# create a cursor object to execute MySQL queries
mycursor = mydb.cursor()

# create a route for creating a new service
@app.route('/services', methods=['POST'])
def create_service():
    # get the service details from the request body
    service_type = request.json['service_type']
    v_type = request.json['v_type']
    service_price = request.json['service_price']
    parts_cost = request.json['parts_cost']

    # create a new service record in the database
    sql = "INSERT INTO service (service_type, V_type, service_price, parts_cost) VALUES (%s, %s, %s, %s)"
    val = (service_type, v_type, service_price, parts_cost)
    mycursor.execute(sql, val)
    mydb.commit()

    return "Service created successfully", 201

if __name__ == '__main__':
    app.run(debug=True)


