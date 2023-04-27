##5 best customers api 


from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sai@12345",
  database="woody_database"
)

# API endpoint for fetching top 5 customers by total service revenue in a given time period
@app.route('/top_customers', methods=['GET'])
def get_top_customers():
    # Define begin date and end date for time period
    begin_date = '2023-04-01'
    end_date = '2023-04-30'
    
    # SQL query to fetch top 5 customers by total service revenue in the given time period
    sql_query = """
        SELECT c.customer_id, SUM(i.total_cost) AS total_revenue
        FROM customer AS c, appointment AS a, appointment_service_invoice AS a_s_i, invoice AS i
        WHERE c.customer_id = a.customer_id AND a.appointment_id = a_s_i.appointment_id 
          AND a_s_i.invoice_id = i.invoice_id AND a.date BETWEEN %s AND %s
        GROUP BY c.customer_id
        ORDER BY total_revenue DESC
        LIMIT 5;
    """
    # Execute SQL query
    cursor = db.cursor()
    cursor.execute(sql_query, (begin_date, end_date))
    result = cursor.fetchall()

    # Convert result to list of dictionaries
    top_customers = []
    for row in result:
        customer = {'customer_id': row[0], 'total_revenue': row[1]}
        top_customers.append(customer)

    return jsonify(top_customers)

if __name__ == '__main__':
    app.run()
