
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'students',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('group_id', sa.Integer(), sa.ForeignKey('groups.id')),
    )

    op.create_table(
        'groups',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('group_name', sa.String(), nullable=False),
    )

    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
    )

    op.create_table(
        'subjects',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('subject_name', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id')),
    )

    op.create_table(
        'grades',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id')),
        sa.Column('subject_id', sa.Integer(), sa.ForeignKey('subjects.id')),
        sa.Column('grade', sa.Integer(), nullable=False),
        sa.Column('date_received', sa.Date(), nullable=False),
    )

def downgrade():
    op.drop_table('grades')
    op.drop_table('subjects')
    op.drop_table('teachers')
    op.drop_table('groups')
    op.drop_table('students')
