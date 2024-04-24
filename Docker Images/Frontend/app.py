# app.py
from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# MySQL configuration
'''mysql_host = "mysql-service"
mysql_user = "root"
mysql_password = "your-root-password"
mysql_database = "user_details"

# Initialize MySQL connection
db = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user details from the form
        name = request.form.get('name')
        email = request.form.get('email')

        # Insert user details into MySQL
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        cursor.close()

    # Retrieve all users from MySQL
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()

    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
