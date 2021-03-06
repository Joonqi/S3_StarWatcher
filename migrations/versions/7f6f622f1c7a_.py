"""empty message

Revision ID: 7f6f622f1c7a
Revises: 5e1c62a4bc54
Create Date: 2021-08-01 20:28:05.106371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f6f622f1c7a'
down_revision = '5e1c62a4bc54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('firm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ticker', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('watchlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('memo', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['ticker'], ['firm.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('watchlist')
    op.drop_table('firm')
    # ### end Alembic commands ###
