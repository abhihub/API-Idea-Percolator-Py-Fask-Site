import sqlite3
DATABASE_NAME = "IdeaPercolator.db"

def get_db():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except Exception as er:
        print(er)

def create_tables():
    try:
        conn = get_db()
        print(conn)
        tables = [
        """CREATE TABLE IF NOT EXISTS ideas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    value TEXT ,
                    maturityLevel TEXT NOT NULL,
                    tags TEXT,
                    FullText TEXT 
                )
            """
        ]
        db = get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)
        print("ideas table created successfully")
    except Exception as er:
        print("ideas table creation failed" + er)
    finally:
        conn.close()