import os

import psycopg2
from dotenv import load_dotenv
load_dotenv()

def create_connection():
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database_name = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection = psycopg2.connect(
    host = host,
    port = port,
    database = database_name,
    user = user,
    password = password
    )
    return connection
