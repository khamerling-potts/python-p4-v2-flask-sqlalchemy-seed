"""Initial migration.

Revision ID: 9df1ffc1ec63
Revises: 
Create Date: 2024-01-18 13:05:28.813262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9df1ffc1ec63'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###
