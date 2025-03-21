from mysql.connector import connect as MySQLConnect
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Database configuration for MySQL
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT"))
}

class MySQLConnection:
    def __init__(self):
        self.conn = MySQLConnect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)
    
    def execute(self, query, params=None):
        self.cursor.execute(query, params)

    def fetchone(self):
        return self.cursor.fetchone()
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def commit(self):
        self.conn.commit()
    
    def close(self):
        self.cursor.close()
        self.conn.close()