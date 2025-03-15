from mysql.connector import connect as MySQLConnect
import db.config as config

# Database configuration for MySQL
DB_CONFIG = {
    "host": config.DB_HOST,
    "user": config.DB_USER,
    "password": config.DB_PASSWORD,
    "database": config.DB_NAME,
    "port": int(config.DB_PORT)
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