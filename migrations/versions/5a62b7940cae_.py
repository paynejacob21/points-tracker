"""empty message

Revision ID: 5a62b7940cae
Revises: 4e4bd2f0e8a4
Create Date: 2015-06-28 22:43:36.138926

"""

# revision identifiers, used by Alembic.
revision = '5a62b7940cae'
down_revision = '4e4bd2f0e8a4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'audio', ['filename'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'audio', type_='unique')
    ### end Alembic commands ###
