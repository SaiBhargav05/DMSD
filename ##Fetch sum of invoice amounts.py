##Fetch sum of invoice amounts for appointments between start date and end date range.

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# define MySQL database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_database"
)

# define API endpoint for fetching invoice sum
@app.route('/invoice-sum/<start_date>/<end_date>')
def invoice_sum(start_date, end_date):
    # execute SQL query to fetch sum of invoice amounts for appointments between start and end date range
    mycursor = mydb.cursor()
    query = "SELECT SUM(i.total_charge) FROM invoice AS i, appointment_service_invoice AS a_s_i, appointment AS a WHERE i.invoice_id = a_s_i.invoice_id AND a_s_i.appointment_id = a.appointment_id AND a.DATE BETWEEN %s AND %s"
    values = (start_date, end_date)
    mycursor.execute(query, values)
    result = mycursor.fetchone()

    # return result as JSON
    return jsonify({'invoice_sum': result[0]})

# run the API
if __name__ == '__main__':
    app.run(debug=True)
