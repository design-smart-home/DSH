"""start

Revision ID: f6f20899a9da
Revises: cadcc9e59a7d
Create Date: 2025-02-07 00:03:09.358752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6f20899a9da'
down_revision: Union[str, None] = 'cadcc9e59a7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('devices', sa.Column('type_device', sa.String(length=6), nullable=False))
    op.add_column('devices', sa.Column('type_value', sa.String(length=10), nullable=False))
    op.add_column('devices', sa.Column('range_value', sa.ARRAY(sa.Integer()), nullable=False))
    op.add_column('devices', sa.Column('current_value', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('devices', 'current_value')
    op.drop_column('devices', 'range_value')
    op.drop_column('devices', 'type_value')
    op.drop_column('devices', 'type_device')
    # ### end Alembic commands ###
