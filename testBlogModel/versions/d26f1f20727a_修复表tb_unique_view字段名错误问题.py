"""修复表tb_unique_view字段名错误问题

Revision ID: d26f1f20727a
Revises: f61da4087031
Create Date: 2021-05-20 11:28:08.995740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd26f1f20727a'
down_revision = 'f61da4087031'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_unique_view', sa.Column('views_count', sa.Integer(), nullable=False, comment='访问量'))
    op.drop_column('tb_unique_view', 'view_count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_unique_view', sa.Column('view_count', sa.INTEGER(), autoincrement=False, nullable=False, comment='访问量'))
    op.drop_column('tb_unique_view', 'views_count')
    # ### end Alembic commands ###
