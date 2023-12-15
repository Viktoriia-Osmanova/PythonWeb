from HW7.my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10
from seed import seed_data
from migration_create_tables import create_tables
from models import Session



def main():
    # Створення таблиць
    create_tables()

    # Заповнення бази даних тестовими даними
    seed_data()

    # Виконання запитів
    result_1 = select_1()
    print("Query 1 Result:", result_1)

    subject_id = 1  # Вкажіть id предмета
    result_2 = select_2(subject_id)
    print("Query 2 Result:", result_2)

    result_3 = select_3(subject_id)
    print("Query 3 Result:", result_3)

    result_4 = select_4()
    print("Query 4 Result:", result_4)

    teacher_id = 1  # Вкажіть id викладача
    result_5 = select_5(teacher_id)
    print("Query 5 Result:", result_5)

    group_id = 1  # Вкажіть id групи
    result_6 = select_6(group_id)
    print("Query 6 Result:", result_6)

    result_7 = select_7(group_id, subject_id)
    print("Query 7 Result:", result_7)

    result_8 = select_8(teacher_id)
    print("Query 8 Result:", result_8)

    student_id = 1  # Вкажіть id студента
    result_9 = select_9(student_id)
    print("Query 9 Result:", result_9)

    result_10 = select_10(student_id, teacher_id)
    print("Query 10 Result:", result_10)

if __name__ == "__main__":
    main()
