"""craete_shopify_theme

Revision ID: c8e87791d866
Revises: f17b8aeeb6a2
Create Date: 2024-04-14 16:52:43.397131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'c8e87791d866'
down_revision: Union[str, None] = 'f17b8aeeb6a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shopify_themes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('theme_id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('role', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('theme_store_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('previewable', sa.Boolean(), nullable=False),
    sa.Column('processing', sa.Boolean(), nullable=False),
    sa.Column('admin_graphql_api_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopify_themes')
    # ### end Alembic commands ###