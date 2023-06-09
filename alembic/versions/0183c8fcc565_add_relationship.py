"""Add relationship

Revision ID: 0183c8fcc565
Revises: ce35ede9155b
Create Date: 2023-05-16 23:51:09.389103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0183c8fcc565'
down_revision = 'ce35ede9155b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weather', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_weather_city_id_city', 'city', ['city_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weather', schema=None) as batch_op:
        batch_op.drop_constraint('fk_weather_city_id_city', type_='foreignkey')

    # ### end Alembic commands ###
