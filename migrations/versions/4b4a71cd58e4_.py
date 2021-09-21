"""empty message

Revision ID: 4b4a71cd58e4
Revises: 00c5363acd7d
Create Date: 2021-09-20 23:48:49.919198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b4a71cd58e4'
down_revision = '00c5363acd7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'price',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'price',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               nullable=True)
    # ### end Alembic commands ###