
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '2bf8bb6b8b58'
down_revision: Union[str, None] = '970e3b09911e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('quanityquantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
  


def downgrade() -> None:
 
    op.drop_table('rooms')
 
