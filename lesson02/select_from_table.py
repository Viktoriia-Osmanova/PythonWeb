query_files = ["query_1.sql", "query_2.sql", "query_3.sql", "query_4.sql", "query_5.sql", "query_6.sql", "query_7.sql", "query_8.sql", "query_9.sql", "query_10.sql"]

def select_from_table(connection, query_files):
    """
    Select from tables using multiple queries
    """
    try:
        with connection.cursor() as cursor:
            for query_file in query_files:
                with open(query_file, "r") as file:
                    query = file.read()
                    cursor.execute(query)
                    result = cursor.fetchall()
                    print(f"Results for {query_file}:", result)
            print("SELECTs work.")
    except Exception as e:
        print(f"Error in SELECT: {e}")


