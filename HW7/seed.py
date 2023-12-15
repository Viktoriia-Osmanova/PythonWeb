from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade
import random

fake = Faker()

engine = create_engine('sqlite:///testdb.db')  
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


groups = [Group(group_name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()


teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()


subjects = [Subject(subject_name=fake.word(), teacher=random.choice(teachers)) for _ in range(8)]
session.add_all(subjects)
session.commit()


students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()


for student in students:
    for subject in subjects:
        for _ in range(20):
            session.add(Grade(student=student, subject=subject, grade=random.randint(60, 100), date_received=fake.date_this_decade()))

session.commit()
