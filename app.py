from flask import Flask
import psycopg2
import os  # <-- Import the 'os' module for environment variables

app = Flask(__name__)

def get_db_connection():
    # Read all credentials from the environment variables provided by Kubernetes
    db_host = "db" # This is the name of your Kubernetes Service for Postgres
    db_name = os.environ.get('POSTGRES_DB')
    db_user = os.environ.get('POSTGRES_USER')
    db_password = os.environ.get('POSTGRES_PASSWORD')

    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    return conn

@app.route('/')
def hello_world():
    # A simple, safe query to verify the connection works
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    cur.close()
    conn.close()

    return f"Successfully connected to PostgreSQL! Version: {db_version}"

if __name__ == '__main__':
    # This tells Flask to be accessible on all network interfaces inside the container
    app.run(host='0.0.0.0', port=5000)