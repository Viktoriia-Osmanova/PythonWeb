from faker import Faker
import random
from connection import create_connection

fake = Faker()

def insert_data(connection):
    """
    Insert data into tables
    """
    try:
        with connection.cursor() as cursor:
            # Наповнення таблиці груп
            for _ in range(3):
                cursor.execute("INSERT INTO groups (group_name) VALUES (%s);", (fake.word(),))

            # Наповнення таблиці викладачів
            for _ in range(5):
                cursor.execute("INSERT INTO teachers (name) VALUES (%s);", (fake.name(),))

            # Наповнення таблиці предметів
            for _ in range(8):
                cursor.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s);", (fake.word(), random.randint(1, 5)))

            # Наповнення таблиці студентів
            for _ in range(50):
                cursor.execute("INSERT INTO students (name, group_id) VALUES (%s, %s);", (fake.name(), random.randint(1, 3)))

            # Наповнення таблиці оцінок
            for student_id in range(1, 51):
                for subject_id in range(1, 9):
                    for _ in range(20):
                        cursor.execute(
                            "INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s);",
                            (student_id, subject_id, random.randint(60, 100), fake.date_this_decade())
                        )

            # Збереження змін у базі даних
            connection.commit()

    except Exception as e:
        print(f"Error inserting data: {e}")
