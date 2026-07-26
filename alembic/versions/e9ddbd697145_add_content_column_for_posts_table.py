"""add content column for posts table

Revision ID: e9ddbd697145
Revises: 2e9341ac4a9f
Create Date: 2026-07-26 15:07:30.621776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9ddbd697145'
down_revision: Union[str, Sequence[str], None] = '2e9341ac4a9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
