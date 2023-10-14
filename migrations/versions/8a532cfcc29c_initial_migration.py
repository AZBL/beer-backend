"""Initial migration

Revision ID: 8a532cfcc29c
Revises: 
Create Date: 2023-09-27 13:05:10.378561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a532cfcc29c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firebase_uid', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('firebase_uid')
    )
    op.create_table('beers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brewery', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('abv', sa.Float(), nullable=True),
    sa.Column('style', sa.String(length=75), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('comments', sa.String(length=500), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('beers')
    op.drop_table('users')
    # ### end Alembic commands ###
