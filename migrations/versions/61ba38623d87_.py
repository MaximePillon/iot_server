"""empty message

Revision ID: 61ba38623d87
Revises: f6d4f756d07c
Create Date: 2018-12-13 11:55:40.133800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61ba38623d87'
down_revision = 'f6d4f756d07c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensor',
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.Column('voltage', sa.Integer(), nullable=True),
    sa.Column('is_activated', sa.Boolean(), nullable=True),
    sa.Column('data_type', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('station_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['station_id'], ['station.station_id'], ),
    sa.PrimaryKeyConstraint('sensor_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sensor')
    # ### end Alembic commands ###
