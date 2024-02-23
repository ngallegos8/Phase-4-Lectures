"""Create tables

Revision ID: 79d4edbad158
Revises: 448e459af673
Create Date: 2024-02-23 10:01:07.309006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79d4edbad158'
down_revision = '448e459af673'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('productions', schema=None) as batch_op:
        batch_op.alter_column('genre',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('productions', schema=None) as batch_op:
        batch_op.alter_column('genre',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###