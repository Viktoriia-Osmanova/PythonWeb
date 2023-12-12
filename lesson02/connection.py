import psycopg2
from contextlib import contextmanager
from psycopg2 import OperationalError

@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    conn = None
    try:
        conn = psycopg2.connect(host='localhost', database='pyweb', user='postgres', password='VIKKI123@')
        yield conn
    except OperationalError as err:
        raise RuntimeError(f"Failed to connect to the database: {err}")
    finally:
        if conn:
            conn.close()
