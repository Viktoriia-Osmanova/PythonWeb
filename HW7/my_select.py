from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models import Base, Session, Student, Grade, Subject, Teacher, Group



def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    session = Session()
    result = (
        session.query(Student, func.avg(Grade.grade).label('average_grade'))
        .join(Grade, Student.student_id == Grade.student_id)
        .group_by(Student.student_id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
    )
    session.close()
    return result

def select_2(subject_id):
    # Знайти студента із найвищим середнім балом з певного предмета.
    session = Session()
    result = (
        session.query(Student, func.avg(Grade.grade).label('average_grade'))
        .join(Grade, Student.student_id == Grade.student_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.student_id)
        .order_by(func.avg(Grade.grade).desc())
        .first()
    )
    session.close()
    return result

def select_3(subject_id):
    # Знайти середній бал у групах з певного предмета.
    session = Session()
    result = (
        session.query(Group.group_name, func.avg(Grade.grade).label('average_grade'))
        .join(Student, Group.group_id == Student.group_id)
        .join(Grade, Student.student_id == Grade.student_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.group_name)
        .all()
    )
    session.close()
    return result

# my_select.py (продовження)

def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    session = Session()
    result = (
        session.query(func.avg(Grade.grade).label('average_grade'))
        .scalar()
    )
    session.close()
    return result

def select_5(teacher_id):
    # Знайти які курси читає певний викладач.
    session = Session()
    result = (
        session.query(Subject.subject_name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    session.close()
    return result

def select_6(group_id):
    # Знайти список студентів у певній групі.
    session = Session()
    result = (
        session.query(Student.name)
        .filter(Student.group_id == group_id)
        .all()
    )
    session.close()
    return result

def select_7(group_id, subject_id):
    # Знайти оцінки студентів у окремій групі з певного предмета.
    session = Session()
    result = (
        session.query(Student.name, Grade.grade)
        .join(Grade, Student.student_id == Grade.student_id)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )
    session.close()
    return result

def select_8(teacher_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    session = Session()
    result = (
        session.query(func.avg(Grade.grade).label('average_grade'))
        .join(Subject, Grade.subject_id == Subject.subject_id)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )
    session.close()
    return result

def select_9(student_id):
    # Знайти список курсів, які відвідує певний студент.
    session = Session()
    result = (
        session.query(Subject.subject_name)
        .join(Grade, Subject.subject_id == Grade.subject_id)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )
    session.close()
    return result

def select_10(student_id, teacher_id):
    # Список курсів, які певному студенту читає певний викладач.
    session = Session()
    result = (
        session.query(Subject.subject_name)
        .join(Grade, Subject.subject_id == Grade.subject_id)
        .join(Teacher, Subject.teacher_id == Teacher.teacher_id)
        .filter(Grade.student_id == student_id, Teacher.teacher_id == teacher_id)
        .all()
    )
    session.close()
    return result

