"""car table

Revision ID: 66dfe2bd012c
Revises: 
Create Date: 2020-11-30 18:42:55.120759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66dfe2bd012c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('condition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('license_plate', sa.String(length=140), nullable=True),
    sa.Column('brand', sa.String(length=140), nullable=True),
    sa.Column('condition_id', sa.Integer(), nullable=True),
    sa.Column('on_go', sa.String(length=64), nullable=True),
    sa.Column('price', sa.String(length=64), nullable=True),
    sa.Column('prod_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['condition_id'], ['condition.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    op.drop_table('condition')
    # ### end Alembic commands ###
