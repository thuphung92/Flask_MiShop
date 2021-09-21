"""empty message

Revision ID: 0c8299634e99
Revises: aed5dd658666
Create Date: 2021-09-18 19:26:39.393094

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0c8299634e99'
down_revision = 'aed5dd658666'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('img', sa.String(), nullable=True))
    op.add_column('product', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.alter_column('product', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('product', 'price',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               nullable=True)
    op.create_index(op.f('ix_product_created_on'), 'product', ['created_on'], unique=False)
    op.drop_column('product', 'image')
    op.drop_column('product', 'added_on')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('added_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('product', sa.Column('image', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_product_created_on'), table_name='product')
    op.alter_column('product', 'price',
               existing_type=sa.NUMERIC(precision=5, scale=2),
               nullable=False)
    op.alter_column('product', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.drop_column('product', 'created_on')
    op.drop_column('product', 'img')
    # ### end Alembic commands ###