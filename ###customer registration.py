###customer registration


from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# create MySQL connection
mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="Sai@12345",
   database="woody_database"
)

# define endpoint for editing customer registration
@app.route('/customer/<int:customer_id>', methods=['PUT'])
def edit_customer(customer_id):
    # get request data
    data = request.json
    first_name = data['first_name']
    last_name = data['last_name']
    phone = data['phone']
    email = data['email']
    address = data['address']
    city = data['city']
    state = data['state']
    zip_code = data['zip_code']

    # create cursor
    mycursor = mydb.cursor()

    # execute update query
    sql = "UPDATE customer SET first_name = %s, last_name = %s, phone = %s, email = %s, address = %s, city = %s, state = %s, zip_code = %s WHERE customer_id = %s"
    val = (first_name, last_name, phone, email, address, city, state, zip_code, customer_id)
    mycursor.execute(sql, val)

    # commit changes
    mydb.commit()

    return "Customer updated successfully"

if __name__ == '__main__':
    app.run(debug=True)
