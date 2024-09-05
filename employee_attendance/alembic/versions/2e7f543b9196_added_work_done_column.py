"""added work done column

Revision ID: 2e7f543b9196
Revises: 6ee27155b4d1
Create Date: 2024-09-05 16:06:31.001020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e7f543b9196'
down_revision: Union[str, None] = '6ee27155b4d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attendances', sa.Column('work_done', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('attendances', 'work_done')
    # ### end Alembic commands ###
