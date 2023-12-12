def create_tables(connection):
    """
    create tables
    """
    try:
        with connection.cursor() as cursor:
            with open("create_tables.sql", "r") as file:
                query = file.read()
                cursor.execute(query)
        print("Tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")
