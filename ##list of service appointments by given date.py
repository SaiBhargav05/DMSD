##list of service appointments by given date and location


from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    host="localhost",
    user="root",
    password="Sai@12345",
    database="woody_database"
}

# Endpoint to list service appointments by date and location
@app.route('/appointments', methods=['GET'])
def get_appointments():
    # Get date and location from query parameters
    date = request.args.get('date')
    location = request.args.get('location')

    # Connect to MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Query appointments
    query = '''
            SELECT a_s_i.service_type
            FROM appointment AS a, location AS l, appointment_service_invoice AS a_s_i
            WHERE a.appointment_id = a_s_i.appointment_id 
            AND l.loc_id = a.loc_id 
            AND a.DATE = %s 
            AND l.loc_id = %s
            '''
    params = (date, location)
    cursor.execute(query, params)

    # Get results and return as JSON
    appointments = [result[0] for result in cursor.fetchall()]
    conn.close()
    return jsonify(appointments)

if __name__ == '__main__':
    app.run(debug=True)
