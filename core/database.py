import os
import sqlite3 as sq


def init_db():
    """Create the data folder (if missing) and ensure the WEBSITES_DATA table exists."""
    os.makedirs('data', exist_ok=True)

    connection = sq.connect('data/websites.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WEBSITES_DATA(
            WEBSITE_NAME VARCHAR(50),
            WEBSITE_URL VARCHAR(150) PRIMARY KEY,
            RESPONSE_TIME REAL,
            STATUS VARCHAR(10)

        )
    ''')

    connection.commit()
    connection.close()