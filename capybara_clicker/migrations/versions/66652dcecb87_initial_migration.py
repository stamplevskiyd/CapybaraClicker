"""Initial migration

Revision ID: 66652dcecb87
Revises: 
Create Date: 2025-04-07 18:44:44.789012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66652dcecb87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('click_counters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('count', sa.Integer(), server_default='0', nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('click_counters')
    op.drop_table('users')
    # ### end Alembic commands ###
