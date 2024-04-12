import os
import pymysql
from pymysql.constants import CLIENT

def check_db_connection():
    try:
        # Retrieve database connection details from environment variables
        db_host = os.environ.get("DB_HOST")
        db_port = os.environ.get("DB_PORT")
        db_name = os.environ.get("DB_NAME")
        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")

        conn = pymysql.connect(
            host=db_host,
            port=int(db_port),
            database=db_name,
            user=db_user,
            password=db_password,
            ssl={'ssl': {'ssl_version': 'TLSv1_2'}}
        )
        print("Successfully connected to the database!")
        conn.close()
    except Exception as e:
        print("Failed to connect to the database:", e)

if __name__ == "__main__":
    check_db_connection()
