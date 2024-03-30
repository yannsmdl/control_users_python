"""create permissions user adm

Revision ID: 5c6b72aadd73
Revises: 8dc186cabd1f
Create Date: 2024-03-30 19:44:10.998556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c6b72aadd73'
down_revision = '8dc186cabd1f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        insert into permission_user_route (user_id, 
                                           route_id, 
                                           created_by
                                           )
                                    select 1 as user_id,
                                           r.id as route_id,
                                           1 as created_by
                                      from route r 
    """)


def downgrade() -> None:
    op.execute("delete from permission_user_route")