##create appointment record



from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_database"
)

# API endpoint to create an appointment record
@app.route('/appointment', methods=['POST'])
def create_appointment():
    data = request.get_json()
    loc_id = data['loc_id']
    date = data['date']
    status = data['status']

    cursor = mydb.cursor()
    query = "INSERT INTO appointment (loc_id, DATE, status) VALUES (%s, %s, %s)"
    values = (loc_id, date, status)
    cursor.execute(query, values)
    mydb.commit()
    
    return jsonify({"message": "Appointment created successfully."}), 201

if __name__ == '__main__':
    app.run(debug=True)
