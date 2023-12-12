from connection import create_connection
from create_table import create_tables
from insert_data import insert_data
from select_from_table import select_from_table, query_files

def main():
    # create connection using context manager
    with create_connection() as connection:
        try:
            # tables creation
            create_tables(connection)

            # insert into tables
            insert_data(connection)

            # queries
            select_from_table(connection, query_files)

        except Exception as e:
            print(f"Error executing SQL queries: {e}")

if __name__ == "__main__":
    main()
