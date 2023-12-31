"""Добавил каскадное удаление желаний, при удалении пользовтаеля

Revision ID: 6a7dad382601
Revises: fdff643eea05
Create Date: 2023-12-09 16:15:53.313438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a7dad382601'
down_revision: Union[str, None] = 'fdff643eea05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('desire_user_id_fkey', 'desire', type_='foreignkey')
    op.create_foreign_key(None, 'desire', 'user', ['user_id'], ['telegram_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'desire', type_='foreignkey')
    op.create_foreign_key('desire_user_id_fkey', 'desire', 'user', ['user_id'], ['telegram_id'])
    # ### end Alembic commands ###
