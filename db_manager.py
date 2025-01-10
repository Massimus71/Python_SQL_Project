import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=database
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def insert_query_log(self, query_type, query_text):
        query = """
        INSERT INTO query_logs (query_type, query_text, search_count) 
        VALUES (%s, %s, 1) 
        ON DUPLICATE KEY UPDATE search_count = search_count + 1;
        """
        self.cursor.execute(query, (query_type, query_text))
        self.connection.commit()

    def get_popular_queries(self):
        query = """
        SELECT query_text, SUM(search_count) as total_searches 
        FROM query_logs 
        GROUP BY query_text 
        ORDER BY total_searches DESC 
        LIMIT 10;
        """
        return self.execute_query(query)

    def close(self):
        self.cursor.close()
        self.connection.close()
