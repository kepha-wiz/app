"""Add student level to User model

Revision ID: 649a75408658
Revises: bb557b58b69c
Create Date: 2025-05-21 09:06:49.011496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '649a75408658'
down_revision = 'bb557b58b69c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_level', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('student_level')

    # ### end Alembic commands ###
