## update appointment status


from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    host="localhost",
    user="root",
    password="Sai@12345",
    database="woody_database"
}

# Endpoint to update the status of an appointment
@app.route('/appointments/<int:appointment_id>/status', methods=['PUT'])
def update_appointment_status(appointment_id):
    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Get the new status from the request body
    new_status = request.json.get('status')

    # Update the status of the appointment with the given ID
    update_query = "UPDATE appointment SET status = %s WHERE appointment_id = %s"
    cursor.execute(update_query, (new_status, appointment_id))

    # Commit the changes to the database
    cnx.commit()

    # Close the database connection
    cursor.close()
    cnx.close()

    return f"Appointment {appointment_id} status updated to {new_status}"

if __name__ == '__main__':
    app.run()


You can then make a PUT request to the endpoint with the appointment ID and the new status in the request body:


PUT /appointments/500/status
Content-Type: application/json

{
    "status": "completed"
}