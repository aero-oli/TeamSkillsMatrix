"""Add training_category to Skill model

Revision ID: 64ddf8620e2d
Revises: 03eee33d9efb
Create Date: 2025-04-11 20:19:28.692047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64ddf8620e2d'
down_revision = '03eee33d9efb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('skill', schema=None) as batch_op:
        batch_op.add_column(sa.Column('training_category', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('skill', schema=None) as batch_op:
        batch_op.drop_column('training_category')

    # ### end Alembic commands ###
