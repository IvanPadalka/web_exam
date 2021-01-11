"""Some migration.

Revision ID: 70a67c8baa2c
Revises: 66dfe2bd012c
Create Date: 2021-01-11 12:56:52.584966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70a67c8baa2c'
down_revision = '66dfe2bd012c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('description', sa.String(length=640), nullable=True))
    op.add_column('car', sa.Column('link', sa.String(length=64), nullable=True))
    op.drop_constraint(None, 'car', type_='foreignkey')
    op.create_foreign_key(None, 'car', 'condition', ['on_go'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'car', type_='foreignkey')
    op.create_foreign_key(None, 'car', 'condition', ['condition_id'], ['id'])
    op.drop_column('car', 'link')
    op.drop_column('car', 'description')
    # ### end Alembic commands ###