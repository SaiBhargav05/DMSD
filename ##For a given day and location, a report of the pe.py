##For a given day and location, a report of the pending service appointments



from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database connection configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sai@12345",
    database="woody_database"
)

# API endpoint to fetch pending service appointments for a given day and location
@app.route('/appointments/pending', methods=['GET'])
def get_pending_appointments():
    location_id = request.args.get('location_id')
    day = request.args.get('day')

    cursor = db.cursor()
    query = "SELECT a_s.service_type " \
            "FROM appointment AS a, location AS l, appointment_service AS a_s, appointment_service_invoice AS a_s_i " \
            "WHERE a.loc_id = l.loc_id " \
            "AND a.appointment_id = a_s.appointment_id " \
            "AND a_s.appointment_service_id = a_s_i.appointment_service_id " \
            "AND a.status = 'pending' " \
            f"AND l.loc_id = '{location_id}' " \
            f"AND a.day = '{day}';"
    cursor.execute(query)
    results = cursor.fetchall()

    # Build response
    response = {
        "location_id": location_id,
        "day": day,
        "pending_appointments": []
    }
    for row in results:
        service_type = row[0]
        response["pending_appointments"].append(service_type)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
