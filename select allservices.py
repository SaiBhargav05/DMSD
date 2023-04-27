##select* services api



from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
config = {
    host="localhost",
    user="root",
    password="Sai@12345",
    database="woody_database"
}

# API endpoint to fetch all services
@app.route('/services', methods=['GET'])
def get_services():
    # Establish a MySQL connection
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Execute the query to fetch all services
    cursor.execute("SELECT * FROM service")
    services = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return the services as JSON response
    return jsonify(services)

if __name__ == '__main__':
    app.run(debug=True)
