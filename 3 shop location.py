

#######Fetch list of top 3 shop locations in descending order of sum of invoice amount for appointments between start date and end date.

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Database Connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_database"
)

# Fetch list of top 3 shop locations in descending order of sum of invoice amount for appointments between start date and end date
@app.route('/top-locations', methods=['GET'])
def top_locations():
    cursor = mydb.cursor()
    query = """SELECT l.loc_id, l.loc_name, SUM(i.total_charge) as total_invoice_amount
               FROM location AS l, appointment AS a, appointment_service_invoice AS a_s_i, invoice AS i
               WHERE l.loc_id = a.loc_id AND a.appointment_id = a_s_i.appointment_id AND a_s_i.invoice_id = i.invoice_id AND a.DATE BETWEEN '2023-04-05' AND '2023-04-09'
               GROUP BY l.loc_id
               ORDER BY total_invoice_amount DESC
               LIMIT 3"""
    cursor.execute(query)
    results = cursor.fetchall()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
